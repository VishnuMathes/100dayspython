import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user-choice = int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for scissors"))
random_choice = random.randint(0, 2)
print("random_choice")
if(random_choice == 0 and user_choice == 2 ):
    print("You won")
elif(random_choice == 1 and user_choice == 2):
    print("You won")
elif(user_choice == 0 and random_choice == 2):
    print("You won")
elif(user_choice == 1 and random_choice == 2):
    print("You won")
elif(user_choice ==  random_choice):
    print("Its a draw")

