# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import math
# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Basic Bot by Habchy#1665", command_prefix="$", pm_help = False)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	print('Support Discord Server: https://discord.gg/FNNNgqb')
	print('Github Link: https://github.com/Habchy/BasicBot')
	print('--------')
	print('You are running ElloBot v0.1') #Do not change this. This will really help us support you, if you need support.
	print('Created by Habchy#1665, modified by AddyPaddy')
	return await client.change_presence(game=discord.Game(name='Wassup!!!')) #This is buggy, let us know if it doesn't work.

# This is a basic example of a call and response command. You tell it do "this" and it does it.
	
@client.command()
async def ping(*args):

	await client.say(":ping_pong: Pong!")
	await asyncio.sleep(3)

@client.command()
async def add(a1, b1):
	a=eval(a1)
	b=eval(b1)
	await client.say(a+b)
	
@client.command()
async def greet():
	await client.say(":smiley: :wave: Hello, there!")
	
@client.command()
async def cat_funny():
	await client.say("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
	
@client.command()
async def multiply(a: int, b: int):

	await client.say(a*b)
	
@client.command()
async def subtract(a: int, b: int):
	await client.say(a-b)
	
@client.command()
async def divide(a: int, b: int):
	await client.say(a/b)

@client.command()
async def modulus(a: int, b: int):
	await client.say(a%b)

@client.command()
async def hello():
	await client.say("Hi there!!!")
	
@client.command()
async def glowing_eyes():
	await client.say("http://i0.kym-cdn.com/photos/images/newsfeed/001/354/102/824.gif")
	
@client.command()
async def beam_me_up_scotty():
	await client.say("**ENERGIZING!!!!**")
	await asyncio.sleep(2)
	await client.say(". . .")
	await asyncio.sleep(2)
	await client.say("DONE!!!")

@client.command()
async def whoami():
    await client.say("I am a bot that doesn't make any sense.")


@client.command()
async def WTF():
        await client.send_message(message.channel, "What the fuck {0.author.mention}")
	# After you have modified the code, feel free to delete the line above so it does not keep popping up everytime you initiate the ping commmand.
	
client.run('<your discord bot token>')

# Basic Bot was created by Habchy#1665
# Please join this Discord server if you need help: https://discord.gg/FNNNgqb
# Please modify the parts of the code where it asks you to. Example: The Prefix or The Bot Token
# This is by no means a full bot, it's more of a starter to show you what the python language can do in Discord.
# Thank you for using this and don't forget to star my repo on GitHub! [Repo Link: https://github.com/Habchy/BasicBot]

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.
