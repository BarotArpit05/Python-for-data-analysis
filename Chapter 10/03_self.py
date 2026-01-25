class Employee:
    salary=12345
    language="Python"

    def getinfo(self):
        print(f"the language is:{self.language}")

obj1=Employee()

print(obj1.salary)
obj1.getinfo()
# Employee.getinfo(obj1)