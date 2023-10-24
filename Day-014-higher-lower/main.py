from game_data import data
from art import vs, logo
from replit import clear
from random import randint

current_score = 0

def get_data():
    person = randint(0, 49)
    name = data[person]['name']
    description = data[person]['description']
    country = data[person]['country']
    followers = data[person]['follower_count']
    return (f"{name}, a {description}, from {country}."), followers


def compare(x, y):
    clear()
    print(logo)
    if x > y:
        global current_score
        current_score += 1
        print(f"You are right! Current score: {current_score}")
        return True
    else:
        print(f"Sorry, you are wrong. Final score: {current_score}")
        return False


def play_game(a,b,afoll,bfoll):

    print(f"Compare A: {a}")
    print(vs)
    print(f"Against B: {b}")
    
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == "a":
        return compare(afoll, bfoll), ""
    elif choice == "b":
        return compare(bfoll, afoll), "b"


print(logo)
a = get_data()
b = get_data()
while a == b:
    b = get_data()
c = play_game(a[0],b[0],a[1],b[1])

while c[0]:
    if c[1] == "b":
        a = b
    b = get_data()
    while a == b:
        b = get_data()
    c = play_game(a[0],b[0],a[1],b[1])