import nextcord
from nextcord.ext import commands
import asyncio

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.warn_count = {}

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
        """Bans a member from the server."""
        try:
            await member.ban(reason=reason)
            await ctx.send(f'User {member} has been banned' + (f' for reason: {reason}' if reason else ''))
            # Log the ban
            print(f"User {member} banned by {ctx.author} for reason: {reason}")
        except nextcord.errors.Forbidden:
            await ctx.send("Error: I do not have permissions to ban this member.")
        except nextcord.errors.HTTPException as e:
            await ctx.send(f"Error banning member: {e}")

    @nextcord.slash_command(name="ban", description="Bans a member from the server")
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def slash_ban(self, interaction: nextcord.Interaction, member: nextcord.Member = nextcord.SlashOption(description="Member to ban"), *, reason=nextcord.SlashOption(description="Reason to ban")):
        """Bans a member from the server (slash command)."""
        try:
            await member.ban(reason=reason)
            await interaction.response.send_message(f'User {member} has been banned' + (f' for reason: {reason}' if reason else ''))
            # Log the ban
            print(f"User {member} banned by {interaction.user} for reason: {reason}")
        except nextcord.errors.Forbidden:
            await interaction.response.send_message("Error: I do not have permissions to ban this member.", ephemeral=True)
        except nextcord.errors.HTTPException as e:
            await interaction.response.send_message(f"Error banning member: {e}", ephemeral=True)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member: nextcord.Member, *, reason=None):
        """Kicks a member from the server."""
        try:
            await member.kick(reason=reason)
            await ctx.send(f'User {member} has been kicked' + (f' for reason: {reason}' if reason else ''))
            # Log the kick
            print(f"User {member} kicked by {ctx.author} for reason: {reason}")
        except nextcord.errors.Forbidden:
            await ctx.send("Error: I do not have permissions to kick this member.")
        except nextcord.errors.HTTPException as e:
            await ctx.send(f"Error kicking member: {e}")

    @nextcord.slash_command(name="kick", description="Kicks a member from the server")
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def slash_kick(self, interaction: nextcord.Interaction, member: nextcord.Member = nextcord.SlashOption(description="Member to kick"), *, reason=nextcord.SlashOption(description="Reason to kick")):
        """Kicks a member from the server (slash command)."""
        try:
            await member.kick(reason=reason)
            await interaction.response.send_message(f'User {member} has been kicked' + (f' for reason: {reason}' if reason else ''))
            # Log the kick
            print(f"User {member} kicked by {interaction.user} for reason: {reason}")
        except nextcord.errors.Forbidden:
            await interaction.response.send_message("Error: I do not have permissions to kick this member.", ephemeral=True)
        except nextcord.errors.HTTPException as e:
            await interaction.response.send_message(f"Error kicking member: {e}", ephemeral=True)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def timeout(self, ctx, member: nextcord.Member, seconds: int):
        """Times out a member for a specified number of seconds."""
        try:
            if seconds <= 0:
                await ctx.send("Timeout duration must be a positive number of seconds.")
                return
            await member.timeout(until=nextcord.utils.utcnow() + asyncio.timedelta(seconds=seconds))
            await ctx.send(f'User {member} has been timed out for {seconds} seconds')
            # Log the timeout
            print(f"User {member} timed out by {ctx.author} for {seconds} seconds.")
        except nextcord.errors.Forbidden:
            await ctx.send("Error: I do not have permissions to timeout this member.")
        except nextcord.errors.HTTPException as e:
            await ctx.send(f"Error timing out member: {e}")

    @nextcord.slash_command(name="timeout", description="Times out a member for a specified number of seconds")
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def slash_timeout(self, interaction: nextcord.Interaction, member: nextcord.Member, seconds: int):
        """Times out a member for a specified number of seconds (slash command)."""
        try:
            if seconds <= 0:
                await interaction.response.send_message("Timeout duration must be a positive number of seconds.", ephemeral=True)
                return
            await member.timeout(until=nextcord.utils.utcnow() + asyncio.timedelta(seconds=seconds))
            await interaction.response.send_message(f'User {member} has been timed out for {seconds} seconds')
            # Log the timeout
            print(f"User {member} timed out by {interaction.user} for {seconds} seconds.")
        except nextcord.errors.Forbidden:
            await interaction.response.send_message("Error: I do not have permissions to timeout this member.", ephemeral=True)
        except nextcord.errors.HTTPException as e:
            await interaction.response.send_message(f"Error timing out member: {e}", ephemeral=True)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def lock(self, ctx):
        """Locks the current channel."""
        try:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
            await ctx.send("Channel locked.")
            # Log the lock
            print(f"Channel {ctx.channel.name} locked by {ctx.author}.")
        except nextcord.errors.Forbidden:
            await ctx.send("Error: I do not have permissions to manage this channel.")
        except nextcord.errors.HTTPException as e:
            await ctx.send(f"Error locking channel: {e}")

    @nextcord.slash_command(name="lock", description="Locks the current channel")
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def slash_lock(self, interaction: nextcord.Interaction):
        """Locks the current channel (slash command)."""
        try:
            await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=False)
            await interaction.response.send_message("Channel locked.")
            # Log the lock
            print(f"Channel {interaction.channel.name} locked by {interaction.user}.")
        except nextcord.errors.Forbidden:
            await interaction.response.send_message("Error: I do not have permissions to manage this channel.", ephemeral=True)
        except nextcord.errors.HTTPException as e:
            await interaction.response.send_message(f"Error locking channel: {e}", ephemeral=True)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        """Unlocks the current channel."""
        try:
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=None)
            await ctx.send("Channel unlocked.")
            # Log the unlock
            print(f"Channel {ctx.channel.name} unlocked by {ctx.author}.")
        except nextcord.errors.Forbidden:
            await ctx.send("Error: I do not have permissions to manage this channel.")
        except nextcord.errors.HTTPException as e:
            await ctx.send(f"Error unlocking channel: {e}")

    @nextcord.slash_command(name="unlock", description="Unlocks the current channel")
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def slash_unlock(self, interaction: nextcord.Interaction):
        """Unlocks the current channel (slash command)."""
        try:
            await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=None)
            await interaction.response.send_message("Channel unlocked.")
            # Log the unlock
            print(f"Channel {interaction.channel.name} unlocked by {interaction.user}.")
        except nextcord.errors.Forbidden:
            await interaction.response.send_message("Error: I do not have permissions to manage this channel.", ephemeral=True)
        except nextcord.errors.HTTPException as e:
            await interaction.response.send_message(f"Error unlocking channel: {e}", ephemeral=True)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def addrole(self, ctx, member: nextcord.Member, *, role: nextcord.Role):
        """Adds a role to a user."""
        try:
            await member.add_roles(role)
            await ctx.send(f"Added role '{role.name}' to {member.mention}.")
            # Log the role addition
            print(f"Role '{role.name}' added to {member} by {ctx.author}.")
        except nextcord.errors.Forbidden:
            await ctx.send("Error: I do not have permissions to manage roles or the specified role is higher than mine.")
        except nextcord.errors.HTTPException as e:
            await ctx.send(f"Error adding role: {e}")

    @nextcord.slash_command(name="addrole", description="Adds a role to a user")
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def slash_addrole(self, interaction: nextcord.Interaction, member: nextcord.Member = nextcord.SlashOption(description="Member to add a role to"), role: nextcord.Role = nextcord.SlashOption(description="Role to add to the member to")):
        """Adds a role to a user (slash command)."""
        try:
            await member.add_roles(role)
            await interaction.response.send_message(f"Added role '{role.name}' to {member.mention}.")
            # Log the role addition
            print(f"Role '{role.name}' added to {member} by {interaction.user}.")
        except nextcord.errors.Forbidden:
            await interaction.response.send_message("Error: I do not have permissions to manage roles or the specified role is higher than mine.", ephemeral=True)
        except nextcord.errors.HTTPException as e:
            await interaction.response.send_message(f"Error adding role: {e}", ephemeral=True)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def removerole(self, ctx, member: nextcord.Member, *, role: nextcord.Role):
        """Removes a role from a user."""
        try:
            await member.remove_roles(role)
            await ctx.send(f"Removed role '{role.name}' from {member.mention}.")
            # Log the role removal
            print(f"Role '{role.name}' removed from {member} by {ctx.author}.")
        except nextcord.errors.Forbidden:
            await ctx.send("Error: I do not have permissions to manage roles or the specified role is higher than mine.")
        except nextcord.errors.HTTPException as e:
            await ctx.send(f"Error removing role: {e}")

    @nextcord.slash_command(name="removerole", description="Removes a role from a user")
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def slash_removerole(self, interaction: nextcord.Interaction, member: nextcord.Member = nextcord.SlashOption(description="Member to remove a role from a user"), role: nextcord.Role = nextcord.SlashOption(description="The role to be removed from a user")):
        """Removes a role from a user (slash command)."""
        try:
            await member.remove_roles(role)
            await interaction.response.send_message(f"Removed role '{role.name}' from {member.mention}.")
            # Log the role removal
            print(f"Role '{role.name}' removed from {member} by {interaction.user}.")
        except nextcord.errors.Forbidden:
            await interaction.response.send_message("Error: I do not have permissions to manage roles or the specified role is higher than mine.", ephemeral=True)
        except nextcord.errors.HTTPException as e:
            await interaction.response.send_message(f"Error removing role: {e}", ephemeral=True)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int):
        """Adds a slowmode to the channel."""
        try:
            if seconds < 0:
                await ctx.send("Slowmode duration cannot be negative.")
                return
            await ctx.channel.edit(slowmode_delay=seconds)
            await ctx.send(f"Set slowmode to {seconds} seconds.")
            # Log the slowmode change
            print(f"Slowmode set to {seconds} seconds in {ctx.channel.name} by {ctx.author}.")
        except nextcord.errors.Forbidden:
            await ctx.send("Error: I do not have permissions to manage this channel.")
        except nextcord.errors.HTTPException as e:
            await ctx.send(f"Error setting slowmode: {e}")

    @nextcord.slash_command(name="slowmode", description="Adds a slowmode to the channel")
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def slash_slowmode(self, interaction: nextcord.Interaction, seconds: int = nextcord.SlashOption(description="How long the slowmode lasts for each messages.")):
        """Adds a slowmode to the channel (slash command)."""
        try:
            if seconds < 0:
                await interaction.response.send_message("Slowmode duration cannot be negative.", ephemeral=True)
                return
            await interaction.channel.edit(slowmode_delay=seconds)
            await interaction.response.send_message(f"Set slowmode to {seconds} seconds.")
            # Log the slowmode change
            print(f"Slowmode set to {seconds} seconds in {interaction.channel.name} by {interaction.user}.")
        except nextcord.errors.Forbidden:
            await interaction.response.send_message("Error: I do not have permissions to manage this channel.", ephemeral=True)
        except nextcord.errors.HTTPException as e:
            await interaction.response.send_message(f"Error setting slowmode: {e}", ephemeral=True)

    @commands.command()
    @commands.has_permissions(kick_members=True, ban_members=True)
    async def warn(self, ctx, member: nextcord.Member, *, reason=None):
        """Warns a user. 3 warnings = kick, 6 warnings = ban."""
        try:
            if member.bot:
                await ctx.send("You cannot warn bots.")
                return
            if member.id == ctx.author.id:
                await ctx.send("You cannot warn yourself.")
                return

            if member not in self.warn_count:
                self.warn_count[member] = 0
            self.warn_count[member] += 1

            await ctx.send(f'{member.mention} has been warned.' + (f' Reason: {reason}' if reason else '') + f' They now have {self.warn_count[member]} warnings.')
            # Log the warn
            print(f"User {member} warned by {ctx.author}. Current warns: {self.warn_count[member]}. Reason: {reason}")

            if self.warn_count[member] == 3:
                await member.kick(reason="3 warnings")
                await ctx.send(f'User {member} has been kicked due to 3 warnings.')
                print(f"User {member} kicked due to 3 warnings.")
                del self.warn_count[member] # Reset warn count after kick
            elif self.warn_count[member] == 6:
                await member.ban(reason="6 warnings")
                await ctx.send(f'User {member} has been banned due to 6 warnings.')
                print(f"User {member} banned due to 6 warnings.")
                del self.warn_count[member] # Reset warn count after ban

        except nextcord.errors.Forbidden:
            await ctx.send("Error: I do not have permissions to warn, kick, or ban this member.")
        except nextcord.errors.HTTPException as e:
            await ctx.send(f"Error during warn action: {e}")
        except Exception as e:
            print(f"An unexpected error occurred in warn command: {e}")
            await ctx.send("An unexpected error occurred.")

    @nextcord.slash_command(name="warn", description="Warns a user. 3 warnings = kick, 6 warnings = ban")
    @commands.has_permissions(kick_members=True, ban_members=True)
    async def slash_warn(self, interaction: nextcord.Interaction, member: nextcord.Member = nextcord.SlashOption(description="Member to warn"), *, reason = nextcord.SlashOption(description="Reason to warn a member.")):
        """Warns a user. 3 warnings = kick, 6 warnings = ban (slash command)."""
        try:
            if member.bot:
                await interaction.response.send_message("You cannot warn bots.", ephemeral=True)
                return
            if member.id == interaction.user.id:
                await interaction.response.send_message("You cannot warn yourself.", ephemeral=True)
                return

            if member not in self.warn_count:
                self.warn_count[member] = 0
            self.warn_count[member] += 1

            await interaction.response.send_message(f'{member.mention} has been warned.' + (f' Reason: {reason}' if reason else '') + f' They now have {self.warn_count[member]} warnings.')
            # Log the warn
            print(f"User {member} warned by {interaction.user}. Current warns: {self.warn_count[member]}. Reason: {reason}")

            if self.warn_count[member] == 3:
                await member.kick(reason="3 warnings")
                await interaction.followup.send(f'User {member} has been kicked due to 3 warnings.')
                print(f"User {member} kicked due to 3 warnings.")
                del self.warn_count[member] # Reset warn count after kick
            elif self.warn_count[member] == 6:
                await member.ban(reason="6 warnings")
                await interaction.followup.send(f'User {member} has been banned due to 6 warnings.')
                print(f"User {member} banned due to 6 warnings.")
                del self.warn_count[member] # Reset warn count after ban

        except nextcord.errors.Forbidden:
            await interaction.response.send_message("Error: I do not have permissions to warn, kick, or ban this member.", ephemeral=True)
        except nextcord.errors.HTTPException as e:
            await interaction.response.send_message(f"Error during warn action: {e}", ephemeral=True)
        except Exception as e:
            print(f"An unexpected error occurred in slash_warn command: {e}")
            await interaction.followup.send("An unexpected error occurred.", ephemeral=True)

    @commands.command()
    @commands.has_permissions(kick_members=True, ban_members=True)
    async def clearwarns(self, ctx, member: nextcord.Member):
        """Clears the warns of a user."""
        try:
            if member in self.warn_count:
                del self.warn_count[member]
                await ctx.send(f"Cleared all warnings for {member.mention}.")
                print(f"Warnings cleared for {member} by {ctx.author}.")
            else:
                await ctx.send(f"{member.mention} has no active warnings.")
        except nextcord.errors.HTTPException as e:
            await ctx.send(f"Error clearing warns: {e}")
        except Exception as e:
            print(f"An unexpected error occurred in clearwarns command: {e}")
            await ctx.send("An unexpected error occurred.")

    @nextcord.slash_command(name="clearwarns", description="Clears the warns of a user")
    @commands.has_permissions(kick_members=True, ban_members=True)
    async def slash_clearwarns(self, interaction: nextcord.Interaction, member: nextcord.Member = nextcord.SlashOption(description="Member to clear warns of")):
        """Clears the warns of a user (slash command)."""
        try:
            if member in self.warn_count:
                del self.warn_count[member]
                await interaction.response.send_message(f"Cleared all warnings for {member.mention}.")
                print(f"Warnings cleared for {member} by {interaction.user}.")
            else:
                await interaction.response.send_message(f"{member.mention} has no active warnings.", ephemeral=True)
        except nextcord.errors.HTTPException as e:
            await interaction.response.send_message(f"Error clearing warns: {e}", ephemeral=True)
        except Exception as e:
            print(f"An unexpected error occurred in slash_clearwarns command: {e}")
            await interaction.followup.send("An unexpected error occurred.", ephemeral=True)
    
    @commands.command(aliases=['clear'])
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        """Purges a specified number of messages from the channel."""
        try:
            if amount <= 0:
                await ctx.send("Please specify a positive number of messages to delete.")
                return
            deleted = await ctx.channel.purge(limit=amount + 1)  # +1 to account for the command message itself
            await ctx.send(f"Successfully purged {len(deleted) - 1} messages.", delete_after=5)
        except nextcord.Forbidden:
            await ctx.send("Error: I do not have permissions to manage messages in this channel.")
        except nextcord.HTTPException as e:
            await ctx.send(f"Error occurred while purging messages: {e}")
        except Exception as e:
            print(f"An unexpected error occurred in purge command: {e}")
            await ctx.send("An unexpected error occurred.")

    @nextcord.slash_command(name="purge", description="Deletes a specified number of messages.")
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def purge_slash(self, interaction: nextcord.Interaction, amount: int = nextcord.SlashOption(description="Amount of messages to purge")):
        """Purges a specified number of messages from the channel (slash command)."""
        try:
            if amount <= 0:
                await interaction.response.send_message("Please specify a positive number of messages to delete.", ephemeral=True)
                return
            await interaction.response.defer(ephemeral=True)  # Acknowledge the command as purge can take time
            deleted = await interaction.channel.purge(limit=amount)
            await interaction.followup.send(f"Successfully purged {len(deleted)} messages.", ephemeral=True)
        except nextcord.Forbidden:
            await interaction.followup.send("Error: I do not have permissions to manage messages in this channel.", ephemeral=True)
        except nextcord.HTTPException as e:
            await interaction.followup.send(f"Error occurred while purging messages: {e}", ephemeral=True)
        except Exception as e:
            print(f"An unexpected error occurred in purge_slash command: {e}")
            await interaction.followup.send("An unexpected error occurred.", ephemeral=True)
def setup(bot):
    bot.add_cog(ModerationCog(bot))
