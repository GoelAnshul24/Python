#wap to extract even and odd numbers from a list

def is_even(n):
    return n%2==0
def is_odd(n):
    return n%2!=0
list_1=[2,3,4,10,12,14,15,16,171,19]
even=list(filter(lambda n:n%2==0, list_1))
odd=list(filter(lambda n:n%2!=0, list_1))
print("Even numbers are: ", even)
print("Odd numbers are: ", odd)