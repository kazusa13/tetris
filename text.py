import pygame


class Text:
    def __init__(self):
        # 指定静态文本的相关参数
        self.font_path_1 = "fonts/字魂110号-武林江湖体.ttf"  # 侧面板文本的字体
        self.font_path_2 = "fonts/STKAITI.ttf"  # 暂停文本的字体
        self.font_size = 24
        self.font = pygame.font.Font(self.font_path_1, self.font_size)
        self.font_pause = pygame.font.Font(self.font_path_2, self.font_size*2)
        self.text_color = (128, 138, 135)
        self.t_bg_color = (255, 255, 255)
        self.t_rect_x = 250
        self.t_rect_y = 0

        # 文本内容
        self.text_line = [
            "当前得分",
            "",
            "历史最高分",
            "",
            "消除行数",
            "",
            "等级",
            "",
            "长条数",
            "",
            "下一个方块"
        ]
        self.t_pause = "游戏暂停中"
