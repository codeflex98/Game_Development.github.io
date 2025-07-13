import turtle
import random

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = -0.6
JUMP_STRENGTH = 12
PLATFORM_COUNT = 12
PLAYER_WIDTH = 20
MIN_PLATFORM_SPACING = 70
MAX_PLATFORM_SPACING = 90
MAX_HORIZONTAL_GAP = 120
MOVE_SPEED = 5

# State
loop_scheduled = False
score = 0
high_score = 0
powerups = []
scored_platforms = set()
last_speed_update = 0

# Screen setup
screen = turtle.Screen()
screen.title("Doodle Jump")
screen.bgcolor("seashell")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.tracer(0)

# Player
player = turtle.Turtle()
player.shape("circle")
player.color("black", "yellow")  # black border, yellow fill
player.shapesize(stretch_wid=1.2, stretch_len=1.2)
player.penup()
player.goto(0, -250)
player.dy = 0

# Text
message = turtle.Turtle()
message.hideturtle()
message.penup()
message.color("red")

score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("black")
score_display.goto(-SCREEN_WIDTH//2 + 20, SCREEN_HEIGHT//2 - 40)

instruction_display = turtle.Turtle()
instruction_display.hideturtle()
instruction_display.penup()
instruction_display.color("blue")
instruction_display.goto(0, SCREEN_HEIGHT//2 - 60)

# Platform class
class Platform(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=3)
        self.penup()
        self.goto(x, y)
        self.speed_x = random.choice([-1, 1]) * random.uniform(0.5, 1.5)
        self.is_disappearing = False
        self.assign_type()

    def assign_type(self):
        self.showturtle()
        self.is_disappearing = False
        if random.random() < 0.2:
            self.color("red")
            self.is_disappearing = True
        else:
            self.color("lime")

    def disappear(self):
        self.hideturtle()
        self.goto(0, -1000)

# Power-up class
class PowerUp(turtle.Turtle):
    def __init__(self, x, y, kind):
        super().__init__()
        self.kind = kind
        self.penup()
        self.shape("circle")
        self.shapesize(0.7)
        self.goto(x, y)
        if kind == "jump":
            self.color("blue")
        elif kind == "score":
            self.color("yellow")

# Generate initial platforms
platforms = []
start_y = -SCREEN_HEIGHT // 2 + 20
current_y = start_y
last_x = 0
for _ in range(PLATFORM_COUNT):
    x_offset = random.randint(-MAX_HORIZONTAL_GAP, MAX_HORIZONTAL_GAP)
    x = max(-180, min(180, last_x + x_offset))
    p = Platform(x, current_y)
    platforms.append(p)
    current_y += random.randint(MIN_PLATFORM_SPACING, MAX_PLATFORM_SPACING)
    last_x = x

player.setx(platforms[0].xcor())
player.sety(platforms[0].ycor() + 20)

# Movement
moving_left = False
moving_right = False
game_over = False

# Controls
def start_move_left():
    global moving_left
    moving_left = True

def stop_move_left():
    global moving_left
    moving_left = False

def start_move_right():
    global moving_right
    moving_right = True

def stop_move_right():
    global moving_right
    moving_right = False

screen.listen()
screen.onkeypress(start_move_left, "Left")
screen.onkeyrelease(stop_move_left, "Left")
screen.onkeypress(start_move_right, "Right")
screen.onkeyrelease(stop_move_right, "Right")

# UI
def show_game_over():
    message.goto(0, 0)
    message.clear()
    message.write("GAME OVER\nPress R to Restart", align="center", font=("Arial", 24, "bold"))

def show_speed_up():
    message.goto(0, 100)
    message.clear()
    message.write("Speed Up!", align="center", font=("Arial", 20, "bold"))
    screen.ontimer(message.clear, 1000)

def update_instruction():
    instruction_display.clear()
    if score >= 50:
        instruction_display.write("Press SPACE for Power Jump", align="center", font=("Arial", 14, "bold"))

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}   High Score: {high_score}", font=("Arial", 16, "bold"))
    update_instruction()

# Reset game
def reset_game():
    global game_over, score, powerups, last_speed_update
    message.clear()
    game_over = False
    score = 0
    last_speed_update = 0
    update_score()
    update_instruction()
    player.goto(0, -250)
    player.dy = 0
    scored_platforms.clear()

    current_y = start_y
    last_x = 0
    for plat in platforms:
        while True:
            x_offset = random.randint(-MAX_HORIZONTAL_GAP, MAX_HORIZONTAL_GAP)
            x = max(-180, min(180, last_x + x_offset))
            if abs(x - last_x) >= 30:
                break
        plat.goto(x, current_y)
        plat.speed_x = random.choice([-1, 1]) * random.uniform(0.5, 1.5)
        plat.assign_type()
        current_y += random.randint(MIN_PLATFORM_SPACING, MAX_PLATFORM_SPACING)
        last_x = x

    for p in powerups:
        p.hideturtle()
    powerups.clear()

    player.setx(platforms[0].xcor())
    player.sety(platforms[0].ycor() + 20)

screen.onkeypress(reset_game, "r")

def perform_super_jump():
    global score
    if score >= 50:
        score -= 50
        update_score()
        player.dy = 15
        original_fill = player.fillcolor()
        player.fillcolor("orange")
        screen.ontimer(lambda: player.fillcolor(original_fill), 300)

screen.onkeypress(perform_super_jump, "space")

# Main game loop
def game_loop():
    global platforms, game_over, loop_scheduled, score, last_speed_update, high_score

    if not game_over:
        if moving_left:
            x = player.xcor() - MOVE_SPEED
            player.setx(max(-SCREEN_WIDTH // 2 + PLAYER_WIDTH, x))
        if moving_right:
            x = player.xcor() + MOVE_SPEED
            player.setx(min(SCREEN_WIDTH // 2 - PLAYER_WIDTH, x))

        player.dy += GRAVITY
        player.sety(player.ycor() + player.dy)

        for plat in platforms:
            new_x = plat.xcor() + plat.speed_x
            if new_x < -SCREEN_WIDTH // 2 + 40 or new_x > SCREEN_WIDTH // 2 - 40:
                plat.speed_x *= -1
                new_x = plat.xcor() + plat.speed_x
            plat.setx(new_x)

        # Accurate bounce detection
        player_bottom = player.ycor() - (12 * player.shapesize()[0])
        player_top = player.ycor() + (12 * player.shapesize()[0])
        player_left = player.xcor() - (10 * player.shapesize()[1])
        player_right = player.xcor() + (10 * player.shapesize()[1])

        for plat in platforms:
            plat_top = plat.ycor() + 5
            plat_bottom = plat.ycor() - 5
            plat_left = plat.xcor() - 30
            plat_right = plat.xcor() + 30

            if player.dy < 0 and \
               player_bottom <= plat_top and \
               player_top >= plat_bottom and \
               player_right >= plat_left and \
               player_left <= plat_right:

                player.sety(plat_top + (12 * player.shapesize()[0]))
                player.dy = JUMP_STRENGTH

                if plat not in scored_platforms:
                    score += 10
                    update_score()
                    scored_platforms.add(plat)

                    if plat.is_disappearing:
                        screen.ontimer(plat.disappear, 300)

        for p in powerups[:]:
            if player.distance(p) < 20:
                if p.kind == "jump":
                    player.dy += 20
                elif p.kind == "score":
                    score += 50
                    update_score()
                p.hideturtle()
                powerups.remove(p)

        if score - last_speed_update >= 100:
            speed_multiplier = 1 + (score // 100) * 0.2
            for plat in platforms:
                direction = 1 if plat.speed_x > 0 else -1
                plat.speed_x = direction * random.uniform(0.5, 1.5) * speed_multiplier
            last_speed_update = score
            show_speed_up()

        if player.ycor() > 100:
            offset = player.ycor() - 100
            player.sety(100)
            for plat in platforms:
                plat.sety(plat.ycor() - offset)
                if plat.ycor() < -SCREEN_HEIGHT // 2:
                    base_y = max(p.ycor() for p in platforms)
                    last_x = platforms[-1].xcor()
                    while True:
                        direction = random.choice([-1, 1])
                        horizontal_shift = random.randint(30, MAX_HORIZONTAL_GAP) * direction
                        new_x = player.xcor() + horizontal_shift
                        new_x = max(-SCREEN_WIDTH // 2 + 40, min(SCREEN_WIDTH // 2 - 40, new_x))
                        if abs(new_x - last_x) >= 30:
                            break
                    new_y = base_y + random.randint(MIN_PLATFORM_SPACING, MAX_PLATFORM_SPACING)
                    plat.goto(new_x, new_y)
                    plat.speed_x = random.choice([-1, 1]) * random.uniform(0.5, 1.5)
                    plat.assign_type()
                    scored_platforms.discard(plat)

                    if random.random() < 0.3:
                        kind = random.choice(["jump", "score"])
                        p = PowerUp(new_x, new_y + 10, kind)
                        powerups.append(p)

        if player.ycor() < -SCREEN_HEIGHT // 2:
            if score > high_score:
                high_score = score
            show_game_over()
            game_over = True

    screen.update()

    if not loop_scheduled:
        globals()["loop_scheduled"] = True
        screen.ontimer(game_loop, 20)
        globals()["loop_scheduled"] = False

# Start loop
game_loop()
screen.mainloop()