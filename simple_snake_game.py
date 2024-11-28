# Simple Snake Game for K-9 Students

import turtle
import time
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Simple Snake Game")
screen.bgcolor("lightgreen")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off animation for smoother gameplay

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)  # Start in the middle of the screen
head.direction = "stop"  # Initially, the snake is not moving

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)  # Place food at a random starting position

# Segments (the snake's body)
segments = []  # Start with no body segments

# Functions to control the snake's direction
def go_up():
    if head.direction != "down":  # Prevent reversing direction
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Function to move the snake
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings to control the snake
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Main game loop
while True:
    screen.update()

    # Check for collision with the screen borders
    if (
        head.xcor() > 290 or head.xcor() < -290
        or head.ycor() > 290 or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)  # Reset the snake's position
        head.direction = "stop"  # Stop the snake
        # Clear the body segments
        for segment in segments:
            segment.hideturtle()
        segments.clear()

    # Check if the snake eats the food
    if head.distance(food) < 20:
        # Move food to a random position
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a new body segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the body segments
    for i in range(len(segments) - 1, 0, -1):
        # Move each segment to the position of the segment ahead of it
        segments[i].goto(segments[i - 1].pos())
    if len(segments) > 0:
        # Move the first segment to the position of the head
        segments[0].goto(head.pos())

    # Move the snake's head
    move()

    # Check for collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # Clear all segments
            for segment in segments:
                segment.hideturtle()
            segments.clear()

    time.sleep(0.1)  # Control the game speed
