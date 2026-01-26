class Employee: #Parent Class
    company="ITC"
    def show(self):
        print(f"The name is :{self.name} and Salary is :{self.salary}")



class Programmer(Employee): #Child Class
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is:{self.name} he is good with{self.language} language")

a=Employee()
b=Programmer()

b.name="Arpit"
b.salary=25752
b.show()

print(a.company)
print(b.company)