import nextcord
from nextcord.ext import commands
import random
import sympy
from sympy.parsing.mathematica import parse_mathematica

class MiscCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
    async def echo_slash(self, interaction: nextcord.Interaction, message: str):
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
    async def roast_slash(self, interaction: nextcord.Interaction, member: nextcord.Member):
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
        """Shows information about the bot."""
        try:
            embed = nextcord.Embed(
                title="About the Bot",
                description="This is a fun bot with various commands.",
                color=nextcord.Color.blue()
            )
            embed.add_field(name="Version", value="3.5.4", inline=False)
            embed.add_field(name="Author", value="Kiryu Kazuma & Darkin", inline=False)
            embed.add_field(name="Hosted by", value="Render.com & GitHub", inline=False)
            await ctx.send(embed=embed)
        except nextcord.HTTPException as e:
            await ctx.send(f"Error occurred while sending embed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred in about command: {e}")
            await ctx.send("An unexpected error occurred.")

    @nextcord.slash_command(name="about", description="Shows information about the bot.")
    async def about_slash(self, interaction: nextcord.Interaction):
        """Shows information about the bot via a slash command."""
        try:
            embed = nextcord.Embed(
                title="About the Bot",
                description="""This is a fun bot with various commands.

                **Version**
                3.5.4

                **Author**
                Made by <@1221614686865461259>

                **Hosted by**
                https://github.com/
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
`l!dad`: A silly command.
`l!roll [min] [max]`: Rolls a random number between the specified range (default 1-100).
`l!joke`: Tells a random joke.
`l!fact`: Shows a random fact.
`l!roast <@member>`: Roasts the mentioned member.
`l!solve <expression>`: Solves a mathematical expression (supports +, -, *, /, ^, basic functions).
`l!honestreaction`: Shows a video about "My Honest Reaction 🗿". (Note: This command is not implemented in this cog)

__Admin Commands__
Moderation commands for server management.
`l!ban <@member> [reason]`: Bans a member from the server.
`l!kick <@member> [reason]`: Kicks a member from the server.
`l!warn <@member> [reason]`: Warns a member.
`l!clearwarns <@member>`: Clears the warnings of a user.
`l!lock`: Locks the current channel.
`l!unlock`: Unlocks the current channel.
`l!addrole <@member> <role name>`: Adds a role to a user.
`l!removerole <@member> <role name>`: Removes a role from a user.
`l!slowmode <seconds>`: Sets a slow mode for the channel.
`l!clear <amount>`: Clears a specified number of messages.
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
        try:
            description = """
__Fun Commands__
Commands that are for fun
`/dad`: A silly command.
`/roll [min] [max]`: Rolls a random number between the specified range (default 1-100).
`/fact`: Shows a random fact about the world.
`/joke`: Tells you a random joke.
`/roast <user>`: Tells a friendly roast.
`/solve <expression>`: Solves a mathematical expression.
`/train`: Show's a video about an edit of the A-Train
__Admin Commands__
Moderation commands for this bot.
`/ban <user> [reason]`: Bans a member, self explanatory
`/kick <user> [reason]`: Pretty self explanatory
`/warn <user> [reason]`: Warns a member, if a member gets 3 warns they will get kicked if they get 6 warns they will get banned.
`/clearwarns <user>`: Clear's the warns of a user
`/lock`: Locks a channel
`/unlock`: Unlocks a channel
`/addrole <user> <role>`: Add's a role to a user
`/removerole <user> <role>`: Remove's a role from a user
`/slowmode <seconds>`: Add's a slowmode to a channel
`/clear <amount>`: Clear's a specified amount of messages
"""

            embed = nextcord.Embed(
                title='__Commands__',
                description=description,
                color=nextcord.Color.from_rgb(47, 49, 54),
            )

            embed.set_author(name="By Kiryu Kazuma and Darkin")

            await interaction.response.send_message(embed=embed, ephemeral=True)
            await interaction.followup.send("A help message with a list of commands has been sent to you privately!", ephemeral=True)
        except nextcord.HTTPException as e:
            await interaction.followup.send(f"Error occurred while sending embed or message: {e}", ephemeral=True)
        except Exception as e:
            print(f"An unexpected error occurred in help_slash command: {e}")
            await interaction.followup.send("An unexpected error occurred.", ephemeral=True)

    @commands.command()
    async def solve(self, ctx, *, math_expression: str):
        """Solves a mathematical expression using sympy."""
        try:
            # Use sympy.sympify to parse the expression
            expression = sympy.sympify(math_expression)
            # Evaluate the expression to get a numerical result
            result = expression.evalf()
            await ctx.send(f"The result is: {result}")
        except (sympy.parsing.mathematica.UnrecognizedSymbolException, sympy.SympifyError) as e:
            await ctx.send(f"Invalid mathematical expression: {e}")
        except nextcord.HTTPException as e:
            await ctx.send(f"Error occurred while sending message: {e}")
        except Exception as e:
            print(f"An unexpected error occurred in solve command: {e}")
            await ctx.send("An unexpected error occurred.")

    @nextcord.slash_command(name="solve", description="Solves a math expression.")
    async def solve_slash(self, interaction: nextcord.Interaction, math_expression: str):
        """Solves a mathematical expression using sympy via a slash command."""
        try:
            expression = sympy.sympify(math_expression)
            result = expression.evalf()
            await interaction.response.send_message(f"The result is: {result}")
        except (sympy.parsing.mathematica.UnrecognizedSymbolException, sympy.SympifyError) as e:
            await interaction.response.send_message(f"Invalid mathematical expression: {e}")
        except nextcord.HTTPException as e:
            await interaction.followup.send(f"Error occurred while sending message: {e}", ephemeral=True)
        except Exception as e:
            print(f"An unexpected error occurred in solve_slash command: {e}")
            await interaction.followup.send("An unexpected error occurred.", ephemeral=True)

def setup(bot):
    bot.add_cog(MiscCommands(bot))
