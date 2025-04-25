import os
import random
from typing import Final
import discord_ios
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from keep_alive import keep_alive
from dotenv import load_dotenv

keep_alive()


intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='td!', intents=intents)
bot.help_command = None

@bot.event
async def on_ready():
   print('Logged in as {}'.format(bot.user.name))
   game = nextcord.Game("td!help")
   await bot.change_presence(
     activity=game
   )

# Load the moderation commands.
bot.load_extension('moderation_cog')
# Load the misc commands.
bot.load_extension('misc_commands')
# Loads the video commands.
bot.load_extension('video_commands')

# RUN THE BOT
load_dotenv()
TOKEN: Final[str] = os.getenv('NEXTCORD_TOKEN')
bot.run(TOKEN)
