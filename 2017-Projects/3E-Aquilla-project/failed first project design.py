import turtle, math
turtle.setup(400,400)
wn=turtle.Screen()
wn.bgcolor("antique white")

rocket =turtle.Turtle()
target= turtle.Turtle()
#def loser():
#def winner():
angle = None
def fn_up(a):
    #if angle<=85:
    angle=angle+5

def fn_down():
    #if angle>=5:
    angle=angle-5
velocity= None
def fn_left():
    #if velocity >= 5:
    velocity = velocity - 5

def fn_right():
    #if velocity <= 95:
    velocity = velocity + 5
launchGo= None
def fn_launch(launchGo):
    launchGo = launchGo + 1

def launch(angle,velocity,rocket):
    angle = math.radians(angle)
    rocket.dx=velocity* math.cos(angle)
    rocket.dy=velocity* math.sin(angle) - 5 #gravity
    #stop when rocket.xcor() == target.xcor()

def hitfinder1(rocket, target):
    if rocket.ycor() < target.ycor() + 10 and rocket.ycor() > target.ycor() - 10 :
        return 1
    else:
        return 0



def gameloop(lives,level):
    while lives>0 and level<4:
        update = gamelvl(level)
        lives = lives - update
        level = level + update
    if lives==0:
        loser()
    if level == 4:
        winner()

def gamelvl(level):
    if level==1:
        hitResult = lvl1(rocket,target)
        return hitResult
    if level==2:
        hitResult = lvl1(rocket,target)
        return hitResult
    if level==3:
        hitResult = lvl3()
        return hitResult

def turtleLoop():
    while launchGo != 1:
        wn.onkey(fn_up, "Up")
        wn.onkey(fn_down, "Down")
        wn.onkey(fn_left, "Left")
        wn.onkey(fn_right, "Right")
        wn.onkey(fn_launch, "l")
        wn.listen()
        turtle.update()
        wn.ontimer(turtleLoop, 10)



def lvl1(rocket,target):
    rocket.setpos(0,0)
    target.penup()
    target.setpos(100,0)
   # angle = 45
   # velocity = 10
   # launchGo = 0
    wn.ontimer(turtleLoop, 10)
    if launchGo == 1:
        launch(45,10,rocket)
    hitResult = hitfinder1(rocket, target)
    return hitResult





gameloop(5,1)


