class Student:
    id=0
    def __init__(self,address,name,age):
        self.id = +1
        self.address=address
        self.name=name
        self.age=age

    def display(self):
        print("id no :"+str(self.id))
        print("ID no "+str(self.id)+" of address is :"+self.address)
        print("ID no"+str(self.id)+" of Name is :"+self.name)
        print("ID no "+str(self.id)+"of age is "+str(self.age))
        print("\n")



s1 = Student("Mandalay","Su Su",19)
s2 = Student("Sagaing","Hla Hla",15)
s3= Student("Taunggyi","Mg Mg",23)
s4=Student("Bago","Aung Aung",20)
s5=Student("Mohnyin","Ma Ma",25)

s1.display()
s2.display()
s3.display()
s4.display()
s5.display()