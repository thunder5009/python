num=int(input("Enter a non-negative integer: "))
if num<0:
    print("Factorial is not defined ")
else:
    result=1
    for i in range(1, num + 1):
        result=i
    print(f"Factorial of {num} = {result}")
