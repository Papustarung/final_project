# Tom must be saved

Dynamic Ball Game with Real-Time Physics

## Project Description

This project is a dynamic ball game involving real-time physics. Players control a player ball to avoid hazard balls, use a shield for defense, and aim to cross a win line to achieve victory. The game simulates realistic ball-to-ball collisions and interactions with a player-controlled shield.

### Features

- **Multiple Ball Objects**: Hazard balls move independently and collide with each other dynamically.
- **Shield Mechanics**: The player can activate a shield to deflect hazard balls- .
- **Real-Time Physics**: Elastic collisions and realistic movement.
- **Win and Lose Conditions**: Players win by crossing the win line or lose by colliding with hazard balls.
___
## How to Install and Run the Project
### Installation
1. Clone the repository:
```bash
git clone https://github.com/Papustarung/final_project.git
```
2. Navigate to the project directory:
```bash
cd <repository-directory>
```
3. Run the game:
```
python main.py
```
___
## Usage
### Controls

- **Up Arrow**: Move the player ball upward.
- **Down Arrow**: Move the player ball downward.
- **Spacebar**: Activate the shield to deflect hazard balls.

### Objectives
**Win Condition**: Move the player ball past the right boundary of the screen.
**Lose Condition**: Avoid colliding with any hazard ball. Collision ends the game.
___
## Project Design and Implementation
### UML Class Diagram
```
https://lucid.app/lucidchart/d3fe0e1e-0b82-425d-a1db-03a70e6a3bd9/edit?viewport_loc=-309%2C-313%2C1299%2C1557%2C0_0&invitationId=inv_37ee103d-ffcc-4b9b-ae50-651764664d7d
```
### Class Descriptions

1. **Ball**
    - Handles generic ball movement, boundary collisions (ball-to-wall), and ball-to-ball collisions.
2. **PlayerBall**
    - Inherits from Ball.
    - Adds player-controlled movement and collision detection with hazard balls.
3. **Shield**
    - Represents a defensive shield around the player ball.
    - Handles interactions and deflection of hazard balls.
4. **GameManager**
    - Coordinates all game elements (player, hazard balls, shield).
    - Implements win/lose conditions, screen updates, and collision handling.

### Baseline Code Usage, Extension, and Modifications

1. **Baseline Code Usage**
    - **Ball Mechanics**: 
      - Simulated basic ball movement, boundary collisions, and velocity updates.
    - **Event handling**: 
      - Keyboard bindings
2. **Extensions**
    - **Shield Mechanism**: 
      - Added a Shield class that deflects hazard balls within a radius when activated (similar to bouncing mechanism).
      - Shield activation and cooldown were new mechanics added to the game logic.
    - **Player-Controlled Ball**: 
      - There is a `PlayerBall` class extending from `Ball` class to allow user-controlled movement (up and down).
    - **Game Objectives**:
      - Add win and lose condition.
3. **Modifications**:
    - **Removed Prediction**: 
      - Unlike the baseline, prediction-based event handling was not used. Instead, the update method checks for collisions and updates positions at every frame (frame-based), ensuring simplicity and real-time behavior.

### Testing and Known Bugs

#### Testing

- Ball-to-Ball Collisions:
  - Verified momentum conservation and no overlap after collisions.

- Shield Deflection:
  - Tested deflection for stationary, slow, and fast-moving hazard balls.

- Win/Lose Conditions:
  - Confirmed game ends correctly when objectives are met.

- Boundary Handling:
  - Checked proper bouncing for all ball objects at screen edges.

#### Known Bugs

- Edge Case Collisions:
  - Rare cases where two balls overlap slightly before resolving collisions.

- Shield Interaction:
  - Shield cooldown may reset incorrectly under heavy ball interaction.
___
## Sophistication Level

90
- Real-time collisions and shield mechanics.
- Dynamic deflection