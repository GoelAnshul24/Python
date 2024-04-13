'''Write a python program that counts the total no. of words in a sentence'''


def frequency(str):
    count=0
    str=str+' '+'a'
    for i in range(0,len(str)):
        if str[i]==' ' and str[i+1]!=' ':
            count=count+1
    
    print(count)

frequency(input("enter sentence: "))

