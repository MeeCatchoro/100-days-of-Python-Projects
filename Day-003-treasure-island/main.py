print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input(
    '\nYou find yourself at a beach, with a forest lying ahead. You stand at a crossroads: venture into the forest or opt to stroll along the sandy shores. Type "Enter" to step into the forest, or "Walk around" to explore the beach.\n'
)

if choice1.lower() == "enter":
    choice2 = input(
        '\nWhile navigating through the trees and bushes of this humid forest, you come across a massive, black-furred creature sleeping on a sandy path. You have two options: you can attempt to sneak past it quietly or try to scare it by letting out a loud scream. Type "Sneak" to cautiously avoid it or "Scream" to attempt to frighten it.\n'
    )

    if choice2.lower() == "sneak":
        choice3 = input(
            '\nWhile cautiously circling the creature, you realize that it is, in fact, lifeless. It appears to have fallen victim to a much larger assailant. With this newfound assurance, you opt to stride over the animal and follow the sandy path ahead. The trail eventually leads you to an ancient temple with three entrances, each distinguished by a distinct color: red, green, and blue. To proceed, type "red" for the red entrance, "yellow" for the yellow entrance, or "blue" for the blue entrance.\n'
        )

        if choice3.lower() == "red":
            print(
                "\nWhile traversing the crimson corridor, an unpleasant odor emanates from the walls themselves, causing dizziness and an urge to vomit. Not wanting to stay any longer, you opt to sprint back to the entrance. However, in your haste, you inadvertently trigger a pressure plate beneath your feet. The walls swiftly close in on you, inflicting a crushing fate.\nGame over, hit 'Run' to restart."
            )

        elif choice3.lower() == "yellow":
            print(
                "\nAs you progress through the gilded corridor, the walls' radiant gleam instills a sense of confidence that a treasure awaits further along. Following hours of traversing an endless hallway, you finally reach a chamber adorned with golden statues, heaps of coins, and the most dazzling diamonds ever to be cut. Overjoyed with your discovery, you gather as many valuables as your arms can hold, stuffing your pockets with treasure. Happy with your newfound wealth, you make your way back to the shore.\n\n   Thank you so much for playing my game and congratulations on finding the treasure!"
            )

        elif choice3.lower() == "blue":
            print(
                "\nWhile making your way through the blue corridor, each step is accompanied by the echoing sound of water beneath your feet. As you delve deeper into the dimly illuminated passageway, faint splashes reach your ears, akin to the footsteps of an unseen pursuer. Instinctively, you pick up your pace, transitioning from a gradual stroll to a brisk walk. The sounds from behind intensify in frequency and volume, steadily gaining ground. Before long, you break into a run, compelled by a rising sense of urgency. A moment later, you steal a glance over your shoulder only to encounter a monstrous, black-scaled creature hurtling towards you.\nGame over, hit 'Run' to restart"
            )

        else:
            print("\nError, not a choice")

    elif choice2.lower() == "scream":
        print(
            "\nAs you scream with every ounce of your being, attempting to get a response from the creature, it remains completely motionless. Baffled by its lack of reaction, you choose to approach and examine it more closely. As you poke what appears to be remnants of another creature's meal, a beast even larger than the deceased one emerges from the corner of your vision. You make a frantic attempt to flee, but to no avail.\nGame over, hit 'Run' to restart"
        )
    else:
        print("\nError, not a choice")

elif choice1.lower() == "walk around":
    print(
        "\nAppears like you've been walking for hours without discovering anything. The thought that the beach might stretch on endlessly begins to cross your mind. The intense heat has left you wandering aimlessly, eventually causing you to collapse from dehydration.\nGame over, hit 'Run' to restart"
    )

else:
    print("\nError, not a choice")
