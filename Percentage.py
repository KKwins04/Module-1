#Take marks as input from user
print("Enter marks Obtained in 4 subjects: ")
math = int(input("maths: "))
english = int(input("english: "))
science = int(input("science: "))
tamil = int(input("tamil: "))

#Lets calculate percentage of marks
sum = math + science + english + tamil
print("Total marks for all subjects: ", sum)

perc = (sum/400)*100

print(end="Percentage Mark: ")
print(perc)