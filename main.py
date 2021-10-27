from random import randint 

choices = ["rock", "paper", "scissors"]

# player will be the weapon the player chooses via input

player = False

# these lives need to decrement when a player loses a round
playerLives = 2
computerLives = 2

def winorlose(status):
    print ("You " + status)

    choice = input("Do you want to play again? y/n: ")

    global playerLives
    global computerLives
    global player

    if choice == "n":
        print("===============Thank you==============")
        exit ()
    elif choice == "y":
        playerLives = 2
        computerLives = 2
        player = False

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

    if playerLives == 0:
        winorlose("lost")

    elif computerLives == 0:
        winorlose("won")

    player = False
