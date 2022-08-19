''' Color Palette 
(1) #172915 = Phthalo Green
(2) #F18F01 = Carrot Orange
'''

# Import Turtle Graphics and random module mopdule.
import turtle
import random

# Define program constants.
WIDTH = 755     # Width of window.
HEIGHT = 500    # Height of window. 
DELAY = 100     # The number of miliseconds between screen updates. 
FOOD_SIZE = 10  # Food size is 10 pixels.

'''~~~~~~~~~~~~ SNAKE CONTROLS ~~~~~~~~~~~~'''
offsets = { # Python dictionary containing offsets determine how much the snake moves in each direction. 
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0) 
}

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "w")
    screen.onkey(lambda: set_snake_direction("down"), "s")
    screen.onkey(lambda: set_snake_direction("left"), "a")
    screen.onkey(lambda: set_snake_direction("right"), "d")

def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down": # No self-collision simply by pressing the wrong key. 
            snake_direction = "up"
    elif direction == "down":
        if snake_direction != "up": # No self-collision simply by pressing the wrong key. 
            snake_direction = "down"
    elif direction == "left":
        if snake_direction != "right": # No self-collision simply by pressing the wrong key. 
            snake_direction = "left"
    elif direction == "right":
        if snake_direction != "left": # No self-collision simply by pressing the wrong key. 
            snake_direction = "right"

# Define game_loop animation function.
def game_loop():
    global snake_direction
    
    stamper.clearstamps() # Removes existing stamps made by stamper.
    
    # Copy Head by creating a new list item for the new head:
    new_head = snake[-1].copy()                          # 'snake[-1]' means the rightmost item. It must be copied or the original would be modified by the next step. 
    new_head[0] += offsets[snake_direction][0]           # Increment the x coordinate of new_head using new_head[0] = offsets of the snake direction. 
    new_head[1] += offsets[snake_direction][1]           # Y coordinate 
    
    # Check snake-to-snake and snake-to-wall collisions:
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
            or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset() # Closes Turtle Graphics program. 
    else: 
        # No collision so we can continue moving the snake. 
        snake.append(new_head)
        
        # Check food collision:
        if not food_collision():
            snake.pop(0) # Keep the snake the same length unless fed. 
        
        # Draw snake for the first time using a 'for loop': 
        for segment in snake:
            stamper.goto(segment[0], segment[1]) # X, Y
            stamper.stamp()
        
        # Refresh screen
        screen.title(f"Snake Game. Score: {score}")
        screen.update()
        
        # Rinse and repeat
        turtle.ontimer(game_loop, DELAY)

# Check snake-to-food collisions.
def food_collision():
    global food_pos, score 
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True 
    return False    
        
# Create function to generate random position of food. 
def get_random_food_pos():
    x = random.uniform(- WIDTH / 2 + FOOD_SIZE, WIDTH / 2 - FOOD_SIZE)
    y = random.uniform(- HEIGHT / 2 + FOOD_SIZE, HEIGHT / 2 - FOOD_SIZE)
    return (x, y)

# Pythagoras' Theorem to find distance between two points.     
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5 
    return distance
    
# Create reset function 
def reset():
    global score, snake, snake_direction, food_pos
    score = 0
     # Snake Representation shown as a 2D list of pairs of x, y coordinates. The segments of the snake are currently all lying horizontally, with y coordinates of 0.
    snake = [[0,0], [0, 20], [0, 40], [0, 60], [0, 80]] # Tail -----segments of snake-----> Head
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos) # tuple - if no second argument provided this is treated as an x, y pair. 
    game_loop()
    
'''~~~~~~~~~~~~ GAME OBJECTS ~~~~~~~~~~~~'''
# Create a window where we will do our drawing. It's good to have reference to screen objects. 
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)                  # Set the dimmensions of the Turtle Graphics window. 
screen.title("Snake Game")                   # Program Title.
screen.bgpic("SnakeGame_bgJungle.png")       # Set background image.
screen.tracer(0) 

# Create a turtle object to do your bidding. # This Turtle is defined at the global level, so is available to move_snake().
stamper = turtle.Turtle(shape = "square")       # module.class_within_module which represents a turtle object. 
stamper.color("#172915")                        # property = color of object = Phthalo Green. 
stamper.penup()                                 # pen does not stamp as it moves. 
                
# Food
food = turtle.Turtle()
food.shape("circle")
food.color("#F18F01") # Food is Carrot Orange
food.shapesize(FOOD_SIZE / 20)
food.penup()

'''~~~~~~~~~~~~ GAME EVENTS / CALLBACKS ~~~~~~~~~~~~'''
# Event handlers for event loop where key presses change the direction of the snake. 
screen.listen() 
bind_direction_keys()

# Your turtle awaits your command(s). Set animation in motion. 
reset()

# Finish.
turtle.done() 