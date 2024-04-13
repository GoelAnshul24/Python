'''01/02/24
wap to find the largest element in the list 
'''


list=[10,30,20,40,15]
largest_number = list[0]
for num in list:
    if num > largest_number:
        largest_number = num
print(largest_number)