import turtle
import time
from game_manager import GameManager

def main():
    num_hazard_balls = 15
    game = GameManager(num_hazard_balls)
    screen = game.screen
    screen.setup(width=1000, height=600)
    game.update()
    game.refresh_screen()
    time.sleep(1)
    screen.listen()
    screen.onkey(lambda: game.player.move_vertically(1), "Up")  # Move up
    screen.onkey(lambda: game.player.move_vertically(-1), "Down")  # Move down
    screen.onkey(game.activate_shield, "space")

    while True:
        game.update()          # Update all positions
        game.refresh_screen()  # Clear and redraw everything

        # Add a small delay to control the frame rate
        time.sleep(0.01)

        # Exit the loop after winning the game
        if game.check_win_condition():
            break

    turtle.done()  # Keep the screen open after the game ends

if __name__ == "__main__":
    main()
