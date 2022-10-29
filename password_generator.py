# Create a random password that is impossible to crack :) in python.

import random
import math

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' # List of all the upper/lowercase letters in the alphabet
symbols = '~!@#$%^&*()_+=-`<>,./?;:\][{}' # A bunch of symbols from the keyboard
psswd_len  = 20; # password length

password = ''

for x in range(psswd_len):

	char_choice = math.floor(random.random() * 3); # A random number. Either 0, 1, or 2
	
	# Depending on the char_choice, either alphabet, symbol, or number will be the next character in the password
	
	if char_choice == 0:
		random_char = str(math.floor(random.random() * 10))
	elif char_choice == 1:
		random_char = symbols[math.floor(random.random() * len(symbols))]
	else:
		random_char = alphabet[math.floor(random.random() * len(alphabet))] 

	password += random_char;

print(password);
