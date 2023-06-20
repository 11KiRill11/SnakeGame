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

class Snake:

    def __init__(self):

        self.length = 1
        self.positions = [((window_width // 2), (window_height // 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = red
        self.speed = speeds['medium']

    def get_head_position(self):

        return self.positions[0]

    def move(self):

        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * gridsize)) % window_width), (cur[1] + (y * gridsize)) % window_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):

        self.length = 1
        self.positions = [((window_width // 2), (window_height // 2))]
        self.direction = random.choice([up, down, left, right])

    def draw(self, surface):

        for p in self.positions:
            pygame.draw.rect(surface, self.color, pygame.Rect(p[0], p[1], gridsize, gridsize))

    def handle_keys(self, keys):

        if keys[pygame.K_UP] or keys[ord('w')]:
            self.direction = up
        elif keys[pygame.K_DOWN] or keys[ord('s')]:
            self.direction = down
        elif keys[pygame.K_LEFT] or keys[ord('a')]:
            self.direction = left
        elif keys[pygame.K_RIGHT] or keys[ord('d')]:
            self.direction = right

class Authentication:
    def __init__(self):
        self.users = {"player": "123"}

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            print("Авторизация успешна.")
            return True
        return False

class Apple:
    def __init__(self):
        self.position = (0, 0)
        self.color = pygame.Color(0, 255, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, window_width // gridsize - 1) * gridsize,
                         random.randint(0, window_height // gridsize - 1) * gridsize)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.position[0], self.position[1], gridsize, gridsize))
