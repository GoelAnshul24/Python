num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
symbol=str(input("Enter the symbol: "))
if symbol == '+':
    print(num1, "+", num2, "=", num1+num2)
elif symbol == '-':
    print(num1, "-", num2, "=", num1-num2)
elif symbol == '%':
    print(num1, "%", num2, "=", num1%num2)
elif symbol == '*':
    print(num1, "*", num2, "=", num1*num2)