import turtle
import math


class Ball:
    def __init__(self, size: float, x: float, y: float,
                 vx: float, vy: float, color: any):
        self.size = size
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.mass = 100 * size**2
        self.canvas_width = 400.0
        self.canvas_height = 150.0
        self.shield_collision_cd = 0

    def draw(self):
        """Draw the filled ball"""
        turtle.penup()
        turtle.color(self.color)
        turtle.fillcolor(self.color)
        turtle.goto(self.x, self.y - self.size)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(self.size)
        turtle.end_fill()

    def move(self):
        """
        - Move the ball
        - Handle collisions after hitting walls
        """
        self.x += self.vx
        self.y += self.vy

        # Handle boundary collisions
        if (self.x + self.size > self.canvas_width
            or self.x - self.size < -self.canvas_width):
            self.vx = -self.vx
            self.x = max(-self.canvas_width + self.size,
                         min(self.x, self.canvas_width - self.size))

        if (self.y + self.size > self.canvas_height
            or self.y - self.size < -self.canvas_height):
            self.vy = -self.vy
            self.y = max(-self.canvas_height + self.size,
                         min(self.y, self.canvas_height - self.size))

    def distance(self, that) -> float:
        """Calculate the distance between two balls."""
        dx, dy = that.x - self.x, that.y - self.y
        return math.sqrt(dx**2 + dy**2)

    def is_colliding(self, other) -> bool:
        """Check if this ball is colliding with another."""
        return self.distance(other) <= self.size + other.size

    def bounce_off(self, that):
        """
        - Bouncing when collide with other balls.
        - Handling overlapping.
        """
        dx, dy = that.x - self.x, that.y - self.y
        distance = self.distance(that)

        if distance == 0:  # Prevent division by zero
            return

        # Normalize collision vector
        nx, ny = dx / distance, dy / distance

        # Relative velocity
        dvx, dvy = that.vx - self.vx, that.vy - self.vy
        dot_product = dvx * nx + dvy * ny

        if dot_product > 0:  # Skip if already moving apart
            return

        # Calculate impulse (momentum transfer)
        factor = 2 * dot_product / (self.mass + that.mass)

        # Update velocities
        self.vx += factor * that.mass * nx
        self.vy += factor * that.mass * ny
        that.vx -= factor * self.mass * nx
        that.vy -= factor * self.mass * ny

        # Adjust positions to prevent overlap
        overlap = self.size + that.size - distance
        if overlap > 0:
            correction = overlap / 2
            self.x -= nx * correction
            self.y -= ny * correction
            that.x += nx * correction
            that.y += ny * correction
