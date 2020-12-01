def prime_checker(number):
    for i in range(2,number):
        if number%i == 0:
            print("It is not a prime number")
            return
    print("It is a prime number")

n = int(input("Check this number:"))
prime_checker(number = n)