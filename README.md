# Python-Discord-Bot
2 versions of the bot. 

## ***bot.py*** contains the older version of the bot.

It only uses bot.py

It responds to general events, specifically any message containing "ratlord"

Uses discord.Client and responds to events.

## ***new_bot.py*** contains the newer version of the bot.

Must have new_bot.py & eng_to_morse.py in same directory!

It only responds to commands, that must begin with '!' 

Inputting !help into discord makes the bot give instructions.

Uses discord.ext.commands.Bot instead of discord.Client and responds to commands.

I added code to let the bot encode strings of letters and spaces into morse. Screen shot of this in example_images.

### Useful commands of new_bot:

!help, !helpp, !ratlord, !rolld, !eng2morse
___________________________________________________________________________________________________

***.env*** contains some environmental variables required by the bot.

***eng_to_morse.py*** has code needed by new_bot.py

***example_images*** shows the bot working

***images*** contains images used by the bot
