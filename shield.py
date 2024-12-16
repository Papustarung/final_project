import turtle
import time

class Shield:
    def __init__(self, radius: float, owner):
        self.radius = radius
        self.owner = owner
        self.active = False
        self.last_activated = 0
        self.cooldown = 1.0  # Seconds
        self.duration = 0.5  # Seconds

    def activate(self, balls):
        """Activate the shield if it is not on cooldown."""
        # Check if the shield is ready
        if time.time() - self.last_activated < self.cooldown:
            print(f"Shield is on cooldown for "
                  f"{self.cooldown - (time.time() - self.last_activated):.1f}"
                  f" seconds")
            return

        self.active = True
        self.last_activated = time.time()
        print("Shield activated!")

    def deactivate(self):
        """Deactivate the shield."""
        self.active = False

    def is_near(self, ball):
        """Check if a ball is near the shield for deflection."""
        dx = ball.x + ball.size - self.owner.x
        dy = ball.y + ball.size - self.owner.y
        distance = (dx**2 + dy**2)**0.5
        return distance <= self.radius + ball.size

    def bounce_off(self, ball):
        """Deflect a ball outward from the shield's center."""
        # Calculate the vector from the shield center to the ball
        dx = ball.x - self.owner.x
        dy = ball.y - self.owner.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance == 0:
            return

        # Normalize the vector
        nx = dx / distance
        ny = dy / distance

        # Compute the velocity component along the normal
        dot_product = ball.vx * nx + ball.vy * ny

        if dot_product < 0:
            # Reflect the velocity vector
            ball.vx -= 2 * dot_product * nx
            ball.vy -= 2 * dot_product * ny

        # Ensure minimum deflection speed
        min_velocity = 3.0
        # Current speed of the ball
        velocity = (ball.vx ** 2 + ball.vy ** 2) ** 0.5
        if velocity < min_velocity:
            # Scale the velocity to the minimum speed in the outward direction
            ball.vx = nx * min_velocity
            ball.vy = ny * min_velocity

    def draw(self):
        """Draw the shield if active."""
        if not self.active:
            return

        turtle.penup()
        turtle.goto(self.owner.x, self.owner.y - self.radius)
        turtle.pendown()
        turtle.fillcolor((200, 210, 255))
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()

