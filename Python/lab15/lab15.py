# Lab 15 - Student Information Management System

# Student records are stored using roll numbers as dictionary keys.
students = {
    "101": {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [74, 80, 82]
    }
}




while True:
    
    
    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ").strip()


    # 1. Show all student records
    if choice == "1":
        if not students:
            print("No student records found.")
        else:
            print("\n--- Enrolled Student Records ---")
            for roll, student in students.items():
                print(
                    f"Roll No: {roll} | Name: {student['Name']} | "
                    f"Branch: {student['Branch']} | Sem: {student['Semester']} "
                    f"| Marks: {student['Marks']}"
                )
            print("Total Enrolled Students:", len(students))



    # 2. Search for a student
    elif choice == "2":
        roll = input("Enter Roll Number to search: ").strip()
        student = students.get(roll)

        if student is not None:
            print(f"\n[FOUND] Record for Roll No {roll}:")
            print("  Name     :", student["Name"])
            print("  Branch   :", student["Branch"])
            print("  Semester :", student["Semester"])
            print("  Marks    :", student["Marks"])
        else:
            print("[ERROR] Student record not found.")



    # 3. Register a new student
    elif choice == "3":
        print("\n--- Register New Student ---")
        roll = input("Enter Roll Number: ").strip()

        if not roll:
            print("[ERROR] Roll number cannot be empty.")
        elif roll in students:
            print("[ERROR] This roll number already exists.")
        else:
            name = input("Enter Student Name: ").strip()
            branch = input("Enter Branch (e.g. BCA AI): ").strip()
            semester = input("Enter Semester: ").strip()

            try:
                marks = []
                for i in range(3):
                    mark = int(input(f"Enter marks for Subject {i + 1}: "))
                    if mark < 0 or mark > 100:
                        raise ValueError
                    marks.append(mark)

                if not name or not branch or not semester:
                    print("[ERROR] Name, branch and semester cannot be empty.")
                else:
                    students[roll] = {
                        "Name": name,
                        "Branch": branch,
                        "Semester": semester,
                        "Marks": marks
                    }
                    print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")
            except ValueError:
                print("[ERROR] Please enter valid marks from 0 to 100.")




    # 4. Update a student's branch or semester
    elif choice == "4":
        roll = input("Enter Roll Number to update: ").strip()
        student = students.get(roll)

        if student is None:
            print("[ERROR] Student record not found.")
        else:
            print(f"Current details for {student['Name']} (Roll {roll}):")
            print("1. Branch")
            print("2. Semester")
            field = input("Choose field to update (1 or 2): ").strip()

            if field == "1":
                new_branch = input("Enter new branch: ").strip()
                if new_branch:
                    student["Branch"] = new_branch
                    print("[SUCCESS] Branch updated successfully.")
                else:
                    print("[ERROR] Branch cannot be empty.")
            elif field == "2":
                new_semester = input("Enter new semester: ").strip()
                if new_semester:
                    student["Semester"] = new_semester
                    print("[SUCCESS] Semester updated successfully.")
                else:
                    print("[ERROR] Semester cannot be empty.")
            else:
                print("[ERROR] Please choose 1 or 2.")



    # 5. Calculate and display academic performance
    elif choice == "5":
        roll = input("Enter Roll Number for Academic Performance: ").strip()
        student = students.get(roll)

        if student is None:
            print("[ERROR] Student record not found.")
        else:
            total = sum(student["Marks"])
            average = total / len(student["Marks"])
            result = "PASS" if average >= 40 else "FAIL"

            print("\n" + "=" * 18 + " ACADEMIC REPORT " + "=" * 18)
            print(f"Student Name : {student['Name']} (Roll: {roll})")
            print("Subject Marks:", student["Marks"])
            print(f"Total Marks  : {total} / 300")
            print(f"Average Marks: {average:.2f}%")
            print(f"Final Result : {result}")
            print("=" * 52)



    # 6. Delete a student record safely
    elif choice == "6":
        roll = input("Enter Roll Number to delete: ").strip()
        student = students.pop(roll, None)

        if student is not None:
            print(f"[SUCCESS] Record for '{student['Name']}' (Roll No: {roll}) deleted successfully.")
        else:
            print("[ERROR] Student record not found.")

            

    # 7. Exit the program
    elif choice == "7":
        print("\nThank you for using Student Information System.")
        print("Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 7.")
