import discord
from discord.ext import commands

class CogCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog):
        """Deletes the command message and sends the provided message."""
        try:
            self.bot.unload_extension(cog)
            await ctx.send("Unloaded the cog with no effort.")
        except Exception as e:
            await ctx.send(f"Cound not unload {cog}")
            return
        await ctx.send(f"Unloaded {cog}")
    @commands.slash_command(name="unload", description="Unloads a cog to avoid rebooting.")
    @commands.is_owner()
    async def unloadsl(self, interaction, cog: str = discord.Option(description="Cog to unload")):
        try:
            self.bot.unload_extension(cog)
            await interaction.response.send_message("Unloaded the cog with no effort.", ephemeral=True)
        except Exception as e:
            await interaction.followup.send("An unexpected error occurred.", ephemeral=True)

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, cog):
        """Deletes the command message and sends the provided message."""
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f"Cound not load {cog}")
            return
        await ctx.send(f"Loaded {cog}")
    @commands.slash_command(name="load", description="Loads a cog to avoid rebooting.")
    @commands.is_owner()
    async def loadsl(self, interaction, cog: str = discord.Option(description="Cog to load")):
        try:
            self.bot.load_extension(cog)
            await interaction.response.send_message("Loaded the cog with no effort.", ephemeral=True)
        except Exception as e:
            await interaction.followup.send("An unexpected error occurred.", ephemeral=True)

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog: str):
        """Deletes the command message and sends the provided message."""
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f"Cound not restart {cog}")
            return
        await ctx.send(f"Restarted {cog}")

    @commands.slash_command(name="reload", description="Reloads a cog to avoid rebooting.")
    @commands.is_owner()
    async def reload(self, interaction, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
            await interaction.response.send_message("Reloaded the cog with no effort.", ephemeral=True)
        except Exception as e:
            await interaction.followup.send("An unexpected error occurred.", ephemeral=True)

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx):
        """Deletes the command message and sends the provided message."""
        try:
            await self.bot.sync_application_commands()
        except Exception as e:
            await ctx.send(f"Synced the application commands with some errors.")
            return
        await ctx.send(f"Synced the application commands with no effort")

    @commands.slash_command(name="sync", description="Syncs all the application commands.")
    @commands.is_owner()
    async def syncsl(self, interaction):
        try:
            await self.bot.sync_application_commands()
            await interaction.response.send_message("Synced the application commands with no effort.", ephemeral=True)
        except Exception as e:
            await interaction.followup.send("An unexpected error occurred.", ephemeral=True)

def setup(bot):
    bot.add_cog(CogCommands(bot))
