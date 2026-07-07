a=input("Enter the number:")
print(f"Multiplication table of {a} is:")
try:  # Handle the case when the input is not a valid number
    for i in range(1,11):
        print(f"{a} x {i} = {int(a)*i}")
except:  # Handle the case when the input is not a valid number
    print("Please enter a valid number.")

print("Program ended.")

try:
    num = int(input("Enter a integer: "))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Please enter a valid integer.")

except IndexError:
    print("Index out of range. Please enter a valid index.")

print("WELCOME TO EXCEPTION HANDLING IN PYTHON PROGRAM LANGUAGE ****")
try:
    l=[1,5,6,7]
    i=int    (input("Enter the index:"))
    print(l[i])
except :    # Handle the case when the input is not a valid integer or index is out of range
    print("Please enter a valid index.")
finally: # make sure this block is executed no matter what 
    print("I am always executed.")     

