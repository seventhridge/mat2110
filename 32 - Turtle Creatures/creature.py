"""
This program is an example program showing how to manipulate turtles in real time and
interactively.  You can learn a lot by studying this code!
"""

import turtle, math, random, time

def msTime():
    return int(time.perf_counter()*1000)


class Animator:

    def __init__(self, creature=None, animation=None, msDuration=0, **kwargs):
        self.creature    = creature
        self.animation   = animation
        self.msDuration  = msDuration
        self.startTimeMS = msTime()
        self.properties  = kwargs

    def __str__(self):
        if self.animation == self.pulseOutline:
            animation='pulseOutline'
        else:
            animation=str(id(self.animation))
        return str({'creature Type': type(self.creature),
             'animation': animation,
             'creature ID': id(self.creature),
             'msDuration':self.msDuration,
             }.update(self.properties))

    def animate(self):
        """ perform the designated animation.  Return False when done.
        If there is no animation, return True (keep going with no error, nothing to animate) """
        return self.animation(self) if self.animation else True

    def pulseOutline(self):
        """ pulse the creature.
        msPulse=<duration of pulse in ms>, colorON=<color for ON pulse>, colorOFF=<color for OFF pulse>  """
        now = msTime()
        elapsedMS = now - self.startTimeMS

        if self.msDuration == 0 or elapsedMS > self.msDuration:
            return False

        try:
            if self._lastPulseTime + self.properties['msPulse'] < now:
                # time to toggle the pulse!
                self._pulse = not self._pulse
                self._lastPulseTime = now
                # print(elapsedMS,self._pulse)
                self.creature.pencolor( self.properties['colorON']  if self._pulse else self.properties['colorOFF'] )
        except:
            self._lastPulseTime =  now
            self._pulse = False
            self.creature.pencolor(self.properties['colorOFF'])

        return True



    def winkOut(self):
        """ make the creature shrink out of existence
        msDuration=<ms before creature winks out>"""
        now = msTime()
        dieTimePercentUsed = int( 100 * (now - self.startTimeMS) / self.msDuration) # percent through birth
        if dieTimePercentUsed > 100:
            self.creature.hideturtle()
            return False
        else:  # fade it out in size
            sizeFraction = (100 - dieTimePercentUsed) / 100
            sizeFraction = 1 if sizeFraction > 1 else (0.1 if sizeFraction < 0.1 else sizeFraction)
            self.creature.shapesize( sizeFraction,  sizeFraction, 1)
            return True


class Creature(turtle.Turtle):
    """
    everything in this game is a creature of some kind.
    This class defines the basic creature functionality from which all others extend.
    """

    DEFAULT_SPEED = 5
    DEFAULT_RADIUS = 10


    def __init__(self, shape="circle", color="antiquewhite", x=0, y=0, boxWidth=None, boxHeight=None, **kwargs):
        super().__init__(**kwargs) # initialize the turtle
        # then set some basic properties
        self.showturtle()
        self.penup()
        self.goto(x,y)
        self.shape(shape)
        self.color(color)
        self.dx = 0
        self.dy = 0
        self.goto(x,y)
        self.radius = self.DEFAULT_RADIUS
        self.setState('BIRTH')
        self.initTime = time.perf_counter()
        self.animation = Animator() # a blank animator
        self.__lastChanceForAChange = {}

        (canvWidth, canvHeight) = turtle.screensize()
        self.boxWidth  = boxWidth   if boxWidth  is not None else 200
        self.boxHeight = boxHeight  if boxHeight is not None else 200


    # these set up the event handler functions to use with lambdas
    # They don't do anything at all.  Extend them to do something.
    # these set up the event handler functions to use with lambdas
    # They don't do anything at all.  Extend them to do something.

    def onKey(self, key=None):
        pass

    def onKeyRelease(self, key=None):
        pass

    def onClick(self, x, y):
        pass

    def chanceForAChange(self, changeKind, percentageSuccess):
        """every 1/2 a second, see if it is randomly time for something to change.
        The probablility is the chance of a change within that half a second. """
        try:
            elapsed = msTime() - self.__lastChanceForAChange[changeKind]
            #print("Elapsed Now", elapsed, 'for ', changeKind)
        except:
            self.__lastChanceForAChange[changeKind] = msTime()
            elapsed = 0
            #print("Elapsed is 0", 'for ', changeKind)
        if elapsed > 500:  # do this twice a second
            #print("Go!  with % ", percentageSuccess, 'for ', changeKind)
            self.__lastChanceForAChange[changeKind] = msTime()
            result = random.randrange(100) < (percentageSuccess)
            #print("result: ", result, 'for ', changeKind)
            return result

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

    def move(self):
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
            self.dx = self.dx
            self.dy = self.dy
        except:
            print("Error, probably because dx and dy are not properties of the turtle")


    def collidesWith(self, otherCreature):
        if otherCreature.getState() in ['DYING', 'DEAD']:
            return False
        return  self.distance(otherCreature) < (self.radius + otherCreature.radius)

    def hostileTo(self, otherCreature):
        return True

    def getState(self):
        return self.state[0]

    def setState(self, state):
        self.state = (state, msTime())




