Intercord
=

![Intercord](./assets/banner.png)

Easy to use interactive discord bot structure written in python, by [noid#6900](https://discordapp.com/users/981079408850903111/).

Features
-

- Async IO
- Easy to use

Examples
-
```py
import asyncio
import logging

import disnake

import intercord


async def main():
    client = intercord.InteractiveClient(channel_id=0000000000000000000, intents=disnake.Intents(message_content=True))
    await client.start("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```