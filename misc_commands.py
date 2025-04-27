import nextcord
from nextcord.ext import commands
import random
import sympy
from sympy import Symbol, diff, integrate
class MiscCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fly(self, ctx, Member: nextcord.Member):
        """Deletes the command message and sends the provided message."""
        if Member == None:
            Member = ctx.author
        try:
            await ctx.send(f"Fly high {Member.mention}")
            await ctx.send("https://tenor.com/view/angel-wings-fly-gif-14506801")
        except nextcord.HTTPException as e:
            await ctx.send(f"Error occurred while sending message: {e}")
        except Exception as e:
            print(f"An unexpected error occurred in echo_slash command: {e}")
            await ctx.send("An unexpected error occurred.",)

    @nextcord.slash_command(name="fly", description="Redbull gives you wings.")
    async def fly_slash(self, interaction: nextcord.Interaction, Member: nextcord.Member = nextcord.SlashOption(description="Member to give redbull to")):
        try:
            await interaction.response.send_message(f"Fly high {Member.mention}")
            await interaction.followup.send("https://tenor.com/view/angel-wings-fly-gif-14506801")
        except nextcord.HTTPException as e:
            await interaction.followup.send(f"Error occurred while sending message: {e}", ephemeral=True)
        except Exception as e:
            print(f"An unexpected error occurred in echo_slash command: {e}")
            await interaction.followup.send("An unexpected error occurred.", ephemeral=True)

    @commands.command()
    @commands.is_owner()
    async def echo(self, ctx, *, message: str):
        """Deletes the command message and sends the provided message."""
        try:
            await ctx.message.delete()
            await ctx.send(message)
        except nextcord.Forbidden:
            await ctx.send("Error: I do not have permissions to delete messages.")
        except nextcord.HTTPException as e:
            await ctx.send(f"Error occurred while sending or deleting message: {e}")
        except Exception as e:
            print(f"An unexpected error occurred in echo command: {e}")
            await ctx.send("An unexpected error occurred.")

    @nextcord.slash_command(name="echo", description="Echoes your message back to you.")
    async def echo_slash(self, interaction: nextcord.Interaction, message: str = nextcord.SlashOption(description="Message to relay back to you.")):
        """Echoes the provided message back to the user via a slash command."""
        try:
            await interaction.response.send_message(message)
        except nextcord.HTTPException as e:
            await interaction.followup.send(f"Error occurred while sending message: {e}", ephemeral=True)
        except Exception as e:
            print(f"An unexpected error occurred in echo_slash command: {e}")
            await interaction.followup.send("An unexpected error occurred.", ephemeral=True)

    @commands.command()
    async def joke(self, ctx):
        """Tells a random joke."""
        try:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the chicken go to the seance? To talk to the other side!",
                "Parallel lines have so much in common... it’s a shame they’ll never meet."
            ]
            await ctx.send(random.choice(jokes))
        except nextcord.HTTPException as e:
            await ctx.send(f"Error occurred while sending message: {e}")
        except Exception as e:
            print(f"An unexpected error occurred in joke command: {e}")
            await ctx.send("An unexpected error occurred.")

    @nextcord.slash_command(name="joke", description="Tells a random joke.")
    async def joke_slash(self, interaction: nextcord.Interaction):
        """Tells a random joke via a slash command."""
        try:
            jokes = [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the chicken go to the seance? To talk to the other side!",
                "Parallel lines have so much in common... it’s a shame they’ll never meet."
            ]
            await interaction.response.send_message(random.choice(jokes))
        except nextcord.HTTPException as e:
            await interaction.followup.send(f"Error occurred while sending message: {e}", ephemeral=True)
        except Exception as e:
            print(f"An unexpected error occurred in joke_slash command: {e}")
            await interaction.followup.send("An unexpected error occurred.", ephemeral=True)

    @commands.command()
    async def fact(self, ctx):
        """Tells a random fact."""
        try:
            facts = [
                "Did you know? The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
                "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
                "Did you know? A group of flamingos is called a flamboyance."
            ]
            await ctx.send(random.choice(facts))
        except nextcord.HTTPException as e:
            await ctx.send(f"Error occurred while sending message: {e}")
        except Exception as e:
            print(f"An unexpected error occurred in fact command: {e}")
            await ctx.send("An unexpected error occurred.")

    @nextcord.slash_command(name="fact", description="Tells a random fact.")
    async def fact_slash(self, interaction: nextcord.Interaction):
        """Tells a random fact via a slash command."""
        try:
            facts = [
                "Did you know? The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
                "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
                "Did you know? A group of flamingos is called a flamboyance."
            ]
            await interaction.response.send_message(random.choice(facts))
        except nextcord.HTTPException as e:
            await interaction.followup.send(f"Error occurred while sending message: {e}", ephemeral=True)
        except Exception as e:
            print(f"An unexpected error occurred in fact_slash command: {e}")
            await interaction.followup.send("An unexpected error occurred.", ephemeral=True)

    @commands.command()
    async def roast(self, ctx, member: nextcord.Member):
        """Roasts the mentioned member in a (hopefully) lighthearted way."""
        try:
            roasts = [
                f"{member.mention}, I've had coffee mugs with more personality than you.",
                f"{member.mention}, is your brain made of sponges? Because it soaks up everything but knowledge.",
                f"{member.mention}, I'm not saying you're dumb, but you stare at orange juice because it says 'Concentrate'.",
                f"{member.mention}, you're like a broken pencil - pointless.",
                f"{member.mention}, if laughter is the best medicine, your face must be curing the world."
            ]
            roast = random.choice(roasts)
            await ctx.send(roast)
        except nextcord.HTTPException as e:
            await ctx.send(f"Error occurred while sending message: {e}")
        except Exception as e:
            print(f"An unexpected error occurred in roast command: {e}")
            await ctx.send("An unexpected error occurred.")

    @nextcord.slash_command(name="roast", description="Tells a friendly roast to the mentioned member.")
    async def roast_slash(self, interaction: nextcord.Interaction, member: nextcord.Member = nextcord.SlashOption(description="Member to roast")):
        """Roasts the mentioned member via a slash command."""
        try:
            roasts = [
                f"{member.mention}, I've had coffee mugs with more personality than you.",
                f"{member.mention}, is your brain made of sponges? Because it soaks up everything but knowledge.",
                f"{member.mention}, I'm not saying you're dumb, but you stare at orange juice because it says 'Concentrate'.",
                f"{member.mention}, you're like a broken pencil - pointless.",
                f"{member.mention}, if laughter is the best medicine, your face must be curing the world."
            ]
            roast = random.choice(roasts)
            await interaction.response.send_message(roast)
        except nextcord.HTTPException as e:
            await interaction.followup.send(f"Error occurred while sending message: {e}", ephemeral=True)
        except Exception as e:
            print(f"An unexpected error occurred in roast_slash command: {e}")
            await interaction.followup.send("An unexpected error occurred.", ephemeral=True)

    @commands.command()
    async def about(self, ctx):
        """Shows information about the bot"""
        try:
            embed = nextcord.Embed(
                title="About the Bot",
                description=f"""This is a bot built on memes and various moderation commands.

                **Version**
                3.5.5

                **Author**
                Made by <@1221614686865461259>

                **Open-sourced on**
                https://github.com/gentoo-based/Dragon

                **Self hosted**
                Self hosted on a mid-end computer integrated with 32 shards in place, to prepare the bot for immense usage in the future.
                """,
                color=nextcord.Color.blue()
            )
            await ctx.send(embed=embed)
        except nextcord.HTTPException as e:
            await ctx.send(f"Error occurred while sending embed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred in about_slash command: {e}")
            await ctx.send("An unexpected error occurred.")

    @nextcord.slash_command(name="about", description="Shows information about the bot.")
    async def about_slash(self, interaction: nextcord.Interaction):
        """Shows information about the bot via a slash command."""
        try:
            embed = nextcord.Embed(
                title="About the Bot",
                description=f"""This is a bot built on memes and various moderation commands.

                **Version**
                3.5.5

                **Author**
                Made by <@1221614686865461259>

                **Open-sourced on**
                https://github.com/gentoo-based/Dragon

                **Self hosted**
                Self hosted on a mid-end computer integrated with 32 shards in place, to prepare the bot for immense usage in the future.
                """,
                color=nextcord.Color.blue()
            )
            await interaction.response.send_message(embed=embed)
        except nextcord.HTTPException as e:
            await interaction.followup.send(f"Error occurred while sending embed: {e}", ephemeral=True)
        except Exception as e:
            print(f"An unexpected error occurred in about_slash command: {e}")
            await interaction.followup.send("An unexpected error occurred.", ephemeral=True)

    @commands.command()
    async def help(self, ctx):
        """Sends a help message with a list of commands via direct message."""
        try:
            description = """
__Fun Commands__
Commands for entertainment.
`td!roll [min] [max]`: Rolls a random number between the specified range (default 1-100).
`td!joke`: Tells a random joke.
`td!fact`: Shows a random fact.
`td!roast <@member>`: Roasts the mentioned member.
`td!solve <expression>`: Solves a mathematical expression (supports +, -, *, /, ^, basic functions, algebra, and basic calculus using prefixes like 'diff' and 'integrate').
`td!meme`: Sends any meme in the bot's repository.
`td!purge <amount>`: Deletes a specified number of messages.

__Admin Commands__
Moderation commands for server management.
`td!ban <@member> [reason]`: Bans a member from the server.
`td!kick <@member> [reason]`: Kicks a member from the server.
`td!warn <@member> [reason]`: Warns a member.
`td!clearwarns <@member>`: Clears the warnings of a user.
`td!lock`: Locks the current channel.
`td!unlock`: Unlocks the current channel.
`td!addrole <@member> <role name>`: Adds a role to a user.
`td!removerole <@member> <role name>`: Removes a role from a user.
`td!slowmode <seconds>`: Sets a slow mode for the channel.
`td!clear <amount>`: Clears a specified number of messages.
"""

            embed = nextcord.Embed(
                title='__Commands__',
                description=description,
                color=nextcord.Color.from_rgb(47, 49, 54),
            )
            embed.set_author(name="By Kiryu Kazuma and Darkin")

            await ctx.author.send(embed=embed)
            await ctx.send("Help message sent to your DMs!")
        except nextcord.Forbidden:
            await ctx.send("Could not send you a private message. Please make sure your DMs are open.")
        except nextcord.HTTPException as e:
            await ctx.send(f"Error occurred while sending embed or message: {e}")
        except Exception as e:
            print(f"An unexpected error occurred in help command: {e}")
            await ctx.send("An unexpected error occurred.")

    @nextcord.slash_command(name="help", description="Shows the list of commands privately.")
    async def help_slash(self, interaction: nextcord.Interaction):
        """Shows the list of commands privately."""

        description = """
__Fun Commands__
Commands for entertainment.
`td!roll [min] [max]`: Rolls a random number between the specified range (default 1-100).
`td!joke`: Tells a random joke.
`td!fact`: Shows a random fact.
`td!roast <@member>`: Roasts the mentioned member.
`td!solve <expression>`: Solves a mathematical expression (supports +, -, *, /, ^, basic functions, algebra, and basic calculus using prefixes like 'diff' and 'integrate').
`td!meme`: Sends any meme in the bot's repository.
`td!purge <amount>`: Deletes a specified number of messages.

__Admin Commands__
Moderation commands for server management.
`td!ban <@member> [reason]`: Bans a member from the server.
`td!kick <@member> [reason]`: Kicks a member from the server.
`td!warn <@member> [reason]`: Warns a member.
`td!clearwarns <@member>`: Clears the warnings of a user.
`td!lock`: Locks the current channel.
`td!unlock`: Unlocks the current channel.
`td!addrole <@member> <role name>`: Adds a role to a user.
`td!removerole <@member> <role name>`: Removes a role from a user.
`td!slowmode <seconds>`: Sets a slow mode for the channel.
`td!clear <amount>`: Clears a specified number of messages.
"""

        embed = nextcord.Embed(
            title='__Commands__',
            description=description,
            color=nextcord.Color.from_rgb(47, 49, 54),
        )
        embed.set_author(name="By Kiryu Kazuma and Darkin")
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.followup.send("A help message with a list of commands has been sent to you privately!", ephemeral=True)

    @nextcord.slash_command(name="solve", description="Solves mathematical expressions.")
    async def solve_slash(self, interaction: nextcord.Interaction):
        pass  # This is the parent command, subcommands will be added here

    @solve_slash.subcommand(name="algebra", description="Solves algebraic expressions.")
    async def solve_algebra(self, interaction: nextcord.Interaction, expression: str):
        """Solves algebraic expressions via a slash command."""
        try:
            result = sympy.sympify(expression).evalf()
            await interaction.response.send_message(f"The result is: {result}")
        except (sympy.parsing.mathematica.UnrecognizedSymbolException, sympy.SympifyError) as e:
            await interaction.response.send_message(f"Invalid algebraic expression: {e}")
        except Exception as e:
            await interaction.response.send_message(f"An unexpected error occurred: {e}")

    @solve_slash.subcommand(name="calculus", description="Solves calculus problems.")
    async def solve_calculus(self, interaction: nextcord.Interaction):
        pass # Sub-subcommands will be added here

    @solve_calculus.subcommand(name="diff", description="Calculates the derivative of an expression.")
    async def solve_diff(self, interaction: nextcord.Interaction, expression: str, variable: str):
        """Calculates the derivative of an expression via a slash command."""
        try:
            x = Symbol(variable)
            result = diff(sympy.sympify(expression), x)
            await interaction.response.send_message(f"The derivative of {expression} with respect to {variable} is: {result}")
        except (sympy.parsing.mathematica.UnrecognizedSymbolException, sympy.SympifyError) as e:
            await interaction.response.send_message(f"Invalid expression or variable: {e}")
        except Exception as e:
            await interaction.response.send_message(f"An unexpected error occurred: {e}")

    @solve_calculus.subcommand(name="integrate", description="Calculates the integral of an expression.")
    async def solve_integrate(self, interaction: nextcord.Interaction, expression: str, variable: str):
        """Calculates the integral of an expression via a slash command."""
        try:
            x = Symbol(variable)
            result = integrate(sympy.sympify(expression), x)
            await interaction.response.send_message(f"The integral of {expression} with respect to {variable} is: {result}")
        except (sympy.parsing.mathematica.UnrecognizedSymbolException, sympy.SympifyError) as e:
            await interaction.response.send_message(f"Invalid expression or variable: {e}")
        except Exception as e:
            await interaction.response.send_message(f"An unexpected error occurred: {e}")

    @commands.command()
    async def solve(self, ctx, *, math_expression: str):
        """Solves a mathematical expression (supports +, -, *, /, ^, basic functions, algebra, and basic calculus using prefixes like 'diff' and 'integrate')."""
        try:
            if math_expression.startswith("diff "):
                parts = math_expression.split()
                if len(parts) >= 3:
                    expression_str = parts[1]
                    variable_str = parts[2]
                    x = Symbol(variable_str)
                    expression = sympy.sympify(expression_str)
                    result = diff(expression, x)
                    await ctx.send(f"The derivative of {expression_str} with respect to {variable_str} is: {result}")
                else:
                    await ctx.send("Invalid differentiation format. Use: `solve diff <expression> <variable>`")
                return
            elif math_expression.startswith("integrate "):
                parts = math_expression.split()
                if len(parts) >= 3:
                    expression_str = parts[1]
                    variable_str = parts[2]
                    x = Symbol(variable_str)
                    expression = sympy.sympify(expression_str)
                    result = integrate(expression, x)
                    await ctx.send(f"The integral of {expression_str} with respect to {variable_str} is: {result}")
                else:
                    await ctx.send("Invalid integration format. Use: `solve integrate <expression> <variable>`")
                return

            # Default to solving algebraic or numerical expressions
            expression = sympy.sympify(math_expression)
            result = expression.evalf()
            await ctx.send(f"The result is: {result}")
        except (sympy.parsing.mathematica.UnrecognizedSymbolException, sympy.SympifyError) as e:
            await ctx.send(f"Invalid mathematical expression: {e}")
        except nextcord.HTTPException as e:
            await ctx.send(f"Error occurred while sending message: {e}")
        except Exception as e:
            await ctx.send(f"An unexpected error occurred: {e}")

    @commands.command()
    async def whois(self, ctx, *, user: nextcord.Member = None):
        """Returns information about a specific user."""
        if user is None:
            user = ctx.author

        embed = nextcord.Embed(title=user.name, color=nextcord.Color.dark_gray())
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.add_field(name="User ID", value=user.id, inline=False)
        embed.add_field(name="Discriminator", value=user.discriminator, inline=False)
        embed.add_field(name="Account Created At", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S UTC"), inline=False)

        if isinstance(user, nextcord.Member) and ctx.guild:
            embed.add_field(name="Nickname", value=user.nick if user.nick else "None", inline=False)
            embed.add_field(name="Joined Server At", value=user.joined_at.strftime("%Y-%m-%d %H:%M:%S UTC"), inline=False)
            roles = [role.name for role in user.roles if role != ctx.guild.default_role]
            if roles:
                embed.add_field(name="Roles", value=", ".join(roles), inline=False)
            embed.add_field(name="Top Role", value=user.top_role.name, inline=False)
            embed.add_field(name="Is Bot", value=user.bot, inline=False)
            embed.add_field(name="Is Owner", value=user == ctx.guild.owner, inline=False)

        await ctx.send(embed=embed)

    @nextcord.slash_command(name="whois", description="Returns information about a specific user.")
    async def whois_slash(self, interaction: nextcord.Interaction, user: nextcord.Member = nextcord.SlashOption(required=False, description="Member to show information of.")):
        """Returns information about a specific user (slash command)."""
        if user is None:
            user = interaction.user

        embed = nextcord.Embed(title=user.name, color=nextcord.Color.dark_gray())
        embed.set_thumbnail(url=user.display_avatar.url)
        embed.add_field(name="User ID", value=user.id, inline=False)
        embed.add_field(name="Discriminator", value=user.discriminator, inline=False)
        embed.add_field(name="Account Created At", value=user.created_at.strftime("%Y-%m-%d %H:%M:%S UTC"), inline=False)

        if interaction.guild:
            member = interaction.guild.get_member(user.id)
            if member:
                embed.add_field(name="Nickname", value=member.nick if member.nick else "None", inline=False)
                embed.add_field(name="Joined Server At", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S UTC"), inline=False)
                roles = [role.name for role in member.roles if role != interaction.guild.default_role]
                if roles:
                    embed.add_field(name="Roles", value=", ".join(roles), inline=False)
                embed.add_field(name="Top Role", value=member.top_role.name, inline=False)
                embed.add_field(name="Is Bot", value=member.bot, inline=False)
                embed.add_field(name="Is Owner", value=member == interaction.guild.owner, inline=False)

        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(MiscCommands(bot))
