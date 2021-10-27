from random import randint 

choices = ["rock", "paper", "scissors"]

# player will be the weapon the player chooses via input

player = False

# these lives need to decrement when a player loses a round
playerLives = 2
computerLives = 2

#set up our game loop so that we can keep playing and not exit
while player is False:
    player = input("Choose your weapon: rock, paper or scissors: " )
    computer = choices[randint(0,2)]

    print("player chose: " + player)
    print("computer chose: " + computer)

    if computer == player:
        print("Tie! Try again")

    elif player == "rock":
        if computer == "paper":
            print("You lose!")
            playerLives = playerLives - 1
        else:
            print("You win!")
            computerLives = computerLives - 1
  
    elif player == "paper":
        if computer == "scissors":
            print("You lose!")
            playerLives = playerLives - 1
        else:
            print("You win!")
            computerLives = computerLives - 1
       
    elif player == "scissors":
        if computer == "rock":
            print("You lose!")
            playerLives = playerLives - 1
        else:
            print("You win!")
            computerLives = computerLives - 1

    print("Player lives: " + str(playerLives))
    print("Computer lives: " + str(computerLives))

    if playerLives == 0 or computerLives == 0:
        print("Game over! Do you want to play again?")

        choice = input("Do you want to play again? y/n: ")

        if choice is "n":
            exit()

    player = False
