marks = [85, 72, 90, 68, 75, 90, 82, 60, 75, 95]

students = ["Amit", "Rahul", "Priya", "Sneha", "Karan",
            "Neha", "Riya", "Arjun", "Pooja", "Vikas"]

marks_tuple = tuple(marks)

student_marks = {}

for i in range(10):
    student_marks[students[i]] = marks[i]

highest = max(marks)
lowest = min(marks)

total = sum(marks)
average = total / len(marks)

unique_marks = set(marks)

print("Student Marks Analysis")
print("----------------------")

print("\nMarks List:")
print(marks)

print("\nMarks Tuple:")
print(marks_tuple)

print("\nStudent Names and Marks:")
for name in student_marks:
    print(name, ":", student_marks[name])

print("\nHighest Marks :", highest)
print("Lowest Marks :", lowest)
print("Average Marks :", average)

print("\nStudents Scoring Above Average:")
for name in student_marks:
    if student_marks[name] > average:
        print(name, ":", student_marks[name])

print("\nUnique Marks:")
print(unique_marks)
