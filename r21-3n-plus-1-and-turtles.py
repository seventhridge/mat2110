
PROBLEM = 'turtles'
#PROBLEM = 'sequence'

def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    count = 0
    while n != 1:
        count=count +1
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    return count


def find3np1_moreloopsthan(k):
    """ find the smallest n that takes more than k iterations to complete """
    n=1
    found = False
    while not found:
        value = seq3np1(n)
        if value >= k:
            found = True
        else:
            n = n + 1
    return (n, value)


def sequenceMain():
    someK = int(input("what num iterations do you want to exceed? "))
    smallestN, valueN = find3np1_moreloopsthan(someK)
    print("The smallest number that takes more than ", someK, "of iterations is ", smallestN, "at ", valueN)



"""
TURTLE PROGRAM!
"""
import random
import turtle

wn = turtle.Screen()  #wn is a global variable - there's only one Screen anyway.

def isInScreen(x):
    """ is turtle x in the screen or not? """
    leftBound = - wn.window_width() / 2
    rightBound = wn.window_width() / 2
    topBound = wn.window_height() / 2
    bottomBound = -wn.window_height() / 2

    turtleX = x.xcor()
    turtleY = x.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False
    return stillIn


def collided(t1, t2):
    if t1.distance(t2.xcor(),t2.ycor()) < 50:
        return True
    return False



def moveATurtle(t):
    coinx = random.randrange(0, 2)
    turnx = random.randrange(0, 180)
    if coinx == 0:  # heads
        t.left(turnx)
    else:  # tails
        t.right(turnx)
    t.forward(50)



def turtleMain():
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    # move the turtles initially otherwise they start at the same place
    moveATurtle(t1)
    moveATurtle(t2)
    while isInScreen(t1) and isInScreen(t2) and not collided(t1,t2):
        moveATurtle(t1)
        moveATurtle(t2)


if PROBLEM == 'sequence':
    sequenceMain()
else:
    turtleMain()
