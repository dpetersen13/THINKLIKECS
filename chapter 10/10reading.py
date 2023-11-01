import turtle

turtle.setup(800, 800)  # Determine the window size
wn = turtle.Screen()  # Get a reference to the window
wn.title("Handling keypresses!")  # Change the window title
wn.bgcolor("lightgreen")  # Set the background color
tess = turtle.Turtle()  # Create our favorite turtle


# The next four functions are our "event handlers".
def h1():
    tess.forward(30)


def h2():
    tess.left(45)


def h3():
    tess.right(45)


def star(length):
    for i in range(5):
        tess.forward(length)
        tess.right(144)


def square(length):
    for i in range(4):
        tess.forward(length)
        tess.right(90)


def h9():
    length = float(int(input("How Far do you want to move?     ")))
    shape = input("Which shape do you want to draw? ").lower()

    if shape == "star":
        star(length)
    if shape == "square":
        square(length)

    return length


def h5():
    wn.clear()
    initialize()


def initialize():
    turtle.setup(400, 500)  # Determine the window size
    wn = turtle.Screen()  # Get a reference to the window
    wn.title("Handling keypresses!")  # Change the window title
    wn.bgcolor("lightgreen")  # Set the background color
    tess = turtle.Turtle()


def h4():
    wn.bye()  # Close down the turtle window


def h6():
    tess.penup()


def h7():
    tess.pendown()


# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.onkey(h5, "c")
wn.onkey(h6, "u")
wn.onkey(h7, "d")
wn.onkey(h9, "s")


# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()
