# Import Turtle Graphics mopdule.
import turtle

# Define program constants.
WIDTH = 500     # Width of window.
HEIGHT = 500    # Height of window. 
DELAY = 20      # The number of miliseconds between screen updates. 

# Define animation with functions.
def move_turtle():                      # Defined global varable: my_turtle 
    my_turtle.forward(1)                # Turtle moves forward 1 pixel.
    my_turtle.right(1)                  # Turtle is rotated 1 degree. 
    screen.update()                     # Screen is updated. 
    screen.ontimer(move_turtle, DELAY)  # After 'DELAY' milliseconds, call move_turtle() again. 
    
# Create a window where we will do our drawing. It's good to have reference to screen objects. 
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)         # Set the dimmensions of the Turtle Graphics window. 
screen.title("Turtle Animation")    # Program Title
screen.bgcolor("cyan")              # Window's background color. 
screen.tracer(0)                    # Turns off automatic animation to manually control the animation. 

# Create a turtle object to do your bidding. 
my_turtle = turtle.Turtle()     # module.class_within_module which represents a turtle object. 
my_turtle.shape("turtle")       # property = shape of object.
my_turtle.color("red")          # property = color of object. 


# Your turtle awaits your command(s). Set animation in motion. Sample command: myturtle.forward(100).
move_turtle()  

# Finish.
turtle.done() 
