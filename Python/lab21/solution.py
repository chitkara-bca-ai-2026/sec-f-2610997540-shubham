import os

def get_document_statistics(filename):
    """Reads the file and returns a tuple: (line_count, word_count, char_count)."""
    if not os.path.exists(filename):
        print(f"Error: {filename} does not exist.")
        return 0, 0, 0
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.splitlines()
    line_count = len(lines)
    
    # Count words across all lines separated by whitespace
    words = content.split()
    word_count = len(words)
    
    char_count = len(content)
    
    return line_count, word_count, char_count

def display_document(filename):
    """Reads and prints each line prefixed by its line number."""
    if not os.path.exists(filename):
        print(f"Error: {filename} does not exist.")
        return
    
    print(f"\n--- Document Preview ({filename}) ---")
    with open(filename, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f, start=1):
            print(f"{idx} | {line.rstrip()}")

def create_sample_file(filename="document.txt"):
    """Pre-populates the sample text file if it doesn't exist."""
    if not os.path.exists(filename):
        sample_text = (
            "Artificial Intelligence is transforming modern industries.\n"
            "Python provides powerful libraries for text processing and data analysis.\n"
            "Developers use file handling to store and retrieve persistent records.\n"
            "Modular programming ensures code is clean, reusable, and easy to maintain."
        )
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(sample_text)

def main():
    filename = "document.txt"
    create_sample_file(filename)
    
    while True:
        print("\nDOCUMENT STATISTICS ANALYZER")
        print("Select an operation:")
        print("1. Calculate Document Statistics")
        print("2. Display Document Content")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == '1':
            lines, words, chars = get_document_statistics(filename)
            print(f"\n--- DOCUMENT REPORT ---")
            print(f"Target File         : {filename}")
            print(f"Total Lines         : {lines}")
            print(f"Total Words         : {words}")
            print(f"Total Characters    : {chars}")
        elif choice == '2':
            display_document(filename)
        elif choice == '3':
            print("\nThank you for using Document Statistics Analyzer. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please select between 1 and 3.")

if __name__ == "__main__":
    main()