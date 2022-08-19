'''The Game Loop
(1) Clear the existing snake from the screen.
(2) Draw the snake in its new position.
(3) Check for collisions with walls, self, or food, and handle appropriately.'''

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
DELAY = 200      # The number of miliseconds between screen updates. 

# Python dictionary containing offsets determine determine how much the snake moves in each direction. 
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0) 
}

# Global variable for snake direction. 
def go_up():
    global snake_direction
    if snake_direction != "down":
        snake_direction = "up"

def go_down():
    global snake_direction
    if snake_direction != "up":
        snake_direction = "down"

def go_left():
    global snake_direction
    if snake_direction != "right":
        snake_direction = "left"

def go_right():
    global snake_direction
    if snake_direction != "left":
        snake_direction = "right"      

# Define animation with functions.
def game_loop():
    stamper.clearstamps() # Removes existing stamps made by stamper.
    
    # Copy Head by creating a new list item for the new head:
    new_head = snake[-1].copy()                          # 'snake[-1]' means the rightmost item. It must be copied or the original would be modified by the next step. 
    new_head[0] += offsets[snake_direction][0]           # Increment the x coordinate of new_head using new_head[0] = offsets of the snake direction. 
    new_head[1] += offsets[snake_direction][1]           # Y coordinate 
    
    # Check snake-to-snake and snake-to-wall collisions:
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
        or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT /2: 
        turtle.bye() # Closes Turtle Graphics program. 
    else: 
        # Add new head to snake body:
        snake.append(new_head)
        
        # Remove last segment of snake:
        snake.pop(0)
        
        # Draw snake for the first time using a 'for loop': 
        for segment in snake:
            stamper.goto(segment[0], segment[1]) # X, Y
            stamper.stamp()
        
        # Refresh screen
        screen.update()
        
        # Rinse and repeat
        turtle.ontimer(game_loop, DELAY)
    
# Create a window where we will do our drawing. It's good to have reference to screen objects. 
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)                  # Set the dimmensions of the Turtle Graphics window. 
screen.title("Snake")                        # Program Title.
screen.bgpic("SnakeGame_bgJungle.png")       # Set background image.
screen.tracer(0)                             # Turn off automatic animation. 

# Event handlers for event loop where key presses change the direction of the snake. 
screen.listen() 
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

# Create a turtle object to do your bidding. 
stamper = turtle.Turtle()     # module.class_within_module which represents a turtle object. 
stamper.shape("square")       # property = shape of object.
stamper.color("#172915")      # property = color of object = Phthalo Green. 
stamper.penup()               # pen does not stamp as it moves. 

# Create Snake Representation shown as a 2D list of pairs of x, y coordinates. The segments of the snake are currently all lying horizontally, with y coordinates of 0.
snake = [[0, 0], [20, 0], [40, 0], [60, 0]] # Tail -----segments of snake-----> Head
snake_direction = "up"                      # Global variable 


# Draw snake for the first time using a 'for loop': 
for segment in snake:
    stamper.goto(segment[0], segment[1]) # X, Y
    stamper.stamp()

# Your turtle awaits your command(s). Set animation in motion. Sample command: myturtle.forward(100).
game_loop()

# Finish.
turtle.done() 