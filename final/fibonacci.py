def Fib(n,a,b):
    if(n!=0):
        c=a+b
        print(c)
        Fib(n-1,b,c)
