import random
import pygame

# 遊戲初始化
pygame.init()

window_size = [800, 600]
screen = pygame.display.set_mode(window_size)
screen.fill([255, 255, 255])

color_red = pygame.color.Color('red')
r = 50
# 顯示圖片到視窗上 (400, 300) 位置，記錄好初始位置
image_x = 400
image_y = 300
# 宣告 font 文字物件
head_font = pygame.font.SysFont(None, 60)
# 渲染方法會回傳 surface 物件
text_surface = head_font.render('Hello World!', True, (0, 0, 0))

# 繪製圖片初始位置
pygame.draw.circle(screen, color_red,(image_x,image_y), r, 0)

# 這個是決定是否跳出遊戲迴圈的變數
is_game_over = False
# 取出起始時間
time_start = pygame.time.get_ticks()
# 文字模組，用來顯示文字，可用來顯示儀表板資料。第一個參數為文字內容（這邊因為初始值為 None），第二個為大小
point_font = pygame.font.SysFont(None, 30)
time_font = pygame.font.SysFont(None, 30)
# 遊戲分數
points = 0
# 總遊戲時間
total_time = 60

while not is_game_over:
    # 目前時間
    time_now = pygame.time.get_ticks()
    # 取出當下時間，若時間超過 30 秒，則印出 over 30secs 遊戲結束
    during_time = (time_now - time_start) // 1000

    if during_time >= total_time:
        print('over', total_time ,'secs')
        print('You got',points,'Points')
        is_game_over = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
                    
            x = mouse_position[0] - image_x
            y = mouse_position[1] - image_y
            
            if (x**2 + y**2)**0.5 < r:
                points += 5
                # 當被點擊後圖片隨機產生新位置
                r = 10 + 5 * random.randint(0, 10)
                image_x = random.randint(r, 800 - r)
                image_y = random.randint(r, 600 - r)
                pygame.draw.circle(screen, color_red,(image_x,image_y), 50, 0)               


    screen.fill([255, 255, 255])
    # 遊戲剩餘時間
    remaining_time = total_time -  during_time
    # 製作遊戲分數文字元素
    point_font_surface = point_font.render('Points: {}'.format(points), True, (0, 0, 0))
    # 繪製遊戲分數文字到視窗
    screen.blit(point_font_surface, (10, 0))
    # 製作剩餘時間文字元素
    time_font_surface = time_font.render('Time: {}'.format(remaining_time), True, (0, 0, 0))
    # 繪製剩餘時間文字到視窗
    screen.blit(time_font_surface, (10, 30))
    # 繪製圖片
    pygame.draw.circle(screen, color_red,(image_x,image_y), r, 0)
    # 記得更新畫面（有點像是 tkinter 的 update）
    pygame.display.flip()

# 最後記得關閉 pygame
pygame.quit()