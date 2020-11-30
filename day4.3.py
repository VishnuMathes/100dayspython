# Who is going to pay the bill
import random

test_seed = int(input("Create your seed number: \n"))
random.seed(test_seed)
nameascsv = input("Give everybodys name: \n")
names = nameascsv.split(",")
# Get the length of the names
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_pay_the_bill = names[random_choice]
print(person_who_pay_the_bill , "is going to pay for the meal")

# person_who_pay_the_bill = random.choice(names)