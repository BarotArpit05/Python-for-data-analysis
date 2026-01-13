age=int(input("Enter your age: "))
#if elif else ladder
if(age>=18):#semicolon is necessary 
    print("You are above the age of consent") #here the space you see at the start of  line is because of indentation 
    print("Your age is :",age)

elif(age<0):
    {
        print("Age cannot be in the negative")
    }

else:
    print("You are not above the age of consent")
print("End of program")