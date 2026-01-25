class Employee:
    language="py" #this is  a class attribute
    salary=120000
obj1=Employee()
obj1.name="ABC" #this  is an instance  attribute 
obj1.salary=1300#instance attrribute take preference over class attribute 
print(obj1.salary,obj1.name)

