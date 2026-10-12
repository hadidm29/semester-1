# Worksheet 1.2: Task 1 Solution
import sys
grade = input("Enter integer grade between 0 & 100: ")

if not grade.isdecimal() or int(grade) < 0 or int(grade) > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

grade = int(grade)
if grade >=70:
    result = "Distinction"
elif grade >= 40:
    result = "Pass"
else:
    result = "Fail"

print(f"{grade} is a {result}")