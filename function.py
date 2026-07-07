#make function not call again make one function use it multiple time to in code 
def calcmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))  
#mean = (a*b)/(a+b)
#print(mean) 
calcmean(a,b) #use function call not make a function 
c=int(input("Enter third number: "))
d=int(input("Enter fourth number: ")) 
#mean = (a*b)/(a+b)
#print(mean) 
calcmean(c,d) #use function call not make a function
