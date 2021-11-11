def gameResult(player, computer):

    result = 2
    if computer == player:
            print("Tie! Try again")

    elif player == "rock":
        if computer == "paper":
            print("You lose!")
            result = 1
        else:
            print("You win!")
            result = 0

    elif player == "paper":
        if computer == "scissors":
            print("You lose!")
            result = 1
        else:
            print("You win!")
            result = 0
    
    elif player == "scissors":
        if computer == "rock":
            print("You lose!")
            result = 1
        else:
            print("You win!")
            result = 0

    return result