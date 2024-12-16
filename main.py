import turtle
import time
from game_manager import GameManager

def main():
    """Main function to initialize and run the game."""
    num_hazard_balls = 10

    # Initialize the game manager
    game = GameManager(num_hazard_balls)

    # Setup game screen
    screen = game.screen
    screen.setup(width=1000, height=600)

    # Preparation phase
    game.update()
    game.refresh_screen()
    time.sleep(1)  # Delay time for player to prepare

    # Setup keyboard controls
    screen.listen()
    screen.onkey(lambda: game.player.move_vertically(1), "Up")     # Move up
    screen.onkey(lambda: game.player.move_vertically(-1), "Down")  # Move down
    screen.onkey(game.activate_shield, "space")

    try:
        while True:
            # Update all positions
            game.update()

            # Clear and redraw everything
            game.refresh_screen()

            # Limit frame rate
            time.sleep(0.01)
    except turtle.Terminator:
        print("--Game exited--")

if __name__ == "__main__":
    main()
