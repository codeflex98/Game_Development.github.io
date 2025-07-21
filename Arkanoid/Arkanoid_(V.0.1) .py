import turtle
import time
import random
from math import sqrt

# Screen setup
screen = turtle.Screen()
screen.title("Aranoid - Enhanced Edition")
screen.bgcolor("#111122")
screen.setup(width=800, height=600)
screen.tracer(0)

# Graceful window close handler
def on_close():
    global running
    running = False
    try:
        screen.bye()
    except:
        pass

screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", on_close)

# Globals
bricks = []
balls = []
powerups = []
score = 0
running = True

# Paddle and shadow
shadow = turtle.Turtle()
shadow.shape("square")
shadow.color("#222222")
shadow.shapesize(stretch_wid=1, stretch_len=6)
shadow.penup()

paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()

# Score display
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)

# Message display
message = turtle.Turtle()
message.color("yellow")
message.penup()
message.hideturtle()
message.goto(0, 0)

# Movement flags
move_left = False
move_right = False

# Power-up effect tracking
big_ball_end_time = 0

# Ball creation function with glow
def create_ball(x, y, dx=6, dy=6, size=1.0):
    glow = turtle.Turtle()
    glow.shape("circle")
    glow.color("red")
    glow.penup()
    glow.goto(x, y)
    glow.shapesize(size * 1.8)
    glow.speed(0)
    glow.hideturtle()

    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.speed(0)
    ball.goto(x, y)
    ball.shapesize(size)
    ball.dx = dx
    ball.dy = dy
    ball.glow = glow
    return ball

# Power-up creation (rotating triangle)
def create_powerup(x, y, kind):
    pu = turtle.Turtle()
    pu.shape("triangle")
    pu.color("cyan" if kind == "multi" else "orange")
    pu.penup()
    pu.goto(x, y)
    pu.kind = kind
    pu.tiltangle(0)
    powerups.append(pu)

# Setup game state
def setup_game():
    global bricks, balls, score, running, powerups, big_ball_end_time
    score = 0
    running = True
    big_ball_end_time = 0

    paddle.goto(0, -250)
    shadow.goto(3, -253)
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
    message.clear()

    for pu in powerups:
        pu.hideturtle()
    powerups.clear()

    for b in bricks:
        b.hideturtle()
    bricks.clear()

    for b in balls:
        b.hideturtle()
        if hasattr(b, "glow"):
            b.glow.hideturtle()
    balls.clear()

    balls.append(create_ball(0, -100))

    for y in range(250, 150, -30):
        for x in range(-350, 350, 70):
            brick = turtle.Turtle()
            brick.shape("square")
            brick.shapesize(stretch_wid=1, stretch_len=3)
            brick.penup()
            brick.goto(x, y)

            if random.random() < 0.2:
                brick.has_powerup = True
                brick.powerup_type = random.choice(["multi", "big"])
                brick.color("cyan" if brick.powerup_type == "multi" else "orange")
            else:
                brick.has_powerup = False
                brick.powerup_type = None
                brick.color("lightgray")

            bricks.append(brick)

# Movement controls
def start_left():
    global move_left
    move_left = True

def stop_left():
    global move_left
    move_left = False

def start_right():
    global move_right
    move_right = True

def stop_right():
    global move_right
    move_right = False

def restart_game():
    global running
    if not running:
        setup_game()

screen.listen()
screen.onkeypress(start_left, "Left")
screen.onkeyrelease(stop_left, "Left")
screen.onkeypress(start_right, "Right")
screen.onkeyrelease(stop_right, "Right")
screen.onkey(restart_game, "Return")

setup_game()

try:
    while True:
        screen.update()
        time.sleep(0.02)

        if not running:
            continue

        if move_left and paddle.xcor() > -340:
            paddle.setx(paddle.xcor() - 10)
            shadow.setx(paddle.xcor() + 3)
        if move_right and paddle.xcor() < 340:
            paddle.setx(paddle.xcor() + 10)
            shadow.setx(paddle.xcor() + 3)

        for pu in powerups[:]:
            pu.sety(pu.ycor() - 5)
            pu.settiltangle((pu.tiltangle() + 15) % 360)
            if pu.ycor() < -280:
                pu.hideturtle()
                powerups.remove(pu)
            elif pu.distance(paddle) < 50:
                if pu.kind == "multi" and len(balls) < 3:
                    b = balls[0]
                    balls.append(create_ball(b.xcor(), b.ycor(), -b.dx, b.dy))
                elif pu.kind == "big":
                    for b in balls:
                        b.shapesize(2.0, 2.0)
                        b.glow.shapesize(3.5)
                    big_ball_end_time = time.time() + 10
                pu.hideturtle()
                powerups.remove(pu)

        if big_ball_end_time and time.time() > big_ball_end_time:
            for b in balls:
                b.shapesize(1.0, 1.0)
                b.glow.shapesize(1.8)
            big_ball_end_time = 0

        for ball in balls[:]:
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)
            ball.glow.goto(ball.xcor(), ball.ycor())

            if ball.xcor() > 390 or ball.xcor() < -390:
                ball.dx *= -1
            if ball.ycor() > 290:
                ball.dy *= -1
            if ball.ycor() < -290:
                balls.remove(ball)
                ball.hideturtle()
                ball.glow.hideturtle()
                if not balls:
                    message.write("Game Over!\nRestart by pressing Enter", align="center", font=("Courier", 24, "bold"))
                    running = False

            if -260 < ball.ycor() < -230 and abs(ball.xcor() - paddle.xcor()) < 70:
                offset = ball.xcor() - paddle.xcor()
                ball.sety(-230)
                speed = sqrt(ball.dx ** 2 + ball.dy ** 2)
                normalized_offset = max(-0.9, min(0.9, offset / 60))
                ball.dx = speed * normalized_offset
                min_dy = speed * 0.4
                ball.dy = sqrt(max(min_dy ** 2, speed ** 2 - ball.dx ** 2))

            for brick in bricks:
                if brick.distance(ball) < 35:
                    bx, by = brick.xcor(), brick.ycor()
                    bw, bh = 60, 20
                    if abs(ball.xcor() - bx) < bw and abs(ball.ycor() - by) > bh:
                        ball.dy *= -1
                    elif abs(ball.ycor() - by) < bh and abs(ball.xcor() - bx) > bw:
                        ball.dx *= -1
                    else:
                        ball.dy *= -1

                    if brick.has_powerup:
                        create_powerup(brick.xcor(), brick.ycor(), brick.powerup_type)

                    brick.goto(1000, 1000)
                    brick.hideturtle()
                    bricks.remove(brick)

                    score += 10
                    score_display.clear()
                    score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

                    speed_multiplier = 1.01
                    max_speed = 12
                    if abs(ball.dx) < max_speed:
                        ball.dx *= speed_multiplier
                    if abs(ball.dy) < max_speed:
                        ball.dy *= speed_multiplier
                    break

        if not bricks:
            message.clear()
            message.write("You Win!\nRestart by pressing Enter", align="center", font=("Courier", 24, "bold"))
            running = False
except turtle.Terminator:
    print("Game window closed.")
