# Grade Calculator:

# Write a program that calculates and displays the letter grade

# for a given numerical score (e.g., A, B, C, D, or F)

# based on the following grading scale

# A: 90-100

# B: 80-89

# C: 70-79

# D: 60-69

# F: 0-59


# 1 -> User Inputs - score -> int

# 2 ->  O/p -> str -> A, B
score = int(input("Enter your score (0-100): "))

if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80 and score < 90:
    grade = "B"
elif score >= 70 and score < 80:
    grade = "C"
elif score >= 60 and score < 70:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)
