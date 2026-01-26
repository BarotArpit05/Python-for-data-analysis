class Employee: #Parent class of Programmer
    company="ITC"
    def show(self):
        print(f"The name is :{self.name} and Salary is :{self.salary}")

class Coder: #parent class of programmer
    language="Python"
    def print_lang(self):
        print(f"Out of all language here is  your langugae :{self.language}")


class Programmer(Employee,Coder): #Child class of Employee,Coder
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is: {self.company} he is good with {self.language} language")

a=Employee()
b=Programmer()

b.name="Arpit"
b.salary=25752
b.show()
b.showLanguage()
b.print_lang()

