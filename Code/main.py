import nextcord
import random
import nextcord
from nextcord import *
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from config import *
import keep_alive
keep_alive.keep_alive()


client = commands.Bot(command_prefix='mc!')

testingserver = 927316756027035699

@client.slash_command(description="Add numbers!", guild_ids=None)
async def addnumbers(interaction : Interaction, number1 : int, number2 : int):
  await interaction.response.send_message(f'```Answer: {number1+number2}```', ephemeral=True)

@client.slash_command(description="Subtract numbers!", guild_ids=None)
async def subtractnumbers(interaction : Interaction, subtractfrom : int, subtractionamount : int):
  await interaction.response.send_message(f'```Answer: {subtractfrom-subtractionamount}```', ephemeral=True)

@client.slash_command(description="Multiply numbers!", guild_ids=None)
async def multiplynumbers(interaction : Interaction, multiply : int, by : int):
  await interaction.response.send_message(f'```Answer: {multiply*by}```', ephemeral=True)

@client.slash_command(description="Divide numbers!", guild_ids=None)
async def dividenumbers(interaction : Interaction, dividend : int, divisor : int):
  await interaction.response.send_message(f"```Answer: {dividend/divisor}```", ephemeral=True)

@client.slash_command(description="Credits for the bot.")
async def credits(interaction : Interaction):
  embed = nextcord.Embed(title="Credits", description="Credits for the bot!", color=nextcord.Color.green())
  embed.add_field(name="uptimerobot.com", value="Hosting")
  embed.add_field(name="<https://www.youtube.com/watch?v=gamozdALD9I>", value="uptimerobot.com tutorial")
  embed.add_field(name="repl.it", value="Hosting")
  embed.add_field(name="https://medium.com/geekculture/solving-math-problems-using-python-quick-code-python-52b1b37a79d5", value="Celsius to Fahrenheit code & idea for Celsius to Fahrenheit and Fahrenheit to Celsius")
  embed.add_field(name="https://www.pythonforbeginners.com/code-snippets-source-code/python-code-celsius-and-fahrenheit-converter", value="Fahrenheit to Celsius code")
  embed.add_field(name="<@436312795076886528>", value="Random choice numbers command idea")
  await interaction.response.send_message(embed=embed, ephemeral=True)


@client.slash_command(description="DEV ONLY - STATUS CHANGE")
@commands.has_role(920449565633687612)
async def statuschange(interaction : Interaction):
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.listening, name="bot math commands"))
    embed = nextcord.Embed(title="Status Change", description=f"Accepted, I assume!", color=nextcord.Color.green())
    await interaction.response.send_message(embed=embed, ephemeral=False)

@client.slash_command(description="Celcius to Fahrenheit")
async def celsiustofahrenheit(interaction : Interaction, celsius : int):
  calccelcius = 9.0/5.0 * celsius + 32
  await interaction.response.send_message(f"```Answer: {calccelcius}```", ephemeral=True)

@client.slash_command(description="Fahrenheit to Celcius")
async def fahrenheittocelcius(interaction : Interaction, fahrenheit : int):
  calfahrenheit = (fahrenheit - 32) * 5.0/9.0
  await interaction.response.send_message(f"```Answer: {calfahrenheit}```", ephemeral=True)

@client.slash_command(description="Random answer with the numbers!")
async def randomchoicenumbers(interaction : Interaction, number1 : int, number2 : int):
  randomchoicenumberslist = [f"```Answer: {number1+number2}, for addition```", f"```Answer: {number1*number2}, for multiplication```", f"```Answer: {number1/number2}, for division```", f"```Answer: {number1-number2}, for subtraction```"]
  await interaction.response.send_message(random.choice(randomchoicenumberslist), ephemeral=True)

client.run('BOT_TOKEN')  
