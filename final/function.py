def calculator(num1 :int ,num2:int, operator: chr)->int:
    if(operator=='+'):
        return num1+num2
    elif(operator=='-'):
        return num1-num2
    elif(operator=='/'):
        return num1/num2
    elif(operator=='*'):
        return num1*num2

num1=int(input("ENTER FIRST NUMBER "))
num2=int(input("ENTER SECOND NUMBER "))
operator=str(input("ENTER OPERATOR "))
print(calculator(num1,num2,operator))
print("😊")