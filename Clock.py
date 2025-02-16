import turtle as t

screen = t.Screen()
t.speed(0)
t.hideturtle()


def draw_clock_face():
    for i in range(1, 13):
        angle = 90 + (i * -30)
        t.setheading(angle)
        t.penup()
        t.forward(300)
        t.pendown()
        t.forward(30)
        t.penup()
        t.forward(20)
        t.pendown()
        t.write(str(i), align='center', font=('Arial', 16, 'bold'))
        t.penup()
        t.goto(0, 0)  # Go back to the center without resetting the pen position

def draw_second_hand():
    global second_angle
    second_hand.clear()  # Clear the previous second hand

    second_angle = (second_angle - 6) % 360  # Rotate by 6 degrees every second (360°/60)

    # Set the second hand's direction and draw it
    second_hand.penup()
    second_hand.goto(0, 0)
    second_hand.setheading(second_angle)
    second_hand.pendown()
    second_hand.forward(280)

    # Draw the tick mark
    second_hand.penup()
    second_hand.forward(20)
    second_hand.dot(5, "red")  # Use a red dot to mark the tick

    # Update every second
    screen.ontimer(draw_second_hand, 1000)  # Fix by passing the function reference instead of a string

# Create the second hand turtle
second_hand = t.Turtle()
second_hand.color("red")
second_hand.speed(0)
second_hand.hideturtle()
second_hand.width(2)

# Initialize the global second hand angle (starting from 12 o'clock)
second_angle = 90

# Draw the clock face and start the second hand
draw_clock_face()
draw_second_hand()

# Call t.exitonclick() to keep the window open
t.exitonclick()

