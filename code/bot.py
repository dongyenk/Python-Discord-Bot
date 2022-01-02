# similar to c++'s #include <standard_header> or "local_header.hpp"
import os # provides OS dependent functionality, such returning value from environmental variable key-value pair
import discord # discord API wrapper, makes Discord API easy to use
from dotenv import load_dotenv # load environmental variables from local .env file

# Looked at discordpy.readthedocs.io, docs.python.org, pypi.org to understand what these modules and functions do

load_dotenv() # loads data from .env file in local directory, which contains # DISCORD_TOKEN contains the thing required for this program to connect to Discord
TOKEN = os.getenv('DISCORD_TOKEN') # returns value corresponding to the environmental variable argument given in the string
GUILD = os.getenv('DISCORD_GUILD')

# looking at discord.py docs, creating this subclass makes more sense to me # 2 ways to register events are to use discord.Client.event decorator, or to create a discord.Client subclass
class MyClient(discord.Client): # creating a subclass. Can't use code directly, must create a class instance first.
	async def on_connect(self):
		print(f"Beep boop beep, connecting\n") # was just trying out overriding another of discord.Client's functions	
	async def on_ready(self): # functions seem to take the class itself as default argument
		# for loop to get guild variable to contain active guild
		for guild in self.guilds:
			if guild.name == GUILD:
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

client = MyClient() # creating an instance of my subclass

client.run(TOKEN)


