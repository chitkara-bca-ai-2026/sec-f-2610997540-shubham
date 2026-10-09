
Product_Name = input("Enter Product Name : ")
Price = float(input("Enter Price        : "))
Quantity = int(input("Enter Quantity     : "))

Total_Price = Price * Quantity

Amount_Str = str(Total_Price)

print(f"""
------------------------------------------
          TYPE CASTING SUMMARY
------------------------------------------

Variable        Value          Python Type
------------------------------------------
product_name    {Product_Name}          {type(Product_Name)}
price           {Price}          {type(Price)}
quantity        {Quantity}             {type(Quantity)}
total_price     {Total_Price}          {type(Total_Price)}
amount_str      {Amount_Str}          {type(Amount_Str)}
""")
print(f"""
------------------------------------------
              TAX INVOICE
------------------------------------------

Product Name    : {Product_Name}
Price per Unit  : Rs. {Price}
Quantity        : {Quantity}
------------------------------------------
Invoice Total   : Rs. {Amount_Str}
==========================================
""")