#imports
import random
from art import *

#print logo and greet user
print(logo)
print("Welcome to everyone's favourite game: 'ROSHAMBO!' or if you're uncultures 'Rock-Paper-Scissors'. ")

#import art from art.py and add them to a list
art_list = [rock, paper, scissors]

#reset the choice of user and computer
user_choice = 0
pc_choice = 0

#prompt the user to input a number
user_choice = int(input("Choose a number as your pick ('0' for rock, '1' for paper, '2' for scissors): "))

#generate a random number as choice for pc
pc_choice = random.randint(0, 2)

#print whatever the user and pc chose in the form of art
print(f"You chose\n {art_list[user_choice]}")
print(f"Computer chose\n {art_list[pc_choice]}")

#check for conditions for which the user won
if (user_choice == 1 and pc_choice == 0) or (user_choice == 2 and pc_choice == 1) or (user_choice == 0 and pc_choice == 2):
    print("You win!")
#if the user and pc chose same thing
elif user_choice == pc_choice:
    #we delcare draw
    print("It's a draw.")
#if not, then it means we lost.
else:
    print("You lose!")

