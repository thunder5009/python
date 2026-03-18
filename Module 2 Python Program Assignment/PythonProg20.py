words = input("Enter words separated by spaces: ").split()
if not words:
    print("Empty list.")
else:
    longest = max(words, key=len)
    print(f"Longest word: '{longest}' (length: {len(longest)})")