class Monster(Creature) :

    MONSTER_SPEED = 10
    DANGER_TIME = 2000  #  secs to be danger before going angry
    DIE_TIME   = 500  # how long it takes to go POOF!

    DIRECTION_SHIFT_CHANCE = 5  # pct chance of a random direction shift per second
    PHASE_SHIFT_CHANCE = 10     # pct chance of a random phase shift per second

    def __init__(self, x=0, y=0, initialSpeed=None, tenderColor="blue", warningColor = 'yellow', dangerColor='red', **kargs):
        super().__init__(x=x,y=y,**kargs)
        if initialSpeed is None: initialSpeed = self.MONSTER_SPEED

        self.tenderColor  = tenderColor
        self.dangerColor  = dangerColor
        self.warningColor = warningColor
        self.goto(x,y)

        self.color(self.warningColor)
        self.animation = Animator(creature=self, animation=Animator.pulseOutline,
                                  msDuration=2000, msPulse=200, colorON="red", colorOFF="yellow")
        self.setState('DANGER')

    # do not return.  Go directly into doing danger.
    def chooseNewDirection(self, speedRange=None):
        """ set a new direction for turtle t
        Uses optional named parameter speedRange which defaults to SPEED, a constant
        You can make it choose a new direction that is slow by doing:
        chooseNewDirection(fred, speed=2)
        """
        if speedRange is None: speedRange = self.MONSTER_SPEED
        self.dx = random.randint(-speedRange, speedRange)
        self.dy = random.randint(-speedRange, speedRange)

    def __bounceRandomlyOffEdges(self):
        # get the location we WOULD go to
        newX = self.xcor() + self.dx
        newY = self.ycor() + self.dy
        while  (abs (newX) > self.boxWidth) or (abs(newY) > self.boxHeight):
            # print("choosing new direction... ",end="")
            self.chooseNewDirection()
            # print(self.dx, self.dy)
            newX = self.xcor() + self.dx
            newY = self.ycor() + self.dy


    def move(self):
        """ if monster is about to move outside our bounding box, choose a new direction """

        self.__bounceRandomlyOffEdges()

        if self.getState() == 'DANGER':
            if not self.animation.animate():
                self.color('red')
                self.setState('ANGRY')
                self.chooseNewDirection()


        if self.getState() == 'DYING':
            if not self.animation.animate():
                self.setState('DEAD')


        if self.getState() == 'TENDER':
            self.animation.animate()
            if self.chanceForAChange("direction", self.DIRECTION_SHIFT_CHANCE):
                self.chooseNewDirection()

            if self.chanceForAChange("state", self.PHASE_SHIFT_CHANCE):

                self.color(self.warningColor)
                self.animation = Animator(creature=self, animation=Animator.pulseOutline,
                                  msDuration=self.DANGER_TIME, msPulse=200, colorON=self.dangerColor, colorOFF=self.warningColor)
                self.setState('DANGER')

        if self.getState() == 'ANGRY':
            self.animation.animate()
            if self.chanceForAChange("direction", self.DIRECTION_SHIFT_CHANCE):
                self.chooseNewDirection()

            if self.chanceForAChange("state", self.PHASE_SHIFT_CHANCE):
                self.animation = Animator()
                self.setState('TENDER')
                self.color(self.tenderColor)
            self.__bounceRandomlyOffEdges()

        # now move our monster
        super().move()


    def die(self):
        if self.getState() not in ['DYING', 'DEAD']:
            self.setState('DYING')
            self.dx, self.dy = 0,0
            self.animation = Animator(self,animation=Animator.winkOut,msDuration=500)


    def isHostile(self):
        return self.getState() in ['ANGRY']

class Player(Creature):

    MAX_CLICK_SPEED = 10
    FRICTION = 0.1

    def __init__(self, color="purple", **kwargs):
        kwargs['color'] = color  # default Creature to be purple
        super().__init__(**kwargs)
        self.setState('ALIVE')

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
        #print("click", x, y,self.dx, self.dy)


    def move(self):
        animationContinues = self.animation.animate()

        if self.getState() == 'ALIVE':
            super().move()
            self.dx *= (1 - self.FRICTION)
            self.dy *= (1 - self.FRICTION)

        elif self.getState() == 'DYING':
            if not animationContinues:
                self.setState = ('DEAD' )


    def winsBattle(self, creature):
        if creature.isHostile():
            return False
        else:
            return True


    def die(self):
        if self.getState() not in ['DYING', 'DEAD']:
            self.setState ('DYING')
            self.dx, self.dy = 0, 0
            self.animation = Animator(self, animation=Animator.winkOut, msDuration=1000)
