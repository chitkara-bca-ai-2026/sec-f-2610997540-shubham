Tuition_Fee = float(input("Enter tuition fee: "))
Lab_Fee = float(input("Enter lab fee: "))
Library_Fee = float(input("Enter library fee: "))
Exam_Fee = float(input("Enter exam fee: "))
Discount_Amount = float(input("Enter discounted amount: "))

Total_before_discount = Tuition_Fee + Lab_Fee + Library_Fee + Exam_Fee

Total_after_discount = Total_before_discount - Discount_Amount

Anual_fee = Total_after_discount * 2
Monthly_instalment = Anual_fee / 12

print(f"Tuition Fee: {Tuition_Fee}\nLab Fee: {Lab_Fee}\nLibrary Fee: {Library_Fee}\nExam Fee: {Exam_Fee}\nTotal Fee: {Total_before_discount}\nDiscount: {Discount_Amount}\nFee after Discount: {Total_after_discount}\nAnnual Fee: {Anual_fee}\nMonthly Installment: {Monthly_instalment}")