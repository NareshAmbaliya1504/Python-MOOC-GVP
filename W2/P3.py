NUM_STUDENTS = 10
NUM_SUBJECTS = 5

subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]

students = []

print("Enter Student Details")

for i in range(NUM_STUDENTS):
    print(f"\nStudent {i + 1}")
    roll = int(input("Roll Number: "))
    name = input("Name: ")

    marks = []
    for j in range(NUM_SUBJECTS):
        mark = float(input(f"Marks in {subjects[j]}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / NUM_SUBJECTS

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    student = {
        "Roll": roll,
        "Name": name,
        "Marks": tuple(marks),
        "Total": total,
        "Percentage": percentage,
        "Grade": grade
    }

    students.append(student)

print("\nSTUDENT RECORDS")

for s in students:
    print(f"""
Roll Number : {s['Roll']}
Name        : {s['Name']}
Marks       : {s['Marks']}
Total       : {s['Total']}
Percentage  : {s['Percentage']:.2f}
Grade       : {s['Grade']}
""")

class_avg = sum(s["Percentage"] for s in students) / NUM_STUDENTS

print(f"Class Average Percentage = {class_avg:.2f}")

highest = max(s["Total"] for s in students)

print("\nHighest Scorer(s):")
for s in students:
    if s["Total"] == highest:
        print(f"{s['Name']} ({s['Total']})")

lowest = min(s["Total"] for s in students)

print("\nLowest Scorer(s):")
for s in students:
    if s["Total"] == lowest:
        print(f"{s['Name']} ({s['Total']})")

print("\nStudents Above Class Average:")
for s in students:
    if s["Percentage"] > class_avg:
        print(s["Name"], f"({s['Percentage']:.2f}%)")

print("\nStudents Failed in One or More Subjects:")
failed = False

for s in students:
    if any(mark < 40 for mark in s["Marks"]):
        print(s["Name"])
        failed = True

if not failed:
    print("No student failed.")

grade_dict = {}

for s in students:
    grade = s["Grade"]
    if grade not in grade_dict:
        grade_dict[grade] = []
    grade_dict[grade].append(s["Name"])

print("\nStudents Grouped by Grade")
for grade, names in grade_dict.items():
    print(grade, ":", names)

print("\nNames in Alphabetical Order")
for name in sorted([s["Name"] for s in students]):
    print(name)

first = -1
second = -1
second_student = None

for s in students:
    total = s["Total"]

    if total > first:
        second = first
        first = total
        second_student = None
    elif first > total > second:
        second = total
        second_student = s

print("\nSecond Highest Scorer:")
if second_student:
    print(second_student["Name"], second_student["Total"])
else:
    print("No unique second highest scorer.")

subject_totals = [0] * NUM_SUBJECTS

for s in students:
    for i in range(NUM_SUBJECTS):
        subject_totals[i] += s["Marks"][i]

subject_avg = [x / NUM_STUDENTS for x in subject_totals]

max_avg = max(subject_avg)
best_subject = subject_avg.index(max_avg)

print("\nSubject-wise Averages")
for i in range(NUM_SUBJECTS):
    print(subjects[i], ":", f"{subject_avg[i]:.2f}")

print(f"\nSubject with Highest Average: {subjects[best_subject]} ({max_avg:.2f})")

name_count = {}
duplicates = []

for s in students:
    name = s["Name"]
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1

for name, count in name_count.items():
    if count > 1:
        duplicates.append(name)

print("\nDuplicate Student Names")

if duplicates:
    print("Duplicate Entries:")
    for name in duplicates:
        print(name)

    unique_names = list(dict.fromkeys([s["Name"] for s in students]))
    print("\nNames after Removing Duplicates:")
    print(unique_names)
else:
    print("No duplicate names found.")
