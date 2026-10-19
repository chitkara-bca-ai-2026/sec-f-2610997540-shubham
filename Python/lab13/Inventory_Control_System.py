
# Lab 13 - Inventory Control System


store = ["Notebook", "Pen", "Eraser", "Ruler"]

while True:
    
    print("=" * 40)
    print("       INVENTORY CONTROL SYSTEM")
    print("=" * 40)

    print("\nSelect an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    c = input("\nEnter your choice (1-5): ")

   
    if c == "1":
        print("\n--- Current Inventory ---")

        if len(store) == 0:
            print("Inventory is empty.")
        else:
            i=1
            for  item in store:
                print(f"{i}. {item}")
                i += 1
    
    elif c == "2":
        item = input("Enter item name to add: ").strip()

        if i in item:
            store.append(i)
            print(f'[SUCCESS] "{i}" added to inventory.')
        else:
            print("Error: Item name cannot be empty.")

   
    elif c == "3":
        item = input("Enter item name to remove: ").strip()

        if item in store:
            store.remove(item)
            print(f'[SUCCESS] "{item}" removed from inventory.')
        else:
            print(f'Error: "{item}" not found in inventory.')

    
    elif c == "4":
        store.sort(key=str.lower)

        print("\n[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")

        for i, item in enumerate(store, start=1):
            print(f"{i}. {item}")

    
    elif c == "5":
        print("\nThank you for using the Inventory Control System!")
        break

   
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
