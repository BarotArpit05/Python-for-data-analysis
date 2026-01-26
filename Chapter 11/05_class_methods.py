class Employee:
    a=1
    @classmethod # this is used to access the class attribue without it it will give print of 45
    def show(cls):
        print(f"the class value of a is : {cls.a}")

e=Employee()
e.a=45
e.show()