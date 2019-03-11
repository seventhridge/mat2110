import turtle, math, random
turtle.setup(1000,400)
wn=turtle.Screen()
bird=turtle.Turtle()

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

#def newenemyturtle():


# spawn 2 new enemy turtles (one 20 above the other
# send turtles to the left at a constant speed

def gameloop():
    flyingturtlemove()
    turtle.update()
    wn.ontimer(gameloop, 5)






# main loop of the game


wn.listen()
wn.onkey(fn_up, "space")
bird.penup()
setbird()
wn.ontimer(gameloop,5)
wn.mainloop()

