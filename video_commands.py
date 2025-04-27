import nextcord
from nextcord.ext import commands
import os

class Vidss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.blacklist = {"main", "misc_commands", "moderation_cog", "video_commands"}
        self.supported_extensions = ['.mp4', '.gif', '.mov', '.webm', '.avi', '.mkv']

    def is_blacklisted(self, filename: str) -> bool:
        return filename in self.blacklist

    async def find_file(self, base_name: str):
        for ext in self.supported_extensions:
            filename = f"{base_name}{ext}"
            if os.path.isfile(filename):
                return filename
        return None

    @commands.command()
    async def meme(self, ctx, *, meme: str):
        if self.is_blacklisted(meme):
            await ctx.send("This file is blacklisted and cannot be sent.")
            return
        
        found_file = await self.find_file(meme)
        if not found_file:
            await ctx.send("No file found with that name and supported extensions.")
            return
        
        try:
            video_file = nextcord.File(found_file)
            await ctx.send(file=video_file)
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")

    @nextcord.slash_command(name="meme", description="Sends a meme within the formats of gif, mp4, and mov.")
    async def memesl(self, interaction: nextcord.Interaction, *, meme: str = nextcord.SlashOption(description="Meme to display")):
        if self.is_blacklisted(meme):
            await interaction.response.send_message("This file is blacklisted and cannot be sent.")
            return
        
        found_file = await self.find_file(meme)
        if not found_file:
            await interaction.response.send_message("No file found with that name and supported extensions.")
            return
        
        try:
            video_file = nextcord.File(found_file)
            await interaction.response.send_message(file=video_file)
        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {str(e)}")

def setup(bot):
    bot.add_cog(Vidss(bot))