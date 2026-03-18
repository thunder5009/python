a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a == b:
    print(True)
elif a + b == 5:
    print(True)
elif a - b == 5 or b - a == 5:
    print(True)
else:
    print(False)