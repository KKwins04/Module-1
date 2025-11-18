print("Enter your marks for 5 subjects(out of 100)")
Math = int(input("Maths:"))
Science = int(input("Science:"))
Humanities = int(input("Humanities (Choose 1 out of 3):"))
Best_Subject = int(input("Best Subject (other than the ones listed):"))
Next_Best_Subject = int(input("Next best Subject (other than the ones listed):"))
sum = Math + Science + Humanities + Best_Subject + Next_Best_Subject
avg = sum/5

if avg >= 75 and avg <= 100:
    print("You have acheived A1")
elif avg >= 70 and avg <= 74:
    print("You have acheived A2")
elif avg >= 65 and avg <= 69:
    print("You have acheived B3")
elif avg >= 60 and avg <= 64:
    print("You have acheived B4")
elif avg >= 55 and avg <= 59:
    print("You have acheived C5")
elif avg >= 50 and avg <= 54:
    print("You have acheived C6")
elif avg >= 45 and avg <= 49:
    print("You have acheived D7")
elif avg >= 40 and avg <= 44:
    print("You have achieved E8")
elif avg >= 0 and avg <= 39:
    print("You have acheived F9")
else:
    print("Invalid input!")