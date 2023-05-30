import pygame.font


class Button:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # 定义按钮的尺寸和间距
        self.button_width = 200
        self.button_height = 50
        self.button_spacing = 40

        # 计算按钮的纵坐标位置
        button_width = 200
        button_height = 50
        self.button_x = (self.screen_width - button_width) // 2
        self.button_y = (self.screen_height - button_height * 3) // 2

        # 定义按钮的颜色
        self.button_color = (100, 100, 100)
        self.button_hover_color = (150, 150, 150)

        # 定义按钮字体
        self.font_path = "fonts/字魂73号-江南手书.ttf"
        self.in_font_path = "fonts/字魂36号-正文宋楷.ttf"
        self.font_size = 24
        self.in_font_size = 20

    def draw_button(self, text, x, y, width, height):
        pygame.font.init()
        pygame.draw.rect(self.screen, self.button_color, (x, y, width, height))
        font = pygame.font.Font(self.font_path, self.font_size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
        self.screen.blit(text_surface, text_rect)

    def create_button(self):
        self.screen.fill((0, 0, 0))
        self.draw_button("开始游戏", self.button_x, self.button_y, self.button_width,
                         self.button_height)
        self.draw_button("游戏介绍", self.button_x,
                         self.button_y + self.button_height + self.button_spacing, self.button_width,
                         self.button_height)
        self.draw_button("退出游戏", self.button_x, self.button_y + (self.button_height + self.button_spacing) * 2,
                         self.button_width, self.button_height)

    def get_instruction(self):
        # 读取文本文件内容
        file_path = "txt/instruction.txt"
        font = pygame.font.Font(self.in_font_path, self.in_font_size)
        with open(file_path, "r", encoding="utf-8") as file:
            file_content = file.readlines()
        text_surfaces = []
        line_height = font.get_linesize()

        for i, line in enumerate(file_content):
            if i == 0:  # 第一行
                text_surface = font.render(line.strip(), True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(self.screen_width // 2, line_height))
            else:
                text_surface = font.render(line.strip(), True, (255, 255, 255))
                text_rect = text_surface.get_rect(x=10, y=i * line_height)
            text_surfaces.append((text_surface, text_rect))
        self.screen.fill((0, 0, 0))
        for text_surface, text_rect in text_surfaces:
            self.screen.blit(text_surface, text_rect)
        pygame.display.flip()
