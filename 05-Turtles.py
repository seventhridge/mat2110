import turtle

# Set up the window and its attributes
turtle.setup(400,400)
wn = turtle.Screen()
wn.bgcolor("antique white")

# named colors are here:  http://wiki.tcl.tk/37701

mike = turtle.Turtle()  # create mike
sam  = turtle.Turtle()  # create sam
jane = turtle.Turtle()

mike.color("hotpink")   # colors can be name
sam.color("#c0f000")   # colors can be hex codes rrggbb
# set how rgb colors work (0 is float, 255 is 0..255)
wn.colormode(255)
jane.color( (0,0,40) )   # or rgb

mike.left(90)
mike.forward(100)

sam.left(180)
sam.forward(100)

jane.left(-90)
jane.forward(100)

# wait for click before we go away


wn.exitonclick()