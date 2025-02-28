# Dwarf Resource Gathering Game

## Description
This is a simple turn-based resource-gathering game where players control dwarves and place them on resource fields based on dice rolls. The game progresses through seasons and months, and players must strategically place their dwarves to gather resources effectively.

## Features
- Turn-based gameplay with season and month tracking.
- Dice rolling mechanics that determine resource field availability.
- Players can place dwarves on available fields based on dice values.
- Dwarves can be removed and repositioned.
- A visual interface with images for tokens, background, and dice.

## How to Play
1. Click the "Roll Dice" button to roll 7 six-sided dice.
2. Each resource field will display 1 or 2 dice values.
3. Click on a dwarf token from the bottom pool to select it.
4. Click on a resource field with a matching dice value to place the token.
5. If needed, click on an already placed token to return it to the pool.
6. The game progresses through months and seasons automatically.
7. The game ends after "Winter:3," and the final resources are tallied.

## Controls
- **Mouse Click**: Interact with tokens, dice, and placement.
- **Roll Dice Button**: Rolls the dice and unlocks resource placement.
- **Dwarves Pool**: Click to pick a dwarf and place it on the board.
- **Resource Fields**: Click to place a dwarf if dice values match.

## Installation
### Prerequisites
- Python 3.x
- Pygame (`pip install pygame`)

### Running the Game
1. Clone or download this repository.
2. Navigate to the game directory.
3. Run the script:
   ```sh
   python main.py
   ```

## Assets
- **Backgrounds**: Stored in `resources/background/`.
- **Tokens**: Stored in `resources/token/`.
- **Dice Faces**: Stored in `resources/dice/`.

## Future Improvements
- Adding a resource counter for collected materials.
- Implementing AI opponents for solo play.
- Enhancing graphics and animations.
- Balancing game rules for better strategy.

## License
This project is open-source and free to use and modify.

