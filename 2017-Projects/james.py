import turtle, math, random, time




print("The goal of this game is to set the angle and velocity of a cannon shot, trying to hit a target on the other side of the screen. In order to win, you must hit the target "
     "5 times. If you miss the target, the target will move towards you. If the target reaches you, it is GAME OVER. THere are three difficulities: EASY, NORMAL, and HARD. In the "
     "EASY difficulty, the target does not move toward you, and so you can enjoy playing until you win. In the NORMAL difficulty, the target moves towards you but once you hit it, it is reset "
     "back to its starting position. In the HARD difficulty, the target moves towards you and does not reset if hit. WHICH WILL YOU PLAY?")




TESTING = False


def setDifficulty():    #sets difficulty of game
   moveOn = False
   while not(moveOn):  #infinite loop until acceptable answer is given
       difficulty = input("What would you like the difficulty to be [EASY, NORMAL, HARD]?")
       difficulty = difficulty.upper()
       if difficulty == "EASY" or difficulty == "NORMAL" or difficulty == "HARD":
           moveOn = True
       else:
           print("Unacceptable response. Difficulty must be EASY, NORMAL, or HARD. Try again.")    #if answer is not easy, medium, or hard, asks user again
   print("Difficulty set to " + difficulty + ".")
   return difficulty


def setWindow(wn):  #sets up window information (title and color)
   wn.bgcolor("black")
   wn.title("Hit The Target")


def modifyTurtle(t):    #sets up turtle info (color, penup, speed)
   t.color("white")
   t.penup()
   t.speed(0)


def createGround(t):    #creates ground using turtle
   t.setheading(0)
   t.goto(-400,-100)
   t.pendown()
   t.forward(800)
   t.penup()


def moveCannon(t):  #moves the cannon turtle to its set location
   t.setheading(0)
   t.goto(-300,-100)


def moveTarget(t,miss): #moves the target turtle to its set location
   t.setheading(0)
   t.goto(300-(100*miss),-100) #target moves towards player with each miss, then if it is hit it moves back to original position


def buildTarget(t,size,height,miss):    #builds the target with height and size of target dimensions set at random numbers
   t.setheading(0)
   t.pendown()
   t.left(90)
   t.forward(height)
   t.right(90)
   t.forward(size/2)
   for side in range(4):
       t.left(90)
       t.forward(targetSize)
   t.penup()
   moveTarget(t=t,miss=miss)
   t.hideturtle()


def setVariable(variable):
   moveOn = False
   while not(moveOn):  #makes certain that response is acceptable
       if variable == "angle":
           output = input("What is the angle of the cannon? [degress above horizontal]")
       elif variable == "velocity":
           output = input("What is the velocity of the shot? [m/s]")
       try:
           output = int(output)
           if variable == "angle":
               if output <= 90 and output >= 0:
                   moveOn = True
           else:
               moveOn = True
       except:
           print("Unacceptable response. Answer must be an integer. Try again.")
   return output


def angleOfCannon(t, angle):   #asks user for angle of cannon input
   t.setheading(angle) #sets turtles angle to be specified angle
   radianAngle = math.radians(angle)   #radianAngle will be used in velocityOfShot function
   return radianAngle


def unitTest_angleOfCannon():
   testingWn = turtle.Screen()
   testingTurtle = turtle.Turtle()
   testingTurtle.hideturtle()
   if angleOfCannon(t=testingTurtle,angle=90) != math.pi/2:
       print("angleOfCannon Test 1 Failed")
   if angleOfCannon(testingTurtle,30) != 0.5235987755982988:
       print("angleOfCannon Test 2 Failed")


def velocityOfShot(radianAngle,velocity):    #separates and determines x and y direction velocity of shot from input velocity
   xVelocity = velocity * math.cos(radianAngle)    #x direction velocity
   yVelocity = velocity * math.sin(radianAngle)    #y direction velocity
   return xVelocity, yVelocity


def unitTest_velocityOfShot():
   if velocityOfShot(radianAngle=math.pi/2,velocity=10)[0] != 6.123233995736766e-16:
       print("velocityOfShot Test 1 Failed")
   if velocityOfShot(radianAngle=math.pi/2,velocity=10)[1] != 10.0:
       print("velocityOfShot Test 2 Failed")


