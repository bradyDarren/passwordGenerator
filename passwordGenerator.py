# Randomly generate a combination of letters, numbers, and symbols. 
import random
import string

alpha_upper = string.ascii_uppercase
alpha_lower = string.ascii_lowercase
symbols = string.punctuation
nums = string.digits

total_count = input("How many characters total would you like your password to be?")

alpha_count = input("How many alphabetical characters would you like to be included in your password? : ")
num_count = input("How many numerical characters would you like to be included in your password? : ")
symbol_count = input("How man symbols would you like included in your password? : ")

# Function that will make a choice between an uppercase alpha character or a lowercase alpha character.
def upper_or_lower(upper_list, lower_list):

    alpha_choice = [upper_list, lower_list]
    list_options = random.choice(alpha_choice)
    if list_options == upper_list: 
        return random.choice(upper_list)
    elif list_options == lower_list:
        return random.choice(lower_list)

# Function that will choose a random symbol and remove backticks (``), backslashes(\), and forwardslashes (/)
def symbol(symbol_list):
    unapproved_symbols = ['`','/','\\']
    rand_symbol = random.choice(symbol_list)
    while True: 
        if rand_symbol in unapproved_symbols:
            continue
        else: 
            break
