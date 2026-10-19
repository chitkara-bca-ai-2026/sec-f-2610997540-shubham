# University Library Management System


books = [
    ("Python Programming", "Guido van Rossum", 1991, "Programming"),
    ("Artificial Intelligence", "Stuart Russell", 2020, "AI"),
    ("Data Structures", "Mark Allen Weiss", 2013, "Computer Science")
]

library_categories = {"Programming", "AI", "Computer Science"}
student_wishlist = {"AI", "Cloud", "Cybersecurity"}


while True:
    print("\n===== UNIVERSITY LIBRARY =====")
    print("1. View Books")
    print("2. Add Book")
    print("3. View Categories")
    print("4. Add Wishlist")
    print("5. Gap Analysis")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    
    if choice == "1":
        print("\n--- Library Books ---")

        for book in books:
            title, author, year, category = book
            print("Title:", title)
            print("Author:", author)
            print("Year:", year)
            print("Category:", category)
            print("--------------------")

        print("Total books:", len(books))

    
    elif choice == "2":
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        year_input = input("Enter publication year: ").strip()
        category = input("Enter category: ").strip()

        if title and author and year_input and category:
            try:
                year = int(year_input)

                
                new_book = (title, author, year, category)

               
                books.append(new_book)
                library_categories.add(category)

                print("[SUCCESS] Book added!")

            except ValueError:
                print("[ERROR] Year must be a number.")
        else:
            print("[ERROR] All fields are mandatory.")

    
    elif choice == "3":
        print("\n--- Unique Library Categories ---")

        for category in sorted(library_categories):
            print(category)

        print("Total genres:", len(library_categories))

    
    elif choice == "4":
        requested_category = input(
            "Enter requested category: "
        ).strip()

        if requested_category:
            student_wishlist.add(requested_category)
            print("[SUCCESS] Added to wishlist!")
        else:
            print("[ERROR] Category cannot be empty.")

    
    elif choice == "5":
        already_in_stock = (
            library_categories & student_wishlist
        )

        purchase_order_needed = (
            student_wishlist - library_categories
        )

        full_combined_coverage = (
            library_categories | student_wishlist
        )

        print("\n--- Category Gap Analysis ---")
        print("1. Already in Stock:", already_in_stock)
        print("2. Purchase Order Needed:", purchase_order_needed)
        print("3. Full Combined Coverage:", full_combined_coverage)

    
    elif choice == "6":
        print("Thank you. Goodbye!")
        break

    
    else:
        print("[INVALID] Enter a number from 1 to 6.")
