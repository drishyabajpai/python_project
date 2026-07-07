#if else condition
'''a=int(input("Enter your age: "))
print("Your age is ,   ",a)

if a>=18:
    print("You are eligible to vote")
else:
    print("OHH SORRY! You are not eligible to vote")

'''
#Nested if else condition
'''num = int(input ("Enter a num:"))

if (num<0):
    print("Tu Depression mai Negative lala ")

elif (num==0):
    print("Salee ZERO hai tu")

else: 
    print("Tu Positive ho gya bhai") 



print("FUCK OFF!") '''
'''
number = int(input("Enter a number: ")) 
if (number < 0):
    print("Negative number")
    print(number)

elif (number > 0):
    if (number <= 10):
        print("Number is between 1 and 10")
        print(number)
    else:
        print("Number is positive but greater than 10")
        print(number)
else:
    print("Number is zero") 
    print(number)
'''

#greeting exc.. 21/06/26 time is 18:29 location is libarary 

time = (int(input("Enter the time (0-23):")))
if (time < 12):
    print("Good morning!")
elif (time < 16):
    print("Good afternoon!")
elif (time < 20):
        
    print("Good evening!")
else:
   print("Good night!")