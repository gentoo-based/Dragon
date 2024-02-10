import nextcord
from nextcord.ext import commands
import asyncio

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.warn_count = {}

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)  # +1 to include the command message itself

    @commands.Bot.slash_command(name="clear", description="Clears a specific number of messages from a channel")
    @commands.has_permissions(manage_messages=True)
    async def slash_clear(self, ctx: nextcord.Interaction, amount: int):
        await ctx.channel.purge(limit=amount)  # Slash command message won't be counted
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'User {member} has been banned')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: nextcord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kicked')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def timeout(self, ctx, member: nextcord.Member, seconds: int):
        role = nextcord.utils.get(ctx.guild.roles, name="Timeout")
        if not role:
            role = await ctx.guild.create_role(name="Timeout")
            for channel in ctx.guild.channels:
                await channel.set_permissions(role, send_messages=False)
        await member.add_roles(role)
        await ctx.send(f'User {member} has been timed out for {seconds} seconds')
        await asyncio.sleep(seconds)
        await member.remove_roles(role)

    @commands.Bot.slash_command(name="ban", description="Bans a member from the server")
    @commands.has_permissions(ban_members=True)
    async def slash_ban(self, ctx: nextcord.Interaction, member: nextcord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'User {member} has been banned')

    @commands.Bot.slash_command(name="kick", description="Kicks a member from the server")
    @commands.has_permissions(kick_members=True)
    async def slash_kick(self, ctx: nextcord.Interaction, member: nextcord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kicked')

    @commands.Bot.slash_command(name="timeout", description="Times out a member for a specified number of seconds")
    @commands.has_permissions(manage_messages=True)
    async def slash_timeout(self, ctx: nextcord.Interaction, member: nextcord.Member, seconds: int):
        role = nextcord.utils.get(ctx.guild.roles, name="Timeout")
        if not role:
            role = await ctx.guild.create_role(name="Timeout")
            for channel in ctx.guild.channels:
                await channel.set_permissions(role, send_messages=False)
        await member.add_roles(role)
        await ctx.send(f'User {member} has been timed out for {seconds} seconds')
        await asyncio.sleep(seconds)
        await member.remove_roles(role)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send("Channel locked.")

    @commands.Bot.slash_command(name="lock", description="Locks the current channel")
    @commands.has_permissions(manage_channels=True)
    async def slash_lock(self, ctx: nextcord.Interaction):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send("Channel locked.")

    @commands.command()
    @commands.has_permissions(kick_members=True, ban_members=True)
    async def warn(self, ctx, member: nextcord.Member, *, reason=None):
        if member not in self.warn_count:
            self.warn_count[member] = 0
        self.warn_count[member] += 1

        if self.warn_count[member] == 3:
            await member.kick(reason="3 warnings")
            await ctx.send(f'User {member} has been kicked due to 3 warnings')
        elif self.warn_count[member] == 6:
            await member.ban(reason="6 warnings")
            await ctx.send(f'User {member} has been banned due to 6 warnings')
        else:
            await ctx.send(f'User {member} has been warned. They now have {self.warn_count[member]} warnings')

    @commands.Bot.slash_command(name="warn", description="Warns a user. 3 warnings = kick, 6 warnings = ban")
    @commands.has_permissions(kick_members=True, ban_members=True)
    async def slash_warn(self, ctx: nextcord.Interaction, member: nextcord.Member, *, reason=None):
        if member not in self.warn_count:
            self.warn_count[member] = 0
        self.warn_count[member] += 1

        if self.warn_count[member] == 3:
            await member.kick(reason="3 warnings")
            await ctx.send(f'User {member} has been kicked due to 3 warnings')
        elif self.warn_count[member] == 6:
            await member.ban(reason="6 warnings")
            await ctx.send(f'User {member} has been banned due to 6 warnings')
        else:
            await ctx.send(f'User {member} has been warned. They now have {self.warn_count[member]} warnings')

def setup(bot):
    bot.add_cog(ModerationCog(bot))
