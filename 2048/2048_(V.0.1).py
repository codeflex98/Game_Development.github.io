import turtle
import random

# Constants
GRID_SIZE = 4
TILE_SIZE = 100
FONT = ("Arial", 24, "bold")
WIDTH = HEIGHT = GRID_SIZE * TILE_SIZE
START_TILES = 2

# Screen setup
screen = turtle.Screen()
screen.title("2048 with Turtle")
screen.setup(WIDTH + 200, HEIGHT + 150)
screen.bgcolor("#bbada0")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

# Game data
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
score = 0

def draw_tile(x, y, value):
    pen.goto(x + TILE_SIZE / 2, y - TILE_SIZE + 10)
    pen.fillcolor(get_color(value))
    pen.begin_fill()
    pen.setheading(0)
    pen.pendown()

    # Rounded rectangle imitation
    for _ in range(2):
        pen.forward(TILE_SIZE - 20)
        pen.circle(10, 90)
        pen.forward(TILE_SIZE - 20)
        pen.circle(10, 90)

    pen.end_fill()
    pen.penup()

    if value != 0:
        pen.goto(x + TILE_SIZE / 2 + 40, y - TILE_SIZE / 2 - 15 )
        pen.color("black" if value <= 8 else "white")
        font_size = 32 if value < 128 else 28
        pen.write(str(value), align="center", font=("Arial", font_size, "bold"))

def get_color(value):
    colors = {
        0: "#cdc1b4", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
        16: "#f59563", 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72",
        256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
    }
    return colors.get(value, "#3c3a32")

def draw_grid():
    pen.clear()
    start_x = -WIDTH / 2
    start_y = HEIGHT / 2

    # Title
    pen.goto(0, HEIGHT / 2 + 25)
    pen.color("white")
    pen.write("2048", align="center", font=("Arial", 36, "bold"))

    # Scoreboard
    pen.goto(WIDTH / 2 - 90, HEIGHT / 2 + 20)
    pen.color("white")
    pen.write(f"Score: {score}", font=("Arial", 20, "bold"))

    # Draw all tiles
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            val = grid[y][x]
            px = start_x + x * TILE_SIZE
            py = start_y - y * TILE_SIZE
            draw_tile(px, py, val)

    screen.update()

def add_random_tile():
    empty = [(y, x) for y in range(GRID_SIZE) for x in range(GRID_SIZE) if grid[y][x] == 0]
    if empty:
        y, x = random.choice(empty)
        grid[y][x] = random.choice([2] * 9 + [4])  # 90% 2, 10% 4

def compress(row):
    return [num for num in row if num != 0] + [0] * row.count(0)

def merge(row):
    global score
    for i in range(GRID_SIZE - 1):
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            score += row[i]
            row[i + 1] = 0
    return row

def move_left():
    moved = False
    for i in range(GRID_SIZE):
        original = list(grid[i])
        row = compress(grid[i])
        row = merge(row)
        row = compress(row)
        grid[i] = row
        if grid[i] != original:
            moved = True
    if moved:
        add_random_tile()
    draw_grid()
    check_game_over()

def move_right():
    moved = False
    for i in range(GRID_SIZE):
        original = list(grid[i])
        row = grid[i][::-1]
        row = compress(row)
        row = merge(row)
        row = compress(row)
        grid[i] = row[::-1]
        if grid[i] != original:
            moved = True
    if moved:
        add_random_tile()
    draw_grid()
    check_game_over()

def move_up():
    moved = False
    for col in range(GRID_SIZE):
        column = [grid[row][col] for row in range(GRID_SIZE)]
        original = list(column)
        column = compress(column)
        column = merge(column)
        column = compress(column)
        for row in range(GRID_SIZE):
            grid[row][col] = column[row]
        if column != original:
            moved = True
    if moved:
        add_random_tile()
    draw_grid()
    check_game_over()

def move_down():
    moved = False
    for col in range(GRID_SIZE):
        column = [grid[row][col] for row in range(GRID_SIZE)][::-1]
        original = list(column)
        column = compress(column)
        column = merge(column)
        column = compress(column)
        column = column[::-1]
        for row in range(GRID_SIZE):
            grid[row][col] = column[row]
        if column[::-1] != original:
            moved = True
    if moved:
        add_random_tile()
    draw_grid()
    check_game_over()
        
