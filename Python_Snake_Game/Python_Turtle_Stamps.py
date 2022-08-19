''' Color Palette 
(1) #222E50 = Space Cadet
(2) #172915 = Phthalo Green
(3) #8DAA9D = Morning Blue
(4) #7B0828 = Claret
(5) #F18F01 = Carrot Orange
'''

# Import Turtle Graphics mopdule.
import turtle

# Define program constants.
WIDTH = 755     # Width of window.
HEIGHT = 500    # Height of window. 
DELAY = 20      # The number of miliseconds between screen updates. 

# Define animation with functions.
    
# Create a window where we will do our drawing. It's good to have reference to screen objects. 
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)                     # Set the dimmensions of the Turtle Graphics window. 
screen.title("Stamping")                        # Program Title.
screen.bgpic("SnakeGame_bgJungle.png")          # Set background image.

# Create a turtle object to do your bidding. 
stamper = turtle.Turtle()     # module.class_within_module which represents a turtle object. 
stamper.shape("square")       # property = shape of object.
stamper.color("#172915")      # property = color of object = Phthalo Green. 
stamper.shapesize(50 / 20)    # property = shape size of object. 20 is default size of a square in Turtle Graphics. Our stamp is 50 pixels.  
stamper.stamp()               # property = the current location of the stamper will make a stamp. 
stamper.penup()               # penup = stamper does not make a mark while moving. 
stamper.shapesize(10 / 20)    # reduces size of stamp. 
stamper.goto(100, 100)
stamper.stamp()

# Your turtle awaits your command(s). Set animation in motion. Sample command: myturtle.forward(100).

# Finish.
turtle.done() 


