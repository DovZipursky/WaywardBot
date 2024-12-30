import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from discord.ext import commands
from typing import Final

#get token
load_dotenv()
TOKEN: Final[str] = os.getenv('TOKEN')

#client set up
intents: Intents = Intents.default()
intents.message_content = True # NOQA
bot = commands.Bot(command_prefix='/', intents=intents)

#functionality


