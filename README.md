Intercord
=

![Intercord](./assets/banner.png)

Easy to use interactive discord bot structure written in python, by [noid#6900](https://discordapp.com/users/981079408850903111/).

Intercord offers an object for the implementation of a discord bot that acts like a user due to it taking input by the operator over the bot having assigned operations and answers. Intercord also can be a good way to have a good time with your buddies by joking around with them as you "control" your bot with your mind.

Features
-

- Asynchronous IO
- Easy to use

Examples
-
```py
import asyncio
import logging

import disnake

import intercord


async def main():
    client = intercord.InteractiveClient(channel_id=0000000000000000000, intents=disnake.Intents(message_content=True, guilds=True))
    await client.start("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```