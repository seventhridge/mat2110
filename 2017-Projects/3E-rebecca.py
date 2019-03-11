import turtle
import math

# Set up the window and its attributes
wn = turtle.Screen()
wn.bgcolor("light blue")

# CONSTANTS


WINDOWSIZE = 400
SPEED = 5
FRAME_DELAY = 1000 // 10  # 10 frames per second
BOX_RANGE = WINDOWSIZE // 2 - 50


def set_normalized_direction(t, x, y, speed):
    """ set turtle t's dx and dy to go towards x,y at the given speed
     """
    curr_x = t.xcor()
    curr_y = t.ycor()
    destination_x = curr_x + speed
    destination_y = curr_y + speed
    # get actual vector from t to x,y
    dx_actual = destination_x + curr_x
    dy_actual = destination_y + curr_y

    # get the length of that vector.  Can also use turtle.distance
    length = math.hypot(dx_actual, dy_actual)

    # now scale the vector
    t.dx = dx_actual / length * speed
    t.dy = dy_actual / length * speed


def move(t, object2, object3, object4, friction=0.01, gravity=0.01):
    """ move turtle t according to direction vector
    The turtle t must have its dx and dy attributes defined.
    The optional parameter friction has default value 0.0 and represents the
    amount the turtle will slow down after moving.
    :type friction: float
    :type t: object
    """
    if (abs(t.xcor() - object2.xcor()) < 0.01) and ((abs(t.ycor() - object2.ycor()) < 0.01)):
        if (abs(t.xcor() - object3.xcor()) < 0.01) and ((abs(t.ycor() - object3.ycor()) < 0.01)):
            if (abs(t.xcor() - object4.xcor()) < 0.01) and ((abs(t.ycor() - object4.ycor()) < 0.01)):
                try:
                    new_x = t.xcor() + t.dx
                    new_y = t.ycor() + t.dy
                    # apply friction
                    t.dx = t.dx * (1 - friction)
                    t.dy = t.dy * (1 - friction) * (1 - gravity)
                    t.goto(new_x, new_y)
                except:
                    print("Error, probably because dx and dy are not properties of the turtle")
            else:
                object4.forward(500)
                t.goto(-125, -125)
        else:
            object3.forward(500)
            t.goto(-125, -125)
    else:
        object2.forward(500)
        t.goto(-125, -125)


def prep(object1, object2, object3, object4):
    # position objects for start of game
    object1.up()  # position dart
    object1.goto(-125, -125)
    object2.up()  # position bird1
    object2.goto(50, -100)
    object3.up()  # position bird2
    object3.goto(100, -150)
    object4.up()  # position bird3
    object4.goto(175, -50)


def play(object1, object2, object3, object4):
    angle = int(input("What angle from 0-90 would you like?"))
    speed = int(input("What initial speed from 1-10 would you like?"))
    if object1.xcor() < WINDOWSIZE and object1.ycor() < WINDOWSIZE:
        x = object1.xcor()
        y = object1.ycor()
        set_normalized_direction(object1, x, y, speed)
        move(object1, object2, object3, object4)
    else:
        object1.goto(-125, -125)
    if object2.xcor() > WINDOWSIZE and object2.ycor() > WINDOWSIZE:
        if object3.xcor() > WINDOWSIZE and object3.ycor() > WINDOWSIZE:
            if object4.xcor() > WINDOWSIZE and object4.ycor() > WINDOWSIZE:
                print("You win!")
            else:
                play(object1, object2, object3, object4)
        else:
            play(object1, object2, object3, object4)
    else:
        play(object1, object2, object3, object4)


dart = turtle.Turtle()
dart.shape("arrow")
dart.color("black")

bird1 = turtle.Turtle()
bird1.shape("circle")
bird1.color("red")

bird2 = turtle.Turtle()
bird2.shape("circle")
bird2.color("green")

bird3 = turtle.Turtle()
bird3.shape("circle")
bird3.color("yellow")

prep(dart, bird1, bird2, bird3)
play(dart, bird1, bird2, bird3)

