import os


def append_entry(filename, entry):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(entry + "\n")
    print(f"[SUCCESS] New entry logged to '{filename}'.")


def display_log(filename):
    with open(filename, "r", encoding="utf-8") as file:
        entries = file.readlines()

    print("\n============= DAILY LOG BOOK =============")
    for number, entry in enumerate(entries, start=1):
        print(f"[{number:02}] {entry.strip()}")

    print(f"\nTotal Logged Entries: {len(entries)}")
    print("===========================================")


def show_menu():
    print("\nSelect an operation:")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")


def main():
    filename = "daily_log.txt"

    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write("09:00 AM - System server startup verified.\n")
            file.write("10:30 AM - Morning attendance synchronized.\n")
            file.write("02:15 PM - Network security patch applied.\n")

    print("=" * 40)
    print("          OFFICE DAILY LOG BOOK")
    print("=" * 40)

    while True:
        show_menu()
        choice = input("\nEnter choice (1-3): ").strip()

        if choice == "1":
            entry = input("Enter log entry: ").strip()

            if entry:
                append_entry(filename, entry)
            else:
                print("Error: Log entry cannot be empty.")

        elif choice == "2":
            display_log(filename)

        elif choice == "3":
            print("Thank you for using the Daily Log Book. Goodbye!")
            break

        else:
            print("Invalid choice! Please select from 1 to 3.")


if __name__ == "__main__":
    main()
