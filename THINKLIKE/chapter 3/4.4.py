# import turtle

# def draw_square(t, sz):
#     """Make turtle t draw a square of sz."""
#     for i in range(8):
#         t.forward(sz)
#         t.left(45)
        


# wn = turtle.Screen()        # Set up the window and its attributes
# wn.bgcolor("lightgreen")
# wn.title("Alex meets a function")

# alex = turtle.Turtle()      # Create alex
# draw_square(alex, 120)       # Call the function to draw the square
# wn.mainloop()

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")      # Set the window background color
wn.title("Hello, Tess!")      # Set the window title

tess = turtle.Turtle()
tess.color("blue")            # Tell tess to change her color
tess.pensize(7)               # Tell tess to set her pen width
# tess.speed(1)
for i in range(20):
    for j in range(4):
        tess.forward(120)    
        tess.right(90)
    tess.right(18)

     

    
    
    
    # tess.forward(50)
# tess.forward(50)

wn.mainloop()