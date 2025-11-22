# Simple Student Grade Calculator System

print("=== Student Grade Calculator ===")

prelim = float(input("Enter Prelim Grade: "))
midterm = float(input("Enter Midterm Grade: "))
finals = float(input("Enter Final Exam Grade: "))

final_grade = (prelim * 0.30) + (midterm * 0.30) + (finals * 0.40)

print("\nFinal Grade:", round(final_grade, 2))

if final_grade >= 75:
    print("Status: PASSED")
else:
    print("Status: FAILED")
