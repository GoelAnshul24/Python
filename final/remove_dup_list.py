'''03/02
wap to remove duplicates from a list'''


list = [1, 2, 3, 4, 2, 3, 5]
empty_list = []

for i in list:
    if i not in empty_list:
        empty_list.append(i)

print(empty_list)
