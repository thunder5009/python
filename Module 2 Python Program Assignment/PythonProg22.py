s=input("Enter a string: ")
if len(s) < 2:
    print("String is short (need 2 characters)")
else:
    result = s[:2] + s[-2:]
    print(f"First 2 + Last 2 = '{result}'")
