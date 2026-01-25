# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,picode):
        self.name=name
        self.salary=salary
        self.pincode=picode
p1=Programmer("Arpit",13243,382350)
print(p1.name,p1.salary,p1.pincode,p1.company)    
p2=Programmer("XYZ",1322343,383350)
print(p2.name,p2.salary,p2.pincode,p2.company)        
        