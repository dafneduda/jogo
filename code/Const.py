import pygame

# C
COLOR_PURPLE = (128, 0, 128)
COLOR_BLUE = (0, 0, 255)
COLOR_CYAN = (0, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_WHITE = (255, 255, 255)

# E

ENTITY_DAMAGE = {
    'lv1-0': 0,
    'lv1-1': 1,
    'lv1-2': 2,
    'lv1-3': 3,
    'lv1-4': 4,
    'Player1': 1,
    'Player2': 1,
    'Enemy1': 1,
    'Enemy2': 1,
}

EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SCORE = {
    'lv1-0': 0,
    'lv1-1': 0,
    'lv1-2': 0,
    'lv1-3': 0,
    'lv1-4': 0,
    'Player1': 0,
    'Player2': 0,
    'Enemy1': 100,
    'Enemy2': 125,
}


ENTITY_SPEED = {
    'lv1-0': 0,
    'lv1-1': 1,
    'lv1-2': 2,
    'lv1-3': 3,
    'lv1-4': 4,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1,
}

ENTITY_HEALTH = {
    'lv1-0': 999,
    'lv1-1': 999,
    'lv1-2': 999,
    'lv1-3': 999,
    'lv1-4': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 50,
    'Enemy2': 60,
}

# M
MENU_OPTION = ('NEW GAME 1P', 'NEW GAME 2P', 'SCORE', 'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}

# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
