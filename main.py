
import random
from art import *

print(logo)
print("Welcome to everyone's favourite game: 'ROSHAMBO!' or if you're uncultures 'Rock-Paper-Scissors'. ")

art_list = [rock, paper, scissors]
user_choice = 0
pc_choice = 0
user_choice = int(input("Choose a number as your pick ('0' for rock, '1' for paper, '2' for scissors): "))
pc_choice = random.randint(0, 2)

print(f"You chose\n {art_list[user_choice]}")
print(f"Computer chose\n {art_list[pc_choice]}")

if (user_choice == 1 and pc_choice == 0) or (user_choice == 2 and pc_choice == 1) or (user_choice == 0 and pc_choice == 2):
    print("You win!")
elif user_choice == pc_choice:
    print("It's a draw.")
else:
    print("You lose!")
