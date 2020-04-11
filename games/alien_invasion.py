import sys
import pygame
from pygame.sprite import Group

from settings import Settings 
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    #ai_settings = Settings(1200, 800, (0, 245, 245))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Hello pygame!")
    ship = Ship(ai_settings, screen)
    bullets = Group()


    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
