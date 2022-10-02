#100 Days of Code: Project Day #3

#Introduction to the game
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure!")
print("Lets begin...")
print("")

#Choice 1
left_or_right = input("You come to a crossroads. Do you go left or right? Enter 'right' to go right or 'left' to go left! ").lower()

#Outcome depending on Choice 1
if left_or_right == "left":
    print("You continue left, undisturbed. ")
else:
    print("You fell in a hole and died...lol")
    quit()

#Spacing to make it look neater
print("")

#Choice 2
swim_or_wait = input("You find a lake with an island in the middle...At the lake you could wait for a boat or try swim to the island. If you want to swim, type 'swim' if you want to wait for a boat type 'wait'! ")

#Outcome depending on Choice 2
if swim_or_wait == "wait":
    print("You got across the lake unharmed. ")
else:
    print("You got eaten be a crocodile...oof!")
    quit()

#Spacing to make it look neater
print("")

#Choice 3
which_door = input("You find a house, in the house you find three doors, the first is yellow, the second is blue and the third one is red...maybe there's treasure behind one of them...Which door do you choose? Type 'yellow' for the yellow door; 'blue' for the blue door or 'red' for the red door! ")

#Outcome depending on Choice 3
if which_door == 'red':
    print("Congratulations you found the treasure!")
elif which_door == 'yellow':
    print("You were eaten by the monster waiting for you!")
elif which_door == 'blue':
    print("You fell down a trap hole and were impaled!")