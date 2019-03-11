import turtle, math, random
turtle.setup(1000,400)
wn=turtle.Screen()
bird=turtle.Turtle()
t1=turtle.Turtle()
t2=turtle.Turtle()
t1.color("red")
t2.color("red")

def setbird():
    bird.setpos(-400,0)
    bird.dy = 0
def flyingturtlemove():
    fall=bird.ycor() + bird.dy
    bird.goto(bird.xcor(),fall)
    if bird.dy>-4:
        bird.dy -= .1 #gravity
    if bird.ycor()> 190:
        bird.dy=-1



# how the flying turtle moves

def fn_up():
    if bird.dy<3:
        if bird.dy<-2:
            bird.dy += 5 #amount the bird jumps

        if bird.dy>-2:
            bird.dy += 4


# Make turtle jump

def newenemyturtle():
    r=random.randint(-190,90)
    t1.goto(200,r)
    t2.goto(200,r+100)


# spawn 2 new enemy turtles (one 20 above the other
# send turtles to the left at a constant speed
def enemyturtlemove():
    t1.goto(t1.xcor()-5,t1.ycor())
    t2.goto(t2.xcor()-5, t2.ycor())


def gameloop():
    while t1.xcor()> -450:
        flyingturtlemove()
        enemyturtlemove()
    else:
        if bird.ycor()> t1.ycor() and bird.ycor()< t2.ycor(): #if the bird goes through the gate
            newenemyturtle()

        if bird.ycor()< t1.ycor() or bird.ycor()> t2.ycor(): #outside

            wn.bye()
            print("you lose")


    wn.ontimer(gameloop, 10)






# main loop of the game


wn.listen()
wn.onkey(fn_up, "space")
bird.penup()
t1.penup()
t2.penup()
newenemyturtle()
setbird()
wn.ontimer(gameloop,10)
wn.mainloop()

