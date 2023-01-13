mylist=[]
n=int(input("Enter number of elements in list"))
for i in range(1,n+1):
    ele=int(input("Enter element"))
    mylist.append(ele)
print('The elements in list are:',mylist)

print("Tne maximum Element in list is:",max(mylist))
print("Tne minimum Element in list is:",min(mylist))

newele=int(input("Enter element to be inserted in list"))
mylist.append(newele)
print('The elements in list are:',mylist)

delele=int(input("Enter element to be Deleted in list")) 
if delele in mylist:
    mylist.remove(delele)
else :
    print("Element not Found")
print('The elements in list are:',mylist)

temp=int(input("Enter element to be Searched in list")) 
if temp in mylist:
    print('Element found at index:',mylist.index(temp)+1)
else :
    print("Element not Found")
