import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна игры
window_width = 640
window_height = 480

# Цвета
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

# Размер ячейки сетки
gridsize = 20

# Направления
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

# Скорости змейки для разных уровней сложности
speeds = {
    'easy': 10,
    'medium': 15,
    'hard': 20
}
