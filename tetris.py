import random


class Tetris:
    def __init__(self):
        # 创建元素块
        self.all_block = [
            [[0, 0], [0, -1], [0, 1], [0, 2]],  # I型方块
            [[0, 0], [0, 1], [1, 1], [1, 0]],  # 田型方块
            [[0, 0], [0, -1], [-1, 0], [-1, 1]],  # Z型方块
            [[0, 0], [0, 1], [-1, -1], [-1, 0]],  # 倒Z型方块
            [[0, 0], [0, 1], [1, 0], [0, -1]],  # 土型方块
            [[0, 0], [1, 0], [-1, 0], [1, -1]],  # L型方块
            [[0, 0], [1, 0], [-1, 0], [1, 1]]  # J型方块
        ]
        # 每种元素块对应不同的颜色
        self.color_block = (
            (255, 0, 255),
            (255, 0, 255),
            (255, 0, 0),
            (255, 0, 0),
            (255, 0, 255),
            (0, 0, 255),
            (0, 0, 255)
        )
        # 选择元素块
        self.num_I = 0
        self.number = random.randint(0, 6)
        if self.number == 0:
            self.num_I += 1
        self.select_block = list(self.all_block[self.number])  # 当前方块
        self.select_block_color = list(self.color_block[self.number])  # 当前颜色
        self.number = random.randint(0, 6)
        self.next_select_block_color = list(self.color_block[self.number])
        self.next_select_block = list(self.all_block[self.number])

    def update_tetris(self):
        # 更新方块
        if self.number == 0:
            self.num_I += 1
        self.select_block.clear()
        self.select_block.extend(self.next_select_block)
        self.select_block_color.clear()
        self.select_block_color.extend(self.next_select_block_color)
        self.number = random.randint(0, 6)
        self.next_select_block.clear()
        self.next_select_block_color.clear()
        self.next_select_block_color = list(self.color_block[self.number])  # 下一个方块的颜色
        self.next_select_block = list(self.all_block[self.number])  # 下一个方块

    def backdoor_update_tetris(self):
        self.num_I += 1
        self.select_block.clear()
        self.next_select_block.clear()
        self.select_block_color.clear()
        self.next_select_block_color.clear()
        self.next_select_block = list(self.all_block[0])
        self.next_select_block_color = list(self.color_block[0])
        self.select_block = list(self.all_block[0])
        self.select_block_color = list(self.color_block[0])
