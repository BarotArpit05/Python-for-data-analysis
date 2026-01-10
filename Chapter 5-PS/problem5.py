#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
d={}
for i in range(4):
    name=input("Enter Name :")
    lang=input("Enter Language")
    d.update({name:lang})
print(d)

#If the names of 2 friends are same; what will happen to the program in problem 6?
#then it will show common key once only

#If languages of two friends are same; what will happen to the program in problem 6?
#it will show its regular answer only