print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))


total_bill = total_bill * (1 + tip / 100)
total_bill = total_bill / people
total_bill = round(total_bill, 2)

#Wymuszenie 0 po przecinku. Bez tego wygladało by $36.6 a wygląda $36.60 Konwertowanie wyniku na strina z miejscami
#po przecinku
total_bill = "{:.2f}".format(total_bill)

print(f"Each person should pay: ${total_bill}")