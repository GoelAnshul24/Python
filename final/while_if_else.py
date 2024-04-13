sec_num=7
guess_count=0

while guess_count<3:
    guess=int(input("enter the no to guess: "))
    if guess!= sec_num:
        print("try again")
        guess_count+=1
    else:
        guess==sec_num
        print("you won")
        break       
if guess_count == 3:
    print("The correct number was: ", sec_num)