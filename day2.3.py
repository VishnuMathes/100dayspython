# Tip calculator
print("Welcome to tip calculator")
bill_amount = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, 15 ? "))
bill_with_tip = bill_amount * (1 + (tip_percent/100))
no_of_people = int(input("How many people like to split the bill? "))
split_bill = float((bill_with_tip)/no_of_people)
# print(split_bill)
final_bill = round(split_bill,2)
print("Each person should pay: ", final_bill)


