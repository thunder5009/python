import random
sys_num=random.randint(1,10)

while True:
    user_num=int(input("enter number: "))   
    if user_num==sys_num:
        print("You Win")
        break
    else:
        print("Lost")