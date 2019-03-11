


"""
So far, computer has 0 wins and you have 0 wins.
Would you like to play a hand of blackjack?  yes
play play play play play
The computer won!

So far, computer has 1 wins and you have 0 wins.
Would you like to play a hand of blackjack?  yes
play play play play play
You won!

initialize the number of wins to 0
    for computer wins and player wins
display the score
ask the user if they want to play a hand
as long as we want to play another hand of blackjack
   play a hand and see who won
   add one to the right number of wins
   display the score again
   ask the user if they want to play a hand



OR .. hmm... how to get rid of the repeated code???

initialize number of wins, and playing flag
as long as we are playing..:
    display the current score
    ask the user if they want to play a hand
    if they do then
        play a hand
        add one to the right number of wins
    otherwise
        we are not playing anymore
"""

import random

def playHand():
    print("play play play play play")
    if random.randint(0,1) == 0:
        return 'C'
    return 'P'


def playBlackjack():
    winsC, winsP = 0,0
    playing = True
    while playing:
        print("The computer has ", winsC,
              " wins and you have", winsP, "wins.")
        answer = input("do you want to play a hand?  ")
        if answer.lower() in ['yes-yeah-oui-si-dude.']:
            result = playHand()
            if result == "C":
                winsC = winsC + 1
            else:
                winsP = winsP + 1
        else:
            playing = False
    #end while
#end def

playBlackjack()