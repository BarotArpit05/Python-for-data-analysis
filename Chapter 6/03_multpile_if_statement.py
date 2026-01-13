age=int(input("Enter your age: "))

#if statement no :- 1
if(age%2==0):
    {
        print("Age is even ")
    }
#end of if statement 1


#if statement no:-2
if(age>=18):#semicolon is necessary 
    print("You are above the age of consent") #here the space you see at the start of  line is because of indentation 
    print("Your age is :",age)

elif(age<0):
    {
        print("Age cannot be in the negative")
    }

else:
    print("You are not above the age of consent")
#end of if statement 2
print("End of program")