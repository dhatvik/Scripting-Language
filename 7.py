class Student:
    def __init__(self):
        pass
    def accept(self):
        self.name=input("enter the name of student")
        self.age=int(input("Enter the age of student"))
        m1=int(input("Enter sub1 Marks\t"))
        m2=int(input("Enter sub2 Marks\t"))
        m3=int(input("Enter sub3 Marks\t"))
        self.marks=[m1,m2,m3]

    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("Marks:",self.marks)

a=Student()
print("Enter the Details")
a.accept()
print("Display Details")
a.display()
