import turtle
def star(length):
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")      # Set the window background color
    wn.title("Hello, Tess!")      # Set the window title

    tess = turtle.Turtle()
    tess.color("blue")            # Tell tess to change her color
    tess.pensize(2)               # Tell tess to set her pen width
    # tess.speed(1)
    #to do 
    for i in range(5):
        tess.forward(length)
        tess.right(144)
    wn.mainloop()
        
        
star(100)
