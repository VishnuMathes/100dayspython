# Pizza Order
print("Welcome to Vishnu Pizza Deliveries!")
size = input("What size pizza do you want? S , M , L \n")
add_pepporoni = input("Do you want pepporoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
bill = 0
if(size == 'S'):
    bill = 15
    if(add_pepporoni == 'Y'):
        bill = bill + 2
    if(extra_cheese == 'Y'):
        bill = bill + 1
    print(f"Your final bill is {bill}")
elif(size == 'M'):
    bill = 20
    if(add_pepporoni == 'Y'):
        bill = bill + 3
    if(extra_cheese == 'Y'):
        bill = bill + 1
    print(f"Your final bill is {bill}")
elif(size == 'L'):
    bill = 25
    if(add_pepporoni == 'Y'):
        bill = bill + 5
    if(extra_cheese == 'Y'):
        bill = bill + 1
    print(f"Your final bill is {bill}")    
else:
    print(f"Your final bill is {bill}")






