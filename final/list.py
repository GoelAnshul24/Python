list=[i for i in range(1,101)]
list1=[i for i in range(1,101) if i%2==0]
list2=[i for i in range(1,101) if i%2!=0]
print(list)
print(' ')
print(list1)
print(' ')
print(list2)
print(' ')
print(' ')
print(' ')

list_mixed=["1","harshit","2", "goel"]
l1 = [s for s in list_mixed if s.isdigit()]
print(l1)