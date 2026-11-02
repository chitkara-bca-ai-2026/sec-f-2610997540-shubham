
n = int(input("enter no. of rows "))

print("""
Enter the number of rows:
Pattern 1: Star Triangle
------------------------
""")

for row in range(1, n + 1):

    for col in range(row):
        print("*", end=" ")

    print()

print("""
Pattern 2: Number Triangle
--------------------------
""")

for row in range(1, n + 1):

    for col in range(1, row + 1):
        print(col, end=" ")

    print()

print("""
Pattern 3: Inverted Star Triangle
---------------------------------
""")

for row in range(n, 0, -1):

    for col in range(row):
        print("*", end=" ")

    print()

print("""
Pattern 4: Pyramid
------------------
""")

for row in range(1, n + 1):

    for space in range(n - row):
        print(" ", end=" ")

    for col in range(2 * row - 1):
        print("*", end=" ")

    print()