"""
This program is an example program showing how to manipulate turtles in real time and
interactively.  You can learn a lot by studying this code!
"""

import turtle, creature, math, random

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
eventCreature = None
allCreatures  = None



def quitTheGame():
    wn.bye()                        # Close down the turtle window


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
    for thisTurtle in allCreatures:  # better not do "for turtle in allTurtles.  Why???
        thisTurtle.move()

    turtle.update()  # draw the current screen since animation is turned off

    # this function wires up another call to the game loop,
    # it fires off in 100 milliseconds.  (1/10th of a sec)  See constants
    wn.ontimer(gameLoop, FRAME_DELAY)


# Set up the "game"

# Note that we can set arbitrary values on a turtle.
# Not the best coding practice, but it does work.
# named colors are here:  http://wiki.tcl.tk/37701


"""
Note that we can put the turtles in our list now.
We could, potentially, append new turtles to this list
And they might move around once I append them there.
"""

mars = creature.Player()
allCreatures  = [mars]

# make 10 random monsters
for i in range(10):
    monster = creature.Monster()
    monster.chooseNewDirection()
    allCreatures.append(monster)



turtle.tracer(0)  # turn off auto animation altogether



# These lines "wire up" keypresses and clicks to the handlers we've defined.
# notice that the last one starts the gameLoop!

wn.onkey(lambda : mars.onKey('Up'),    "Up")
wn.onkey(lambda : mars.onKey('Left'),  "Left")
wn.onkey(lambda : mars.onKey('Right'), "Right")
wn.onkey(lambda : mars.onKey('Down'),  "Down")
wn.onkey(quitTheGame, "q")
wn.onclick(lambda x,y: mars.onClick(x,y))  # Wire up a click on the window.
wn.ontimer(gameLoop, FRAME_DELAY)


# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()

