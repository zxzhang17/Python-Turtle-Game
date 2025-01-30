import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Rainbow Runner")

# Player turtle setup
player = turtle.Turtle()
player.shape("turtle")
player.speed(0)
player.penup()
player.goto(0, 0)
player.pendown()

# List of colors for the rainbow trail
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Obstacle setup with random colors
obstacles = []
for _ in range(5):
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color(random.choice(colors))  # Assign a random color to each obstacle
    obstacle.penup()
    obstacle.goto(random.randint(-250, 250), random.randint(-250, 250))
    obstacles.append(obstacle)

# Function to randomly change the direction of the player
def random_direction():
    choice = random.choice(["left", "right", "straight", "reverse"])
    if choice == "left":
        player.left(90)  # Turn left
    elif choice == "right":
        player.right(90)  # Turn right
    elif choice == "reverse":
        player.left(180)  # Reverse direction
    # "straight" does not modify the current heading

# Function to move the player
def move():
    player.color(random.choice(colors))  # Change the pen color
    random_direction()  # Change direction randomly
    player.forward(20)  # Move forward

    # Check boundaries
    if player.xcor() > 290 or player.xcor() < -290 or player.ycor() > 290 or player.ycor() < -290:
        player.penup()
        player.goto(0, 0)  # Reset to center
        player.pendown()

    # Check collision with obstacles
    for obstacle in obstacles:
        if player.distance(obstacle) < 20:  # Collision detected
            player.penup()
            player.goto(0, 0)  # Reset to center
            player.pendown()

# Main game loop
while True:
    move()

turtle.done()
