import time
import pygame
from define import *
from player import Player
from Ball import Ball  # Thêm class Ball mới


pygame.font.init()
WINDOW_GAME = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game Ping Pong")
WINDOW_COLOR = COLOR_BLACK
font = pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()

def show_text(text):
    WINDOW_GAME.fill(COLOR_WHITE)  # Tô nền trắng
    message = font.render(text, True, COLOR_BLACK)
    WINDOW_GAME.blit(message, (200, 250))  # Vị trí thông báo
    pygame.display.update()

def end_game():
    WINDOW_GAME.fill(COLOR_WHITE)
    text = font.render("End Game!")
# Hiển thị thông báo chờ

def countdown(seconds):
    for i in range(seconds, 0, -1):
        show_text(f"Start game in {i} seconds...")
        pygame.time.delay(1000)  # Chờ 1 giây trước khi giảm
    show_text("Start game now!")


countdown(3)


def key_event():
    global run, WINDOW_COLOR
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerRight.move_up()
            if event.key == pygame.K_DOWN:
                playerRight.move_down()
            if event.key == pygame.K_w:
                playerLeft.move_up()
            if event.key == pygame.K_s:
                playerLeft.move_down()

# Khởi tạo player
playerLeft = Player(COLOR_RED, 0, WINDOW_HEIGHT // 2 - PLAYER_HEIGHT // 2)
playerRight = Player(COLOR_BLUE, WINDOW_WIDTH - PLAYER_WIDTH, WINDOW_HEIGHT // 2 - PLAYER_HEIGHT // 2)

# Khởi tạo quả bóng
ball = Ball(COLOR_WHITE, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 15, 5, 5)


run = True
while run:
    pygame.time.delay(30)
    WINDOW_GAME.fill(WINDOW_COLOR)
    key_event()

    # Vẽ line ở giữa sân
    pygame.draw.line(WINDOW_GAME, COLOR_YELLOW, (WINDOW_WIDTH//2, 0), (WINDOW_WIDTH//2, WINDOW_HEIGHT), width=16)

    # Vẽ các player
    playerLeft.show(WINDOW_GAME)
    playerRight.show(WINDOW_GAME)

    # Hiển thị số mạng của các player
    playerLeft.show_lives(WINDOW_GAME, 30)  # Vị trí của trái tim cho playerLeft
    playerRight.show_lives(WINDOW_GAME, WINDOW_WIDTH - 150)  # Vị trí của trái tim cho playerRight

    # Di chuyển và vẽ quả bóng
    ball.move()
    ball.show(WINDOW_GAME)

    # Kiểm tra va chạm với các người chơi
    ball.check_collision_with_players(playerLeft, playerRight)

    # Kiểm tra số mạng của các người chơi
    if playerLeft.lives <= 0:
        print("Player Right Wins!")
        run = False
    elif playerRight.lives <= 0:
        print("Player Left Wins!")
        run = False

    # Cập nhật giao diện
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()
