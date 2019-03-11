"""
This program is an example program showing how to manipulate turtles in real time and
interactively.  You can learn a lot by studying this code!
"""

import turtle, creature, math, random, time


class Game:
    """ This container class creates a global namespace
    to hold all our game variables and constants. """

    WINDOWSIZE = 600
    FRAME_DELAY = 1000 // (10)  # 10 frames per second

    mars = None
    allCreatures = []
    score = 0
    level = 1

    writeTurtle = turtle.Turtle()
    writeTurtle.penup()
    writeTurtle.hideturtle()



def setupWindow():
    """ set up the game. Define the window and title and such. """
    turtle.setup(Game.WINDOWSIZE,Game.WINDOWSIZE)
    Game.wn = turtle.Screen()
    Game.wn.bgcolor("antique white")
    Game.wn.title("Mars Move Around!")     # Change the window title
    turtle.tracer(0)  # turn off auto animation altogether



def updateScore():
    Game.writeTurtle.clear()
    Game.writeTurtle.goto(0,Game.WINDOWSIZE//2-30)
    message = "Level: {}    Score:    {}".format(str(Game.level), str(Game.score))
    Game.writeTurtle.write(message, align="center", font=('Arial',18,"normal"))
    print ( "Score is now: ", Game.score)

def announceLevel(levelNum):
    Game.writeTurtle.goto(0,0)
    messageStages = [('ready?',1), ('set ...',1), ('GO!',0.3)]
    for (messageStage,messageDelay) in messageStages:
        Game.writeTurtle.clear()
        Game.writeTurtle.write("Level {} ".format(levelNum) + messageStage,
                               align="center", font=('Arial',18,"normal"))
        time.sleep(messageDelay)
    Game.updateScore()

def quit():
    """ quit the game """
    Game.wn.bye()

def spawn():
    monster = creature.Monster(x=random.randint(-150, 150), y=random.randint(-150, 150))
    monster.chooseNewDirection()
    Game.allCreatures.append(monster)




def gameLoop():
    """
    Run the game.
    So this is kind of like our main routine.  It is ALSO an eventhandler
    This is what we are going to do over and over again.
    Initially, we are going to set up this function as an event handler
    that happens when a timer goes off.
    But since the function sets up a new event handler at the end of itself,
      with a new timer,
    when THAT timer goes off it will call itself again.
    And thus it runs over and over again.  Until we quit.
    """
    # move all the turtles around in their current direction.
    for thing in Game.allCreatures:  # better not do "for turtle in allTurtles.  Why???
        thing.move()

    if Game.mars.chanceForAChange("spawn",10):
        spawn(Game.level)

    # see if mars hits anything
    for creature in Game.allCreatures:  # better not do "for turtle in allTurtles.  Why???
        if creature is not Game.mars:
            if Game.mars.collidesWith(creature):

                if Game.mars.winsBattle(creature):
                    Game.score += 1
                    updateScore()
                    creature.die()
                else:
                    Game.mars.die()

    #clean up dead creatures.  Have to step thru list backwards cause we delete elements.
    for i,creature in reversed(list(enumerate(Game.allCreatures))):
        if creature.getState() == 'DEAD':
            # it would seem that turtles never really go away.
            Game.allCreatures[i].hideturtle()
            del Game.allCreatures[i]


    turtle.update()  # draw the current screen since animation is turned off

    # this function wires up another call to the game loop,
    # it fires off in 100 milliseconds.  (1/10th of a sec)  See constants
    Game.wn.ontimer(gameLoop, Game.FRAME_DELAY)



# These lines "wire up" keypresses and clicks to the handlers we've defined.
# notice that the last one starts the gameLoop!
setupWindow()

Game.wn.onkey(lambda : Game.mars.onKey('Up'),    "Up")
Game.wn.onkey(lambda : Game.mars.onKey('Left'),  "Left")
Game.wn.onkey(lambda : Game.mars.onKey('Right'), "Right")
Game.wn.onkey(lambda : Game.mars.onKey('Down'),  "Down")
Game.wn.onkey(lambda : quit(), "q")
Game.wn.onclick(lambda x,y: Game.mars.onClick(x,y))  # Wire up a click on the window.

# here we go!
Game.mars =  creature.Player()
Game.allCreatures.append(Game.mars)

updateScore()
announceLevel(1)
gameLoop()


# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
Game.wn.listen()
Game.wn.mainloop()

