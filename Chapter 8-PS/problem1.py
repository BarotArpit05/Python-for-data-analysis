#Write a program using functions to find greatest of three numbers
a=int(input("Enter Number :"))
b=int(input("Enter Number :"))
c=int(input("Enter Number :"))

def greater(a,b,c):
    if(a>b and a>c):
        print("A is Greater than other Number")
    elif(b>a and b>c):
        print("B is Greater than Other Numbers")
    elif(c>a and c>b):
        print("C is the greatest than other number")
    else:
        print("All are same ")
greater(a,b,c)