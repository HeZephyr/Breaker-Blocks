'''
开发项目：Block Breaker游戏
开发者：贺志飞
班级：软件开发191班
学号：5720191408
完成时间：2021.1.7
'''

import sys, time, random, math, pygame
from pygame.locals import *
from MyLibrary import *

#八个关卡
levels = (
(1,1,1,1,1,1,1,1,1,1,1,1, 
 1,1,1,1,1,1,1,1,1,1,1,1, 
 1,1,1,1,1,1,1,1,1,1,1,1, 
 1,1,1,1,1,1,1,1,1,1,1,1, 
 1,1,1,1,1,0,0,1,1,1,1,1, 
 1,1,1,1,1,0,0,1,1,1,1,1, 
 1,1,1,1,1,1,1,1,1,1,1,1, 
 1,1,1,1,1,1,1,1,1,1,1,1, 
 1,1,1,1,1,1,1,1,1,1,1,1, 
 1,1,1,1,1,1,1,1,1,1,1,1),

(2,2,2,2,2,2,2,2,2,2,2,2, 
 2,0,0,2,2,2,2,2,2,0,0,2, 
 2,0,0,2,2,2,2,2,2,0,0,2, 
 2,2,2,2,2,2,2,2,2,2,2,2, 
 2,2,2,2,2,2,2,2,2,2,2,2, 
 2,2,2,2,2,2,2,2,2,2,2,2, 
 2,2,2,2,2,2,2,2,2,2,2,2, 
 2,0,0,2,2,2,2,2,2,0,0,2, 
 2,0,0,2,2,2,2,2,2,0,0,2, 
 2,2,2,2,2,2,2,2,2,2,2,2),

(3,3,3,3,3,3,3,3,3,3,3,3, 
 3,3,0,0,0,3,3,0,0,0,3,3, 
 3,3,0,0,0,3,3,0,0,0,3,3, 
 3,3,0,0,0,3,3,0,0,0,3,3, 
 3,3,3,3,3,3,3,3,3,3,3,3, 
 3,3,3,3,3,3,3,3,3,3,3,3, 
 3,3,0,0,0,3,3,0,0,0,3,3, 
 3,3,0,0,0,3,3,0,0,0,3,3, 
 3,3,0,0,0,3,3,0,0,0,3,3, 
 3,3,3,3,3,3,3,3,3,3,3,3),

(4,4,4,4,4,4,4,4,4,4,4,4,
 4,0,4,0,0,4,4,0,0,0,0,4,
 4,0,4,0,0,4,4,0,0,0,0,4,
 4,4,4,0,0,4,4,0,0,0,0,4,
 4,4,4,4,4,4,4,4,4,4,4,4,
 4,4,4,4,4,4,4,4,4,4,4,4,
 4,4,4,0,0,4,4,0,0,0,4,4,
 4,0,4,0,4,0,4,0,4,0,4,4,
 4,0,4,0,4,0,4,0,4,0,4,4,
 4,4,4,4,4,4,4,4,4,4,4,4),

(5,5,5,5,5,5,5,5,5,5,5,5,
 0,5,5,5,5,5,5,5,5,5,5,0,
 0,5,5,5,5,5,5,5,5,5,5,0,
 0,5,5,5,5,5,5,5,5,5,5,0,
 0,5,5,5,5,5,5,5,5,5,5,0,
 0,5,5,5,5,5,5,5,5,5,5,0,
 0,5,5,5,5,5,5,5,5,5,5,0,
 0,5,5,5,5,5,5,5,5,5,5,0,
 0,5,5,5,5,5,5,5,5,5,5,0,
 5,5,5,5,5,5,5,5,5,5,5,5),

(6,6,6,6,6,6,6,6,6,6,6,6,
 6,6,6,6,6,6,6,6,6,6,6,6,
 6,6,6,6,6,6,6,6,6,6,6,6,
 6,6,6,6,6,6,6,6,6,6,6,6,
 6,6,6,6,6,6,6,6,6,6,6,6,
 6,6,6,6,6,6,6,6,6,6,6,6,
 6,6,6,6,6,6,6,6,6,6,6,6,
 6,6,6,6,6,6,6,6,6,6,6,6,
 6,6,6,6,6,6,6,6,6,6,6,6,
 6,6,6,6,6,6,6,6,6,6,6,6),
(7,7,7,7,7,7,7,7,7,7,7,7,
 7,7,7,7,7,7,7,7,7,7,7,7,
 7,7,7,7,7,7,7,7,7,7,7,7,
 7,7,7,7,7,7,7,7,7,7,7,7,
 7,7,7,7,7,0,0,7,7,7,7,7,
 7,7,7,7,7,0,0,7,7,7,7,7,
 7,7,7,7,7,7,7,7,7,7,7,7,
 7,7,7,7,7,7,7,7,7,7,7,7,
 7,7,7,7,7,7,7,7,7,7,7,7,
 7,7,7,7,7,7,7,7,7,7,7,7),

(8,8,8,8,8,8,8,8,8,8,8,8,
 8,0,8,8,8,0,0,8,8,8,0,8,
 8,8,8,8,8,8,8,8,8,8,8,8,
 8,8,8,8,8,8,8,8,8,8,8,8,
 8,8,8,8,8,8,8,8,8,8,8,8,
 8,8,8,8,8,0,0,8,8,8,8,8,
 8,8,8,8,8,8,8,8,8,8,8,8,
 8,8,8,8,8,8,8,8,8,8,8,8,
 8,0,8,8,8,0,0,8,8,8,0,8,
 8,8,8,8,8,8,8,8,8,8,8,8),
)
#注：global关键字是为了允许有些函数能去修改在程序中任何其他定义的一个变量。
#该函数用于增加关卡编号，确保位于定义的关卡范围之内。
def goto_next_level():
    global level, levels#声明为global，用于更改函数外部变量。
    level += 1
    if level > len(levels)-1: level = 0#如果超过所定义关卡，则回到第一关
    load_level()

