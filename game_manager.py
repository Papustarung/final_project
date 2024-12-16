import time
import random
import turtle
from player_ball import PlayerBall
from ball import Ball
from shield import Shield


class GameManager:
    """Class for controlling the game flow"""
    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 150
    SHIELD_DURATION = 0.5  # Duration the shield stays active (in seconds)
    SHIELD_COOLDOWN = 5    # Cooldown frames for shield deflections
    WIN_CONDITION_X = 400  # Player must cross this x-coordinate to win

    def __init__(self, num_balls: int):
        """Initialize the game manager."""
        turtle.colormode(255)
        self.hazard_balls = [
            Ball(
                size=10,
                x=random.randint(-self.CANVAS_WIDTH + 100, self.CANVAS_WIDTH),
                y=random.randint(-self.CANVAS_HEIGHT, self.CANVAS_HEIGHT),
                vx=random.randint(-3, 2),
                vy=random.randint(-2, 3),
                color=(random.randint(180, 255), 100, 100),
            )
            for _ in range(num_balls)
        ]
        self.player = PlayerBall(15, -self.CANVAS_WIDTH, 0, 2, 0, "blue")
        self.shield = Shield(100, self.player)
        self.screen = turtle.Screen()
        self.screen.setup(width=2 * self.CANVAS_WIDTH, height=2 * self.CANVAS_HEIGHT)
        self.screen.tracer(0)  # Disable auto-refresh
        self.screen.listen()
        turtle.hideturtle()

    def activate_shield(self):
        """Activate the shield if not on cooldown."""
        self.shield.activate(self.hazard_balls)

    def draw_border(self):
        """Draw the game boundaries."""
        border_turtle = turtle.Turtle()
        border_turtle.hideturtle()
        border_turtle.penup()
        border_turtle.goto(-self.CANVAS_WIDTH, -self.CANVAS_HEIGHT)
        border_turtle.pensize(2)
        border_turtle.pendown()
        border_turtle.color("black")
        for _ in range(2):
            border_turtle.forward(2 * self.CANVAS_WIDTH)
            border_turtle.left(90)
            border_turtle.forward(2 * self.CANVAS_HEIGHT)
            border_turtle.left(90)

    def check_win_condition(self) -> bool:
        """Check if the player has won the game."""
        return self.player.x > self.WIN_CONDITION_X

    def check_lose_condition(self) -> bool:
        """Check if the player collides with any hazard ball."""
        for ball in self.hazard_balls:
            if self.player.check_collision(ball):
                return True
        return False

    def update(self):
        """Update all game elements."""
        # Move player ball
        self.player.move_automatically()

        # Update hazard balls
        for i, ball in enumerate(self.hazard_balls):
            ball.move()

            # Check for ball-to-ball collisions
            for j in range(i + 1, len(self.hazard_balls)):
                other_ball = self.hazard_balls[j]
                if ball.is_colliding(other_ball):
                    ball.bounce_off(other_ball)

            # Handle shield collisions
            if (
                self.shield.active
                and self.shield.is_near(ball)
                and ball.shield_collision_cd == 0
            ):
                self.shield.bounce_off(ball)
                ball.shield_collision_cd = self.SHIELD_COOLDOWN

            # Decrement shield collision cooldown
            if ball.shield_collision_cd > 0:
                ball.shield_collision_cd -= 1

        # Check win or lose conditions
        if self.check_win_condition():
            print("You Win!")
            time.sleep(2)
            turtle.bye()
        if self.check_lose_condition():
            self.player.change_size(50)
            self.player.change_color((255,150,75))
            self.refresh_screen()
            print("Game Over! You lost!")
            time.sleep(2)
            turtle.bye()

        # Deactivate the shield after its duration
        if self.shield.active and time.time() - self.shield.last_activated > self.SHIELD_DURATION:
            self.shield.deactivate()

    def refresh_screen(self):
        """Refresh the game screen."""
        turtle.clear()
        # Draw the shield (if active)
        self.shield.draw()

        # Draw all hazard balls
        for ball in self.hazard_balls:
            ball.draw()

        # Draw the player ball
        self.player.draw()

        # Draw the game boundary
        self.draw_border()

        # Update the turtle screen
        turtle.update()
