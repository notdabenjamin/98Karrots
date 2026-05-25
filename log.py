import discord
from discord import app_commands
from discord.ext import commands

version = "1.0.0"

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.default())

        
    async def setup_hook(self):
        await self.tree.sync()

bot = MyBot()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}\n\nLogs:\n')
    await bot.change_presence(
        status=discord.Status.online, 
        activity=discord.Activity(type=discord.ActivityType.listening, name="voted #1 best discord bot out of all 3 of them")
    )
    print("SYSTEM: Presence set successfully.")

# /meow | meow
@bot.tree.command(name="meow", description="meow")
async def word(interaction: discord.Interaction):
    print(f"{interaction.user}: /meow | {interaction.channel} | Response: meow")
    await interaction.response.send_message("meow")

# /about | About 98Karrots
@bot.tree.command(name="about", description="About 98Karrots")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def info(interaction: discord.Interaction):
    embed = discord.Embed(
        title="About 98Karrots",
        description="98Karrots is a meme bot meant to add personalization to your server.\n\nCreated by NotDaBenjamin\n© 2026 NotDaBenjamin\nThis project is licesned under the MIT License.",
        color=discord.Color.red()
    )
    
    embed.add_field(name="Important commands", value="/about - This!\n/privacy - THE MOST IMPORTANT COMMAND, this shows what is logged when adding the bot.\n/add - Add the bot!\n/commands - Shows all commands!", inline=True)
    embed.add_field(name="Info", value="Website: https://notdb.pages.dev/98/w\nTerms: https://notdb.pages.dev/98/t\nWhat is logged?/Privacy Policy: https://notdb.pages.dev/98/wil\n More Projects: https://tr.ee/notdabenjamin\n Source Code: https://notdb.pages.dev/98/c", inline=True)
    
    embed.set_footer(text=f"Version: {version}\nRequested by {interaction.user.name}")
    embed.set_thumbnail(url="https://notdabenjamin.neocities.org/img/projects/98karrots.png")
    
    print(f"{interaction.user}: /about | {interaction.channel} | Response: About 98Karrots - EMBED")
    await interaction.response.send_message(embed=embed)

# /privacy | Privacy Policy
@bot.tree.command(name="privacy", description="Privacy Policy")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def privacy(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Privacy Policy",
        description="Note: When the bot is offline, commands can not be ran and nothing is Logged, I have tried my best to minimize the amount of data that is collected when a command is ran.\nBelow is a list of what is logged and what isn't. The data that is collected is used to help improve the bot and fix bugs.\nIf you have any questions about the privacy policy or what is logged, email notdabenjamin@gmail.com for support.\nAny collection of data tied to the bot, but not on Discord is mentioned in the Privacy Policy: https://notdb.pages.dev/98/wil",
        color=discord.Color.red()
    )
    
    embed.add_field(name="What is logged", value="✅User who ran a specific command (NOT NICKNAME IN SERVER)\n✅Name of the channel where the command was used\n✅The command that was used\n✅The response given by the bot", inline=True)
    embed.add_field(name="What isn't logged", value="❌Server name\n❌Server ID\n❌User ID\n❌User avatar URL\n❌Message ID\n❌Any other messages not related to the bots activity (Including messages sent before and after the command, non-command messages will never be logged)", inline=True)
    embed.add_field(name="Logging is", value="✅Enabled", inline=True)

    
    embed.set_footer(text=f"Version: {version}\nRequested by {interaction.user.name}")
    embed.set_thumbnail(url="https://notdabenjamin.neocities.org/img/projects/98karrots.png")
    
    print(f"{interaction.user}: /privacy | {interaction.channel} | Response: Privacy Policy - EMBED")
    await interaction.response.send_message(embed=embed)

# /whoknows | Who Knows?
@bot.tree.command(name="whoknows", description="Who Knows?")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def sendfile(interaction: discord.Interaction):
    await interaction.response.defer()

    file = discord.File("who_knows_v3.mov")

    await interaction.followup.send(
        file=file
    )
    print(f"{interaction.user}: /whoknows | {interaction.channel} | Response: who_knows_v3.mov")

# /whoasked | Like genuinely who asked?
@bot.tree.command(name="whoasked", description="Like genuinely who asked?")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def whoasked(interaction: discord.Interaction):
    await interaction.response.defer()

    file = discord.File("who_asked.mov")

    await interaction.followup.send(
        file=file
    )
    print(f"{interaction.user}: /whoasked | {interaction.channel} | Response: who_asked.mov")

# /amogus | #reviveamogus
@bot.tree.command(name="amogus", description="#reviveamogus")
@app_commands.allowed_contexts(
    guilds=True,
    dms=True,
    private_channels=True
)
async def whoasked(interaction: discord.Interaction):
    await interaction.response.defer()

    file = discord.File("amogus.png")

    await interaction.followup.send(
        content="<a:amonguschairspin:1508320990306766858><a:amongus3d:1508321342137831445><:amogus:1508321339348488192>",
        file=file
    )
    print(f"{interaction.user}: /amogus | {interaction.channel} | Response: amogus.png")

# DMs Response
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        await message.channel.send(f"Hello, {message.author.name}!\n\nThis bot is not meant to be used in DMs, for questions or support, please join the Discord server https://discord.com/invite/T3Xd3WHgXK or email notdabenjamin@gmail.com!\n\nPLEASE DO NOT USE THIS BOT IN DMs, AS IT CAUSES SERVERS TO SPIT OUT ERRORS AS LOGS, CAUSING CONFUSION.\n\n-# This is an automated message.")

    print(f"{message.author} | DM | Response: Hello, message.author.name! This bot is not meant to be used in DMs, for questions...")
    await bot.process_commands(message)

bot.run('no-token-4-u')
