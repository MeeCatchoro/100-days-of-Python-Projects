# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt", "r") as name_list:
    names = name_list.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for name in names:
        a = name.strip()
        named_letter = letter.replace("[name]", f"{a}")
        with open(f"./Output/ReadyToSend/letter_to_{a}", "w") as new_letter:
            new_letter.write(named_letter)


