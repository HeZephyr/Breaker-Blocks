# MyLibrary.py

import sys, time, random, math, pygame
from pygame.locals import *


#使用提供的字体打印文本。
def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen = pygame.display.get_surface() #函数移入MyLibrary时需要，即获取当前显示屏幕对象。
    screen.blit(imgText, (x,y))#绘制图像。

# MySprite类扩展了pygame.sprite.Sprite,即精灵类的继承。
class MySprite(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #扩展基本的Sprite类
        self.master_image = None
        self.frame = 0#当前帧数
        self.old_frame = -1#过去的帧数
        self.frame_width = 1#帧宽
        self.frame_height = 1#帧高。
        self.first_frame = 0#前帧
        self.last_frame = 0#后帧
        self.columns = 1#列数。
        self.last_time =0 #记录过去一帧的时间，方便与当前时间进行对比。
        self.direction = 0
        self.velocity = Point(0.0,0.0)#弹射方向。

    # 横坐标x属性
    def _getx(self): return self.rect.x
    def _setx(self,value): self.rect.x = value
    X = property(_getx,_setx)#说明X属性可读可写

    # 纵坐标y属性
    def _gety(self): return self.rect.y
    def _sety(self,value): self.rect.y = value
    Y = property(_gety,_sety)#说明Y属性可读可写

    #位置属性
    def _getpos(self): return self.rect.topleft
    def _setpos(self,pos): self.rect.topleft = pos
    position = property(_getpos,_setpos)#说明位置属性可读可写
        
    #该函数用于加载精灵序列图。
    def load(self, filename, width=0, height=0, columns=1):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.set_image(self.master_image, width, height, columns)

    def set_image(self, image, width=0, height=0, columns=1):
        self.master_image = image
        if width==0 and height==0:
            #说明图像宽高未设置，则获取图像宽高
            self.frame_width = image.get_width()
            self.frame_height = image.get_height()
        else:
            #使用已提供的宽高。
            self.frame_width = width
            self.frame_height = height
            rect = self.master_image.get_rect()
            self.last_frame = (rect.width//width) * (rect.height//height) - 1
        self.rect = Rect(0,0,self.frame_width,self.frame_height)
        self.columns = columns

    def update(self, current_time, rate=30):#第二个参数为当前时间，第三个参数为帧率。
        if self.last_frame > self.first_frame:
            #更新动画帧号
            if current_time > self.last_time + rate:#如果当前时间大于之前的时间+所设置帧率。
                self.frame += 1#帧数+1.
                if self.frame > self.last_frame:#如果月结
                    self.frame = self.first_frame
                self.last_time = current_time
        else:
            self.frame = self.first_frame

        #仅当当前框架改变时才构建
        if self.frame != self.old_frame:
            #计算单个帧左上角的x，y位置值
            frame_x = (self.frame % self.columns) * self.frame_width
            #用帧数目除以行数，然后在乘上帧的高度
            frame_y = (self.frame // self.columns) * self.frame_height
            #将计算好的x，y值传递给位置rect属性。
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)#实现精灵动画。
            self.old_frame = self.frame#更新过去帧

    #测试调试函数。
    def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + \
               "," + str(self.last_frame) + "," + str(self.frame_width) + \
               "," + str(self.frame_height) + "," + str(self.columns) + \
               "," + str(self.rect)

#Point类
class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    #横坐标x属性
    def getx(self): return self.__x
    def setx(self, x): self.__x = x
    x = property(getx, setx)#x属性可读可写

    #纵坐标y属性
    def gety(self): return self.__y
    def sety(self, y): self.__y = y
    y = property(gety, sety)#y属性可读可写

    #打印对象属性的属性信息，方便调试代码。
    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x) + \
            ",Y:" + "{:.0f}".format(self.__y) + "}"
    
