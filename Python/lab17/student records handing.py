
def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


def display_student(roll, student):
    marks = student["Marks"]
    total, average = calculate_results(marks)

    print(
        f"Roll No: {roll} | Name: {student['Name']:<12} | "
        f"Marks: {marks} | Total: {total} | Average: {average:.2f}%"
    )


def add_student(records, roll, name, marks):
    if roll in records:
        print("Error: This roll number already exists.")
    else:
        records[roll] = {
            "Name": name,
            "Marks": marks
        }

        print(
            f"[SUCCESS] Student '{name}' "
            f"(Roll No: {roll}) added successfully."
        )


def show_menu():
    print("\nSelect an operation:")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")


def main():
    students = {
        "101": {
            "Name": "Aman",
            "Marks": [85, 90, 78]
        },
        "102": {
            "Name": "Riya",
            "Marks": [92, 88, 95]
        },
        "103": {
            "Name": "Karan",
            "Marks": [74, 80, 82]
        }
    }

    print("=" * 40)
    print("    STUDENT RECORDS MANAGEMENT SYSTEM")
    print("=" * 40)

    while True:
        show_menu()

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "1":
            print("\n--- All Student Records ---")

            for roll, student in students.items():
                display_student(roll, student)

            print("Total Students:", len(students))

        elif choice == "2":
            print("\n--- Add New Student ---")

            roll = input("Enter Roll Number: ").strip()

            if roll in students:
                print("Error: This roll number already exists.")
                continue

            name = input("Enter Student Name: ").strip()

            try:
                marks = []

                for subject in range(1, 4):
                    mark = int(
                        input(f"Enter marks for Subject {subject}: ")
                    )

                    if mark < 0 or mark > 100:
                        print("Error: Marks must be between 0 and 100.")
                        break

                    marks.append(mark)

                if len(marks) == 3:
                    add_student(students, roll, name, marks)

            except ValueError:
                print("Error: Please enter marks as whole numbers.")

        elif choice == "3":
            roll = input("Enter Roll Number to search: ").strip()

            student = students.get(roll)

            if student is not None:
                print("[RECORD FOUND]")
                display_student(roll, student)

            else:
                print(
                    f"[ERROR] No student found with "
                    f"Roll Number '{roll}'."
                )

        elif choice == "4":
            print(
                "Thank you for using the Student Records System. "
                "Goodbye!"
            )
            break

        else:
            print("Invalid choice! Please select from 1 to 4.")


if __name__ == "__main__":
    main()
