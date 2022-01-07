eng_morse_dict = { # letters and spaces
	"a" : ".-",
	"b" : "-...",
	"c" : "-.-.",
	"d" : "-..",
	"e" : ".",
	"f" : "..-.",
	"g" : "--.",
	"h" : "....",
	"i" : "..",
	"j" : ".---",
	"k" : "-.-",
	"l" : ".-..",
	"m" : "--",
	"n" : "-.",
	"o" : "---",
	"p" : ".--.",
	"q" : "--.-",
	"r" : ".-.",
	"s" : "...",
	"t" : "-",
	"u" : "..-",
	"v" : "...-",
	"w" : ".--",
	"x" : "-..-",
	"y" : "-..--",
	"z" : "--..",

	" " : "  ",
}

	


def ascii_char_to_morse( char ):
	if char in list(eng_morse_dict.keys()):
		return eng_morse_dict[ char ]
	else:
		return "#" # error symbol

def ascii_string_to_morse( string ):
	string = string.lower()
	final_string = ""
	for char in string:
		final_string += ascii_char_to_morse( char )
		final_string += " " # to make individual morse units clear
	return final_string

# accessing dictionary key through value # key_list [ element of values list ] -> corresponding key
#print( list( eng_morse_dict.keys() ) [ list(eng_morse_dict.values() ).index("-..-") ] ) # start of my testing to translate other way round