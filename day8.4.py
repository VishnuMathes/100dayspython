alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# def encrypt(plain_text,shift_amt):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amt
#         new_letter = alphabet[new_position]
#         cipher_text = cipher_text + new_letter
#     print(f"The encoded string is {cipher_text}")


# def decrypt(cipher_text, shift_amt):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amt
#         new_letter = alphabet[new_position]
#         plain_text = plain_text + new_letter
#     print(f"The decoded sting is {plain_text}")

# if direction == "encode":
#     encrypt(plain_text = text, shift_amt = shift)
# elif direction == "decode":
#     decrypt(cipher_text = text, shift_amt = shift) 

# Ceaser function
def caeser(start_text,shift_amt,cipher_direction):
    end_text=""
    if cipher_direction == "decode":
        shift_amt = shift_amt * -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amt
            end_text = end_text + alphabet[new_position]
        else:
            end_text = end_text + char
            
    print(f"Here's the {direction}d result: {end_text}")

should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25

    caeser(start_text = text,shift_amt = shift,cipher_direction = direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")