

Username = input("Enter your username: ")
Password = input("Enter your password: ")

Length_Check = len(Password) >= 8

Digit_Check = False
Uppercase_Check = False

for ch in Password:

    if ch.isdigit():
        Digit_Check = True

    if ch.isupper():
        Uppercase_Check = True

print(f"""
==========================================
       PASSWORD VALIDATION REPORT
==========================================

Username: {Username}
Password: {"*" * len(Password)}

--- Validation Rules ---

[{"PASS" if Length_Check else "FAIL"}] Minimum 8 characters ({len(Password)} characters)
[{"PASS" if Digit_Check else "FAIL"}] At least one digit
[{"PASS" if Uppercase_Check else "FAIL"}] At least one uppercase letter

--- Result ---
""")

if Length_Check and Digit_Check and Uppercase_Check:

    print(f"Password is VALID!")
    print(f"Account created successfully for {Username}!")

else:

    print("Password is INVALID.")

print("""
==========================================
""")