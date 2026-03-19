s=input("Enter a string: ")
if len(s)%4==0:
    print(f"Reversed: {s[::-1]}")
else:
    print(f"Length is not a multiple of 4. String unchanged: {s}")
