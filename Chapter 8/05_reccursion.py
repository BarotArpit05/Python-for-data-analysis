#Recursion is a function calling itself
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)
n=int(input("Enter Number: "))
print("Factorial of this number is :",factorial(n))