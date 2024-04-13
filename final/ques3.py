#wap to find the sum of list using recursion

def sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum(lst[1:])

my_list = [1, 2, 3, 4, 5, 10, 20, 30, 40 ,50]
print("Sum of the list:", sum(my_list))