num = float(input("Enter a number: "))

if num < 0:
    print("Square root of a negative number is not defined in real numbers.")
else:
    result = num ** 0.5
    print("Square root:", result)
