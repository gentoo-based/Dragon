import nextcord
from nextcord.ext import commands
import os

class Vidss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.blacklist = {"main.py", "misc_commands.py", "moderation_cog.py", "video_commands.py"}  # Add filenames to blacklist here

    def is_blacklisted(self, filename: str) -> bool:
        # Check if the filename is in the blacklist
        return filename in self.blacklist

    @commands.command()
    async def video(self, ctx, *, video_filename: str):
        if self.is_blacklisted(video_filename):
            await ctx.send("This file is blacklisted and cannot be sent.")
            return
        
        try:
            video_file = nextcord.File(video_filename)
            await ctx.send(file=video_file)
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")

    @nextcord.slash_command(name="video", description="Sends a video.")
    async def video_slash(self, interaction: nextcord.Interaction, video_filename: str):
        if self.is_blacklisted(video_filename):
            await interaction.response.send_message("This file is blacklisted and cannot be sent.")
            return
        
        try:
            video_file = nextcord.File(video_filename)
            await interaction.response.send_message(file=video_file)
        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {str(e)}")

def setup(bot):
    bot.add_cog(Vidss(bot))

