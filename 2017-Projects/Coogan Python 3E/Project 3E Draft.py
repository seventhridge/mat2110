import turtle, time, random, math


# CONSTANTS
# Remember that values that appear in your program code should be defined as constants
# that appear at the top of your program.


WINDOWSIZE_WIDTH  = 1000
WINDOWSIZE_HEIGHT = 400
CANNON_SPEED      = 15
SKEET_SPEED       = 2.5
FRAME_DELAY       = 1000 // (10)   # 10 frames per second
BOX_RANGE         = WINDOWSIZE_WIDTH // 2 - 50


"""
 Utility Functions


 These are often put in a separate file in the same directory as other parts of the program
 And then imported into the main routine.
 If this file were called utility.py, you could import them all INTO THE CURRENT NAMESPACE with


       from utility import  *


 This is different from "import utility" because with "import utility" you have to use the
 namespace with a selector reference to access things.  Like utility.setNormalizedDirection(...)


 With the from utility import * commands, all the things inside utility.py are included directly
   in the namespace here... so it is the same as if they were just written here.


"""

def landscapeRandomGeneration(turtlesToPlace, lengthNeeded, windowFull):
  for i in range(30):
  #randomly pick one of the for level images
      selector = random.choice(turtlesToPlace)
      selector.goto(windowFull, -(WINDOWSIZE_HEIGHT//2))
      selector.stamp()
  # and place it flush next to the last image
      windowFull = windowFull + 40


def importImages(list):
   for image in list:
       wn.addshape(image)

def setNormalizedDirection(t, x, y, speed):
    """ set turtle t's dx and dy to go towards x,y at the given speed
     The turtle t need not have dx and dy attributes already set.

     The cool thing is that turtles don't normally HAVE a dx and a dy attribute
     When you set them, though, they are there to use.
     """
    currX = t.xcor()
    currY = t.ycor()
    # get actual vector from t to x,y
    dXactual = x - currX
    dYactual = y - currY

    # get the length of that vector.  Can also use turtle.distance
    length = math.hypot(dXactual, dYactual)

    # now scale the vector
    t.dx = dXactual / length  * speed
    t.dy = dYactual / length  * speed

def move(t, friction = 0.0):
    """ move turtle t according to direction vector
    The turthe t must have its dx and dy attributes defined.
    The try block is what gets run, but if it gets a runtime error
        like as if dx or dy doesn't exist as attributes of t,
    Then Python will immediately jump to the except: part.

    The optional parameter friction has default value 0.0 and represents the
    amount the turtle will slow down after moving.
    """
    try:
        newX = t.xcor() + t.dx
        newY = t.ycor() + t.dy
        t.goto(newX, newY)
        # apply friction
        t.dx = t.dx * (1 - friction)
        t.dy = t.dy * (1 - friction)
    except:
        print("Error, probably because dx and dy are not properties of the turtle")


def boundingBox(t):
   """ if turtle t is about to move outside our bounding box, choose a new direction """
   try:
        if (abs(t.xcor()) > BOX_RANGE) or (abs(t.ycor()) > BOX_RANGE):
            return True
        else:
            return False
        # get the location we WOULD go to

   except:
       print("Error in boundingBox - probably because turtle t has no dx or dy.")

# Event Handler Functions


"""
The next four functions are  "event handlers".
You cannot add parameters to event handler functions.
Some of them, like onclick, use a function that takes parameters that come from the operating system
Others, like onkey, use a function that takes no parameters
Setting up the event handlers is called "binding"
  Where we pass one of our event handler functions as a parameter
  To tell onlclick to, for example, call the fn_click function that we're getting
  ready to define here.
"""


"""
I set this global variable so that it can work kinda like a parameter.
The code can change the "eventTurtle" at any time to refer to the turtle that
I want to use to be affected by the function.
"""
eventTurtle = None
skeetTurtle = None
clickTurtle = None
cannonTurtle = None
allTurtles  = None # this will eventually be a list of turtles in our game
#         allTurtles is defined here so that the gameLoop function can use it
#         since the gameLoop function is also an event handler, it cannot have
#         parameters that I want.


#def fn_up():
#    try:
#        wn.ontimer(gameLoop, FRAME_DELAY)
#    except:
#        print("fn_up eventTurtle has no forward method, or it got an error")



#def fn_left():
#   try:
#       eventTurtle.left(45)
#   except:
#       print("fn_left eventTurtle has no left method, or it got an error")


#def fn_right():
#   try:
#       eventTurtle.right(45)
#   except:
#       print("fn_right eventTurtle has no right method or it got an error")


def fn_quit():
   wn.bye()                        # Close down the turtle window


def fn_click(x,y):
    try:
        # the above line will throw an error if there is no dx property.
        setNormalizedDirection(clickTurtle, x, y, CANNON_SPEED)
    except:
        print("Some error happened in fn_click.  Maybe eventTurtle is not set.")

def isInBox(turtle1, turtle2):
    try:
        #if (aimTurtle.x > (targetTurtle.x - 10) and (aimTurtle.y < (targetTurtle.y + 10))):
            #targetTurtle.write("Hit!")
        turtle1Position = turtle1.pos()
        turtle2Position = turtle2.pos()
        if turtle1.distance(turtle2Position) < 10:
            return True

        else:
            return False

    except:
        print("Error in isInBox function")

"""
So this is kind of like our main routine.  It is ALSO an eventhandler
This is what we are going to do over and over again.
Initially, we are going to set up this function as an event handler
that happens when a timer goes off.
But since the function sets up a new event handler at the end of itself,
 with a new timer,
when THAT timer goes off it will call itself again.
And thus it runs over and over again.  Until we quit.
"""


def gameLoop():

    initCannonxCoordinate = (WINDOWSIZE_WIDTH // 2)-75
    initCannonyCoordinate = (WINDOWSIZE_HEIGHT // 2)-98
    initSkeetXCoordinate = random.randint(0, 250)
    initSkeetYCoordinate = random.randint(100, 300)
   # move all the turtles around in their current direction.
    for thisTurtle in allTurtles:  # better not do "for turtle in allTurtles.  Why???
        boundingBox(thisTurtle)
        move(thisTurtle)
        if boundingBox(thisTurtle) == True:
            print("Oh, Dear! A Miss! Try Again!")
            return True


    setNormalizedDirection(skeetTurtle, initSkeetXCoordinate, initSkeetYCoordinate, SKEET_SPEED)

    isInBox(skeetTurtle, cannonTurtle)

    if isInBox(skeetTurtle, cannonTurtle) == True:
        print("Hit!")
        return True
    turtle.update()  # draw the current screen since animation is turned off


   # this function wires up another call to the game loop,
   # it fires off in 100 milliseconds.  (1/10th of a sec)  See constants
    wn.ontimer(gameLoop, FRAME_DELAY)


##Setup the game
# Set up the window and its attributes
turtle.setup(1000,400)
wn = turtle.Screen()


#turtle.tracer(0)  # turn off auto animation altogether

wn.bgcolor("white")
wn.title("Castles and Cannons") # Change the window title
castleImage = "SMBCastle.gif"         # Load images for game
cannonImage = "pirate cannon.gif"
level1Image = "level1.gif"
level2Image = "level2.gif"
level3Image = "level3.gif"
level4Image = "level4.gif"

imageList = [castleImage, cannonImage, level1Image, level2Image, level3Image, level4Image]

# Load images on canvas
importImages(imageList)


# Generate turtles for landscape parts
castle1 = turtle.Turtle()
castle2 = turtle.Turtle()
cannon = turtle.Turtle()
level1 = turtle.Turtle()
level2 = turtle.Turtle()
level3 = turtle.Turtle()
level4 = turtle.Turtle()


# Generate landscape


level1.penup()
level1.shape(level1Image)

level2.penup()
level2.shape(level2Image)

level3.penup()
level3.shape(level3Image)

level4.penup()
level4.shape(level4Image)

levelList = [level1, level2, level3, level4]
turtle.tracer(0)  # turn off auto animation altogether

landscapeRandomGeneration(levelList, 500, -500)


# Place castle, cannon
castle1.penup()
castle1.shape(castleImage)
castle1.goto(-((WINDOWSIZE_WIDTH // 2)-75), -((WINDOWSIZE_HEIGHT // 2)-98))

cannon.penup()
cannon.shape(cannonImage)
cannon.goto(-((WINDOWSIZE_WIDTH // 2)-75), 0)

castle2.penup()
castle2.shape(castleImage)
castle2.goto(((WINDOWSIZE_WIDTH // 2)-75), -((WINDOWSIZE_HEIGHT // 2)-98))

# Create the turtle that will shoot the cannonball
cannonball = turtle.Turtle()
cannonball.shape("circle")
cannonball.color("grey")
cannonball.penup()

# Put cannonball over castle
cannonball.goto(-((WINDOWSIZE_WIDTH // 2)-75), -((WINDOWSIZE_HEIGHT // 2)-98))
cannonball.dx = 0
cannonball.dy = 0

# Create the skeet
skeet = turtle.Turtle()
skeet.penup()
skeet.left(90)

#Put skeet over castle
skeet.goto(((WINDOWSIZE_WIDTH // 2)-75), -((WINDOWSIZE_HEIGHT // 2)-98))
skeet.dx = 0
skeet.dy = 0

"""
Note that we can put the turtles in our list now.
We could, potentially, append new turtles to this list
And they might move around once I append them there.
"""
allTurtles   = [cannonball, skeet]
eventTurtle = [cannonball]
cannonTurtle = cannonball
skeetTurtle = skeet
clickTurtle = cannonball





# These lines "wire up" keypresses and clicks to the handlers we've defined.
# notice that the last one starts the gameLoop!


wn.ontimer(gameLoop, FRAME_DELAY)
wn.onclick(fn_click)  # Wire up a click on the window.


# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()

