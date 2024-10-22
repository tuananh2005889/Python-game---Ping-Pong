import pygame
from define import *

class Player():
    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color
        self.lives = 3  # Mỗi người chơi có 3 mạng

    def show(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT), width=0)

    def move_up(self):
        self.y -= PLAYER_VELOCITY
        if self.y < 0:
            self.y = 0

    def move_down(self):
        self.y += PLAYER_VELOCITY
        if self.y > WINDOW_HEIGHT - PLAYER_HEIGHT:
            self.y = WINDOW_HEIGHT - PLAYER_HEIGHT

    def lose_life(self):
        self.lives -= 1


    heart_image = pygame.image.load("heart.png")
    heart_image = pygame.transform.scale(heart_image, (30, 30))  # Tùy chỉnh kích thước ảnh nếu cần

    def show_lives(self, surface, x_pos):
        # Dùng self.lives để hiển thị đúng số lượng mạng
        for i in range(self.lives):
            surface.blit(self.heart_image, (x_pos + i * 50, 10))  # Vị trí trái tim dịch theo i