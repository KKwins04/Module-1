# Swap three numbers in a cyclic way

A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))

print("\nBefore swap:")
print("A =", A, "B =", B, "C =", C)

# Cyclic swap: A → B → C → A
temp = A
A = B
B = C
C = temp

print("\nAfter swap:")
print("A =", A, "B =", B, "C =", C)
