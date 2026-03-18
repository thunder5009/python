s = input("Enter a string: ")
if len(s) < 3:
    print(f"Result: {s} (unchanged, length < 3)")
elif s.endswith("ing"):
    print(f"Result: {s + 'ly'}")
else:
    print(f"Result: {s + 'ing'}")
