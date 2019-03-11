
MAXGUESSES = 7

import random
WORDS = """
altercation motorcar television professor smalltalk onion willingness frenzy
"""

def select_word(wordstring):
    """ pick a word somehow """
    wordlist = wordstring.split()
    return random.choice(wordlist)

    return "fred"

print(select_word(WORDS))

def flipSlots(slots, word, letter):
    """ change the slots list based on where letters are in word """
    # note that slots will change
    # this function does not return anything


def main():
    # pick a random word
    word  = selectWord(WORDS)
    # initialize the slots - a list of underscores
    slots = list( "_" * len(word) )
    # set remaining guesses
    guesses = MAXGUESSES
    # while game goes on ( more guesses or word not discovered)
    while guesses > 0 and  ("_" in slots):
        letter = input("Letter?")
        if letter in word:
            flipSlots(slots, word, letter)
        else:
            guesses = guesses - 1
        # show the user what they have
        print(guesses, "guesses left.  You have: ", " ".join(slots) )
    if guesses > 0:
        print("YOU WIN!")
    else:
        print("you lose. :(")

#main()