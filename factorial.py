def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n *factorial(n-1)
print(factorial(5))
#5 * fac(4)
#5 * 4 * fac(3)
#5 * 4 * 3 * fac(2)
#5 * 4 * 3 * 2 * fac(1)
#5 * 4 * 3 * 2 * 1
