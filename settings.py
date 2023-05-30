class Settings:
    # 存放游戏设置的相关模块

    def __init__(self):
        # 游戏初始界面设置
        self.screen_width = 400
        self.screen_height = 500
        self.bg_color = (0, 0, 0)

        # 游戏的设置
        self.level = 1  # 设置游戏初始等级为1
        self.up_to_speed = 100  # 基础帧率
        self.speedup_scale = 1.05  # 速度增加率
        self.score_list = [100, 300, 700, 1500]  # 分数对照表
        self.tet_num = 0  # 计算方块掉落数量
        self.level_up_num = 100  # 每一等级掉落这个数量的方块后，就提升等级
        self.score = 0  # 初始得分
        self.high_score = 0  # 历史最高分
        self.line = 0  # 初始消除行数
        self.gameover = 0  # 设置游戏结束标志
        self.backdoor = False  # 设置是否开挂的标志

        # 其他固定规格设置
        self.rect_size = 25  # 矩形区域大小为25
        self.tet_size = 23  # 方块大小为23
        self.speed = 0  # 每循环30次就掉落一段
        self.move_speed = 0  # 左右移动速度
        self.up_move_speed = 15  # 左右移动帧率控制
        self.disable_duration = 12000  # 暂停键1分钟只能使用1次
        self.last_disable_time = 0  # 上次禁用时间

        # 按键相关设置
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.is_paused = False

        # 游戏计时
        self.current_time = 0

        # 每次进游戏初始化历史最高分
        self.get_high_score()

    def level_up(self):
        # 升级
        self.up_to_speed *= self.speedup_scale
        self.up_move_speed *= self.speedup_scale  # 控制升级后长按左右移动键保持相应的频率
        self.level += 1
        self.tet_num = 0

    def get_score(self, delete_line):
        # 得分=对应行数得分*等级
        self.line += delete_line
        self.score += self.score_list[delete_line - 1] * self.level
        self.update_high_score()

    def get_high_score(self):
        try:
            with open("txt/high_score.txt", "r", encoding="utf-8") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0

    def update_high_score(self):
        if self.score < self.high_score:
            return
        self.high_score = self.score
        with open("txt/high_score.txt", "w", encoding="utf-8") as file:
            file.write(str(self.score))
