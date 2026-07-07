# Simple Modern Password Generator 
import random  #the random module is used to generate random numbers and characters
import string #the string module is used to access predefined character sets like letters, digits, and punctuation 
#ALL possible character 
letters =  string.ascii_letters
numbers = string.digits
symbols = string.punctuation 

# Combine all character 
all_characters = letters + numbers + symbols

# User input 
Length = int(input ("Enter password length : "))
#Generate password 
password = ""
for i in range(Length):
    password += random.choice(all_characters)

# print final password\
print("Generated password : ", password)

'''
| Concept       | Used |
| ------------- | ---- |
| import        | YES  |
| variables     | YES  |
| strings       | YES  |
| loops         | YES  |
| user input    | YES  |
| randomization | YES  |
| concatenation | YES  |

'''