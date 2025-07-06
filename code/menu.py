import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_PURPLE, MENU_OPTION, COLOR_BLUE, COLOR_CYAN


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/som-menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(32, 'Ice Snack Attack', COLOR_CYAN, ((WIN_WIDTH / 2), 90))

            for i in range(len(MENU_OPTION)):
                self.menu_text(15, MENU_OPTION[i], COLOR_BLUE, ((WIN_WIDTH / 2), 170 + 35 * i))

            pygame.display.flip()

            # Trata o problema de não aparecer/fechar a janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('./asset/PressStart2P-Regular.ttf', text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
