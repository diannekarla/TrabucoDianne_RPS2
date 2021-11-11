from random import randint 
from gameComponents import winLose, gameVars, weapons


#set up our game loop so that we can keep playing and not exit
while gameVars.player is False:

    gameVars.player = input("Choose your weapon: rock, paper or scissors: " )
    gameVars.computer = gameVars.choices[randint(0,2)]

    print("player chose: " + gameVars.player)
    print("computer chose: " + gameVars.computer)

    fight = weapons.gameResult(gameVars.player, gameVars.computer)
    
    if fight == 0:
        gameVars.computerLives = gameVars.computerLives - 1

    elif fight == 1:
        gameVars.playerLives = gameVars.playerLives - 1

    print("Player lives: " + str(gameVars.playerLives))
    print("Computer lives: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lost")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won")

    gameVars.player = False
