import random
from art import logo
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_game():
    player_hand = random.choices(cards, k=2)
    dealer_hand = random.choices(cards, k=2)
    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)
    print(
        f" Your cards: {player_hand}, current score: {player_score}\n Computer\'s first card: {dealer_hand[0]}"
    )

    dealer_draw = False
    while dealer_score <= 16:
        dealer_draw = True
        dealer_hand.append(random.choice(cards))
        dealer_score = sum(dealer_hand)
        while 11 in dealer_hand and dealer_score > 21:
            dealer_hand[dealer_hand.index(11)] = 1
            dealer_score -= 10
    if player_score == 21 and dealer_score == 21 and dealer_draw == False:
        return f" Your final hand: {player_hand}, final score: {player_score}\n Computer\'s final hand: {dealer_hand}, final score: {dealer_score}\n Draw"
    elif player_score == 21:
        return f" Your final hand: {player_hand}, final score: {player_score}\n Computer\'s final hand: {dealer_hand}, final score: {dealer_score}\n Win with a blackjack"

    draw_new_card = True
    while draw_new_card:
        draw_card = input(
            "type 'y' to draw another card, type 'n' to pass: ").lower()
        if draw_card == "y":
            player_hand.append(random.choice(cards))
            player_score = sum(player_hand)
            while 11 in player_hand and player_score > 21:
                player_hand[player_hand.index(11)] = 1
                player_score -= 10
            if player_score > 21:
                return f" Your final hand: {player_hand}, final score: {player_score}\n Computer\'s final hand: {dealer_hand}, final score: {dealer_score}\n You went over, you lose"
            elif player_score == 21 and dealer_score == 21 and dealer_draw == False:
                return f" Your final hand: {player_hand}, final score: {player_score}\n Computer\'s final hand: {dealer_hand}, final score: {dealer_score}\n Draw"

            elif player_score == 21:
                return f" Your final hand: {player_hand}, final score: {player_score}\n Computer\'s final hand: {dealer_hand}, final score: {dealer_score}\n Win with a blackjack"
            else:
                print(
                    f" Your cards: {player_hand}, current score: {player_score}\n Computer\'s first card: {dealer_hand[0]}"
                )
        else:
            draw_new_card = False

    if dealer_score > 21:
        return f" Your final hand: {player_hand}, final score: {player_score}\n Computer\'s final hand: {dealer_hand}, final score: {dealer_score}\n Puter busted, you win"
    elif player_score > dealer_score:
        return f" Your final hand: {player_hand}, final score: {player_score}\n Computer\'s final hand: {dealer_hand}, final score: {dealer_score}\n You win"
    elif player_score == dealer_score:
        return f" Your final hand: {player_hand}, final score: {player_score}\n Computer\'s final hand: {dealer_hand}, final score: {dealer_score}\n Draw"
    else:
        return f" Your final hand: {player_hand}, final score: {player_score}\n Computer\'s final hand: {dealer_hand}, final score: {dealer_score}\n You Lose"


continue_playing = True
while continue_playing:
    play = input(
        "Do you want to play a game of blackjack? Type 'y' or 'no': ").lower()
    if play == "y":
        print(logo)
        print()
    else:
        continue_playing = False

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
