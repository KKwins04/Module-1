# Program to store 5 birthdays and show one based on user input

# Step 1: Store birthdays
birthdays = {
    "Alice": "2012-05-14",
    "Bob": "2013-09-22",
    "Charlie": "2013-12-01",
    "Diana": "2011-03-08",
    "Edward": "2012-07-19"
}

# Step 2: Ask for a name
name = input("Enter the person's name: ")

# Step 3: Show the birthday (if the name exists)
if name in birthdays:
    print(f"{name}'s birthday is on {birthdays[name]}")
else:
    print(f"Sorry, I don't have a birthday stored for {name}.")