def fire(t,target,targetSize,targetHeight,xVelocity,yVelocity,numberOfHits):
   t.pendown()
   time = 0
   deltat = 0.01   #increments the loop at 0.01s to ensure accurate smooth lines
   while time <= 100:
       if t.ycor() >= -100 and t.xcor() >= -400 and t.xcor() <= 400:   #makes sure that turtle is still in window
           xVelocity += (0)*deltat #no x direction force present
           yVelocity += (-9.8)*deltat  #gravity is the only y direction force present
           t.setposition(t.xcor() + xVelocity*deltat, t.ycor() + yVelocity*deltat) #moving by changing position from old to new rather than through forward commands
           if t.xcor() >= (target.xcor()-(targetSize/2)) and t.xcor() <= (target.xcor()+(targetSize/2)) and t.ycor() >= (-100 + targetHeight) and t.ycor() <= (-100 + targetHeight + targetSize):  #detects if cannon turtle is within target hitbox
               print("Target Has Been Hit")
               numberOfHits += 1
               break   #breaks loop if target is hit
       time += deltat
   return numberOfHits


def moveScore(t):   #moves score turtle to correct placement
   t.setheading(0)
   t.goto(-25,250)
   t.hideturtle()


def targetScore(t,numberOfHits):    #scores from 0 to 4 are displayed relative to how many targets have been hit
   scoreDict = {0: "pendown, ,forward,50,left,90,forward,70,left,90,forward,50,left,90,forward,70,penup, " ,
                1: "pendown, ,forward,50,forward,-25,left,90,forward,70,left,135,forward,25,penup, ",
                2: "pendown, ,forward,50,forward,-50,left,90,forward,35,right,90,forward,50,left,90,forward,35,left,90,forward,50,penup, ",
                3: "pendown, ,forward,50,left,90,forward,35,left,90,forward,50,forward,-50,right,90,forward,35,left,90,forward,50,penup, ",
                4: "forward,50,left,90,pendown, ,forward,70,forward,-35,left,90,forward,50,right,90,forward,35,penup, ",}  #uses a dictionary that contains the instructions to draw each letter
   instructions = scoreDict[numberOfHits]
   instructions = instructions.split(",")
   for command in range(int(len(instructions)/2)):
       if instructions[command * 2] == "forward":
           t.forward(int(instructions[command * 2 + 1]))
       if instructions[command * 2] == "left":
           t.left(int(instructions[command * 2 + 1]))
       if instructions[command * 2] == "right":
           t.right(int(instructions[command * 2 + 1]))
       if instructions[command * 2] == "penup":
           t.penup()
       if instructions[command * 2] == "pendown":
           t.pendown()


