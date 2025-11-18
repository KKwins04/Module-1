#Using the 'is' identity operator

#Example 1
x = 1.1 
if type(x) is int:
    print("True")
else:
    print("False")


#Example 2
x = 4.9
if type(x) is not float:
    print("True")
else:
    print("False")

#Example 3 - Identity Comparison
x = 22
y = 15
if x is y:
    print("x and y SAME Identity")


#Example 4
y = 30
if x is not y:
     print("x and y DIFERENT Identity")