#该函数用于处理打通关卡的情况。
def update_blocks():
    global block_group, waiting#声明为global，用于更改函数外部变量。
    if len(block_group) == 0: #判断是否所有的块都消失了，即是否通关。
        goto_next_level()
        waiting = True
    block_group.update(ticks, 50)
        
#该函数用于加载关卡
def load_level():
    global level, block, block_image, block_group, levels
    
    block_image = pygame.image.load("images/blocks.png").convert_alpha()#该函数可使图像的背景透明。

    block_group.empty() #清空重置块组

    #遍历关卡数据以创建名为block_group的一个精灵组，其中包含了当前关卡的所有钻块。
    for bx in range(0, 12):
        for by in range(0,10):
            block = MySprite()
            block.set_image(block_image, 58, 28, 4)
            x = 40 + bx * (block.frame_width+1)
            y = 60 + by * (block.frame_height+1)
            block.position = x,y

            #从关卡数据中读取块
            num = levels[level][by*12+bx]#判断该关卡所处位置是否有块。
            block.first_frame = num-1#确定精灵的首帧。
            block.last_frame = num-1
            if num > 0: #0即代表空了
                block_group.add(block)#增加精灵。

    print(len(block_group))

#该函数用来管理pygame的初始化，并且加载位图文件这样的游戏资源。
def game_init():
    global screen, font, timer
    global paddle_group, block_group, ball_group
    global paddle, block_image, block, ball

    pygame.init()#pygame模块初始化。
    screen = pygame.display.set_mode((800,600))#初始化准备显示的一个窗口，大小为800*600
    pygame.display.set_caption("Block Breaker Game")#设置窗口标题。
    font = pygame.font.Font(None, 36)#生成字体对象。
    pygame.mouse.set_visible(False)
    timer = pygame.time.Clock()#创建一个Clock对象用来跟踪时间。

    #创建精灵组，用于管理精灵的更新和绘制
    paddle_group = pygame.sprite.Group()
    block_group = pygame.sprite.Group()
    ball_group = pygame.sprite.Group()

    #创建挡板精灵
    paddle = MySprite()
    paddle.load("images/paddle.png")#加载精灵序列图。
    paddle.position = 400, 540#设置挡板初始坐标
    paddle_group.add(paddle)#添加到精灵组方便管理它们。

    #创建球精灵
    ball = MySprite()
    ball.load("images/ball.png")#加载精灵序列图。
    ball.position = 400,300#设置球的初始坐标
    ball_group.add(ball)#添加精灵用于管理它们。



#该函数用于移动挡板
def move_paddle():
    global movex,movey,keys,waiting
    #waitting标记，使得球等待玩家启动它。

    paddle_group.update(ticks, 50)

    #响应键，即根据按键状态
    if keys[K_SPACE]:
        #判断并处理等待状态。
        if waiting:
            waiting = False
            reset_ball()#设置球的初始弹射方向
    elif keys[K_LEFT]: paddle.velocity.x = -10.0#向左移动
    elif keys[K_RIGHT]: paddle.velocity.x = 10.0#向右移动
    else:
        if movex < -2: paddle.velocity.x = movex
        elif movex > 2: paddle.velocity.x = movex
        else: paddle.velocity.x = 0
    
    paddle.X += paddle.velocity.x
    if paddle.X < 0: paddle.X = 0
    elif paddle.X > 710: paddle.X = 710

#该函数功能用于重置球的方向值。
def reset_ball():
    ball.velocity = Point(4.5, -7.0)

