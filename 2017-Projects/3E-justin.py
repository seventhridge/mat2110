
import turtle, math, random


speed = int(input("What is the starting speed for the turtle?"))
angle = int(input("What is the starting angle for the turtle?"))


#get initial speed and angle


turtle.setup(600,600)
wn = turtle.Screen()
wn.bgcolor("antique white")
wn.title("Mars Move Around!")


#set up base


WINDOWSIZE = 600
SPEED = 5
FRAME_DELAY  = 1000 // (10)   # 10 frames per second
BOX_RANGE = WINDOWSIZE // 2 - 50


def start_charles():
  charles.ht()
  charles.penup()
  charles.goto(-250,-250)
  charles.pendown()
  charles.st()


#move turtle to an initial position(lower left corner)


def moveshooter(t, friction = 0.0):


  rad = math.radians(angle)
  t.dx = (speed) * math.cos(rad)
  t.dy = ((speed) * math.sin(rad))


  # get vertical and horizontal speed


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
   try:
       newX = t.xcor() + t.dx
       newY = t.ycor() + t.dy
       while  (abs (newX) > BOX_RANGE) or (abs(newY) > BOX_RANGE):
           t.goto(0,0)
           print("You have gone out of bounds!")
   except:
       print("Error in boundingBox - probably because turtle t has no dx or dy.")


def movetarget():
   charles2.goto(random.randrange(200, 280), random.randrange(200, 280))


def gameLoop():
   for thisTurtle in allTurtles:
        boundingBox(thisTurtle)
        moveshooter(thisTurtle)


        turtle.update()


        wn.ontimer(gameLoop, FRAME_DELAY)


charles = turtle.Turtle()
charles.shape("circle")
charles.color("purple")


charles2 = turtle.Turtle()
charles2.shape("circle")
charles2.color("green")
charles2.penup()


#create second turtle


allTurtles  = [charles]
eventTurtle = charles


turtle.tracer(0)


start_charles()
movetarget()
wn.ontimer(gameLoop, FRAME_DELAY)


wn.mainloop()


