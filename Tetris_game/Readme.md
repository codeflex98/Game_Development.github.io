# Tetris Game in Python (Turtle Graphics)

This is a simplified version of the classic **Tetris** game built using Python's `turtle` module. It features falling tetrominoes, line clearing, a scoring system, and automatic game reset upon game over.

---

## How to Run

1. Make sure you have Python 3 installed.
2. Save the game code to a file named `tetris.py`.
3. Run the game using:

```bash
python tetris.exe
````
---

## Game Features

* 7 tetromino shapes (O, I, S, Z, L, J, T)
* Real-time keyboard controls
* Line clearing and score tracking
* Automatic game restart on game over
* Basic game border and layout using turtle graphics

---

## Code Structure and Explanation

### Constants

```python
GRID_SIZE = 30
COLS = 10
ROWS = 20
WIDTH = COLS * GRID_SIZE
HEIGHT = ROWS * GRID_SIZE
FRAME_DELAY = int(1000 / 60)
```

* `GRID_SIZE`: Pixel size of one square block.
* `COLS`, `ROWS`: Dimensions of the grid (10x20).
* `WIDTH`, `HEIGHT`: Total screen space for the play area.
* `FRAME_DELAY`: Controls the frame update rate (set to 60 FPS).

---

### Shapes and Colors

```python
SHAPES = {...}
COLORS = {...}
```

* `SHAPES`: Dictionary representing block positions for each tetromino.
* `COLORS`: Color mappings for each shape.

Coordinates in `SHAPES` define block offsets relative to the top-left of the tetromino.

---

### Screen and Drawing Tools

```python
screen = turtle.Screen()
pen = turtle.Turtle()
score_writer = turtle.Turtle()
```

* Initializes the turtle graphics window and two drawing tools:

  * `pen`: Draws the grid and shapes.
  * `score_writer`: Displays score and high score.

---

### Grid Data Structure

```python
grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
```

* A 2D list storing the color of each filled block or `None` if empty.

---

### Drawing Functions

```python
def draw_square(x, y, color)
def draw_grid()
```

* `draw_square`: Draws a single square at grid coordinates.
* `draw_grid`: Draws all filled squares and the outer border of the grid.

---

### Tetromino Class

```python
class Tetromino:
```

Handles tetromino behavior:

* `__init__`: Randomly selects a shape and sets its position.
* `draw()`: Renders the shape using `draw_square`.
* `move(dx, dy)`: Attempts to move the shape if no collision.
* `rotate()`: Rotates the tetromino 90 degrees clockwise.
* `collides(dx, dy, blocks)`: Checks for collision against walls or other blocks.
* `freeze()`: Transfers the tetromino’s blocks to the grid (makes them permanent).

---

### Clearing Lines

```python
def clear_lines():
```

* Checks for full rows.
* Clears filled lines and shifts rows above down.
* Increases the score and updates the high score if necessary.

---

### Score Display

```python
def update_score():
```

* Updates the score and high score text at the top-left of the game area using the `score_writer`.

---

### Game Lifecycle

#### `spawn_new()`

* Spawns a new Tetromino.
* If it immediately collides, the game is over, and `reset_game()` is called.

#### `reset_game()`

* Clears the grid.
* Resets the score to 0.
* Starts a new tetromino.

#### `game_loop()`

* The main loop that:

  * Updates the screen.
  * Moves the active tetromino down.
  * Freezes it if it can't move further.
  * Clears lines and spawns a new tetromino.
  * Repeats at 60 frames per second.

---

### Controls

```python
screen.onkeypress(...)
```

* **Left Arrow**: Move tetromino left
* **Right Arrow**: Move tetromino right
* **Down Arrow**: Move tetromino down (faster)
* **Up Arrow**: Rotate tetromino

---

### Entry Point

```python
current = Tetromino()
update_score()
game_loop()
screen.mainloop()
```

* Initializes the first tetromino.
* Starts the main loop.
* Listens for keyboard inputs using turtle’s `mainloop`.

---

## Potential Improvements

* Add levels and increase drop speed over time.
* Add "Next Piece" and "Hold Piece" features.
* Show a "Game Over" message before restarting.
* Add sound effects and music.
* Persist high score across sessions using file I/O.
* Improve collision detection for edge cases.

---

## License

This project is for educational and personal use. You may modify or share it freely.
