# Create a random password that is impossible to crack :) in py 

import random
import math

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
symbols = '~!@#$%^&*()_+=-`<>,./?;:\][{}'
psswd_len  = 20; # password length

password = ''

for x in range(psswd_len):

	char_choice = math.floor(random.random() * 3); # will be random between the sym, alph, and nums

	if char_choice == 0:
		random_char = str(math.floor(random.random() * 10))

	elif char_choice == 1:
		random_char = symbols[math.floor(random.random() * len(symbols))]

	else:
		random_char = alphabet[math.floor(random.random() * len(alphabet))] 

	password += random_char;

print(password);