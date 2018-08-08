#christina and Heather
#jan 20 , 2018
#Homework 1.986 pt 1.7




def scoring_rps(player1, player2):
    "Take user input to play the game rock paper scissors"

    if (player1 == "rock" and player2 == "rock"
        or player1 == "paper" and player2 == "paper"
        or player1 == "scissors" and player2 == "scissors"):
            print("Its a tie!")
            return "tie"

    elif (player1 == "rock" and player2 == "scissors"
        or player1 == "scissors" and player2 == "paper"
        or player1 == "paper" and player2 == "rock"):
            print("Player 1 wins")
            return "p1"

    elif (player1 == "rock" and player2 == "paper"
        or player1 == "scissors" and player2 == "rock"
        or player1 == "paper" and player2 == "scissors"):
            print("Player 2 wins")
            return "p2"
    

    else:
        print("This is not a valid selection")
        return None

def get_rps_choice(player_name="Player"):
    choices = ["rock", "paper", "scissors"]
    choice = input("{} please type rock, paper, or scissors: ".format(player_name))
    choice = choice.lower()
    if choice in choices:
        return choice
    else:
        print("invalid choice!")
        return None    
       

player1 = get_rps_choice(player_name="Player 1")
player2 = get_rps_choice(player_name="Player 2")



win_list = []
winner = scoring_rps(player1, player2)

if winner:
    if winner is not "tie":
        win_list.append(winner)
    else:
        print("It's a tie! No one wins this round")
        
