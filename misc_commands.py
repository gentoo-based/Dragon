import nextcord
from nextcord.ext import commands
import random

class MiscCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, *, message: str):
        await ctx.message.delete()
        await ctx.send(f"{message}")

    @nextcord.slash_command(name="echo", description="Echoes your message back to you.")
    async def echo_slash(self, interaction: nextcord.Interaction, message: str):
        await interaction.response.send_message(f"{message}")
    @commands.command()
    async def joke(self, ctx):
        jokes = ["Why don't scientists trust atoms? Because they make up everything!", "Why did the chicken go to the seance? To talk to the other side!"]
        await ctx.send(random.choice(jokes))

    @commands.command()
    async def fact(self, ctx):
        facts = ["Did you know? The Eiffel Tower can be 15 cm taller during the summer.", "Did you know? Honey never spoils."]
        await ctx.send(random.choice(facts))

    @commands.command()
    async def roast(self, ctx, member: nextcord.Member):
        roasts = [
            "u so ugly china ate u instead of dogs",
            "u built like a diabolical elephant",
            "u dont get woman pregnant u give them worms cuz of your ugly ass",
            "u so weird and ugly hello kitty said goodbye kitty",
            "u so ugly babies ignore u"
        ]
        roast = random.choice(roasts)
        await ctx.send(f"{member.mention} {roast}")


    @commands.command()
    async def about(self, ctx):
        embed = nextcord.Embed(title="About the Bot", description="This is a fun yakuza bot that supports a lot of commands.", color=nextcord.Color.blue())
        embed.add_field(name="Version", value="3.5.2", inline=False)
        embed.add_field(name="Author", value="The Dragon of Dojima (Kiryu Kazuma)", inline=False)
        embed.add_field(name="Hosted by", value="https://render.com", inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        try:
            embed = nextcord.Embed(
                title='__Commands__',
                description='These are the commands for the bot.',
                color=nextcord.Color.from_rgb(47, 49, 54),
            )
        
            embed.set_author(name="By Kiryu Kazuma and Darkin")
        
            embed.add_field(name='__Fun Commands__', value='Commands that are for fun', inline=False)     
            embed.add_field(name='l!dad', value='Roasts you for being a dumbass and thinking you have a dad.', inline=False)
        
            embed.add_field(name='l!bakamitai', value='Show\'s a video about kiryu singing baka mitai', inline=False)     
            embed.add_field(name='l!awakening', value='Show\'s a video about Kiryu\'s Legend Style "Dragon of Dojima" first appearance.', inline=False)     
            embed.add_field(name='l!sugarcoat', value='Show\'s a video about kiryu singing baka mitai', inline=False)     
            embed.add_field(name='l!egg', value='An egg command, pretty self explanatory', inline=False)     
            embed.add_field(name='l!kys', value='A command that shows low tier god roasting you', inline=False)     
            embed.add_field(name='l!tys', value='A command that shows low tier god complimenting you', inline=False)     
            embed.add_field(name='l!notsugarcoating', value='Show\'s a video of Kiryu not sugarcoating against majima', inline=False)     
            embed.add_field(name='l!scream', value='Show\'s a video singing today is a diamond but kiryu screaming credits to takayuki yagami for this idea', inline=False)     
            embed.add_field(name='l!roll', value='Rolls from a number to another number, pretty self explanatory', inline=False)                         
            embed.add_field(name='l!ip', value='Show\'s a video of captain underpants dancing while grabbing your ip', inline=False)     
            embed.add_field(name='l!china', value='Show\'s a video about the meme "China Airlines"', inline=False)   
            embed.add_field(name='l!dance', value='Show\'s 2 videos about kiryu dancing', inline=False)   
            embed.add_field(name='l!disagree', value='Show\'s a gif of ichiban not agreeing to your opinion', inline=False)   
            embed.add_field(name='l!yakuzillionaire', value='Show\'s a video of a meme of "yakuzillionaire"', inline=False)     
            embed.add_field(name='l!yakuza_fans', value='Show\'s a video of yakuza fans', inline=False)     
            embed.add_field(name='l!fact', value='Show\'s a random fact about the world.', inline=False)     
            embed.add_field(name='l!intro', value='Show\'s a video about kiryu\'s first appearance in Yakuza 7.', inline=False)     
            embed.add_field(name='l!joke', value='Tells you a random joke.', inline=False)     
            embed.add_field(name='l!solve', value='Solve\'s any math problem, it only supports multiplication, addition and division. For multiplication you\'ll you have to use an asterisk "*" ', inline=False)     
            embed.add_field(name='l!train', value='Show\'s a video about an edit of the A-Train', inline=False)     
            embed.add_field(name='l!n_word', value='Show\'s a video about the meme spot becoming black and saying ni-', inline=False)     
            embed.add_field(name='l!honestreaction', value='Show\'s a video about "My Honest Reaction 🗿"', inline=False)
        
            embed2 = nextcord.Embed(
                title='__Admin Commands__',
                description='Moderation commands for this bot.',
                color=nextcord.Color.from_rgb(47, 49, 54),
            )
            embed2.add_field(name='l!ban', value='Bans a member, self explanatory', inline=False)     
            embed2.add_field(name='l!kick', value='Pretty self explanatory', inline=False)     
            embed2.add_field(name='l!warn', value='Warns a member, if a member gets 3 warns they will get kicked if they get 6 warns they will get banned.', inline=False)     
            embed2.add_field(name='l!clearwarns', value='Clear\'s the warns of a user', inline=False)     
            embed2.add_field(name='l!lock', value='Locks a channel', inline=False)     
            embed2.add_field(name='l!unlock', value='Unlocks a channel', inline=False)     
            embed2.add_field(name='l!addrole', value='Add\'s a role to a user', inline=False)     
            embed2.add_field(name='l!removerole', value='Remove\'s a role from a user', inline=False)     
            embed2.add_field(name='l!slowmode', value='Add\'s a slowmode to a channel', inline=False)     
            embed2.add_field(name='l!clear', value='Clear\'s a specified amount of messages', inline=False)
        
            await ctx.author.send(embed=embed)
            await ctx.author.send(embed=embed2)
        
            await ctx.send('Check your dms')
        except nextcord.Forbidden:
            await ctx.send('Bro your dms closed')
        
    @nextcord.slash_command(name="joke", description="Tells a random joke.")
    async def joke_slash(self, interaction: nextcord.Interaction):
        jokes = ["Why don't scientists trust atoms? Because they make up everything!", "Why did the chicken go to the seance? To talk to the other side!"]
        await interaction.response.send_message(random.choice(jokes))

    @nextcord.slash_command(name="fact", description="Tells a random fact.")
    async def fact_slash(self, interaction: nextcord.Interaction):
        facts = ["Did you know? The Eiffel Tower can be 15 cm taller during the summer.", "Did you know? Honey never spoils."]
        await interaction.response.send_message(random.choice(facts))

    @nextcord.slash_command(name="roast", description="Tells a friendly roast.")
    async def roast_slash(self, interaction: nextcord.Interaction, member: nextcord.Member):
        roasts = [
            "u so ugly china ate u instead of dogs",
            "u built like a diabolical elephant",
            "u dont get woman pregnant u give them worms cuz of your ugly ass",
            "u so weird and ugly hello kitty said goodbye kitty",
            "u so ugly babies ignore u"
        ]
        roast = random.choice(roasts)
        await ctx.send(f"{member.mention} {roast}")


    @nextcord.slash_command(name="about", description="Shows information about the bot.")
    async def about_slash(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(title="About the Bot", description="This is a fun yakuza bot that supports a lot of commands.", color=nextcord.Color.blue())
        embed.add_field(name="Version", value="3.5.2", inline=False)
        embed.add_field(name="Author", value="The Dragon of Dojima (Kiryu Kazuma)", inline=False)
        embed.add_field(name="Hosted by", value="https://render.com", inline=False)
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name="help", description="Shows the list of commands.")
    async def help_slash(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(
            title='__Commands__',
            description='These are the commands for the bot.',
            color=nextcord.Color.from_rgb(47, 49, 54),
        )
    
        embed.set_author(name="By Kiryu Kazuma and Darkin")
    
        embed.add_field(name='__Fun Commands__', value='Commands that are for fun', inline=False)     
        embed.add_field(name='l!dad', value='Roasts you for being a dumbass and thinking you have a dad.', inline=False)
    
        embed.add_field(name='l!bakamitai', value='Show\'s a video about kiryu singing baka mitai', inline=False)     
        embed.add_field(name='l!awakening', value='Show\'s a video about Kiryu\'s Legend Style "Dragon of Dojima" first appearance.', inline=False)     
        embed.add_field(name='l!sugarcoat', value='Show\'s a video about kiryu singing baka mitai', inline=False)     
        embed.add_field(name='l!egg', value='An egg command, pretty self explanatory', inline=False)     
        embed.add_field(name='l!kys', value='A command that shows low tier god roasting you', inline=False)     
        embed.add_field(name='l!tys', value='A command that shows low tier god complimenting you', inline=False)     
        embed.add_field(name='l!notsugarcoating', value='Show\'s a video of Kiryu not sugarcoating against majima', inline=False)     
        embed.add_field(name='l!scream', value='Show\'s a video singing today is a diamond but kiryu screaming credits to takayuki yagami for this idea', inline=False)     
        embed.add_field(name='l!roll', value='Rolls from a number to another number, pretty self explanatory', inline=False)                         
        embed.add_field(name='l!ip', value='Show\'s a video of captain underpants dancing while grabbing your ip', inline=False)     
        embed.add_field(name='l!china', value='Show\'s a video about the meme "China Airlines"', inline=False)   
        embed.add_field(name='l!dance', value='Show\'s 2 videos about kiryu dancing', inline=False)   
        embed.add_field(name='l!disagree', value='Show\'s a gif of ichiban not agreeing to your opinion', inline=False)   
        embed.add_field(name='l!yakuzillionaire', value='Show\'s a video of a meme of "yakuzillionaire"', inline=False)     
        embed.add_field(name='l!yakuza_fans', value='Show\'s a video of yakuza fans', inline=False)     
        embed.add_field(name='l!fact', value='Show\'s a random fact about the world.', inline=False)     
        embed.add_field(name='l!intro', value='Show\'s a video about kiryu\'s first appearance in Yakuza 7.', inline=False)     
        embed.add_field(name='l!joke', value='Tells you a random joke.', inline=False)     
        embed.add_field(name='l!solve', value='Solve\'s any math problem, it only supports multiplication, addition and division. For multiplication you\'ll you have to use an asterisk "*" ', inline=False)     
        embed.add_field(name='l!train', value='Show\'s a video about an edit of the A-Train', inline=False)     
        embed.add_field(name='l!n_word', value='Show\'s a video about the meme spot becoming black and saying ni-', inline=False)     
        embed.add_field(name='l!honestreaction', value='Show\'s a video about "My Honest Reaction 🗿"', inline=False)
    
        embed2 = nextcord.Embed(
            title='__Admin Commands__',
            description='Moderation commands for this bot.',
            color=nextcord.Color.from_rgb(47, 49, 54),
        )
        embed2.add_field(name='l!ban', value='Bans a member, self explanatory', inline=False)     
        embed2.add_field(name='l!kick', value='Pretty self explanatory', inline=False)     
        embed2.add_field(name='l!warn', value='Warns a member, if a member gets 3 warns they will get kicked if they get 6 warns they will get banned.', inline=False)     
        embed2.add_field(name='l!clearwarns', value='Clear\'s the warns of a user', inline=False)     
        embed2.add_field(name='l!lock', value='Locks a channel', inline=False)     
        embed2.add_field(name='l!unlock', value='Unlocks a channel', inline=False)     
        embed2.add_field(name='l!addrole', value='Add\'s a role to a user', inline=False)     
        embed2.add_field(name='l!removerole', value='Remove\'s a role from a user', inline=False)     
        embed2.add_field(name='l!slowmode', value='Add\'s a slowmode to a channel', inline=False)     
        embed2.add_field(name='l!clear', value='Clear\'s a specified amount of messages', inline=False)
    
        await interaction.response.send_message(embed=embed)
        await interaction.response.send_message(embed=embed2)
    
    @commands.command()
    async def solve(self, ctx, *, math_expression: str):
        try:
            result = eval(math_expression)
            await ctx.send(f"The result is: {result}")
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")

    @nextcord.slash_command(name="solve", description="Solves a math expression.")
    async def solve_slash(self, interaction: nextcord.Interaction, math_expression: Option(str, "The math expression to solve")):
        try:
            result = eval(math_expression)
            await interaction.response.send_message(f"The result is: {result}")
        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {str(e)}")
def setup(bot):
    bot.add_cog(MiscCommands(bot))
