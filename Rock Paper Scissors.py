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

import random

Player_win = 0
Computer_win = 0

lst = [rock, paper, scissors]

while True:
    ans_player = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissores ")
    ans_computer = random.choice(lst)
    if ans_player == '0':
        print(rock)
        if ans_computer == rock:
            print("Tie")
            print(rock)
        elif ans_computer == paper:
            print("You lose")
            print(paper)
            Computer_win += 1
        else:
            print("You win")
            print(scissors)
            Player_win += 1
    elif ans_player == '1':
        print(paper)
        if ans_computer == rock:
            print("You win")
            print(rock)
            Player_win += 1
        elif ans_computer == paper:
            print("Tie")
            print(paper)
        else:
            print("You lose")
            print(scissors)
            Computer_win += 1
    else:
        print(scissors)
        if ans_computer == rock:
            print("You lose")
            print(rock)
            Computer_win += 1
        elif ans_computer == paper:
            print("You win")
            print(paper)
            Player_win += 1
        else:
            print("Tie")
            print(scissors)
    if ans_player == 'q':
        print(f"You win {Player_win} times, Computer win {Computer_win} times.")
        if Player_win > Computer_win:
            print("You win the game")
        elif Player_win < Computer_win:
            print("You lose the game")
        else:
            print("Tie Game End")
        break
