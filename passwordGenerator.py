# Randomly generate a combination of letters, numbers, and symbols. 
import random
import string

alpha_upper = string.ascii_uppercase
alpha_lower = string.ascii_lowercase
symbols = string.punctuation
nums = string.digits

alpha_count = input("How many alphabetic characters would you like in your password? : ")
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
    while True: 
        rand_symbol = random.choice(symbol_list)
        if rand_symbol in unapproved_symbols:
            continue
        else: 
            return rand_symbol

# Function that will choose a random number
def number(nums_list):
    rand_nums = random.choice(nums_list)
    return rand_nums

# Function that will select random alpha characters, numbers, and symbols.
def complete_password():
    password_list = []
    char_count = int(alpha_count) + int(num_count) + int(symbol_count)
    while len(password_list) < char_count:
        for x in range(int(alpha_count)):
            password_list.append(upper_or_lower(alpha_upper, alpha_lower))
        
        for y in range(int(symbol_count)):
            password_list.append(symbol(symbols))

        for z in range(int(num_count)):
            password_list.append(number(nums))
    
    random.shuffle(password_list)
    password_list = ''.join(password_list)

    return password_list

# print(len(complete_password(total_count)))  # Test Line
print(f" This is your password: {complete_password()}")