#该函数功能用于移动球
def move_ball():
    global waiting, ball, game_over, lives

    #移动球
    ball_group.update(ticks, 50)
    if waiting:
        ball.X = paddle.X + 40
        ball.Y = paddle.Y - 20
    ball.X += ball.velocity.x
    ball.Y += ball.velocity.y
    #判断x和y的情况。
    if ball.X < 0:
        ball.X = 0
        ball.velocity.x *= -1
    elif ball.X > 780:
        ball.X = 780
        ball.velocity.x *= -1
    if ball.Y < 0:
        ball.Y = 0
        ball.velocity.y *= -1
    elif ball.Y > 580: #如果其纵坐标超过580，说明出界没有被挡板接住。
        waiting = True
        lives -= 1#剩余球数减1.
        if lives < 1: game_over = True

#该函数负责处理球和挡板之间的冲突。
def collision_ball_paddle():
    if pygame.sprite.collide_rect(ball, paddle):#pygame.sprite模块的内置函数，处理两个精灵之间的矩形检测
        #垂直方向值使其向上。
        ball.velocity.y = -abs(ball.velocity.y)
        bx = ball.X + 8
        by = ball.Y + 8
        # 获取中心点的位置。
        px = paddle.X + paddle.frame_width/2
        py = paddle.Y + paddle.frame_height/2
        if bx < px: #在挡板的左侧?
            ball.velocity.x = -abs(ball.velocity.x)
        else: #在挡板的右侧?
            ball.velocity.x = abs(ball.velocity.x)

#该函数处理球和钻块之间的冲突。
def collision_ball_blocks():
    global score, block_group, ball
    
    hit_block = pygame.sprite.spritecollideany(ball, block_group)##pygame.sprite模块的内置函数，调用这个函数的时候，一个组中的所有精灵都会逐个地对另外一个单个精灵进行冲突检测，发生冲突的精灵会作为一个列表返回。
    if hit_block != None:#若列表不为空。
        score += 10
        block_group.remove(hit_block)#删除撞击到的块。
        bx = ball.X + 8
        by = ball.Y + 8

        #判断球是从下方还是上方击中砖块的中间。
        if bx > hit_block.X+5 and bx < hit_block.X + hit_block.frame_width-5:
            if by < hit_block.Y + hit_block.frame_height/2: #上方?
                ball.velocity.y = -abs(ball.velocity.y)
            else: #下方?
                ball.velocity.y = abs(ball.velocity.y)

        #判断球是否从左边撞击砖块的?
        elif bx < hit_block.X + 5:
            ball.velocity.x = -abs(ball.velocity.x)
        #判断球是否从右边击中砖块的?
        elif bx > hit_block.X + hit_block.frame_width - 5:
            ball.velocity.x = abs(ball.velocity.x)

        #处理其他情况。
        else:
            ball.velocity.y *= -1
    
    
#主程序开始。
if __name__=="__main__":
    game_init()
    #将全局变量设置为初始值。
    game_over = False#代表游戏是否结束
    waiting = True
    score = 0#得分
    lives = 3#球数，即生命值
    level = 0#关卡
    load_level()
    #重复循环
    while True:
        timer.tick(30)#游戏绘制的最大帧率
        ticks = pygame.time.get_ticks()#获取时间。

        #监听用户事件。
        for event in pygame.event.get():
            #判断用户是否点击了关闭按钮。
            if event.type == QUIT:
                sys.exit()
            #查看鼠标按键
            elif event.type == MOUSEMOTION:
                movex,movey = event.rel#获取相对位移。
            elif event.type == MOUSEBUTTONUP:
                if waiting:
                    waiting = False
                    reset_ball()
            #查看按键释放按键。
            elif event.type == KEYUP:
                if event.key == K_RETURN: goto_next_level()

        #处理按键
        keys = pygame.key.get_pressed()#获取键盘上的所有按键状态。
        if keys[K_ESCAPE]: sys.exit()#即按ESC即视为退出游戏。
        #更新
        if not game_over:
            update_blocks()#更新块
            move_paddle()#移动挡板
            move_ball()#移动球。
            #处理碰撞
            collision_ball_paddle()
            collision_ball_blocks()

        #动作完成一帧后开始绘制界面。
        screen.fill((50,50,100))#设置背景颜色。
        #在screen中绘制精灵组中的精灵，即绘制帧。
        block_group.draw(screen)
        ball_group.draw(screen)
        paddle_group.draw(screen)
        #打印局内信息。
        print_text(font, 0, 0, "SCORE " + str(score))
        print_text(font, 200, 0, "LEVEL " + str(level+1))
        print_text(font, 400, 0, "BLOCKS " + str(len(block_group)))
        print_text(font, 670, 0, "BALLS " + str(lives))
        if game_over:
            print_text(font, 300, 380, "G A M E   O V E R")
        pygame.display.update()#更新屏幕。
    

