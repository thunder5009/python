a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"\nBefore swap: a = {a}, b = {b}")

temp = a
a_swap = b
b_swap = temp
print(f"After swap (with temp): a = {a_swap}, b = {b_swap}")

a, b = b, a
print(f"After swap (without temp): a = {a}, b = {b}")
