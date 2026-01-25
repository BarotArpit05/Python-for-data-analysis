class Employee:
    salary=12345
    language="Python"

    def __init__(self):
        print("I am Creating an object")

    def getinfo(self):
        print(f"the language is:{self.language}")

obj1=Employee()

print(obj1.salary)
obj1.getinfo()