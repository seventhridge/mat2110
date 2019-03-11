

"""
Hi! Please enter your square.
One line of entries, separated by spaces
When you're done with entries, enter a blank line.

> 1 2 3
> 4 5 6
> 7 8 9
>  (this is the blank line the user entered

Okay thanks!
Is it square? Check.
All integers?  Check.
Rows sum to same number?  Bzzt.
Columns sum to same number? Bzzt.
Diagonals?  Bzzt.
This is not a magic square.
"""
VOWELS="aeiou"
CONSONANTS="bcdfghjklmnpqrstvwxyz"

def stringAnalyzer(message):
    vowels, consonants = 0,0
    for ch in message:
        ch = ch.lower()
        if ch in VOWELS:
            vowels = vowels + 1
        if ch in CONSONANTS:
            consonants = consonants + 1
    return vowels, consonants

"""
words = input("Your message? ")
v,c = stringAnalyzer(words)
print("Vowels: ", v, "Consonants:", c)
"""

def thingIsSquare(thing):
    if not (type(thing) is list):
        return False
    thingLen = len(thing)
    if thingLen == 0:
        return False
    for subThing in thing:
        if not (type(subThing) is list):
            return False
        if len(subThing) != thingLen:
            return False
    return True

def unitTest_thingIsSquare():

    if thingIsSquare( [  [  10,   20,   30, ],
       [  "W",  "X",  "Y", "Z", ],
       [  ],
    ] ) == True:
        print("thingIsSquare 1 Failed!")
    if thingIsSquare([ 1,2,3]):
        print("thingIsSquare 2 failed!")
    if thingIsSquare([ ]):
       print("thingIsSquare 3 failed!")
    if not thingIsSquare([ [1,2],[3,4] ]) :
        print("thingIsSquare 4 failed!")
    if thingIsSquare([[1],[2],[3] ]):
        print("thingIsSquare 5 failed!")
    if not thingIsSquare([ [[],2], [3,[[4]]] ]):
        print("thingIsSquare 6 failed!")

unitTest_thingIsSquare()


def thingIsAllInts(t):
    return True

def thingIsAllInts(t):
    """ determine if t is a list of list of ints """
    try:
        # use return on discovery pattern
        # make sure we have something to iterate over
        if len(t) == 0 or len(t[0]) == 0:
            return False
        # step over rows, cols and check its an int.
        for row in t:
            for col in row:
                if not (type(col) is int):
                    return False
        return True
    except:
        return False


def unitTest_thingIsAllInts():
    # some degenerates
    if thingIsAllInts( [] ):  print("Test 1 Failed")
    if thingIsAllInts( 1 ):  print("Test 2 Failed")
    if thingIsAllInts( [1] ):  print("Test 3 Failed")
    if thingIsAllInts( [[], []] ):  print("Test 4 Failed")
    if thingIsAllInts( [[[1]]] ):  print("Test 5 Failed")
    # some realistic cases
    if not thingIsAllInts( [[1, 2], [3, 4, 5]] ):  print("Test 6 Failed")
    if thingIsAllInts( [[1, 2.1], [3, 4, 5]] ):  print("Test 7 Failed")
    if not thingIsAllInts( [[1, 2, 3]] ):  print("Test 8 Failed")
    if thingIsAllInts( [["hi", 2, 3]] ):  print("Test 9 Failed")

unitTest_thingIsAllInts()

def getFirstRowSum(t):
    try:
        sum = 0
        # step over first row of t
        for col in t[0]:
            sum = sum + col
        return sum
    except:
        return 0

def unitTest_getFirstRowSum():
    if getFirstRowSum([]) != 0:  print("getFirstRowSum 1 failed")
    if getFirstRowSum([[]]) != 0:  print("getFirstRowSum 2 failed ")
    if getFirstRowSum([[1,2,3]]) != 6:  print("getFirstRowSum 3 failed")


def thingRowsMatch(candidate, sum):
    try:
        for rowNum in range(len(candidate)):
            # accumulate the row
            rowSum = 0
            for colNum in range(len(candidate[rowNum])):
                rowSum = rowSum + candidate[rowNum][colNum]
            if rowSum != sum:
                return False
        return True
    except:
        return False


