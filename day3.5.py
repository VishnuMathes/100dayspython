height = int(input("What's your height in cm? "))
age = int(input("What's your age?"))
bill = 0
if(height >= 120):
    if(age <12):
        bill=5
        print("The child ticlet is $5")
    elif(age <= 18):
        bill = 7
        print("The adult ticket is $7")
    elif(age > 18 and age < 45 ):
        bill = 9
        print("The younster ticket is $9")
    else:
        bill = 0
        print("The senior ticket is $0")
    want_photo = input("You need to take the photo? Y or N.\n ")
    if(want_photo == 'Y'):
      bill = bill + 3
      print("Your bill amount is: ", bill)
else:
    print("Sorry, You can't ride the roller coaster")