def endGameMessage(t,message): #displays game over if play loses, similar to score set up
   letterDict = {"G":"pendown, ,forward,50,left,90,forward,35,left,90,forward,25,forward,-25,right,90,forward,-35,right,90,forward,-50,left,90,forward,70,right,90,forward,50,penup, ,",
                 "A":"pendown, ,left,90,forward,70,right,90,forward,50,right,90,forward,70,forward,-35,right,90,forward,50,penup, ,",
                 "M":"pendown, ,left,90,forward,70,right,90,forward,25,right,90,forward,70,forward,-70,left,90,forward,25,right,90,forward,70,penup, ,",
                 "E":"pendown, ,forward,50,forward,-50,left,90,forward,35,right,90,forward,50,forward,-50,left,90,forward,35,right,90,forward,50,penup, ,",
                 " ":"",
                 "O":"pendown, ,forward,50,left,90,forward,70,left,90,forward,50,left,90,forward,70,penup, ,",
                 "V":"pendown, ,left,90,forward,70,forward,-70,right,90,forward,50,left,90,forward,70,penup, ,",
                 "R":"pendown, ,left,90,forward,70,right,90,forward,50,right,90,forward,35,right,90,forward,50,forward,-25,left,90,forward,35,penup, ,",
                 "Y":"forward,25,left,90,pendown, ,forward,30,left,90,forward,25,right,90,forward,30,forward,-30,left,90,forward,-50,right,90,forward,30,penup, ,",
                 "U":"pendown, ,left,90,forward,70,forward,-70,right,90,forward,50,left,90,forward,70,penup, ,",
                 "W":"pendown, ,left,90,forward,70,forward,-70,right,90,forward,25,left,90,forward,70,forward,-70,right,90,forward,25,left,90,forward,70,penup, ,",
                 "I":"forward,25,pendown, ,left,90,forward,70,penup, ,",
                 "N":"pendown, ,left,90,forward,70,right,90,forward,25,right,90,forward,70,left,90,forward,25,left,90,forward,70,penup, ,"}
   t.forward(-(len(message)/2)*75) #moves turtle so that message is centered
   for letter in message:
       instructions = letterDict[letter]
       instructions = instructions.split(",")
       startingPos = t.pos()
       for command in range(int(len(instructions)/2)):
           if instructions[command * 2] == "forward":
               t.forward(int(instructions[command * 2 + 1]))
           if instructions[command * 2] == "left":
               t.left(int(instructions[command * 2 + 1]))
           if instructions[command * 2] == "right":
               t.right(int(instructions[command * 2 + 1]))
           if instructions[command * 2] == "penup":
               t.penup()
           if instructions[command * 2] == "pendown":
               t.pendown()
       t.goto(startingPos)
       t.setheading(0)
       t.forward(75)
   t.hideturtle()




if TESTING:
   unitTest_angleOfCannon()
   unitTest_velocityOfShot()




difficulty = setDifficulty()


turtle.setup(800,800)
wn = turtle.Screen()


numberOfHits = 0
miss = 0
gameOver = False
while numberOfHits < 5:
   setWindow(wn=wn)
   if gameOver:
       badNewsTurtle = turtle.Turtle()
       badNewsTurtle.color("green")
       badNewsTurtle.penup()
       badNewsTurtle.speed(0)
       endGameMessage(t=badNewsTurtle,message="GAME OVER")
       wn.exitonclick()
   previousNumberOfHits = numberOfHits
   ground = turtle.Turtle()
   modifyTurtle(t=ground)
   target = turtle.Turtle()
   modifyTurtle(t=target)
   score = turtle.Turtle()
   modifyTurtle(t=score)
   cannon = turtle.Turtle()
   cannon.color("green")
   cannon.penup()
   cannon.speed(0)
   targetSize = random.randint(10,30)
   targetHeight = random.randint(1,250)
   createGround(t=ground)
   moveCannon(t=cannon)
   startingCannonX = cannon.xcor()
   moveTarget(t=target,miss=miss)
   buildTarget(t=target,size=targetSize,height=targetHeight,miss=miss)
   moveScore(t=score)
   targetScore(t=score, numberOfHits=numberOfHits)
   angle=setVariable(variable="angle")
   radianAngle = angleOfCannon(t=cannon,angle=angle)
   velocity = setVariable(variable="velocity")
   initial_xVelocity, initial_yVelocity = velocityOfShot(radianAngle=radianAngle, velocity=velocity)
   print(initial_xVelocity, initial_yVelocity)
   numberOfHits = fire(t=cannon,target=target,targetSize=targetSize,targetHeight=targetHeight,xVelocity=initial_xVelocity,yVelocity=initial_yVelocity,numberOfHits=numberOfHits)
   if difficulty == "MEDIUM" or difficulty == "HARD":
       if numberOfHits == previousNumberOfHits:
           miss += 1
           if 300 - (100 * miss) == startingCannonX:
               print("GAME OVER! YOU HAVE LOST!")
               gameOver = True
       elif difficulty == "MEDIUM":
           miss = 0
   time.sleep(3)   #sleep for 3 seconds to let the player take in their success or failure
   wn.clearscreen()
print("YOU HIT 5 TARGETS! YOU WIN!")
setWindow(wn=wn)
goodNewsTurtle = turtle.Turtle()
goodNewsTurtle.color("green")
goodNewsTurtle.penup()
goodNewsTurtle.speed(0)
endGameMessage(t=goodNewsTurtle,message="YOU WIN")
wn.exitonclick()


