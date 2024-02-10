import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import Option
import random

class vidss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def video(self, ctx, *, video_filename: str):
        try:
            video_file = nextcord.File(f'{video_filename}', filename=f'{video_filename}')
            await ctx.send(file=video_file)
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")

    @commands.Bot.slash_command(name="video", description="Sends a video.")
    async def video_slash(self, interaction: nextcord.Interaction, video_filename: Option(str, "The name of the video file to send")):
        try:
            video_file = nextcord.File(f'{video_filename}', filename=f'{video_filename}')
            await interaction.response.send_message(file=video_file)
        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {str(e)}")

def setup(bot):
    bot.add_cog(vidss(bot))
