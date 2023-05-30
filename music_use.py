import pygame


class music_use:
    def __init__(self):
        self.bg_music_path = "music/俄罗斯方块BGM_剪切版.mp3"

    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.bg_music_path)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
