mean1 = 38
wrong_number = 36
correct_number = 56
total_number = 40

#Sum of 40 numbers
sum = mean1 * total_number
print("The sum of the 40 numbers is: ", sum)

#Correct sum of these numbers
num2 = sum - (wrong_number - correct_number)
print("Corrected sum (sum - (wrong_number - correct_number)): ", num2)

#The correct mean
mean2 = num2 / total_number
print(mean2)