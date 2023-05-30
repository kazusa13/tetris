class Background:
    def __init__(self):
        self.background = [[0 for _ in range(0, 10)] for _ in range(0, 22)]
        self.background[0] = [1 for _ in range(0, 10)]
        self.block_initial_position = [21, 5]
        self.y_drop, self.x_move = self.block_initial_position

    def bg_update(self):
        self.y_drop, self.x_move = self.block_initial_position

    def tm_update(self, x, y):
        self.background[y+self.y_drop][x+self.x_move] = 1
