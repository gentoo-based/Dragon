import os
import random
from typing import Final
import discord_ios
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from keep_alive import keep_alive
from dotenv import load_dotenv
import time

keep_alive()


intents = nextcord.Intents.all()
bot = commands.AutoShardedBot(shard_count=32, command_prefix='td!', intents=intents) 
bot.help_command = None

@bot.event
async def on_ready():
  print('Logged in as {}'.format(bot.user.name))
  presence = nextcord.Game(name='td!help')
  await bot.change_presence(
    activity=presence
  )

# Load the owner-only commands
bot.load_extension('cog_commands')
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
