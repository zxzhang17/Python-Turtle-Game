import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightgray")
screen.title("Car Dodge Game")
screen.setup(width=800, height=600)

# Draw a road
road = turtle.Turtle()
road.speed(0)
road.color("black")
road.penup()
road.goto(-250, -300)
road.pendown()
road.begin_fill()
for _ in range(2):
    road.forward(500)
    road.left(90)
    road.forward(600)
    road.left(90)
road.end_fill()
road.hideturtle()

# Create the player's car
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.shapesize(stretch_wid=1, stretch_len=2)
player.penup()
player.goto(0, -250)

# Create obstacles
obstacles = []
for _ in range(6):
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("red")
    obstacle.shapesize(stretch_wid=1, stretch_len=2)
    obstacle.penup()
    obstacle.goto(random.randint(-200, 200), random.randint(100, 400))
    obstacles.append(obstacle)

# Move the car left and right
def move_left():
    x = player.xcor()
    x -= 20
    if x < -230:  # Stay within the road
        x = -230
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    if x > 230:  # Stay within the road
        x = 230
    player.setx(x)

# Bind keyboard controls
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Move obstacles
def move_obstacles():
    for obstacle in obstacles:
        obstacle.sety(obstacle.ycor() - random.randint(10, 20))
        if obstacle.ycor() < -300:
            obstacle.goto(random.randint(-200, 200), random.randint(300, 400))

# Check for collisions
def check_collision():
    for obstacle in obstacles:
        if player.distance(obstacle) < 20:
            return True
    return False

# Game loop
running = True
while running:
    screen.update()
    move_obstacles()
    if check_collision():
        running = False
        break
    time.sleep(0.05)

# Display "Game Over" message
game_over = turtle.Turtle()
game_over.hideturtle()
game_over.penup()
game_over.goto(0, 0)
game_over.color("black")
game_over.write(
    "Game Over!",
    align="center",
    font=("Arial", 24, "bold")
)

time.sleep(3)
screen.bye()
