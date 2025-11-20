# Program to display ASCII code of different alphabets

text = input("Enter any alphabet(s): ")

for ch in text:
    if ch.isalpha():
        print(f"ASCII value of '{ch}' is:", ord(ch))
    else:
        print(f"'{ch}' is not an alphabet.")
