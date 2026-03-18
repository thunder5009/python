ch = input("Enter a character: ")
if len(ch) != 1:
    print("Please enter a single character.")
else:
    if ch.lower() in "aeiou":
        print(f"'{ch}' is a Vowel")
    else:
        print(f"'{ch}' is a Consonant")
