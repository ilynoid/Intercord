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
        os.system("cls")
        _logger.info("[Event]: Bot Is Ready!")
        _logger.info(f"[Info]: Ready to send messages")

    async def on_message(self, message) -> None:
        if message.author.bot:
            return
        _logger.info(
            f"\n[Event]:\nNew Message:\nContent: {message.content}\nAuthor: {message.author}\nGuild: {message.guild}\nChannel: {message.channel}\nTime: {message.created_at}"
        )

    async def _awaiter(self) -> None:
        await self.wait_until_ready()
        channel = self.get_channel(self.channel_id) or await self.fetch_channel(self.channel_id)
        while True:
            reply = await self.loop.run_in_executor(None, lambda: input(">>> "))
            try:
                await channel.send(reply)
            except (disnake.HTTPException, disnake.Forbidden) as e:
                if isinstance(e, disnake.HTTPException):
                    _logger.error(f"[Error]: An error occurred while sending the message\n    {e}")
                _logger.error(f"[Error]: Forbidden, you do not have the proper permissions to send the message\n    {e}")
                continue
            _logger.info(f"[Event]: Message Sent: {repr(reply)}")

    async def start(self, token: str) -> None:
        self.loop.create_task(self._awaiter())
        await super().start(token)
