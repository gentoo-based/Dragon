import nextcord
from nextcord.ext import commands
import os
class Vidss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.allowed_directory = "Videos"  # Set your allowed directory here

    def is_safe_file(self, filename: str) -> bool:
        # Check if the file is in the allowed directory and exists
        full_path = os.path.join(self.allowed_directory, filename)
        return os.path.isfile(full_path) and full_path.startswith(os.path.abspath(self.allowed_directory))

    @commands.command()
    async def video(self, ctx, *, video_filename: str):
        if self.is_safe_file(video_filename):
            try:
                video_file = nextcord.File(os.path.join(self.allowed_directory, video_filename), filename=video_filename)
                await ctx.send(file=video_file)
            except Exception as e:
                await ctx.send(f"An error occurred: {str(e)}")
        else:
            await ctx.send("You cannot access this file.")

    @nextcord.slash_command(name="video", description="Sends a video.")
    async def video_slash(self, interaction: nextcord.Interaction, video_filename: str):
        if self.is_safe_file(video_filename):
            try:
                video_file = nextcord.File(os.path.join(self.allowed_directory, video_filename), filename=video_filename)
                await interaction.response.send_message(file=video_file)
            except Exception as e:
                await interaction.response.send_message(f"An error occurred: {str(e)}")
        else:
            await interaction.response.send_message("You cannot access this file.")

def setup(bot):
    bot.add_cog(Vidss(bot))
