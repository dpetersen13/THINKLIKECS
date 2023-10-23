import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")      # Set the window background color
wn.title("Hello, Tess!")      # Set the window title

tess = turtle.Turtle()
tess.color("blue")            # Tell tess to change her color
tess.pensize(2)               # Tell tess to set her pen width
# tess.speed(1)
#to do 
length=10
for i in range(50):
    
        tess.forward(length)    
        tess.right(89)
        length+=5

     

    
    
    
    # tess.forward(50)
# tess.forward(50)

wn.mainloop()