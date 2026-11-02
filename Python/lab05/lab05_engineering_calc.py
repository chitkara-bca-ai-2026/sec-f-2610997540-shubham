import math



Value = float(input("Enter a numerical value: "))
Exponent = float(input("Enter an exponent: "))
Decimal_Measurement = float(input("Enter a decimal measurement: "))

Power = math.pow(Value, Exponent)
Square_Root = math.sqrt(Value)
Ceil_Value = math.ceil(Decimal_Measurement)
Floor_Value = math.floor(Decimal_Measurement)

print(f"""
--- Results ---

Value             : {Value}
Exponent          : {Exponent}
Power (pow)       : {Power}
Square Root (sqrt): {Square_Root:.4f}
Decimal Value     : {Decimal_Measurement}
Ceil Value        : {Ceil_Value}
Floor Value       : {Floor_Value}
==========================================
""")