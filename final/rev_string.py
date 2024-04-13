print(" ")
print("with functions")
print(" ")

def rev(str):
    l=len(str)
    ans=""
    for i in range(0,l):
        ans=ans+str[l-i-1]
    
    print(ans)


rev("hello")

print(" ")
print(" ")
print("without functions")
print(" ")

original= "Hello!"
reversed= ""

for char in original[::-1]:
    reversed+= char

print("Original String:", original)
print("Reversed String:", reversed)
