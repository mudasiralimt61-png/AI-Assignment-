def calculate_result(marks):
    total = sum(marks)
    percentage = total / 3

    if percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade


students = []

for i in range(5):
    print("\nEnter details for student", i + 1)
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    python_marks = float(input("Enter Python marks: "))
    ai_marks = float(input("Enter AI marks: "))
    maths_marks = float(input("Enter Maths marks: "))

    marks = [python_marks, ai_marks, maths_marks]
    total, percentage, grade = calculate_result(marks)

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }
    students.append(student)

print("\n----- STUDENT RESULTS -----")
for student in students:
    print("Name:", student["name"])
    print("Roll No:", student["roll_no"])
    print("Total:", student["total"])
    print("Percentage:", round(student["percentage"], 2))
    print("Grade:", student["grade"])
    print("---------------------------")

highest = students[0]
for student in students:
    if student["percentage"] > highest["percentage"]:
        highest = student

with open("results.txt", "w", encoding="utf-8") as file:
    for student in students:
        file.write("Name: " + student["name"] + "\n")
        file.write("Roll No: " + student["roll_no"] + "\n")
        file.write("Total: " + str(student["total"]) + "\n")
        file.write("Percentage: " + str(round(student["percentage"], 2)) + "\n")
        file.write("Grade: " + student["grade"] + "\n")
        file.write("---------------------------\n")

    file.write("Highest Percentage: " + highest["name"] + " - " +
               str(round(highest["percentage"], 2)) + "%\n")

print("Results saved in results.txt")
