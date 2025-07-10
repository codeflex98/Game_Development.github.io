# Snake Game (Python Turtle)

This is a simple implementation of the classic Snake game using Python's built-in `turtle` graphics module. The game features smooth animations, keyboard controls, collision detection, scoring, and visual enhancements.

Play the game on google schrome with this link !

https://codeflex98.github.io/Game_Development.github.io/Snake_game/sample_snake_(V.0.1).html

## Features

- Snake movement using keyboard (WASD)
- Randomly spawning food
- Snake body grows with each food eaten
- Score and high score tracking
- Graceful handling when the game window is closed
- Simple border and color enhancements

## Requirements

- Python 3.x

No external libraries are required — only the standard `turtle`, `random`, and `time` modules are used.

## How to Run

```bash
python snake_game.py
````

## Controls

* W → Move Up
* A → Move Left
* S → Move Down
* D → Move Right

## Code Overview

### 1. Imports and Initialization

```python
import turtle
import time
import random
```

Imports built-in modules used for graphics, delays, and randomness.

---

### 2. Game Configuration

```python
delay = 0.1
score = 0
high_score = 0
```

Sets initial delay (controls speed) and initializes scores.

---

### 3. Screen Setup

```python
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("#aad751")
wn.setup(width=600, height=600)
wn.tracer(0)
```

Creates and configures the main game window.

---

### 4. Border Drawing

A turtle is used to draw the square game area border.

---

### 5. Game Elements

* **Head**: A square representing the snake's head.
* **Food**: A circle that appears at random positions.
* **Pen**: Displays the score and high score at the top of the screen.

---

### 6. Movement Functions

Functions like `go_up()`, `go_down()`, etc. change the snake's direction based on key presses.

---

### 7. Main Game Loop

The game runs inside a `try-except` block to catch `turtle.Terminator` errors when the window is closed.

Within the loop:

* `wn.update()` refreshes the screen.
* Border collision is checked.
* Food collision is checked and handled.
* Segments follow the head to simulate a snake.
* Collision with the body is detected.
* `time.sleep(delay)` controls the game speed.

---

### 8. Error Handling

```python
except turtle.Terminator:
    print("Game window closed. Exiting gracefully.")
```

This prevents the program from throwing an error when the game window is manually closed.

---

## File Structure

```
snake_game/
│
├── snake_game.py         # Main game file
└── README.md             # Project documentation
```

## License

This project is provided under the MIT License.