def check_game_over():
    for row in grid:
        if 0 in row:
            return False
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE - 1):
            if grid[y][x] == grid[y][x + 1]:
                return False
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE - 1):
            if grid[y][x] == grid[y + 1][x]:
                return False
    pen.goto(0, -HEIGHT // 2 - 40)
    pen.color("white")
    pen.write("Game Over!", align="center", font=("Arial", 30, "bold"))
    screen.update()
    return True

import turtle
import random

# Constants
GRID_SIZE = 4
TILE_SIZE = 100
FONT = ("Arial", 24, "bold")
WIDTH = HEIGHT = GRID_SIZE * TILE_SIZE
START_TILES = 2

# Screen setup
screen = turtle.Screen()
screen.title("2048 with Turtle")
screen.setup(WIDTH + 200, HEIGHT + 150)
screen.bgcolor("#bbada0")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

# Game data
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
score = 0

def draw_tile(x, y, value):
    pen.goto(x + TILE_SIZE / 2, y - TILE_SIZE + 10)
    pen.fillcolor(get_color(value))
    pen.begin_fill()
    pen.setheading(0)
    pen.pendown()

    # Rounded rectangle imitation
    for _ in range(2):
        pen.forward(TILE_SIZE - 20)
        pen.circle(10, 90)
        pen.forward(TILE_SIZE - 20)
        pen.circle(10, 90)

    pen.end_fill()
    pen.penup()

    if value != 0:
        pen.goto(x + TILE_SIZE / 2 + 40, y - TILE_SIZE / 2 - 15 )
        pen.color("black" if value <= 8 else "white")
        font_size = 32 if value < 128 else 28
        pen.write(str(value), align="center", font=("Arial", font_size, "bold"))

def get_color(value):
    colors = {
        0: "#cdc1b4", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179",
        16: "#f59563", 32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72",
        256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"
    }
    return colors.get(value, "#3c3a32")

def draw_grid():
    pen.clear()
    start_x = -WIDTH / 2
    start_y = HEIGHT / 2

    # Title
    pen.goto(0, HEIGHT / 2 + 25)
    pen.color("white")
    pen.write("2048", align="center", font=("Arial", 36, "bold"))

    # Scoreboard
    pen.goto(WIDTH / 2 - 90, HEIGHT / 2 + 20)
    pen.color("white")
    pen.write(f"Score: {score}", font=("Arial", 20, "bold"))

    # Draw all tiles
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            val = grid[y][x]
            px = start_x + x * TILE_SIZE
            py = start_y - y * TILE_SIZE
            draw_tile(px, py, val)

    screen.update()

def add_random_tile():
    empty = [(y, x) for y in range(GRID_SIZE) for x in range(GRID_SIZE) if grid[y][x] == 0]
    if empty:
        y, x = random.choice(empty)
        grid[y][x] = random.choice([2] * 9 + [4])  # 90% 2, 10% 4

def compress(row):
    return [num for num in row if num != 0] + [0] * row.count(0)

def merge(row):
    global score
    for i in range(GRID_SIZE - 1):
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            score += row[i]
            row[i + 1] = 0
    return row

def move_left():
    moved = False
    for i in range(GRID_SIZE):
        original = list(grid[i])
        row = compress(grid[i])
        row = merge(row)
        row = compress(row)
        grid[i] = row
        if grid[i] != original:
            moved = True
    if moved:
        add_random_tile()
    draw_grid()
    check_game_over()

def move_right():
    moved = False
    for i in range(GRID_SIZE):
        original = list(grid[i])
        row = grid[i][::-1]
        row = compress(row)
        row = merge(row)
        row = compress(row)
        grid[i] = row[::-1]
        if grid[i] != original:
            moved = True
    if moved:
        add_random_tile()
    draw_grid()
    check_game_over()

def move_up():
    moved = False
    for col in range(GRID_SIZE):
        column = [grid[row][col] for row in range(GRID_SIZE)]
        original = list(column)
        column = compress(column)
        column = merge(column)
        column = compress(column)
        for row in range(GRID_SIZE):
            grid[row][col] = column[row]
        if column != original:
            moved = True
    if moved:
        add_random_tile()
    draw_grid()
    check_game_over()

def move_down():
    moved = False
    for col in range(GRID_SIZE):
        column = [grid[row][col] for row in range(GRID_SIZE)][::-1]
        original = list(column)
        column = compress(column)
        column = merge(column)
        column = compress(column)
        column = column[::-1]
        for row in range(GRID_SIZE):
            grid[row][col] = column[row]
        if column[::-1] != original:
            moved = True
    if moved:
        add_random_tile()
    draw_grid()
    check_game_over()
    
def check_game_over():
    for row in grid:
        if 0 in row:
            return False
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE - 1):
            if grid[y][x] == grid[y][x + 1]:
                return False
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE - 1):
            if grid[y][x] == grid[y + 1][x]:
                return False
    pen.goto(0, -HEIGHT // 2 - 40)
    pen.color("white")
    pen.write("Game Over!", align="center", font=("Arial", 30, "bold"))
    screen.update()
    return True

def restart_game():
    global grid, score
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    score = 0
    pen.clear()  # clear "Game Over" and everything else
    for _ in range(START_TILES):
        add_random_tile()
    draw_grid()

screen.onkeypress(restart_game, "Return")  # "Return" is Enter key

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(restart_game, "Return")  # Try Enter key (often called "Return")

# Start game
for _ in range(START_TILES):
    add_random_tile()
draw_grid()

try:
    screen.mainloop()
except turtle.Terminator:
    pass  # This handles window closure without error

