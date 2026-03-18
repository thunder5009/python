s=input("Enter the main string: ")
to_insert=input("Enter the string to insert: ")
mid=len(s)//2
result=s[:mid]+to_insert+s[mid:]
print(f"Result:{result}")
