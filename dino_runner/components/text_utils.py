import pygame
from dino_runner.utils.constants import FONT_STYLE, COLORS, SCREEN_HEIGHT, SCREEN_WIDTH

class textUtils:

    def get_score_element(self, points):
        font = pygame.fron.Font(FONT_STYLE, 22)
        teext = font.render("Points: " + str(points), True ,COLORS["balck"])
        text_rect = text_rect()
        text_rect.center = (1000,50)
        return text, text_rect
    
    def get_centered_message(self, message, widht = SCREEN_WIDTH //2, height = SCREEN_HEIGHT // 2):
        front = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(message, True, COLORS["black"])
        text_rect = text.get_rect()
        text_rect.center = (widht, height)
        return text, text_rect
        
    



