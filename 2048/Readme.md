# 2048 Game using Python Turtle

This is a graphical implementation of the popular 2048 puzzle game using Python's `turtle` module. The game supports keyboard controls, score tracking, tile merging, game-over detection, and restarting using the **Enter** key.

## Access the game on Chrome through this link :
https://codeflex98.github.io/Game_Development.github.io/2048/2048_(V.0.1).html
---

## Features

- 4x4 game grid
- Keyboard controls (`← ↑ ↓ →`) to move tiles
- Randomly spawning tiles (`2` or `4`)
- Automatic merging and score updates
- Game over detection
- Restart game by pressing **Enter**

---

## How to Play

- Use the **arrow keys** to slide tiles:
  - `←` : Move Left
  - `→` : Move Right
  - `↑` : Move Up
  - `↓` : Move Down
- When two tiles with the same number touch, they merge into one.
- After each move, a new tile (`2` or `4`) will appear in a random empty spot.
- The game ends when no more moves are possible.
- Press **Enter** (Return key) to restart the game at any time.

---

## How It Works

### Grid

- The board is represented as a 2D list:  
  `grid[y][x]` contains the value of the tile at row `y`, column `x`.

### Drawing

- The grid and tiles are rendered using `turtle.Turtle`.
- Tile colors are dynamically determined by value (`2`, `4`, `8`, ...).

### Merging Logic

Each move does the following for each row or column:
1. **Compress**: Remove all zeros (slide tiles).
2. **Merge**: If two adjacent tiles are the same, combine them.
3. **Compress again** to move tiles into empty spaces created by merging.
4. **Add a new tile** if the grid has changed.

### Restarting

- The `restart_game()` function resets the board and score, and places two new tiles.
- It’s triggered by the **Enter/Return** key via `screen.onkeypress()`.

---

## Requirements

This game uses only the **Python Standard Library**. No external packages are needed.

- Python 3.6 or higher
- `turtle` module (comes built-in with Python)

---

## Running the Game

1. Save the code to a file, e.g., `2048_turtle.py`
2. Run it using Python:

```bash
python 2048_turtle.py
