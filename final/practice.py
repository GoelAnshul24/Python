for i in ["Harshit", "Goel"]:
    print(i)
    
a=[1,2]
b=[3,4]
for i in a:
    for j in b:
        print("Inside the inner loop")
        print(i,j)
    print("outside the inner loop")