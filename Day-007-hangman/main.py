import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
display = []
lives = 6
guessed = []

for letter in chosen_word:
    display += "_"

print(logo)
print(f"Pssst, the word is '{chosen_word}'!")

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print(f"You already guessed '{guess}'")
    else:
        guessed += guess
        for letter in range(0, len(chosen_word)):
            if guess == chosen_word[letter]:
                display[letter] = guess

        if guess not in chosen_word:
            print(f'You guessed "{guess}", that\'s not in the word')
            lives -= 1

        print(stages[lives])
        print(display)

if lives > 0:
    print("You win")
else:
    print("You lose")