def unitTest_thingRowsMatch():
    if not thingRowsMatch( [ [ ] ], 0):
        print("thingRowsMatch 1 failed")
    if not thingRowsMatch( [ [1,2],[1,1,1]], 3):
        print("thingRowsMatch 2 failed")

unitTest_thingRowsMatch()

def thingColsMatch(t, sum):
    #return True
    try:
        #build column histogram
        colsHisto = [0] * len(t[0])  # histo for column sums
        for r in range(len(t)):
            for c in range(len(t[r])) :
                colsHisto[c] = colsHisto[c] + t[r][c]
        # see if they're all the same with Return on Discovery
        for colSum in colsHisto:
            if colSum != sum: return False
        return True
    except:
        return False

def reflectMatrix(t):
    """ reflect a copy of the matrix exchanging all rows and columns
    the matrix must be a list of lists.
    One strategy:
    You will need to "build up" the result with append, starting with an empty list.
    """
    t2 = [ ]
    for r in range(len(t)):
        for c in range(len(t[r])):
            if len(t2) <= c:
                t2.append( [] )
            t2[c].append( t[r][c] )
    return t2

def unitTest_reflectMatrix():
    """"test reflectMatrix"""
    """ example 1 :
    1 4   ==>   1 2 3
    2 5         4 5 6
    3 6
    """
    if  [ [1,2,3],[4,5,6]] != reflectMatrix([[1,4],[2,5],[3,6]]):
        print( "reflectMatrix 1 failed")
    """ example 2:
    1 2      =>     1 3
    3 4 5           2 4
                    5
    """
    if [[1,3],[2,4],[5]] != reflectMatrix([ [1,2],[3,4,5]] ):
        print("reflectMatrix 2 failed")

unitTest_reflectMatrix()

def thingColsMatch2(t, sum):
    """ determine if columns of t have matching sums.  Assumes t is square. """
    try:
        copyt = reflectMatrix(t)
        return thingRowsMatch(copyt, sum)
    except:
        return False

def unitTest_thingColsMatch():
    if not thingColsMatch( [ [ ] ], 0):
        print("thingColsMatch 1 failed")
    if not thingColsMatch( [ [1,2],[1,1], [1,0]], 3):
        print("thingColsMatch 2 failed")
    if thingColsMatch([[1, 2], [1, 1], [1, 0]], 2):
        print("thingColsMatch 3 failed")

unitTest_thingColsMatch()


def analyzeSquare(m):
    """ decide if m has the properties of a Magic Square """
    isSquare = thingIsSquare(m)
    isInts = thingIsAllInts(m)
    if not (isSquare and isInts):
        return isSquare, isInts, False, False, False
    sum = getFirstRowSum(m)
    rowsMatch = thingRowsMatch(m, sum)
    colsMatch = thingColsMatch(m, sum)
    diagsMatch = thingDiagsMatch(m, sum)
    return isSquare, isInts, rowsMatch, colsMatch, diagsMatch



def areAllNumbersUnique(ms):
    """ determine if all numbers in the matrix
    are unique by counting them and then going
    through all the counts to see if any of
    them have a count bigger than 1.
    Matrix ms is a list of lists  """
    try:
        counters = {} # set of empty counters
        for rowN in range(len(ms)):
            for colN in range(len(ms[rowN])):
                numAtCell = ms[rowN][colN]
                currCount = counters.get( numAtCell, 0)
                currCount = currCount + 1
                counters[numAtCell] = currCount
                # note we could just do:
                # counters[numAtCell] =
                #     counters.get( ms[rowN, colN], 0) + 1
        for key,val in counters.items():
            if val > 1:
                return False
        return True
    except:
        return False

def unitTest_areAllNumbersUnique():
    # DONT omit degenerates.  Most errors happen there.
    testMS = "Fred"
    if areAllNumbersUnique(testMS):
        print("areAllNumbersUnique Degenerate Test 1 Failed!")
    testMS = [ [14,8], [600,14]]
    if areAllNumbersUnique(testMS):
        print("areAllNumbersUnique Test 1 Failed!")
    testMS = [[14, 8], [600, 1400]]
    if not areAllNumbersUnique(testMS):
        print("areAllNumbersUnique Test 1 Failed!")


def main():
    candidate = getSquareInput()
    square, ints, rows, cols, diags = analyzeSquare(candidate)
    resultOutput = getOutput(square,ints,rows,cols,diags)
    print(resultOutput)

