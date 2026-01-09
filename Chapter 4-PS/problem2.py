#Write a program to accept marks of 6 students and display them in a sorted manner.
marks=[]
S1=int(input("Enter Marks :"))
marks.append(S1)

S2=int(input("Enter Marks :"))
marks.append(S2)
S3=int(input("Enter Marks :"))
marks.append(S3)
S4=int(input("Enter Marks :"))
marks.append(S4)
S5=int(input("Enter Marks :"))
marks.append(S5)
S6=int(input("Enter Marks :"))
marks.append(S6)
marks.sort()
print(marks)