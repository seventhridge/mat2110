def runGame():
    theta = float(input("Enter a launch angle between 0 and 90 degrees:"))
    velocity = int(input('Enter a desired speed between 0 and 10:'))
    #one function containing the entire program so the turtle screen can be reset
    #take an input
    def launchcode():
        theta = float(input("Enter a launch angle between 0 and 90 degrees:"))
        velocity = int(input('Enter a desired speed between 0 and 10:'))
      #'math' the input until it is in dx dy
    def launch():
        newX = t.xcor() + t.dx
        newY = t.ycor() + t.dy
        t.goto(newX, newY)

        t.dx = t.dx - 0.0025
        t.dy = t.dy - .02
    #send rocket based on launchcode
    def gameLoop():
        try:
            if rocket.xcor() < target.xcor() +5 and rocket.ycor()> -5:
                launch(rocket)
                if rocket.xcor() < target.xcor()+5 and rocket.xcor() > target.xcor()-5 \
                    and rocket.ycor()> target.ycor()-5 and rocket.ycor()< target.ycor()+5:
                    wn.bye()
                    print("YOU WON!!!")
                    return None
                if rocket.xcor() > target.xcor() +4 or rocket.ycor()< -4:
                    print("You Missed! Try again.")
                    runGame()
                    return None
            #print(rocket.xcor(), ",", rocket.ycor())
            turtle.update()
            wn.ontimer(gameLoop,1)


        except:
            raise

            print("ERROR")

        if rocket.ycor()<-10:
            print("error")
        if rocket.xcor()>target.xcor()+10:
            print("error2")
        if ((rocket.dx)**2)**.5 != rocket.dx:
            print("error3")
            #making sure it shoots the right direction


    #decide wether it was a hit or miss then reset
