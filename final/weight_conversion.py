weight=float(input("enter the weight: "))
unit=input("enter the unit: ")
if unit in'Kk':
    weight=weight*0.45
    print(weight)   
else:
    weight=weight/0.45
    print(weight)