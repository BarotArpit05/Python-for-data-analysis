#  Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
with open("Chapter 9-PS/poems.txt") as f:
    c=f.read()
    if("twinkle" in c):
        print("twinkle is present in file")
    else:
        print("twinkle is not present ")
