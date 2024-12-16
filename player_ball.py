from ball import Ball

class PlayerBall(Ball):
    def __init__(self, size: float, x: float, y: float, vx: float, vy: float, color: str):
        super().__init__(size, x, y, vx, vy, color)
        self.lives = 1

    def move_automatically(self):
        self.x += self.vx  # Automatic horizontal movement

    def move_vertically(self, direction: int):
        step = 10
        new_y = self.y + direction * step
        self.y = max(-self.canvas_height + self.size,
                     min(new_y, self.canvas_height - self.size))

    def check_collision(self, hazard_ball):
        # Returns False always, as PlayerBall cannot be hit
        dx = self.x - hazard_ball.x
        dy = self.y - hazard_ball.y
        distance = (dx**2 + dy**2)**0.5
        return distance <= self.size + hazard_ball.size

    def change_color(self, color):
        self.color = color

    def change_size(self, size):
        self.size = size