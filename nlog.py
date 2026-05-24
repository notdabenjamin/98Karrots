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
    print(f'Logged in as {bot.user.name}\n\nLogs are disabled.\n')

@bot.tree.command(name="meow", description="meow")
async def word(interaction: discord.Interaction):
    await interaction.response.send_message("meow")

@bot.tree.command(name="about", description="About 98Karrots")
async def info(interaction: discord.Interaction):
    embed = discord.Embed(
        title="About 98Karrots",
        description="98Karrots is a meme bot meant to add personalization to your server.\n\nCreated by NotDaBenjamin\n© 2026 NotDaBenjamin\nThis project is licesned under the MIT License.",
        color=discord.Color.blue()
    )
    
    embed.add_field(name="Important commands", value="/about - This!\n/privacy - THE MOST IMPORTANT COMMAND, this shows what is logged when adding the bot.\n/add - Add the bot!\n/commands - Shows all commands!", inline=True)
    embed.add_field(name="Info", value="Website: https://notdabenjamin.neocities.org/98karrots\nTerms: https://notdabenjamin.neocities.org/98karrots/terms\nWhat is logged?: https://notdabenjamin.neocities.org/98karrots/whatislogged\n More Projects: https://notdabenjamin.neocities.org/\n Source Code: https://github.com/NotDaBenjamin/98Karrots", inline=True)
    
    embed.set_footer(text=f"Version: {version}\nRequested by {interaction.user.name}")
    embed.set_thumbnail(url="https://notdabenjamin.neocities.org/img/projects/98karrots.png")
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="privacy", description="Privacy Policy")
async def privacy(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Privacy Policy",
        description="Note: When the bot is offline, commands can not be ran and nothing is Logged, I have tried my best to minimize the amount of data that is collected when a command is ran. Below is a list of what is logges and what isn't. The data that is collected is used to help improve the bot and fix bugs. If you have any questions about the privacy policy or what is logged, email notdabenjamin@gmail.com for support. Any collection of data tied to the bot, but not on Discord is mentioned in the Privacy Policy: https://notdb.pages.dev/98/wil",
        color=discord.Color.red()
    )
    
    embed.add_field(name="What is logged", value="✅User who ran a specific command (NOT NICKNAME IN SERVER)\n✅Name of the channel where the command was used\n✅The command that was used\n✅The response given by the bot", inline=True)
    embed.add_field(name="What isn't logged", value="❌Server name\n❌Server ID\n❌User ID\n❌User avatar URL\n❌Message ID", inline=True)
    embed.add_field(name="Logging is", value="❌Disabled", inline=True)

    
    embed.set_footer(text=f"Version: {version}\nRequested by {interaction.user.name}")
    embed.set_thumbnail(url="https://notdabenjamin.neocities.org/img/projects/98karrots.png")
    
    await interaction.response.send_message(embed=embed)


# Run the bot with your Discord Token
bot.run('haha-stupid-no-token-4-u')
