

Customer_Name = input("Enter Customer Name: ")
Garment_Name = input("Enter Garment Name: ")
Price = float(input("Enter Price of one garment: "))
Quantity = int(input("Enter Number of Garments: "))

Total_Amount = Price * Quantity

print(f"""
==========================================
                  BILL
==========================================

Customer Name : {Customer_Name}
Garment Name  : {Garment_Name}
Price per Unit: Rs. {Price}
Quantity      : {Quantity}
Total Amount  : Rs. {Total_Amount}

==========================================
""")