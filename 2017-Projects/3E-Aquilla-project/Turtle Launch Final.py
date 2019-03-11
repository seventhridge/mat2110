import turtle, math
turtle.setup(600, 600)
wn = turtle.Screen()
wn.bgcolor("antique white")
wn.title("Target Practice")
WINDOWSIZE = 1600
SPEED = 5

def runGame():
    theta = float(input("Enter a launch angle between 0 and 90 degrees:"))
    velocity = int(input('Enter a desired speed between 0 and 10:'))
    def launchcode(t,w,speed):
        angle = math.radians(w)
        x = math.cos(angle)-00
        y = math.sin(angle)-0
        #converting theta to x and y components
        currX = t.xcor()
        currY = t.ycor()
        # get actual vector from t to x,y
        dXactual = x - currX
        dYactual = y - currY
        # get the length of that vector
        length = math.hypot(dXactual, dYactual)
        # now scale the vector
        t.dx = dXactual / length * speed
        t.dy = dYactual / length * speed

    def launch(t):
        newX = t.xcor() + t.dx
        newY = t.ycor() + t.dy
        t.goto(newX, newY)

        t.dx = t.dx -0.0025 #wind resistance
        t.dy = t.dy -.02 #gravity

    def gameLoop():
        try:
            if rocket.xcor() < target.xcor() +5 and rocket.ycor()> -5:
                launch(rocket) #if rocket is still inbounds, continue step through launch
                if rocket.xcor() < target.xcor()+5 and rocket.xcor() > target.xcor()-5 \
                    and rocket.ycor()> target.ycor()-5 and rocket.ycor()< target.ycor()+5:
                    wn.bye()
                    print("YOU WON!!!")
                    #5x5 hit box
                if rocket.xcor() > target.xcor() +4 or rocket.ycor()< -4:
                    print("You Missed! Try again.")
                    runGame() #resets every value except turtle window
                    #if not ^ gravity and wind resistance would account for last trial

            #print(rocket.xcor(), ",", rocket.ycor())
            #^to show turtle position for diagnostics
            turtle.update()
            wn.ontimer(gameLoop,1)


        except:
            raise #diognostics

            print("ERROR")

        if rocket.ycor()<-10:
            print("error")
        if rocket.xcor()>target.xcor()+10:
            print("error2")
        if ((rocket.dx)**2)**.5 != rocket.dx:
            print("error3")
            #making sure it shoots the right direction

    rocket=turtle.Turtle()
    launchcode(rocket,theta,velocity)
    target=turtle.Turtle()
    target.shape("circle")
    target.color("red")
    rocket.penup()
    rocket.setpos(-250, 0)
    target.penup()
    target.setpos(250, 0)
    #turtle.tracer(0)
    rocket.pendown()#optional
    wn.ontimer(gameLoop, 1)
    wn.mainloop()

runGame()
#start parent function
