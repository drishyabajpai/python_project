#using a for loop (best for beginners)
n = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

"""f
2. Using a while loop
n = int(input("Enter the number of terms: "))

a = 0
b = 1
count = 0

print("Fibonacci Series:")

while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1
3. Using Recursion (Advanced)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter the number of terms: "))

print("Fibonacci Series:")

for i in range(terms):
    print(fibonacci(i), end=" ") """