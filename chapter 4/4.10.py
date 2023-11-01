import turtle 

def star(length):
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")      # Set the window background color
    wn.title("Hello, Tess!")      # Set the window title

    tess = turtle.Turtle()
    tess.color("blue")            # Tell tess to change her color
    tess.pensize(5)               # Tell tess to set her pen width
    tess.speed(1)
    #to do
    for h in range(5):
        for i in range(5):
            tess.forward(length)
            tess.right(144)
        # tess.penup()
        tess.forward(350)
        tess.right(144)
        # tess.pendown()
        
        
    wn.mainloop()
        
        
star(100)
