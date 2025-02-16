import turtle 
import random

# Create a turtle object
t = turtle.Turtle()
t.speed(9)
5
# Function to draw a star shape
def stars(edges, distance, t_color, x, y):
    t.penup()
    t.goto(x, y)  # Move to the specified position
    t.pendown()

    angle = 180 - (180 / edges)  # Calculate the turning angle for drawing the star
    t.color(t_color)

    t.begin_fill()  # Start filling
    for _ in range(edges):
        t.forward(distance)  # Draw a side forward
        t.right(angle)       # Turn by the angle
    t.end_fill()  # End filling

# Set the screen background color
turtle.Screen().bgcolor('blue')

color_list = ['red', 'orange', 'yellow', 'green', 'purple']

t.hideturtle()

while True: 
    # Call the function to draw a fully filled star
    t_color = random.choice(color_list)
    edges = random.randint(2, 5) * 2 + 2
    distance = random.randint(5, 30)
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    stars(edges, distance, t_color, x, y)

# Click to close the screen
turtle.Screen().exitonclick()
