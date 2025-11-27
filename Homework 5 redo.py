# Get input from the user
char = input("Enter a character: ")

# Check if the input is a single character
if len(char) != 1:
    print("Please enter only one character.")
else:
    # Check if character is in the set of alphabets
    if char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is not an alphabet.")
