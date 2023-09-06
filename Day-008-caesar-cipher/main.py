import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    txt = ""
    if direction == "decode":
        shift *= -1
    shift %= 26
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            position += shift
            txt += alphabet[position]
        else:
            txt += letter
    print(f"Here's the {direction}d result:\n{txt}")

proceed = True
while proceed:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "decode" or direction == "encode":
        proceed = True
    else:
        print("Direction not valid")
        proceed = False
        
    text = input("Type your message:\n").lower()
    shift = int(input("Type a shift number between 0 and 26:\n"))
    
    if proceed:
        caesar(text=text, shift=shift, direction=direction)
        
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    
    if go_again == "yes":
        proceed = True
    elif go_again == "no":
        proceed = False
    else:
        print("Invalid input, shutting down.")
        proceed = False