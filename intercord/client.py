from __future__ import annotations

import logging
import os

from disnake.ext import commands

import intercord

from .exts import ExtsContainer

__all__: tuple[str, ...] = ("InteractiveBot",)

_logger = logging.getLogger(__name__)


class InteractiveBot(commands.Bot):
    _COMMANDS: tuple[str, ...] = (
        "help",
        "guilds",
        "users",
    )

    def __init__(
        self,
        *,
        channel_id: int,
        extensions: ExtsContainer | None = None,
        **kwargs
    ) -> None:
        self.channel_id = channel_id
        self.ext = extensions
        super().__init__(**kwargs)

    def _check_and_load_extensions(self) -> None:
        if self.ext:
            for _dir in self.ext.folders:
                self.load_extensions(_dir)
            
            for _file in self.ext.files:
                self.load_extension(_file)

    async def on_ready(self) -> None:
        print(
            f'Intercord {intercord.__version__}\nType "!help" for more information.\n'
        )
        _logger.info("[EVENT]:\n\tBot Is Ready!")
        _logger.info("[EVENT]:\n\tReady to send messages")

    async def on_message(self, message) -> None:
        _logger.info(
            f"\n[EVENT]:\n\tNew Message:\n\t\tContent: {message.content}\n\t\tAuthor: {message.author}\n\t\tGuild: {message.guild}\n\t\tChannel: {message.channel}\n\t\tTime: {message.created_at}"
        )
        await self.process_commands(message)

    async def _awaiter(self) -> None:
        await self.wait_until_ready()
        os.system("cls")
        channel = self.get_channel(self.channel_id) or await self.fetch_channel(
            self.channel_id
        )
        while True:
            message = await self.loop.run_in_executor(None, lambda: input(">>> "))
            if not message.startswith("!"):
                await channel.send(message)
            else:
                if not await self._command_parser(message.lower()[1:]):
                    _logger.warning(f"[WARNING]:\n\tUnknown command named: {message}")

    async def _command_parser(self, message: str) -> bool:
        if message not in self._COMMANDS:
            return False

        if message == "help":
            print(
                'Intercord Help:\n\tCommands(Prefix "!"):\n\t\t'
                + "\n\t\t".join(self._COMMANDS)
            )
            return True

        elif message == "guilds":
            print("\n".join(map(lambda _: _.name, self.guilds)))
            return True

        elif message == "users":
            print("\n".join(map(lambda _: _.name, self.users)))
            return True
        
        return False

    async def start(self, token: str) -> None:
        self.loop.create_task(self._awaiter())
        self._check_and_load_extensions()
        await super().start(token)
