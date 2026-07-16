# Escape Room

## Description

Escape Room is a text-based game that prompts the user to navigate through a hidden room, solve two randomly chosen password puzzles, and reach the exit. The player receives clues about nearby walls and must solve both puzzles before escaping.

## How to Run

To run this program, open `escape_room.py` in a Python IDE and click **Run**, or open a terminal in the project folder and enter:

```bash
python3 escape_room.py
```

No third-party packages are required.

## Features

- Allows the user to move up, down, left, and right through the room
- Alerts the user when there is a wall nearby
- Displays the user's coordinates after each move
- Prompts the user to solve two randomized password puzzles
- Accepts password guesses without considering capitalization
- Tracks completed puzzles so they do not need to be solved again
- Requires both puzzles to be solved before the user can escape

## Next Steps

If I had more time, I would add a feature that displays the parts of the room the user has already explored. The map would update after every move, making navigation easier while still keeping unexplored areas hidden. I would also add more rooms, puzzles, and difficulty levels to make the game more challenging.
