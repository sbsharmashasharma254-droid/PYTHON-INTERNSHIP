# STUDENT MARKS ANALIZER

total = 0

# Taking marks of 5 subjects
for i in range(1, 6):
    marks = float(input(f"Enter marks of subject {i}: "))
    total = total + marks

# Calculate percentage
percentage = total / 5

# Determine grade
if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

# Display result
print("Total Marks =", total)
print("Percentage =", percentage, "%")
print("Grade =", grade)