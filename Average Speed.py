a = int(input("Enter a Value 1: "))
b = int(input("Enter a Value 2: "))
c = int(input("Enter a Value 3: "))

avg = (a + b + c) / 3
print("avg =", avg)

if avg > a and avg > b and avg > c:
    print("%d is higher that %d, %d, %d" % (avg, a, b, c))

elif avg > a and avg > b:
    print("%d is higher that %d, %d," % (avg, a, b))

elif avg > a and avg > c:
    print("%d is higher that %d, %d," % (avg, a, c))

elif avg > b and avg > c:
    print("%d is higher that %d, %d," % (avg, b, c))

elif avg > a:  
    print("%d is higher that %d" % (avg, a))

elif avg > b:
    print("%d is higher that %d" % (avg, b))

elif avg > c:
    print("%d is higher that %d" % (avg, c))