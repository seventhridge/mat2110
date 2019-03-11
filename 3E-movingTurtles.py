"""
This program is an example program showing how to manipulate turtles in real time and
interactively.  You can learn a lot by studying this code!
"""

import turtle, math, random

# Set up the window and its attributes
turtle.setup(400,400)
wn = turtle.Screen()
wn.bgcolor("antique white")
wn.title("Mars Move Around!")     # Change the window title

# CONSTANTS
# Remember that values that appear in your program code should be defined as constants
# that appear at the top of your program.

WINDOWSIZE = 400
SPEED = 5
FRAME_DELAY  = 1000 // (10)   # 10 frames per second
BOX_RANGE = WINDOWSIZE // 2 - 50



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

def chooseNewDirection(t, speedRange=SPEED):
    """ set a new direction for turtle t
    Uses optional named parameter speedRange which defaults to SPEED, a constant
    You can make it choose a new direction that is slow by doing:
    chooseNewDirection(fred, speed=2)
    """
    t.dx = random.randint(-speedRange, speedRange)
    t.dy = random.randint(-speedRange, speedRange)

def boundingBox(t):
    """ if turtle t is about to move outside our bounding box, choose a new direction """
    try:
        # get the location we WOULD go to
        newX = t.xcor() + t.dx
        newY = t.ycor() + t.dy
        while  (abs (newX) > BOX_RANGE) or (abs(newY) > BOX_RANGE):
            chooseNewDirection(t, 10)
            newX = t.xcor() + t.dx
            newY = t.ycor() + t.dy
        # done!
    except:
        print("Error in boundingBox - probably because turtle t has no dx or dy.")


#
# Event Handler Functions

"""
The next four functions are  "event handlers".
You cannot add parameters to event handler functions.
Some of them, like onclick, use a function that takes parameters that come from the oprating system
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
allTurtles  = None # this will eventually be a list of turtles in our game
#         allTurtles is defined here so that the gameLoop function can use it
#         since the gameLoop function is also an event handler, it cannot have
#         parameters that I want.

def fn_up():
    try:
        eventTurtle.forward(30)
    except:
        print("fn_up eventTurtle has no forward method, or it got an error")

def fn_left():
    try:
        eventTurtle.left(45)
    except:
        print("fn_left eventTurtle has no left method, or it got an error")

def fn_right():
    try:
        eventTurtle.right(45)
    except:
        print("fn_right eventTurtle has no right method or it got an error")

def fn_quit():
    wn.bye()                        # Close down the turtle window

def fn_click(x,y):

    try:
        # the above line will throw an error if there is no dx property.
        setNormalizedDirection(eventTurtle, x, y, SPEED)
    except:
        print("Some error happened in setNormalizedDirection.  Maybe eventTurtle is not set.")

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
    # move all the turtles around in their current direction.
    for thisTurtle in allTurtles:  # better not do "for turtle in allTurtles.  Why???
        boundingBox(thisTurtle)
        move(thisTurtle)

    turtle.update()  # draw the current screen since animation is turned off

    # this function wires up another call to the game loop,
    # it fires off in 100 milliseconds.  (1/10th of a sec)  See constants
    wn.ontimer(gameLoop, FRAME_DELAY)


# Set up the "game"

# Note that we can set arbitrary values on a turtle.
# Not the best coding practice, but it does work.
# named colors are here:  http://wiki.tcl.tk/37701

mars     = turtle.Turtle()
danielle = turtle.Turtle()

mars.shape("circle")
mars.color("purple")

danielle.shape("circle")
danielle.color("blue")

mars.dx = 1
mars.dy = 1

danielle.dx = -5
danielle.dy = -5

mars.penup()

"""
Note that we can put the turtles in our list now.
We could, potentially, append new turtles to this list
And they might move around once I append them there.
"""
allTurtles  = [mars, danielle]
eventTurtle = mars

turtle.tracer(0)  # turn off auto animation altogether



# These lines "wire up" keypresses and clicks to the handlers we've defined.
# notice that the last one starts the gameLoop!

wn.onkey(fn_up,    "Up")
wn.onkey(fn_left,  "Left")
wn.onkey(fn_right, "Right")
wn.onkey(fn_quit, "q")
wn.onclick(fn_click)  # Wire up a click on the window.
wn.ontimer(gameLoop, FRAME_DELAY)


# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()

