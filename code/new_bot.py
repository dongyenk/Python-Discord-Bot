import os # to get value of environmental variable, an os dependent functionality
from dotenv import load_dotenv # to load in environmental variables  from a .env file
import random # for some fun
import discord # discord API wrapper that makes it easy to use via python # trying out discord.ext.commands.Bot instead of discord.Client
from discord.ext import commands
from sys import exc_info # function allows me to add more to error file
import time # time.sleep for a dramatic pause

import eng_to_morse

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') # getting values of environmental variables that got loaded
GUILD = os.getenv('DISCORD_GUILD')

class MyBot(discord.ext.commands.Bot): # creating subclass, overwriting inherited on_ready function
	async def on_ready(self): # 3 ways to get guild.
		for guild in self.guilds: # variable from for loop accessible outside loop
			if guild.name == GUILD:
				break # guild now contains name of the one bot is member of
		# Alternatives to above:
			#guild = discord.utils.find( lambda guild : guild.name == GUILD, self.guilds )
			#guild = discord.utils.get( self.guilds, name = GUILD ) # Both look for matching element of the MyBot.guilds iterable
		members = ", ".join( [ member.name for member in guild.members ] ) # str.join( <iterable> ) # slightly rearranged for loop to create iterable
		print( f"{self.user} is a proud member of {guild}.\n" 
			f"Guild member count: {guild.member_count}\n"			
			f"Guild members: {members}\n" # Can get number of members, but guild.members still not returning a list of members
		)

	async def on_command_error( self, context, exception ):
		with open( "err.log", 'a' ) as f:
			f.write( f"{context}\n{exception}\n{exc_info()}\n\n" ) # maybe the message this produces is useless

	

bot = MyBot( command_prefix = '!' ) # To respond to commands, not general on_message events

@bot.command( name = "testex", help = "Test exception handling")
async def handle_testex(ctx):
	raise commands.CommandError() # inherits from discord.DiscordException

@bot.command(name = "helpp", help = "Use !helpp to get more help.")
async def handle_help(ctx):
	await ctx.send(
		f"use !help <command_name> to learn how to masterfully use {bot.user}.\n"
		"e.g:\t !help ratlord"
	)

@bot.command(name ="ratlord", help = "Provider of encouraging words and images.") # using a decorator function extension instead of overwriting inherited functions
async def handle_ratlord( ctx ): # argument is context of command. Works like discord.Message.TextChannel
	x = bot.user			# this command takes no extra arguments
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
		"caterpillar.png",
	]													# pick & add a file name from list to complete the hyperlink
	image = "https://raw.githubusercontent.com/dongyenk/Python-Discord-Bot/main/images/" + random.choice(possible_image)
	await ctx.send(random.choice(possible_text))
	await ctx.send(image) # sending separate messages, because the hyperlink is visible otherwise

@bot.command( name = "rolld", help = "• Rolls 1d6 by default.\n• !rolld <number of dice> <number of sides>.\n• e.g. !rolld 2 6 " )
async def handle_rolld( ctx, num_dice = 1, num_sides = 6 ):

	#for num in range( 1, num_sides ): # this range is only 1-5, because second argument is 1 past the final index
	#for num in range( num_sides ): # this range is 0-5, 6 indexes, so no need to +1 to num_sides
		#print(num)
	
	dice = [ #Using the slightly rearranged for loop to create iterable list
		str( random.choice( range( 1, num_sides+1 ) ) )
		for a_dice in range( num_dice ) # range( number(s) ) returns an iterable
	]
	
	rolls = ", ".join(dice) # str.join(iterable) joins elements of iterable into 1 string, with the preceding str dividing them

	await ctx.send( f"Rolling {num_dice}d{num_sides}" ) 
	time.sleep(2)
	await ctx.send(f"Results:\t{rolls}") 

@bot.command( name = "eng2morse", help = 'Encode strings of letters and spaces into morse!\n!eng2morse <string>\n!eng2morse noSpace\n!eng2morse "hello world"\nYou must use double quotes on strings with spaces!' )
async def handle_eng2morse( ctx, string ):
	await ctx.send( eng_to_morse.ascii_string_to_morse( string ) )

bot.run(TOKEN) # starts loop that listens to events and calls appropriate functions when they happen
