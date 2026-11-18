import os
import csv

def read_all_students(filename):
    """Reads the CSV file and displays all rows in a structured tabular format."""
    if not os.path.exists(filename):
        print(f"\nError: {filename} does not exist.")
        return

    print("\n" + "="*8 + " ALL ENROLLED STUDENTS " + "="*8)
    print(f"{'Roll No':<8}{'Name':<12}{'Subject':<10}{'Marks':<6}")
    print("-" * 38)

    total_records = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_records += 1
            print(f"{row['Roll No']:<8}{row['Name']:<12}{row['Subject']:<10}{row['Marks']:<6}")

    print("-" * 38)
    print(f"Total Records: {total_records}")

def filter_students_above_threshold(filename, threshold=50):
    """Reads the CSV file, filters students with marks > threshold, and prints results."""
    if not os.path.exists(filename):
        print(f"\nError: {filename} does not exist.")
        return

    print("\n" + "="*6 + " STUDENTS WITH MARKS > 50 " + "="*6)
    print(f"{'Roll No':<8}{'Name':<12}{'Subject':<10}{'Marks':<6}")
    print("-" * 38)

    qualified_count = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            marks = int(row['Marks'])
            if marks > threshold:
                qualified_count += 1
                print(f"{row['Roll No']:<8}{row['Name']:<12}{row['Subject']:<10}{row['Marks']:<6}")

    print("-" * 38)
    print(f"Qualified Students Count: {qualified_count}")

def create_sample_csv(filename="students_data.csv"):
    """Pre-populates students_data.csv if it doesn't exist."""
    if not os.path.exists(filename):
        data = [
            ["Roll No", "Name", "Subject", "Marks"],
            ["101", "Anas", "Python", "85"],
            ["102", "Riya", "Python", "92"],
            ["103", "Karan", "Python", "40"],
            ["104", "Neha", "Python", "78"],
            ["105", "Rahul", "Python", "38"],
            ["106", "Pooja", "Python", "62"]
        ]
        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)

def main():
    filename = "students_data.csv"
    create_sample_csv(filename)

    while True:
        print("\nSTUDENT RESULT ANALYSIS SYSTEM")
        print("Select an operation:")
        print("1. Display All Students from CSV")
        print("2. Filter Students (Marks > 50)")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == '1':
            read_all_students(filename)
        elif choice == '2':
            filter_students_above_threshold(filename, 50)
        elif choice == '3':
            print("\nThank you for using Student Result Analysis System. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please select between 1 and 3.")

if __name__ == "__main__":
    main()