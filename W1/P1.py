roll_no = 101
name = "Naresh"
age = 22

python_marks = 85
java_marks = 78
dbms_marks = 92
os_marks = 81
maths_marks = 75

total = python_marks + java_marks + dbms_marks + os_marks + maths_marks
percentage = total / 5

if (python_marks >= 40 and
    java_marks >= 40 and
    dbms_marks >= 40 and
    os_marks >= 40 and
    maths_marks >= 40):
    result = "PASS"
else:
    result = "FAIL"



print("\nInfo")

print(f"Roll Number : {roll_no}")
print(f"Name: {name}")
print(f"Age: {age}")

print("\nMarks")

print(f"Python : {python_marks}")
print(f"Java : {java_marks}")
print(f"DBMS   : {dbms_marks}")
print(f"Operating System  : {os_marks}")
print(f"Mathematics  : {maths_marks}")

print("\nResult")

print(f"Total Marks : {total}")
print(f"Percentage : {percentage:.2f}%")
print(f"Result  : {result}")
