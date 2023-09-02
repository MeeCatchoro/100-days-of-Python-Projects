rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

escolhas = [rock, paper, scissors]

jogador = int(input('Qual você vai jogar? Digite "0" para jogar Pedra, "1" para jogar Papel, "2" para jogar papel'))
computador = random.randint(0,2)

print(f"{escolhas[jogador]} \n o computador escolheu: \n {escolhas[computador]}")

if jogador == 0:
  if computador == 0:
    print("Empate")
  elif computador == 1:
    print("Você perdeu")
  elif computador == 2:
    print("Você ganhou")
  
elif jogador == 1:
  if computador == 1:
    print("Empate")
  elif computador == 2:
    print("Você perdeu")
  elif computador == 0:
    print("Você ganhou")

elif jogador == 2:
  if computador == 2:
    print("Empate")
  elif computador == 0:
    print("Você perdeu")
  elif computador == 1:
    print("Você ganhou")

