import os

from pathlib import Path
from dotenv import load_dotenv

import discord
import random
import unidecode

client = discord.Client()

r0 = ["loquita", "viejita"]
r1 = ["https://andy.venecas.ga/"]


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    n_message = unidecode.unidecode(message.content.strip()).lower()

    if n_message == "mas bien":
        await message.channel.send(random.choice(r0))
    elif n_message == "pasen xno":
        await message.channel.send(random.choice(r1))
    elif "weed" in n_message:
        await message.add_reaction("♥")


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
client.run(DISCORD_BOT_TOKEN)
