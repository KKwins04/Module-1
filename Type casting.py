#Assigning Different Variables
name = "Penguin"
age = 13
is_student = True
weight = 42.7

#Printing Different Variables and their Data Type
print("Name: ", name)
print("Data type of Name is", type(name))

print("Age: ", age)
print("Data type of Age is", type(age))

print("is_student: ", is_student)
print("Data type of is_student is", type(is_student))

print("weight: ", weight)
print("Data type of weight is", type(weight))

#Type casting to convert the datatype of variables
print("\n After type Casting...")
age = str(age)
print("Data type of Age is", type(age))

weight = int(weight)
print("Data type of weight is", type(weight))