import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("🐍 Snake Game")
wn.bgcolor("#aad751")  # Lighter green background
wn.setup(width=600, height=600)
wn.tracer(0)

# Draw play area border
border = turtle.Turtle()
border.speed(0)
border.color("darkgreen")
border.pensize(3)
border.penup()
border.goto(-300, 300)
border.pendown()
for _ in range(4):
    border.forward(600)
    border.right(90)
border.hideturtle()

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#2f4f4f")  # Dark slate gray
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("tomato")
food.penup()
food.goto(0, 100)

segments = []

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 24, "bold"))

# Movement functions
def go_up():
    if head.direction != "down":
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

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# ✅ MAIN GAME LOOP with error handling
try:
    while True:
        wn.update()

        # Border collision
        if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "bold"))

        # Food collision
        if head.distance(food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.goto(x, y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            color = "#556b2f" if len(segments) % 2 == 0 else "#6b8e23"
            new_segment.color(color)
            new_segment.penup()
            segments.append(new_segment)

            delay -= 0.001
            score += 10
            if score > high_score:
                high_score = score

            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "bold"))

        # Move the segments
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        if segments:
            segments[0].goto(head.xcor(), head.ycor())

        move()

        # Collision with self
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(0.5)
                head.goto(0, 0)
                head.direction = "stop"
                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()
                score = 0
                delay = 0.1
                pen.clear()
                pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "bold"))

        time.sleep(delay)

except turtle.Terminator:
    print("Game window closed. Exiting gracefully.")
