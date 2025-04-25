import nextcord
from nextcord.ext import commands

class CogCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, cog):
        """Deletes the command message and sends the provided message."""
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f"Cound not unload {cog}")
            return
        await ctx.send(f"Unloaded {cog}")

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

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, cog):
        """Deletes the command message and sends the provided message."""
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f"Cound not restart {cog}")
            return
        await ctx.send(f"Restarted {cog}")

    @nextcord.slash_command(name="reload", description="Reloads a cog to avoid rebooting.")
    async def reload(self, interaction: nextcord.Interaction, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
            await interaction.response.send_message("Reloaded the cog with no effort.")
        except Exception as e:
            await interaction.followup.send("An unexpected error occurred.", ephemeral=True)

def setup(bot):
    bot.add_cog(CogCommands(bot))
