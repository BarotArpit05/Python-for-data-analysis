class Employee:
    language="py" #this is  a class attribute
    salary=120000
obj1=Employee()
obj1.name="ABC" #this  is an instance  attribute 
print(obj1.salary,obj1.name)

obj2=Employee()
obj2.name="XYZ"
print(obj2.salary,obj2.name)

'''here name is the object attribute and salary and language is the 
class attribute as they directly belong to the  class'''