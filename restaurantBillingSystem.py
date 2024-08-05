name = input("Please enter your name: ")
amount = int(input("Please enter the amount: "))
tip = amount/10
GST = amount/5
total = amount + tip + GST
if amount>20: print(amount),print(tip)
print(f"""
    Restaurant Bill
Name:               {name}
Amount:         Rs. {amount}
Tip (10%):      Rs. {tip}   
GST (20%):      Rs. {GST}   
------------------------------
Total Bill:     Rs. {total}

Thanks for your visit.
Have a nice day!
""")
input("Press Enter to exit...")