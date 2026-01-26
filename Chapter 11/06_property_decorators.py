class Employee:
    a=1
    @classmethod # this is used to access the class attribue without it it will give print of 45
    def show(cls):
        print(f"the class value of a is : {cls.a}")

    @property
    def name(self):
        return self.name

e=Employee()
e.a=45
e.name="Arpit"
print(e.name)
e.show()