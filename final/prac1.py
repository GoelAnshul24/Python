#a=((10+10)*100)//10
#print(a)

temp=float(input("enter temp: "))
if(temp<=40 and temp>=20):
    print("it is very hot")
    print("take much fluids")
elif(temp<=35 or temp>=20):
    print("it is moderate today")
elif(not temp==20):
    print("temperature cant be predicted")
else:
    print('whatever the temperature is, i have to be there')