import turtle, math, random

print("                 ***INVADER*** \nUse the left and right arrow keys to steer your ship,\n"
      "to run over the Space Turtles that have come to take over Earth. \n"
      "Each Alien that you hit gives you 1/2 life and 1 point.\n"
      "Lives are shown on the left in green, and score is on the right in red.\n"
      "Each Alien that you miss takes away 1 life. ")
life=int(input("How many lives would you like to start with? \n(1-3:HARD)(4-6:NORMAL)(7-10:EASY)"))
if life>10:
    life=10
if life<1:
    life=1
lifeStart=10*life -180



turtle.setup(550,450)
wn = turtle.Screen()
wn.bgpic("Space.png")
wn.title("INVADER")
WINDOWSIZE = 450
FRAME_DELAY  = 1000 // (100)   # 10 frames per second
BOX_RANGE = WINDOWSIZE // 2 - 50
def setDirect(t, x, y, speed):
    currX = t.xcor()
    currY = t.ycor()
    # get actual vector from t to x,y
    dXactual = x - currX
    dYactual = y - currY

    # get the length of that vector.
    length = math.hypot(dXactual, dYactual)

    # now scale the vector
    t.dx = dXactual / length * speed
    t.dy = dYactual / length * speed

def newAlienShip(t,speed):
    r=40*random.randint(-5,5)
    t.setpos(r,200)
    setDirect(t,r,-200,speed)
#randomly drop turtles
def moveAlien(t):
    newY = t.ycor() + t.dy
    t.goto(t.xcor(), newY)
    currentscore = (score.ycor() + 180) / 10
    t.dy = t.dy - .0025*currentscore #accelerates faster the better your score is

def fn_left():
    try:
        xcor=ship.xcor()-40 #left 40
        ship.setpos(xcor,-175)
    except:
        print("fn_left eventTurtle has no left method, or it got an error")

def fn_right():
    try:
        xcor = ship.xcor() + 40 #right 40
        ship.setpos(xcor, -175)
    except:
        print("fn_right eventTurtle has no right method or it got an error")

def fn_quit():
    wn.bye()


def gameloop():
    if lives.ycor()>-180:
        if invader.ycor() > -180 and invader.ycor()<-170 and invader.xcor()==ship.xcor():
            lives.forward(5)
            score.forward(10)
            newAlienShip(invader, 1)
            #if you get the turtle

        if invader.ycor() > -190:
            moveAlien(invader)
            #move the turtle down with increasing speed

        if invader.ycor() <= -190:
            lives.backward(10)
            newAlienShip(invader,1)
            #if you let one go you loose a life and a new random turtle is dropped
        turtle.update()
        wn.ontimer(gameloop, FRAME_DELAY)
    #if score.ycor()>= 70:
        # if invader2.ycor() > -180 and invader2.ycor()<-170 and invader2.xcor()==ship.xcor():
           # lives.forward(5)
           # score.forward(10)
            #newAlienShip(invader2, 1)
            #if you get the turtle

       # if invader2.ycor() > -190:
           # moveAlien(invader2)
            #move the turtle down with increasing speed

        #if invader2.ycor() <= -190:
           # lives.backward(10)
            #newAlienShip(invader2,1)
            #if you let one go you loose a life and a new random turtle is dropped
        #turtle.update()
        #wn.ontimer(gameloop, FRAME_DELAY)

    if lives.ycor()<= -180: #when you're out of lives
        wn.bye()
        finalscore=(score.ycor()+180)//10
        print("                 ***GAME OVER*** \n    YOUR SCORE:", finalscore)





ship=turtle.Turtle()
invader=turtle.Turtle()
#invader2=turtle.Turtle()
score=turtle.Turtle()
lives=turtle.Turtle()

ship.color("green")
invader.color("red")
#invader2.color("red")
score.color("red")
lives.color("green")

score.pencolor("red")
score.pensize(10)
lives.pencolor("green")
lives.pensize(10)

screen=invader.getscreen()
screen.register_shape("invader.gif")
invader.shape("invader.gif")

#scren=invader2.getscreen()
#scren.register_shape("invader.gif")
#invader2.shape("invader.gif")

#invader.resizemode(user)
#invader.shapesize(5,5,12)

scrEEn=ship.getscreen()
scrEEn.register_shape("rocket.gif")
ship.shape("rocket.gif")

score.shape('circle')
lives.shape('circle')
#invader.shape("turtle")

ship.penup()
invader.penup()
#invader2.penup()
score.penup()
lives.penup()
turtle.tracer(0)

ship.left(90)
invader.right(90)
#invader2.right(90)
score.left(90)
lives.left(90)

ship.setpos(0,-175)
score.setpos(230,-180)
lives.setpos(-230,-180)
score.pendown()
lives.pendown()
lives.setpos(-230,lifeStart)

wn.onkey(fn_left, "Left")
wn.onkey(fn_right, "Right")
wn.onkey(fn_quit, "q")
wn.listen()
newAlienShip(invader,1)
#invader2.setpos(0,300)
wn.ontimer(gameloop,FRAME_DELAY)
wn.mainloop()