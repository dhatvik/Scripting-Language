# atomic={}
def AtomicDictionary():
    pass
atomic={
        'He':'Helium',
        'Ne':'Neon',
        'Ar':'Argon',
        'C':'Carbon'
        }

name=input("Enter name of new element")
symbol=input("Enter symbol of new element")
atomic.update({symbol:name})
print("The elements in dictionary are:",atomic)    

name=input("Enter name of duplicate element")
symbol=input("Enter symbol of duplicate element")
atomic.update({symbol:name})
print("The elements in dictionary are:",atomic)

print("The number of elements in dictionary are:",len(atomic))

search =input("Enter symbol of name of element to be searched")
if search in atomic:
    print('Element Found')
elif search in atomic.values():
    print("Element Found")
else:
    print("Element not found")        

AtomicDictionary()
