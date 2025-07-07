import random
import sys
from random import choice

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_HEIGHT, COLOR_BLUE, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, EVENT_ALLY, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.timeout = TIMEOUT_LEVEL
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_ALLY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                if ent is not None:
                    self.window.blit(source=ent.surf, dest=ent.rect)
                    ent.move()
                    if ent.name == 'Player1':
                        self.level_text(16, f'Player1 - Health:{ent.health} | Score: {ent.score}', COLOR_BLUE, (10, 25))
                    if ent.name == 'Player2':
                        self.level_text(16, f'Player2 - Health:{ent.health} | Score: {ent.score}', COLOR_BLUE, (10, 45))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_ALLY:
                    choice = random.choice(('Ally1', 'Ally2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout <= 0:
                        return True


            self.level_text(16, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_BLUE, (10, 5))
            self.level_text(16, f'fps: {clock.get_fps() :.0f}', COLOR_BLUE, (10, WIN_HEIGHT - 35))
            self.level_text(16, f'entidades: {len(self.entity_list)}', COLOR_BLUE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # Colisão e Verificação de vida
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
        pygame.display.flip()
