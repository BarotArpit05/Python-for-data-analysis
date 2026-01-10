marks={
    "Arpit":100,
    "Akash":24,
    "Ajay":67,
    "my_list":[10,"hari",34]
}
print(marks.items()) #gives items of dictionary in form of tuple

print(marks.keys())#gives keys of the dictionary 

print(marks.values())#gives values of the dictionary 

marks.update({"Arpit":99,"Aj":100})#we can update the values through it and also add new key values pair through it 

print(marks.get("Aj"))#we get the values through this  methods 
print(marks)

print(marks.get("Aksh"))#it will return None 
print(marks["Aksh"])#it will give error