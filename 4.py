def menu():
    print("1.celcius\n 2.Farenheit\n 3.kelvin\n 4.exit\n")

def Cel(t):
    if t==2:
        return (str(temp*(9/5)+32))+"F"
    elif t==3:
        return (str(temp+273.15))+"K"        


def Far(t):
    if t==1:
        return (str(((temp-32)*5)/9))+"C"
    elif t==3:
        return (str((((temp-32)*5)/9)+273.15))+"K"               


def Kel(t):
    if t==1:
        return (str(temp-273.15))+"C"
    elif t==2:
        return (str((temp-273.15)*(9/5)+32))+"F"          

templist=[]
while True:
    menu()
    fromt=int(input("enter the formate of input temperatue"))
    if fromt==4:        
        print(templist)
        break
    tot=int(input("enter the formate of output temperatue"))
    if tot==4:        
        print(templist)
        break
    temp=int(input("Enter the temperature:"))

    if fromt==1:
        toval=Cel(tot)
        templist.append((str(temp))+"C"+","+toval)
        
    elif fromt==2:
        toval=Far(tot)
        templist.append((str(temp))+"F"+','+toval)
        
    if fromt==3:
        toval=Kel(tot)
        templist.append((str(temp))+"K"+","+toval)