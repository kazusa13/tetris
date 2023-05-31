import sys
import pygame


def draw_block(screen, my_background, my_tetris, ai_settings):
    my_background.bg_update()
    # 绘制掉落方块
    for row, column in my_tetris.select_block:
        row += my_background.y_drop
        column += my_background.x_move
        pygame.draw.rect(screen, my_tetris.select_block_color,
                         (column * ai_settings.rect_size, 500 - row * ai_settings.rect_size, ai_settings.tet_size,
                          ai_settings.tet_size))
    # 把触底的行和列填色
    for row in range(0, 20):
        for column in range(0, 10):
            if my_background.background[row][column]:
                pygame.draw.rect(screen, (255, 165, 0),
                                 (column * ai_settings.rect_size, 500 - row * ai_settings.rect_size,
                                  ai_settings.tet_size, ai_settings.tet_size))


def draw_pause_screen(screen, ai_settings, my_text):
    # 绘制暂停界面
    screen.fill(ai_settings.bg_color)
    pygame.draw.rect(screen, ai_settings.bg_color, (125, 225, 250, 50))
    text_surface = my_text.font_pause.render(my_text.t_pause, True, (255, 255, 255))
    screen.blit(text_surface, (75, 225))
    pygame.display.update()


def draw_screen(screen, my_tetris, ai_settings, my_text):
    # 绘制侧面板
    screen.fill(ai_settings.bg_color)
    pygame.draw.rect(screen, my_text.t_bg_color, (my_text.t_rect_x, my_text.t_rect_y, 250, 500))
    for i in range(9, 0, -2):
        del my_text.text_line[i]
    my_text.text_line.insert(1, str(ai_settings.score))
    my_text.text_line.insert(3, str(ai_settings.high_score))
    my_text.text_line.insert(5, str(ai_settings.line))
    my_text.text_line.insert(7, str(ai_settings.level))
    my_text.text_line.insert(9, str(my_tetris.num_I))
    text_y = my_text.t_rect_y
    i = 0
    for line in my_text.text_line:
        text_surface = my_text.font.render(line, True, my_text.text_color)
        text_x = my_text.t_rect_x + (150 - text_surface.get_width()) // 2
        screen.blit(text_surface, (text_x, text_y))
        if i % 2 != 0:
            text_y += my_text.font_size + 20
        else:
            pygame.draw.rect(screen, ai_settings.bg_color, (my_text.t_rect_x, text_y, 150, 2))
            text_y += my_text.font_size + 5
        i += 1
    for row, column in my_tetris.next_select_block:
        pygame.draw.rect(screen, my_tetris.next_select_block_color, (300 + column * 25, 420 - row * 25, 23, 23))


def block_down_move(my_background, my_tetris, ai_settings):  # 处理方块掉落的相关情况
    my_background.bg_update()
    my_background.y_drop -= 1

    # 更新位置
    for row, column in my_tetris.select_block:
        row += my_background.y_drop
        column += my_background.x_move
        if my_background.background[row][column] == 1:
            break
    else:
        my_background.block_initial_position.clear()
        my_background.block_initial_position.extend((my_background.y_drop, my_background.x_move))
        return

    # 掉落终点更新
    my_background.bg_update()
    for row, column in my_tetris.select_block:
        my_background.tm_update(column, row)

    # 判断是否删除
    complete_row = []
    for row in range(0, 21):
        if 0 not in my_background.background[row + 1]:
            complete_row.append(row)
    complete_row.sort(reverse=True)
    for row in complete_row:
        del my_background.background[row + 1]
        my_background.background.append([0 for _ in range(10)])

    # 得分变化
    if len(complete_row) != 0:
        ai_settings.get_score(len(complete_row))

    # 一个方块掉落完成进行后续操作
    if not ai_settings.backdoor:
        my_tetris.update_tetris()
    else:
        my_tetris.backdoor_update_tetris()
    ai_settings.tet_num += 1
    my_background.block_initial_position.clear()
    my_background.block_initial_position.extend([20, 5])
    my_background.bg_update()
    for row, column in my_tetris.select_block:
        row += my_background.y_drop
        column += my_background.x_move
    for column in range(0, 10):
        if my_background.background[20][column]:
            ai_settings.gameover = 1
    else:
        if ai_settings.tet_num >= ai_settings.level_up_num:
            ai_settings.level_up()


def rotate(my_background, my_tetris):
    # 旋转
    my_background.bg_update()
    rotate_position = [(-column, row) for row, column in my_tetris.select_block]
    for row, column in rotate_position:
        row += my_background.y_drop
        column += my_background.x_move
        if column < 0 or column > 9 or my_background.background[row][column]:
            break
    else:
        my_tetris.select_block.clear()
        my_tetris.select_block.extend(rotate_position)


def check_key_down_events(event, ai_settings, my_background, my_tetris):
    # 处理按下按键的情况
    if event.key == pygame.K_LEFT:
        ai_settings.moving_left = True
        ai_settings.move_speed = 0
        move_left_right(my_background, my_tetris, ai_settings)
    elif event.key == pygame.K_RIGHT:
        ai_settings.moving_right = True
        ai_settings.move_speed = 0
        move_left_right(my_background, my_tetris, ai_settings)
    elif event.key == pygame.K_DOWN:
        ai_settings.moving_down = True
    elif event.key == pygame.K_UP:
        rotate(my_background, my_tetris)
    elif event.key == pygame.K_SPACE:
        if ai_settings.current_time - ai_settings.last_disable_time >= ai_settings.disable_duration:
            ai_settings.is_paused = True
            ai_settings.last_disable_time = ai_settings.current_time
    elif event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()


def check_keyup_events(event, ai_settings):
    # 处理按键抬起的情况
    if event.key == pygame.K_LEFT:
        ai_settings.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ai_settings.moving_right = False
    elif event.key == pygame.K_DOWN:
        ai_settings.moving_down = False
    elif event.key == pygame.K_RETURN:
        if ai_settings.backdoor:
            ai_settings.backdoor = False
        else:
            ai_settings.backdoor = True


def check_events(ai_settings, my_tetris, my_background):
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ai_settings, my_background, my_tetris)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings)


def move_left_right(my_background, my_tetris, ai_settings):
    # 方块左右移动
    my_background.bg_update()
    if ai_settings.moving_right:
        my_background.x_move += 1
    elif ai_settings.moving_left:
        my_background.x_move -= 1
    else:
        return
    for row, column in my_tetris.select_block:
        row += my_background.y_drop
        column += my_background.x_move
        # 边界判断
        if column < 0 or column > 9 or my_background.background[row][column]:
            break
    else:
        # 更新位置
        my_background.block_initial_position.clear()
        my_background.block_initial_position.extend([my_background.y_drop, my_background.x_move])


def drop_out(ai_settings, my_background, my_tetris):
    # 控制方块掉落及左右移动速率
    if ai_settings.speed >= 30:
        block_down_move(my_background, my_tetris, ai_settings)
        ai_settings.speed = 0
    elif ai_settings.moving_down:
        ai_settings.speed += 10
    else:
        ai_settings.speed += 1
    if ai_settings.move_speed <= 11:
        ai_settings.move_speed += 1
    elif ai_settings.move_speed > 11 and (ai_settings.moving_left or ai_settings.moving_right):
        ai_settings.move_speed = 0
        move_left_right(my_background, my_tetris, ai_settings)
