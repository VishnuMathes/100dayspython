# Love Calculator
print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
counting_t = lower_case_name1.count('t') + lower_case_name2.count('t')
counting_r = lower_case_name1.count('r') + lower_case_name2.count('r')
counting_u = lower_case_name1.count('u') + lower_case_name2.count('u')
counting_e = lower_case_name1.count('e') + lower_case_name2.count('e')
count_of_true = (counting_t + counting_r + counting_u + counting_e)
print(count_of_true)
counting_l = lower_case_name1.count('l') + lower_case_name2.count('l')
counting_o = lower_case_name1.count('o') + lower_case_name2.count('o')
counting_v = lower_case_name1.count('v') + lower_case_name2.count('v')
counting_e = lower_case_name1.count('e') + lower_case_name2.count('e')
count_of_love = (counting_l + counting_o + counting_v + counting_e)
print(count_of_love)
love_percent1 = str(count_of_true)
love_percent2 = str(count_of_love)
love_score_str = love_percent1 + love_percent2
love_score = int(love_score_str)
if(love_score < 10 or love_score > 90):
    print(f"Your score is {love_score} , you go together like coke and mentos ")
elif(love_score >= 40 or love_score <= 50):
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")