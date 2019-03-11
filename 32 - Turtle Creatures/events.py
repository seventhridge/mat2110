"""
This module shows how you might handle events in general.
Requires Python 3.3 or later.
"""



import turtle, time

class TurtleEvents:

    def __init__(self, **kwargs):
        self._keysPressed = {}
        self._lastPressed = None
        super().__init__(**kwargs)

    def onKeyPress(self, key):
        if __name__ == "__main__": print("Press", key)
        self._keysPressed[key] = time.perf_counter()
        self._lastPressed = key

    def onKeyRelease(self, key):
        if __name__ == "__main__": print("Release", key)
        self._keysPressed[key] = None

    def getAllKeysPressed(self):
        return self._keysPressed.keys()

    def keyPressed(self, key):
        """ determine how long the key has been held down.  0 if it is not pressed. """
        return 0 \
            if key not in self._keysPressed.keys() \
            else time.perf_counter() - self._keysPressed[key]

    def getLastPressed(self):
        return self._lastPressed

    def onClick(self, x, y):
        self.lastClickX = x
        self.lastClickY = y

    # This next bit defines a CLASS PROPERTY and a CLASS METHOD.
    # The class method uses a "class decorator" (that thing with the @)
    #   which tells Python "Hey, this thing I am getting to see you takes a class object.
    #   not an instance object.  And note that the first variable is "cls" and not "self"
    # it does not work on an instance of a class.  Rather it is just packaged
    # in the class as a whole

    FRAME_DELAY = 100  # 10 times per second
    screen = None

    @classmethod
    def loop(cls, funcToDo):
        if not  cls.screen: cls.screen = turtle.Screen()
        funcToDo()
        cls.screen.ontimer(lambda : cls.loop(funcToDo), cls.FRAME_DELAY)


    @classmethod
    def setFrameDelay(cls,frameDelay):
        cls.FRAME_DELAY = frameDelay


    def bindKey(self, key):
        if not self.screen: self.screen = turtle.Screen()
        self.screen.onkeypress(lambda: self.onKeyPress(key), key)
        self.screen.onkeyrelease(lambda: self.onKeyRelease(key), key)

    def unbindKey(self, key):
        if not self.screen: self.screen = turtle.Screen()
        self.screen.onkeypress(None, key)
        self.screen.onkeyrelease(None, key)

    def bindClick(self):
        if not self.screen: self.screen = turtle.Screen()
        self.screen.onclick(lambda x, y: self.onClick(x, y))

    def unbindClick(self):
        if not self.screen: self.screen = turtle.Screen()
        self.screen.onclick(None)


if __name__ == '__main__':
    """
    Do some testing.  Also shows example usage.
    """
    import turtle

    turtle.setup(400, 400)
    wn = turtle.Screen()

    # here we use a gameState value to hold the state of our game instead of using globals
    # put all your simulation globals in here!
    class gameState:
        count = 0

    class MyBaseClass:
        # this might be the object that all your other objects are based on
        # and does not handle events
        def __init__(self, **kwargs):
            print("Initializing base class and then calling super().__init__")
            super().__init__(**kwargs)

    class MyEventObject(MyBaseClass, TurtleEvents):
        # this might be the object that represents your player,
        # or some instance you want to respond to events.
        # it inherits from two things - including TurtleEvents
        # You can extend onKey and onClick to do what you like.
        #   and use bindKey and bindClick to get them started.

        def __init__(self, **kwargs):
            print("Initializing a myEventObject instance and then calling super().__init__")
            print(kwargs)
            super().__init__(**kwargs)


        def onKeyPress(self, key):
            print("We pressed ", key)
            lastPressed = self.getLastPressed()
            print("We last pressed ", lastPressed)

            super().onKeyPress(key)

            #print('We pressed' , lastPressed, ' time ago in ms:  ', int(1000 * self.keyPressed(lastPressed)))
            # all keys pressed doesn't work yet because the release event
            #  has not yet been figured out.
            #print("All keys pressed: ", self.getAllKeysPressed())

        def onClick(self, x, y):
            print("We clicked here: ",x,y)
            super().onClick(x,y)


    def testingGameRunOneFrame():
        gameState.count += 1
        print("this is loop ", gameState.count)
        if gameState.count >= 10:
            wn.bye()



    someKeyEventObject = MyEventObject()

    someKeyEventObject.bindKey("Up")
    someKeyEventObject.bindKey("Left")
    someKeyEventObject.bindKey("Right")
    someKeyEventObject.bindKey("Down")
    #    wn.onkey(lambda: someKeyEventObject.onKey('Down'), "Down")

    someKeyEventObject.bindClick()
    #wn.onclick(lambda x, y: someKeyEventObject.onClick(x, y))  # Wire up a click on the window.

    # here we go YAY!
    someKeyEventObject.setFrameDelay(5000)
    someKeyEventObject.loop( lambda : testingGameRunOneFrame() )

    wn.listen()
    wn.mainloop()
