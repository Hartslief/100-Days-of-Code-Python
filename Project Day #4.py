#100 Days of Code: Project Day #3

#Importing "random" package
import random

#Introduction
print("Welcome to my Rock, Paper, Scissors Game...")

#Setting what the computer can choose
selection = ('rock', 'paper', 'scissors')

#Setting a baseline of scores to be tallied up to see who won by the end of the game
player_score = 0
comp_score = 0

#Starting while loop to check user inputs
while True:

    #Asking the player to input their choice. Making any input into lowercase to make things easier
    player_choice = input("Please choose rock, paper or scissors. Press 'Q' to quit! ").lower()
    
    #Q will break the while loop so that the player can end the game whenever they feel like it. Even if nothing has happened.
    if player_choice == "q":
        break
    
    #Checks if the user input is a valid choice
    if player_choice not in selection:
        continue
    
    #Making the computers choice random
    comp_choice = selection[random.randint(0,2)]

    #Putting the players input against the computers input to determine who won the round
    if player_choice == "rock" and comp_choice == "scissors":
        print("You won!")
        player_score += 1
    
    elif player_choice == "paper" and comp_choice == "rock":
        print("You won!")
        player_score += 1

    elif player_choice == "scissors" and comp_choice == "paper":
        print("You won!")
        player_score += 1

    else: 
        print("You lost!")
        comp_score += 1

#Tallying up the score of who won how many rounds to see who won the game.
if player_score > comp_score:
    print("Congrats! You beat the computer! You won ", player_score, " times!")

else:
    print("You lost! The computer won ", comp_score, " times!")