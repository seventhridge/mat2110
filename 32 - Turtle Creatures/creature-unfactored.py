"""
This program is an example program showing how to manipulate turtles in real time and
interactively.  You can learn a lot by studying this code!
"""

import turtle, math, random

class Creature(turtle.Turtle):
    """
    everything in this game is a creature of some kind.
    This class defines the basic creature functionality from which all others extend.
    """

    WINDOWSIZE = 400
    DEFAULT_SPEED = 5
    BOX_RANGE = WINDOWSIZE // 2 - 50

    def __init__(self, shape="circle", color="purple"):
        super().__init__() # initialize the turtle
        # then set some basic properties
        self.penup()
        self.shape(shape)
        self.color(color)
        self.dx = 0
        self.dy = 0

    # these set up the event handler functions to use with lambdas
    # They don't do anything at all.  Extend them to do something.

    def onKey(self, key=None):
        pass

    def onKeyRelease(self, key=None):
        pass

    def onClick(self, x, y):
        pass

    def setDirectionTowardPoint(self, x, y, speed):
        """ set turtle t's dx and dy to go towards x,y at the given speed
         The turtle t need not have dx and dy attributes already set.

         The cool thing is that turtles don't normally HAVE a dx and a dy attribute
         When you set them, though, they are there to use.
         """
        currX = self.xcor()
        currY = self.ycor()
        # get actual vector from t to x,y
        dXactual = x - currX
        dYactual = y - currY

        # get the length of that vector.  Can also use turtle.distance
        length = math.hypot(dXactual, dYactual)

        # now scale the vector
        try:
            self.dx = dXactual / length * speed
            self.dy = dYactual / length * speed
        except:
            self.dx = 0
            self.dy = 0

    def move(self, friction = 0.0):
        """ move turtle t according to direction vector
        The turthe t must have its dx and dy attributes defined.
        The try block is what gets run, but if it gets a runtime error
            like as if dx or dy doesn't exist as attributes of t,
        Then Python will immediately jump to the except: part.

        The optional parameter friction has default value 0.0 and represents the
        amount the turtle will slow down after moving.
        """
        try:
            newX = self.xcor() + self.dx
            newY = self.ycor() + self.dy
            self.goto(newX, newY)
            # apply friction
            self.dx = self.dx * (1 - friction)
            self.dy = self.dy * (1 - friction)
        except:
            print("Error, probably because dx and dy are not properties of the turtle")





class Monster(Creature) :

    MONSTER_SPEED = 10

    def __init__(self, x=0, y=0, initialSpeed=None, color = "blue", **kargs):
        super().__init__(**kargs)
        if initialSpeed is None: initialSpeed = self.MONSTER_SPEED
        self.color(color)
        self.goto(x,y)
        self.keyState = "Released"

    def chooseNewDirection(self, speedRange=None):
        """ set a new direction for turtle t
        Uses optional named parameter speedRange which defaults to SPEED, a constant
        You can make it choose a new direction that is slow by doing:
        chooseNewDirection(fred, speed=2)
        """
        if speedRange is None: speedRange = self.MONSTER_SPEED
        self.dx = random.randint(-speedRange, speedRange)
        self.dy = random.randint(-speedRange, speedRange)


    def move(self):
        """ if monster is about to move outside our bounding box, choose a new direction """

        # get the location we WOULD go to
        newX = self.xcor() + self.dx
        newY = self.ycor() + self.dy
        while  (abs (newX) > self.BOX_RANGE) or (abs(newY) > self.BOX_RANGE):
            # print("choosing new direction... ",end="")
            self.chooseNewDirection()
            # print(self.dx, self.dy)
            newX = self.xcor() + self.dx
            newY = self.ycor() + self.dy

        # now move our monster
        super().move()




class Player(Creature):

    MAX_CLICK_SPEED = 5

    def onKey(self, key=None):
        print("Onkey ", key,  end=" ")
        if key == 'Up':
            self.dy += 1
        if key == 'Down':
            self.dy -= 1
        if key == 'Left':
            self.dx -= 1
        if key == 'Right':
            self.dx += 1

        #re-normalize to stop if moving very slow.
        if abs(self.dx) < 1: self.dx = 0
        if abs(self.dy) < 1: self.dy = 0

        print("dir now", self.dx,self.dy)

    def onClick(self,x,y):
        self.setDirectionTowardPoint(x, y, self.MAX_CLICK_SPEED)
