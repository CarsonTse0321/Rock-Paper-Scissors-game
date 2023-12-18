#This is a rock paper scissor game

print("Welcome to the Rock Paper Scissor game")
print("Choices:")
print("1. Rock\n2. Paper\n3. Scissors\n4. q to quit")

import random

list1 = ["Rock", "Paper", "Scissors", "Q"]
list2 = ["Rock", "Paper", "Scissors"]

Player_Win = 0
Computer_Win = 0

while True:
    Player_choice = input("Enter your choice: ").capitalize()
    if Player_choice not in list1:
        print("Invalid choice")
        Player_choice = input("Enter your choice: ").capitalize()
    Computer_Choice = random.choice(list2)
    print(f"You chose {Player_choice} and computer chose {Computer_Choice}")
    if Player_choice == Computer_Choice:
        print("It's a tie!")
    elif Player_choice == "Rock" and Computer_Choice == "Paper":
        print("You lose!")
        Computer_Win += 1
    elif Player_choice == "Rock" and Computer_Choice == "Scissors":
        print("You win!")
        Player_Win += 1
    elif Player_choice == "Paper" and Computer_Choice == "Scissors":
        print("You lose!")
        Computer_Win += 1
    elif Player_choice == "Paper" and Computer_Choice == "Rock":
        print("You win!")
        Player_Win += 1
    elif Player_choice == "Scissors" and Computer_Choice == "Rock":
        print("You lose!")
        Computer_Win += 1
    elif Player_choice == "Scissors" and Computer_Choice == "Paper":
        print("You win!")
        Player_Win += 1
    elif Player_choice == "Q":
        break
print("Game Over")
print(f"Player wins: {Player_Win}")
print(f"Computer wins: {Computer_Win}")
    
    