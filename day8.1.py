# def greet():
#     print("Hello")
#     print("How are you?")
#     print("All is well")

# greet()

# function with 1 input
# def greet_with_name(name): #parameter is name # argument is the value
#     print(f"Hello {name}")
#     print("How are you?")

# greet_with_name("Vishnu")

# Function with more than one input
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# greet_with("Vishnu", "US")

# function with keyword argument
def greet_with_name(name, location): #parameter is name # argument is the value
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with_name(name = "Vishnu" , location = "US" )