# Doodle Jumper (v0.1)

A vertical-scrolling platformer game built using Python's `turtle` module. The player controls a bouncing doodle character that jumps between moving platforms, collects power-ups, and avoids falling off the screen.

## Features

- Jump physics with gravity simulation
- Randomly generated moving platforms
- Two types of platforms:
  - Green: stable
  - Red: disappearing after one jump
- Two types of power-ups:
  - Blue: jump boost
  - Yellow: +50 points
- Super Jump ability when the score reaches 50
- Increasing platform speed with score
- Game Over screen and restart functionality

## Controls

- Left Arrow: Move Left  
- Right Arrow: Move Right  
- R: Restart the game after Game Over  
- Space: Perform Power Jump (score ≥ 50)

## Gameplay Mechanics

- The player bounces automatically on landing.
- Platforms move horizontally and reposition as the player ascends.
- Score increases by 10 for each new platform landed on.
- Power-ups offer boosts or score bonuses.
- High score is tracked per session.

## Requirements

- Python 3.x
- No external dependencies (uses only the built-in `turtle` and `random` modules)

## How to Run

1. Make sure Python 3 is installed on your system.
2. Run the game script:

   ```bash
   python Doodle\ jumper_(V.0.1).exe
