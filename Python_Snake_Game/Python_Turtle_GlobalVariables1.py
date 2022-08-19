# Global variables exist outside of any functions in a program, but can be used inside particular functions if required. 
# Variables inside functions are local. They only exist inside the function and are destroyed once the function call is complete. 
# If you use the global version of the variable inside the function, the value of variable outside of the function will be modified/updated. 
# If a function only needs to read a global variable, there is no need to use the global keyword to make it available to the function. 
# If global variable is going to be modified/updated within the function, the global keyword is needed. 
# The Snake Game makes use of several global variables for simplicity. 

name = "Turtle"         # Global variable is assigned. 
print(name)             # Global variable is called. 

def print_name():       # Local variable is defined as a function. 
    global name         # Global variable is updated within the function, so the value of the variable 'Snake' is recognized outside of the function.
    name = "Snake"
    print(name)
    
print_name()
print(name)

# Expect to see = Turtle, Snake, Snake. 