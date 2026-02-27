name=input("Enter name ")
num=0
for i in name:
    if i=='a' or i=='A':
        num+=1
        print(f"{name} have {num} of a ")