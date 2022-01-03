# similar to c++'s #include <standard_header> or "local_header.hpp"
import os # provides OS dependent functionality, such returning value from environmental variable key-value pair
import discord # discord API wrapper, makes Discord API easy to use
from dotenv import load_dotenv # load environmental variables from local .env file
import random
from sys import exc_info # to write more information to err.log

# Looked at discordpy.readthedocs.io, docs.python.org, pypi.org to understand what these modules and functions do

load_dotenv() # loads data from .env file in local directory, which contains # DISCORD_TOKEN contains the thing required for this program to connect to Discord
TOKEN = os.getenv('DISCORD_TOKEN') # returns value corresponding to the environmental variable argument given in the string
GUILD = os.getenv('DISCORD_GUILD')

# looking at discord.py docs, creating this subclass makes more sense to me # 2 ways to register events are to use discord.Client.event, or to create a discord.Client subclass
class MyClient(discord.Client): # creating a subclass. Can't use code directly, must create a class instance first.		
	async def on_ready(self): # functions seem to take the class itself as default argument
		# for loop to get guild variable to contain active guild
		for guild in self.guilds:
			if guild.name == GUILD: # guild variable not limited to loop scope like it would be in c++
				break 
		# BELOW 2 lines just have functions which simplify above process 
			#guild = discord.utils.find( lambda guild: guild.name == GUILD, self.guilds )				
			#guild = discord.utils.get( self.guilds, name = GUILD ) # accesses each element to find matching attribute value

		print( f"{self.user} is a proud member of the {guild.name} guild !\n" 
			f"Guild ID:\t{guild.id}\n"
		)
		members = ", ".join([member.name for member in guild.members]) # str.join(iterable) joins iterable elements into string
							# slightly rearranged for loop code to create iterable list		
		print(f"Members:\t{members}\n") # print(guild.member_count) # guild.member_count works, but guild.members doesn't return list of members		

	async def on_message(self, message): # gets an instance of discord.Message
		if( message.author == self.user ): # if message from the bot  # without this statement, bot may keep calling itself
			return # guarding / early exit		


		#elif( message.content == "!ratlord"  ):
		elif "ratlord" in message.content.lower(): # message.content is a string.

			x = self.user
			possible_text = [ 
				f"Who summoned {x}?", f"{x}, here for service.", f"{x} deployed.", 
				f"None shall stop {x}.", f"For the {x}!", f"{x} at your command.", 
				f"{x} is our shield.", f"{x} makes us strong.", f"{x} is with you." ,
				f"Heresy grows from the idleness of not using {x}."
				]

			possible_image = [
				"capybara_poster.png",
				"frog_cool.gif",
				"possum_infiltrator.png",
				"rat_book.png",
				"rat_bowl.png",
				"rat_dance.gif",
				"rat_merchant.png", # adding strings for efficiency
				]

			text = random.choice( possible_text )
			image = "https://raw.githubusercontent.com/dongyenk/Python-Discord-Bot/main/images/" + random.choice( possible_image ) # Python allows adding strings like in c++ :)
			await message.channel.send( text ) # function is from discord.Message.TextChannel.send		
			await message.channel.send( image ) # sending both in 1 function causes link to be visible

		elif "raise exception" in message.content:
			raise discord.DiscordException # when exception raised, discord.MyClient.on_error is called. Can let bot crash, or overwrite the function to handle this

	async def on_error(self, event, *args, **kwargs):
		with open("err.log", 'a') as f:
			if event == "on_message":
				f.write( f"Unhandled error:\t{args[0]}\n\t{exc_info()}" )
			else:
				raise # raise exception in default way, unless error came from an on_message event




client = MyClient() # creating an instance of my subclass

client.run(TOKEN)


