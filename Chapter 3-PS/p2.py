#Write a program to fill in a letter template given below with name and date. 

letter='''
    Dear <|name|>,
    You are Selected!
    <|date|>
'''
print(letter.replace("<|name|>","Arpit").replace("<|date|>","27th September"))
