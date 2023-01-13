class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l * self.b    

l1=int(input("Enter length of rectangle1"))
b1=int(input("Enter breadth of rectangle1"))
r1=rectangle(l1,b1)
print("area of rectangle1:",r1.area())

l2=int(input("Enter length of rectangle2"))
b2=int(input("Enter breadth of rectangle2"))
r2=rectangle(l2,b2)
print("area of rectangle1",r2.area())
