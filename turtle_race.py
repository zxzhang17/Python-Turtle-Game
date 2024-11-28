import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Race")
screen.bgcolor("white")

# Draw the start and finish lines
line_drawer = turtle.Turtle()
line_drawer.hideturtle()
line_drawer.speed(0)

# Draw the start line
line_drawer.penup()
line_drawer.goto(-120, 150)
line_drawer.pendown()
line_drawer.right(90)
line_drawer.forward(300)

# Draw the finish line
line_drawer.penup()
line_drawer.goto(200, 150)
line_drawer.pendown()
line_drawer.forward(300)

# Create turtles
colors = ["red", "blue", "green", "yellow"]
turtles = []

start_x = -100
start_y = 100

for color in colors:
    racer = turtle.Turtle()
    racer.color(color)
    racer.shape("turtle")
    racer.penup()
    racer.goto(start_x, start_y)
    start_y -= 50
    turtles.append(racer)

# Start the race
finish_line = 200

while True:
    for racer in turtles:
        racer.forward(random.randint(1, 5))
        if racer.xcor() >= finish_line:
            print(f"The {racer.color()[0]} turtle wins!")
            screen.bye()
            break
    else:
        continue
    break
