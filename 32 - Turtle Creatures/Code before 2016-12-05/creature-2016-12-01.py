"""
This program is an example program showing how to manipulate turtles in real time and
interactively.  You can learn a lot by studying this code!
"""

import turtle, math, random

class Creature(turtle.Turtle):
    WINDOWSIZE = 400

    # Set up the window and its attributes
    turtle.setup(400,400)
    wn = turtle.Screen()
    wn.bgcolor("antique white")
    wn.title("Mars Move Around!")     # Change the window title

    # CONSTANTS
    # Remember that values that appear in your program code should be defined as constants
    # that appear at the top of your program.

    WINDOWSIZE = 400
    DEFAULT_SPEED = 5
    FRAME_DELAY  = 1000 // (10)   # 10 frames per second
    BOX_RANGE = WINDOWSIZE // 2 - 50


    def setNormalizedDirection(self, x, y, speed):
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
            self.dx = dXactual / length  * speed
            self.dy = dYactual / length  * speed
        except:
            self.dx, self.dy = 0,0

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

    def __init__(self, x=0, y=0, initialSpeed=Creature.DEFAULT_SPEED, **kargs):
        super().__init__(**kargs)
        self.goto(x,y)
        self.setNormalizedDirection(x,y,initialSpeed)

    def chooseNewDirection(self, speedRange=Creature.DEFAULT_SPEED):
        """ set a new direction for turtle t
        Uses optional named parameter speedRange which defaults to SPEED, a constant
        You can make it choose a new direction that is slow by doing:
        chooseNewDirection(fred, speed=2)
        """
        self.dx = random.randint(-speedRange, speedRange)
        self.dy = random.randint(-speedRange, speedRange)


    def move(self):
        """ if turtle t is about to move outside our bounding box, choose a new direction """
        try:
            # get the location we WOULD go to
            newX = self.xcor() + self.dx
            newY = self.ycor() + self.dy
            while  (abs (newX) > self.BOX_RANGE) or (abs(newY) > self.BOX_RANGE):
                self.chooseNewDirection(self, 10)
                newX = self.xcor() + self.dx
                newY = self.ycor() + self.dy
            # done!
        except:
            print("Error in boundingBox - probably because turtle t has no dx or dy.")

        # now move our monster
        super().move()

