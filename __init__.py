import pygame
import sys

from settings import Settings
from Button import Button
from tetris import Tetris
from background import Background
from text import Text
from music_use import music_use
import game_functions as gf

my_music = music_use()


def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    my_background = Background()
    my_text = Text()
    pygame.display.set_caption("俄罗斯方块")
    my_tetris = Tetris()

    while True:
        if ai_settings.is_paused:
            gf.draw_pause_screen(screen, ai_settings, my_text)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    ai_settings.is_paused = False
        elif ai_settings.gameover == 0 and not ai_settings.is_paused:
            ai_settings.current_time = pygame.time.get_ticks()
            gf.draw_screen(screen, my_tetris, ai_settings, my_text)
            gf.check_events(ai_settings, my_tetris, my_background)
            gf.drop_out(ai_settings, my_background, my_tetris)
            if ai_settings.gameover:
                game_over()
            gf.draw_block(screen, my_background, my_tetris, ai_settings)
            clock.tick(int(ai_settings.up_to_speed))
            pygame.display.update()
        else:
            game_over()


def show_game_instructions(play_button):
    play_button.get_instruction()
    pygame.display.set_caption("游戏介绍")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                main()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def main():
    play_button = Button()
    my_music.play_music()
    pygame.display.set_caption("游戏主菜单")
    while True:
        play_button.create_button()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                check_button_events(event, play_button)


def check_button_events(event, play_button):
    if event.button == 1:
        mouse_pos = pygame.mouse.get_pos()
        if play_button.button_x <= mouse_pos[0] <= play_button.button_x + play_button.button_width:
            if play_button.button_y <= mouse_pos[1] <= play_button.button_y + play_button.button_height:
                run_game()
            elif play_button.button_y + play_button.button_height + \
                    play_button.button_spacing <= mouse_pos[1] <= play_button.button_y + \
                    (play_button.button_height + play_button.button_spacing) * 2:
                show_game_instructions(play_button)
            elif play_button.button_y + (play_button.button_height + play_button.button_spacing) * 2 \
                    <= mouse_pos[1] <= play_button.button_y + (
                    play_button.button_height + play_button.button_spacing) * 3:
                pygame.quit()
                sys.exit()

def game_over():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                main()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


main()
