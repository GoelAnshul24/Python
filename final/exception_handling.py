def div (m,n):
    try:
       return m/n
    except:
       print("division by 0 is not possible")
a=int(input("first number: "))
b=int(input("second number: "))
print(div(a,b))