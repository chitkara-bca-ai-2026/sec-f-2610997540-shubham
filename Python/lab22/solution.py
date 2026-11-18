import os

def search_keyword(filename, keyword):
    """Searches the document line-by-line for a keyword (case-insensitive)."""
    if not os.path.exists(filename):
        print(f"Error: {filename} does not exist.")
        return

    print(f"\n--- Search Results for '{keyword}' ---")
    total_occurrences = 0
    match_count = 0

    with open(filename, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, start=1):
            # Case-insensitive check using .lower()
            if keyword.lower() in line.lower():
                occurrences_in_line = line.lower().count(keyword.lower())
                total_occurrences += occurrences_in_line
                match_count += 1
                print(f"Line {line_num} ({occurrences_in_line} match): {line.strip()}")

    if match_count == 0:
        print(f"No occurrences of '{keyword}' found in the document.")
    else:
        print(f"\n[FOUND] Total occurrences of '{keyword}': {total_occurrences}")

def display_document(filename):
    """Reads and displays all text lines with line numbers."""
    if not os.path.exists(filename):
        print(f"Error: {filename} does not exist.")
        return

    print(f"\n--- Full Report Document ({filename}) ---")
    with open(filename, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f, start=1):
            print(f"{idx} | {line.rstrip()}")

def create_sample_file(filename="report.txt"):
    """Pre-populates the sample report file if it doesn't exist."""
    if not os.path.exists(filename):
        sample_text = (
            "Annual Technology and AI Progress Report.\n"
            "The adoption of Artificial Intelligence accelerated across business units.\n"
            "AI algorithms improved diagnostic accuracy in healthcare operations.\n"
            "Data engineering pipelines were upgraded to support real-time data streaming.\n"
            "The company plans further investments in AI research and machine learning."
        )
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(sample_text)

def main():
    filename = "report.txt"
    create_sample_file(filename)

    while True:
        print("\nKEYWORD SEARCH UTILITY")
        print("Select an operation:")
        print("1. Search Keyword in Document")
        print("2. View Full Document")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == '1':
            keyword = input("Enter keyword to search: ").strip()
            if keyword:
                search_keyword(filename, keyword)
            else:
                print("Keyword cannot be empty.")
        elif choice == '2':
            display_document(filename)
        elif choice == '3':
            print("\nThank you for using Keyword Search Utility. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please select between 1 and 3.")

if __name__ == "__main__":
    main()