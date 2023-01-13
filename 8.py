from functools import reduce
l=[]
for i in range(6):
    n=int(input("Enter the element"))
    l.append(n)
print("The elements in list\t",l)

l2=[(i*3) for i in l]
print("The elements in new list are\t",l2)
s1=reduce(lambda x,y:x+y,l)
s2=reduce(lambda x,y:x+y,l2)
print("Sum of elemnts of list l\t",s1)
print("Sum of elemnts of new list l2\t",s2)