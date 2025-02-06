import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Turtle Food Hunt")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Turtle setup
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(2)

# Food setup
foods = []
for _ in range(50):  # Create 5 food items
    food = turtle.Turtle()
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(random.randint(-250, 250), random.randint(-250, 250))
    foods.append(food)

# Initialize step length and angle for the star pattern
step_length = 20
angle = 144  # Angle for star movement pattern

# Function to move the turtle in an increasing star pattern
def move():
    global step_length
    player.forward(step_length)
    player.right(angle)
    step_length += 20  # Gradually increase the step length for the star effect

# Check collision
def check_collision():
    for food in foods:
        if player.distance(food) < 20:  # Collision radius
            food.hideturtle()
            foods.remove(food)

# Main game loop
while True:
    move()
    check_collision()
    # Boundaries check: reset position if it hits the wall
    if player.xcor() > 290 or player.xcor() < -290 or player.ycor() > 290 or player.ycor() < -290:
        player.goto(0, 0)  # Reset position to the center
        step_length = 10  # Reset step length

turtle.done()
