from random import randint 

choices = ["rock", "paper", "scissors"]

# player will be the weapon the player chooses via input
player = input("Choose your weapon: rock, paper or scissors: " )

computer = choices[randint(0,2)]

print("player chose: " + player)
print("computer chose: " + computer)


