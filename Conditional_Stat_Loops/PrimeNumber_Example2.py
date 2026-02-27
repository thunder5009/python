num=int(input("Enter a number: "))
temp=0
for i in range(2,num):
    if num%i==0:
        print("Not a Prime Number")
        temp=1
        break
    else:
        temp=0
if temp==0:
    print("Number is Prime")