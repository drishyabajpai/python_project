# assign a string to the variable name
#name = "Drishya"

# iterate over each character in the string and print it separated by commas
#for i in name:
 #   print(i, end=",")

#for k in range(1, 20001):
 #   print(k)
#for k in range(1, 12 ,3):
 #       print(k) 
#count=5
#while (count > 0):
 #   print(count)
  #  count = count  + 1
'''
i=int(input("Enter a number: "))
while (i<=5):
    i=int(input("Enter a number: "))
    print(i)
    i= i + 1 

print("Done")
'''
#break $ continue statements
'''
for i in range(12):
    if (i==5):
        break   #exit the loop when i is 5 its break statement 
    print("5 x", i+1, "=", 5*(i+1))

print("Loop GOt DoWn")

'''
'''
for i in range(12):
    if (i==5):
        print("Loop GOt DoWn")
        continue # skip iteration its continue statement
    print("5 x", i, "=", 5*(i))
'''
i=0
while True:
    print(i)
    i=i+1
    if (i%30 == 0):
        break

