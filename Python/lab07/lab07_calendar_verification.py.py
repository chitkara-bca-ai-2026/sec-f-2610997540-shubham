

Year = int(input("Enter year: "))

if Year <= 0:
    print("Invalid year")
else:

    if Year % 400 == 0:
        Status = "LEAP YEAR"
        Days_In_Year = 366
        Days_In_February = 29
        Reason = "Century year divisible by 400"

    elif Year % 100 == 0:
        Status = "COMMON YEAR"
        Days_In_Year = 365
        Days_In_February = 28
        Reason = "Century year not divisible by 400"

    elif Year % 4 == 0:
        Status = "LEAP YEAR"
        Days_In_Year = 366
        Days_In_February = 29
        Reason = "Divisible by 4 and not a century year"

    else:
        Status = "COMMON YEAR"
        Days_In_Year = 365
        Days_In_February = 28
        Reason = "Not divisible by 4"

    print(f"""
------------------------------------------
Year: {Year}
Status: {Status}
Days in Year: {Days_In_Year} days
Days in February: {Days_In_February} days
Reason: {Reason}
------------------------------------------
""")