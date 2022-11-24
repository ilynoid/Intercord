import logging
import os

import disnake

__all__: tuple[str, ...] = ("InteractiveClient",)

_logger = logging.getLogger(__name__)


class InteractiveClient(disnake.Client):
    def __init__(self, *, channel_id: int, **kwargs) -> None:
        self.channel_id = channel_id
        super().__init__(**kwargs)

    async def on_ready(self) -> None:
        _logger.info("[Event]:\n\tBot Is Ready!")
        _logger.info(f"[Event]:\n\tReady to send messages")

    async def on_message(self, message) -> None:
        _logger.info(
            f"\n[Event]:\n\tNew Message:\n\t\tContent: {message.content}\n\t\tAuthor: {message.author}\n\t\tGuild: {message.guild}\n\t\tChannel: {message.channel}\n\t\tTime: {message.created_at}"
        )

    async def _awaiter(self) -> None:
        await self.wait_until_ready()
        os.system("cls")
        channel = self.get_channel(self.channel_id) or await self.fetch_channel(self.channel_id)
        while True:
            reply = await self.loop.run_in_executor(None, lambda: input(">>> "))
            await channel.send(reply)


    async def start(self, token: str) -> None:
        self.loop.create_task(self._awaiter())
        await super().start(token)
