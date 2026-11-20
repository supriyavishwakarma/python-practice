#==========================================
#PROJECT: SMART STUDENT MANAGEMENT SYSTEM
#==========================================

# CONCEPT 1: VARIABLES AND INPUT
# Take student personal information

student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
roll_number = int(input("Enter roll number: "))
college_name = input("Enter college name: ")

# CONCEPT 2: DATA TYPES
# Take marks of five subjects

python_marks = float(input("Enter Python marks: "))
java_marks = float(input("Enter Java marks: "))
math_marks = float(input("Enter Maths marks: "))
dbms_marks = float(input("Enter DBMS marks: "))
coa_marks = float(input("Enter COA marks: "))

# CONCEPT 3: ARITHMETIC OPERATORS
# Calculate total, average and percentage

total_marks = (python_marks + java_marks +
               math_marks + dbms_marks + coa_marks)

average = total_marks / 5
percentage = (total_marks / 500) * 100

# CONCEPT 4: COMPARISON OPERATORS
# Compare marks and identify highest/lowest

highest_marks = max(python_marks, java_marks,
                    math_marks, dbms_marks, coa_marks)

lowest_marks = min(python_marks, java_marks,
                   math_marks, dbms_marks, coa_marks)

# CONCEPT 5: ASSIGNMENT OPERATORS
# Calculate college fee details

total_fees = float(input("Enter total college fees: "))
paid_fees = float(input("Enter fees already paid: "))

remaining_fees = total_fees
remaining_fees -= paid_fees

# CONCEPT 6: ARITHMETIC OPERATORS
# Calculate fee payment percentage

fee_percentage = (paid_fees / total_fees) * 100

# CONCEPT 7: OUTPUT AND TYPE FUNCTION
# Display complete student report

print("\n================================")
print("       STUDENT REPORT CARD")
print("================================")

print("Student Name:", student_name)
print("Student Age:", student_age)
print("Roll Number:", roll_number)
print("College:", college_name)

print("\n---------- MARKS ----------")
print("Python:", python_marks)
print("Java:", java_marks)
print("Maths:", math_marks)
print("DBMS:", dbms_marks)
print("COA:", coa_marks)

print("\n---------- RESULT ----------")
print("Total Marks:", total_marks, "/ 500")
print("Average:", average)
print("Percentage:", percentage, "%")
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)

print("\n---------- FEES ----------")
print("Total Fees:", total_fees)
print("Paid Fees:", paid_fees)
print("Remaining Fees:", remaining_fees)
print("Fee Payment Percentage:", fee_percentage, "%")

# CONCEPT 8: TYPE CHECKING

print("\n---------- DATA TYPES ----------")
print("Name Type:", type(student_name))
print("Age Type:", type(student_age))
print("Marks Type:", type(python_marks))
print("Percentage Type:", type(percentage))

print("\n================================")
print("       REPORT GENERATED!")
print("================================")
