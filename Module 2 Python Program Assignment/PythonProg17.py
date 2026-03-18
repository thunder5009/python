str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if len(str1) < 2 or len(str2) < 2:
    print("Both strings must have at least 2 characters.")
else:
    news1=str2[:2]+str1[2:]
    news2=str1[:2]+str2[2:]
    print(f"After swapping first 2 chars: '{news1}' and '{news2}'")
