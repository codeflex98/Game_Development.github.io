import turtle
import random

# Constants
GRID_SIZE = 30
COLS = 10
ROWS = 20
WIDTH = COLS * GRID_SIZE
HEIGHT = ROWS * GRID_SIZE
FRAME_DELAY = int(1000 / 60)  # 60 FPS

# Tetromino Shapes
SHAPES = {
    'O': [(0, 0), (1, 0), (0, 1), (1, 1)],
    'I': [(0, 1), (1, 1), (2, 1), (3, 1)],
    'S': [(1, 0), (2, 0), (0, 1), (1, 1)],
    'Z': [(0, 0), (1, 0), (1, 1), (2, 1)],
    'L': [(0, 0), (0, 1), (0, 2), (1, 2)],
    'J': [(1, 0), (1, 1), (1, 2), (0, 2)],
    'T': [(0, 1), (1, 1), (2, 1), (1, 2)],
}

COLORS = {
    'O': 'yellow',
    'I': 'cyan',
    'S': 'lime green',
    'Z': 'red',
    'L': 'orange',
    'J': 'blue',
    'T': 'purple'
}

# Setup screen
screen = turtle.Screen()
screen.setup(WIDTH + 200, HEIGHT + 100)
screen.title("Tetris Game")
screen.bgcolor("black")
screen.tracer(0)

# Drawing Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

# Score
score = 0
high_score = 0

score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.color("white")

# Grid Data
grid = [[None for _ in range(COLS)] for _ in range(ROWS)]

def draw_square(x, y, color):
    pen.goto(-WIDTH // 2 + x * GRID_SIZE, HEIGHT // 2 - y * GRID_SIZE - GRID_SIZE)
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.pendown()
        pen.forward(GRID_SIZE)
        pen.right(90)
    pen.end_fill()
    pen.penup()

def draw_grid():
    pen.clear()
    # Grid tiles
    for y in range(ROWS):
        for x in range(COLS):
            if grid[y][x]:
                draw_square(x, y, grid[y][x])
    # Grid border
    pen.color("white")
    pen.pensize(2)
    pen.goto(-WIDTH // 2, HEIGHT // 2.25)
    pen.setheading(0)
    pen.pendown()
    for _ in range(2):
        pen.forward(WIDTH)
        pen.right(90)
        pen.forward(HEIGHT)
        pen.right(90)
    pen.penup()

class Tetromino:
    def __init__(self):
        self.shape = random.choice(list(SHAPES.keys()))
        self.blocks = SHAPES[self.shape][:]
        self.color = COLORS[self.shape]
        self.x = COLS // 2 - 2
        self.y = 0
        self.counter = 0

    def draw(self):
        for dx, dy in self.blocks:
            draw_square(self.x + dx, self.y + dy, self.color)

    def move(self, dx, dy):
        if not self.collides(dx, dy, self.blocks):
            self.x += dx
            self.y += dy
            return True
        return False

    def rotate(self):
        rotated = [(-dy, dx) for dx, dy in self.blocks]
        if not self.collides(0, 0, rotated):
            self.blocks = rotated

    def collides(self, dx, dy, blocks):
        for bx, by in blocks:
            nx = self.x + bx + dx
            ny = self.y + by + dy
            if nx < 0 or nx >= COLS or ny >= ROWS:
                return True
            if ny >= 0 and grid[ny][nx]:
                return True
        return False

    def freeze(self):
        for dx, dy in self.blocks:
            gx = self.x + dx
            gy = self.y + dy
            if 0 <= gx < COLS and 0 <= gy < ROWS:
                grid[gy][gx] = self.color

def clear_lines():
    global score, high_score
    lines = 0
    new_grid = [row for row in grid if any(cell is None for cell in row)]
    lines = ROWS - len(new_grid)
    for _ in range(lines):
        new_grid.insert(0, [None] * COLS)
    for y in range(ROWS):
        grid[y] = new_grid[y]
    score += lines * 100
    if score > high_score:
        high_score = score
    update_score()

def update_score():
    score_writer.clear()
    score_writer.goto(-WIDTH // 2 + 10, HEIGHT // 2)
    score_writer.write(f"Score: {score}", font=("Arial", 16, "bold"))
    score_writer.goto(-WIDTH // 2 + 10, HEIGHT // 2 - 30)
    score_writer.write(f"High Score: {high_score}", font=("Arial", 16, "bold"))
    
def spawn_new():
    global current
    current = Tetromino()
    if current.collides(0, 0, current.blocks):
        print(f"Game Over! Final Score: {score}")
        reset_game()
        
def reset_game():
    global grid, score, current
    grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
    score = 0
    update_score()
    current = Tetromino()

def game_loop():
    screen.update()
    draw_grid()
    current.draw()

    current.counter += 1
    if current.counter >= 30:  # drop speed
        if not current.move(0, 1):
            current.freeze()
            clear_lines()
            spawn_new()
        current.counter = 0

    screen.ontimer(game_loop, FRAME_DELAY)

# Controls
def left(): current.move(-1, 0)
def right(): current.move(1, 0)
def down(): current.move(0, 1)
def rotate(): current.rotate()

screen.listen()
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")
screen.onkeypress(down, "Down")
screen.onkeypress(rotate, "Up")

# Start
current = Tetromino()
update_score()
game_loop()
screen.mainloop()