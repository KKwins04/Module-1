# Program to check whether user input is an alphabet or not

char = input("Enter a character: ")

if len(char) == 1:  # Ensure only one character is entered
    if char.isalpha():
        print("It is an alphabet.")
    else:
        print("It is not an alphabet.")
else:
    print("Please enter only one character.")
