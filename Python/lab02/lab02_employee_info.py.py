Employee_Name = input("Enter Employee Name: ")
print("Data type:", type(Employee_Name))

Employee_ID = int(input("Enter Employee ID: "))
print("Data type:", type(Employee_ID))

Salary = float(input("Enter Salary: "))
print("Data type:", type(Salary))

Department = input("Enter Department: ")
print("Data type:", type(Department))

Active_Input = input("Is the employee active? (yes/no): ")
Active = Active_Input == "yes"
print("Data type:", type(Active))

print(f"--- Employee Details --- \nName       : {Employee_Name}\nID         : {Employee_ID}\nSalary     : {Salary}\nDepartment : {Department}\nActive     : {Active}")