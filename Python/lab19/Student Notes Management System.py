import os


def write_notes(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"[SUCCESS] Notes successfully saved to '{filename}'.")


def read_notes(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    return "No notes file exists yet."


def show_menu():
    print("\nSelect an operation:")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")


def main():
    filename = "notes.txt"

    print("=" * 40)
    print("       STUDENT NOTES MANAGEMENT SYSTEM")
    print("=" * 40)

    while True:
        show_menu()
        choice = input("\nEnter choice (1-3): ").strip()

        if choice == "1":
            content = input("Enter notes to save: ")
            write_notes(filename, content)

        elif choice == "2":
            content = read_notes(filename)
            print(f"\n--- Notes Content ({filename}) ---")
            print(content)

        elif choice == "3":
            print("Thank you for using the Notes Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please select from 1 to 3.")


if __name__ == "__main__":
    main()
