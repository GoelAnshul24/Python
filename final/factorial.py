num=int(input("Enter the number"))
fact=1
if num==0:
    print(0)
else:
    while num>0:
        fact=fact*num
        num-=1
    print(fact)