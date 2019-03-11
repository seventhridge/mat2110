def myFinder(word, findC):
    for pos in range(len(word)):  # step thru word.  Use current "pos"
        charAtPos = word[pos]
        # Does the character at "pos" match the character I seek?
        foundIt = (charAtPos == findC)
        if foundIt:  # Yes:
            return pos  # Give back that pos
        # No?  just keep going
    # Oh no I'm at the end.  I've stepped through them all.
    return None  # Give back None


w = input("Type a word:")
c = input("Type a char:")

print("My finder thinks the char is at ",
      myFinder(w, c))
print("The string library one thinks it is ",
      w.find(c))

s = "There's always GLAD in gladfelter!"
s.find("'")  # the single quote
s.find('cowpie')
s.find('GLAD')
