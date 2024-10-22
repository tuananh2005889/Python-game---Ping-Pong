import pygame
from define import * 

class Ball():
    def __init__(self, color, x, y, radius, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def show(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Kiểm tra va chạm với biên trên và dưới
        if self.y - self.radius < 0 or self.y + self.radius > WINDOW_HEIGHT:
            self.velocity_y = -self.velocity_y  # Đổi hướng theo trục y

    def check_collision_with_players(self, playerLeft, playerRight):
        # Va chạm với playerLeft
        if self.x - self.radius < playerLeft.x + PLAYER_WIDTH and playerLeft.y < self.y < playerLeft.y + PLAYER_HEIGHT:
            self.velocity_x = -self.velocity_x  # Đổi hướng bóng

        # Va chạm với playerRight
        elif self.x + self.radius > playerRight.x and playerRight.y < self.y < playerRight.y + PLAYER_HEIGHT:
            self.velocity_x = -self.velocity_x  # Đổi hướng bóng

        # Nếu bóng chạm biên trái mà không chạm vào playerLeft, playerLeft mất mạng
        elif self.x - self.radius < 0:
            playerLeft.lose_life()
            self.reset()

        # Nếu bóng chạm biên phải mà không chạm vào playerRight, playerRight mất mạng
        elif self.x + self.radius > WINDOW_WIDTH:
            playerRight.lose_life()
            self.reset()

    def reset(self):
        # Đặt lại vị trí của bóng ở giữa màn hình
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.velocity_x = -self.velocity_x  # Đổi hướng bóng
