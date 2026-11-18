# Student Information Management System 

print("=============================")
print(" STUDENT INFORMATION SYSTEM ")
print("=============================")

#Taking student information 
name = input("Enter Student name:")
age = int(input("Enter Student age: "))
course = input("Enter your course: ")
semester = int(input("Enter semester: "))

#Taking academic information 
python_marks = float(input("Enter python marks: "))
java_marks = float(input("Enter Java marks: "))
maths_marks = float(input("Enter Maths marks: "))

#Boolean data type
is_student = True

#List data type
subjects = ["python", "java", "maths"]

#Tuple dtat type
college_details = ("RCU", "Bishrampur")

#Dictionary data type 
student = {
    "name": name,
    "age": age,
    "semester": semester,
    "college": college_details[0]

}
#Calculating results
total_marks = python_marks + java_marks + maths_marks
average = total_marks /3

#Displaying information
print("\n===========STUDENT REPORT===========")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Semester:", student["semester"])
print("College:", student["college"])


print("\n========== ACADEMIC DETAILS ==========")

print("Subjects:", subjects)
print("Python Marks:", python_marks)
print("Java Marks:", java_marks)
print("Maths Marks:", maths_marks)

print("Total Marks:", total_marks)
print("Average Marks:", average)

print("\n========== DATA TYPES ==========")

print("Name Type:", type(name))
print("Age Type:", type(age))
print("Marks Type:", type(python_marks))
print("Student Status Type:", type(is_student))
print("Subjects Type:", type(subjects))
print("College Details Type:", type(college_details))
print("Student Dictionary Type:", type(student))

print("\n===================================")
print("       REPORT GENERATED!")
print("===================================")
