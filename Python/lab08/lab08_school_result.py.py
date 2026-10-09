

Student_Name = input("Enter Student Name: ")
Roll_Number = int(input("Enter Roll Number: "))

print("""
--- Enter Marks for 5 Subjects (0-100) ---
""")

Total_Marks = 0
Failed = False

for i in range(1, 6):

    Marks = float(input(f"Enter marks for Subject {i}: "))

    if Marks < 0 or Marks > 100:
        print("Invalid marks")
        exit()

    Total_Marks = Total_Marks + Marks

    if Marks < 40:
        Failed = True

Percentage = (Total_Marks / 500) * 100

if Failed:
    Result = "FAIL"
    Grade = "F"
    Remarks = "Failed in one or more subjects"

elif Percentage >= 90:
    Result = "PASS"
    Grade = "A+"
    Remarks = "Outstanding"

elif Percentage >= 80:
    Result = "PASS"
    Grade = "A"
    Remarks = "Excellent"

elif Percentage >= 70:
    Result = "PASS"
    Grade = "B"
    Remarks = "Very Good"

elif Percentage >= 60:
    Result = "PASS"
    Grade = "C"
    Remarks = "Good"

elif Percentage >= 50:
    Result = "PASS"
    Grade = "D"
    Remarks = "Satisfactory"

else:
    Result = "PASS"
    Grade = "E"
    Remarks = "Pass"

print(f"""
==========================================
          STUDENT REPORT CARD
==========================================

Student Name : {Student_Name}
Roll Number  : {Roll_Number}

------------------------------------------

Total Marks  : {Total_Marks} / 500.0
Percentage   : {Percentage:.2f}%
Result       : {Result}
Grade        : {Grade}
Remarks      : {Remarks}

==========================================
""")