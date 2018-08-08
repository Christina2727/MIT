#christina amd heather
#1-31-18
#nims and stones
#exc. 2.6



def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.
    param pile: the number of stones in the pile to start
    param max_stones: the maximum number of stones you can take on one turn
    '''
    print("There are",pile,"stones in the pile.")
    current_player = 1
    while pile > 0:
        valid_num = False
        while valid_num == False: #starts at false so that it will ask prompt
            player_prompt = "Player "+str(current_player)+ \
                            ", choose a number between 1 and "+ \
                            str(max_stones)+": "
            # creating var,. num, changing guess into an integer
            num = int(input(player_prompt))
            # checks if its valid or invalid, if not valid promtps to try again
            if 1 <= num <= max_stones:
                valid_num = True
            else:
                print("Not valid. Try again.")
# subtracts the players guess from total pile
        pile = pile - num
        if pile == 0:
            print("Player", current_player, "wins!")
            print ("Game over")
            return
        else: # ends a turn
            print("There are now ", pile, "stones in the pile.")

# Looks at who is playing and if it is player 1, changes variable value to 2,
# so that its player 2
# if it is 2 and goes to "else" it changes variable to 1
        if current_player == 1 :
              current_player = 2
        else:
            current_player = 1

   


play_nims(100,5)

