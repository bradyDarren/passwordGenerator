# Randomly generate a combination of letters, numbers, and symbols. 
import random

alpha_chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 

alpha_rand = random.choice(alpha_chars)

print(alpha_rand)

total_count = input("How many characters total would you like your password to be?")

alpha_count = input("How many alphabetical characters would you like to be included in your password? : ")
num_count = input("How many numerical characters would you like to be included in your password? : ")
symbol_count = input("How man symbols would you like included in your password? : ")

