import os

def store_student(filename, name, marks):
    """Opens student_marks.txt in append mode and stores name,marks."""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"{name},{marks}\n")
    print(f"\n[SUCCESS] Record for '{name}' ({marks} marks) stored successfully.")

def display_and_calculate_average(filename):
    """Checks file, parses lines, computes totals, and displays student table."""
    if not os.path.exists(filename):
        print("\nNo student records found yet.")
        return

    print("\n" + "="*8 + " STUDENT MARKS LEDGER " + "="*8)
    print(f"{'No.':<5}{'Student Name':<20}{'Marks Obtained':<15}")
    print("-" * 43)

    total_students = 0
    total_marks = 0

    with open(filename, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f, start=1):
            line = line.strip()
            if line:
                parts = line.split(',')
                if len(parts) == 2:
                    name, marks_str = parts[0].strip(), parts[1].strip()
                    marks = int(marks_str)
                    total_students += 1
                    total_marks += marks
                    print(f"{idx:<5}{name:<20}{marks:<15}")

    print("-" * 43)
    print(f"Total Students : {total_students}")
    print(f"Total Marks    : {total_marks}")
    
    if total_students > 0:
        class_average = total_marks / total_students
        print(f"Class Average  : {class_average:.2f}")
    else:
        print("Class Average  : 0.00")
    print("=" * 39)

def create_sample_file(filename="student_marks.txt"):
    """Pre-populates sample records if the file doesn't exist."""
    if not os.path.exists(filename):
        sample_data = "Anas,85\nRiya,92\nKaran,40\n"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(sample_data)

def main():
    filename = "student_marks.txt"
    create_sample_file(filename)

    while True:
        print("\nSTUDENT MARKS FILE HANDLING TOOL")
        print("Select an operation:")
        print("1. Display Records & Class Average")
        print("2. Add & Store Student Marks")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == '1':
            display_and_calculate_average(filename)
        elif choice == '2':
            name = input("Enter Student Name: ").strip()
            if not name:
                print("Name cannot be empty.")
                continue
            
            try:
                marks = int(input("Enter Marks (0-100): ").strip())
                if 0 <= marks <= 100:
                    store_student(filename, name, marks)
                else:
                    print("Error: Marks must be between 0 and 100.")
            except ValueError:
                print("Error: Please enter a valid integer for marks.")
        elif choice == '3':
            print("\nThank you for using Student Marks Text. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please select between 1 and 3.")

if __name__ == "__main__":
    main()