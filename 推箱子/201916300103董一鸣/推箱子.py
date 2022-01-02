# 引入pygame库
import pygame, sys, os
from pygame.locals import *

# 移动箱子在地图上的位置，level为地图列表，i为箱子的位置
def move_box(level, i):
    # 如果位置原来为空间或人，则标为箱子，否则标为箱子和目标点重合效果        
    if level[i] == '-' or level[i] == '@':                             
        level[i] = '$'                                                  
    else:                                                                          
        level[i] = '*'

# 移动人在地图中的位置，level为地图列表，i为人的位置
def move_man(level, i):
    # 如果目标位置为空间或箱子，则替换成人
    if level[i] == '-' or level[i] == '$':
        level[i]='@'
    # 否则标成人和目标点重合
    else:
        level[i]='+'

# 移动后的位置重置，人移动走了位置需要重标为空间或目标点
def move_floor(level, i):
    # 如果原来为人或箱子，则标为空间，否则标为目标点
    if level[i] == '@' or level[i] == '$':
        level[i]='-'
    else:
        level[i]='.'

# 获取地图中移动的位移量：d为移动的方向，width为游戏窗口宽度
def get_offset(d, width):
    offset_map = { 'l': -1, 'u': -width, 'r': 1, 'd': width }
    return offset_map[d.lower()]

class Sokoban:

    # 初始化推箱子游戏
    def __init__(self):
        # 设置地图
        self.level = list(
            "----#####----------"
            "----#---####-------"
            "----#$-----###-----"           
            "--###--$-----#-----"
            "--#--$-$-#-$-#-----"
            "###-#-##-#---######"
            "#---#-##-#####--..#"
            "#-$--$---------...#"
            "#####-###-#@##--..#"
            "----#-----#########"
            "----#######--------")

        # 设置地图的宽度和高度以及人在地图中的位置（地图列表中的索引值）
        # 共19列
        self.w = 19

        # 共11行
        self.h = 11

        # 人的初始化位置在self.level[163]
        self.man = 163

        # 使用solution记录每次移动，可用来实现撤销操作undo
        self.solution = []

        # 记录推箱子的次数
        self.push = 0

        # 使用todo记录撤销操作，用来实现重做操作redo
        self.todo = []

    # 画图，根据地图level将内容显示到pygame的窗口中
    def draw(self, screen, skin):

        # 获取每个图像元素的宽度
        w = skin.get_width() / 4

        # 遍历地图level中的每个字符元素
        for i in range(0, self.w):
            for j in range(0, self.h):

                # 获取地图中的第j行第i列
                item = self.level[j*self.w + i]

                # 该位置显示为墙#
                if item == '#':
                    # 使用pygame的blit方法将图像显示到指定位置，
                    # 位置坐标为(i*w, j*w)，图像在skin中的坐标及长宽为(0,2*w,w,w)
                    screen.blit(skin, (i*w, j*w), (0,2*w,w,w))
                # 该位置显示为空间-    
                elif item == '-':
                    screen.blit(skin, (i*w, j*w), (0,0,w,w))
                # 该位置显示为人：@
                elif item == '@':
                    screen.blit(skin, (i*w, j*w), (w,0,w,w))
                # 该位置显示为箱子：$
                elif item == '$':
                    screen.blit(skin, (i*w, j*w), (2*w,0,w,w))
                # 该位置显示为目标点：.
                elif item == '.':
                    screen.blit(skin, (i*w, j*w), (0,w,w,w))
                # 该位置显示为人和目标点重合效果
                elif item == '+':
                    screen.blit(skin, (i*w, j*w), (w,w,w,w))
                # 该位置显示为箱子放到了目标点的效果
                elif item == '*':
                    screen.blit(skin, (i*w, j*w), (2*w,w,w,w))

    # 移动操作，d用来表示移动的方向
    def move(self, d):
        # 调用内部函数_move实现移动操作
        self._move(d)
        # 重置todo列表为空，一旦有移动操作则重做操作失效，
        # 重做操作只有在撤销操作后才可以被激活
        self.todo = []

    # 内部移动操作函数：用来更新移动操作后各个元素在地图中的位置变化，d表示移动的方向   
    def _move(self, d):
        # 获得移动在地图中的位移量
        h = get_offset(d, self.w)

        # 如果移动的目标区域为空间或目标点，则只需要移动人即可
        if self.level[self.man + h] == '-' or self.level[self.man + h] == '.':
            # 移动人到目标位置
            move_man(self.level, self.man + h)
            # 人移动后设置人原来的位置
            move_floor(self.level, self.man)
            # 人所在的新位置
            self.man += h
            # 将移动操作存入solution
            self.solution += d

        # 如果移动的目标区域为箱子，则需要移动箱子和人
        elif self.level[self.man + h] == '*' or self.level[self.man + h] == '$':
            # 箱子下一个位置和人所在位置的位移
            h2 = h * 2
            # 需要判断箱子下一个位置为空间或目标点才可以移动
            if self.level[self.man + h2] == '-' or self.level[self.man + h2] == '.':
                # 移动箱子到目标点
                move_box(self.level, self.man + h2)
                # 移动人到目标点
                move_man(self.level, self.man + h)
                # 重置人当前位置
                move_floor(self.level, self.man)
                # 设置人所在的位置
                self.man += h
                # 将移动操作标为大写字符表示该步骤推了箱子
                self.solution += d.upper()
                # 将推箱子步数加一
                self.push += 1

    # 撤销操作：撤销前一次移动的步骤           
    def undo(self):
        # 判断是否已经有移动记录
        if self.solution.__len__()>0:
            # 将移动记录存储到todo列表中，用来实现重做操作
            self.todo.append(self.solution[-1])
            # 删除移动记录
            self.solution.pop()

            # 获取撤销操作要移动的位移量：为上次移动的位移量取反
            h = get_offset(self.todo[-1],self.w) * -1

            # 判断如果该操作步骤没有推箱子，仅是人的移动
            if self.todo[-1].islower():
                # 将人回退到原来的位置
                move_man(self.level, self.man + h)
                # 设置人当前位置
                move_floor(self.level, self.man)
                # 设置人在地图中的位置
                self.man += h
            else:
                # 如果该步骤推了箱子，则依次重新移动人，箱子，对应_move中相关操作
                move_floor(self.level, self.man - h)
                move_box(self.level, self.man)
                move_man(self.level, self.man + h)
                self.man += h
                self.push -= 1

    # 重做操作：当撤销操作执行后被激活，重新移动到撤销前的位置           
    def redo(self):
        # 判断如果记录了撤销操作才执行
        if self.todo.__len__()>0:
            # 重新移动撤销的步骤
            self._move(self.todo[-1].lower())
            # 将该条记录删除
            self.todo.pop()

def main():

    # 启动并初始化pygame
    pygame.init()
    # 设置pygame显示窗口大小为宽400，高300像素
    screen = pygame.display.set_mode((400,300))

    # 加载图像元素，所有图像元素都写在一个文件中
    skinfilename = os.path.join('borgar.png')
    try:
        skin = pygame.image.load(skinfilename)
    except pygame.error as msg:
        print('cannot load skin')
        raise SystemExit(msg)
    skin = skin.convert()

    # 设置窗口显示的背景颜色，使用文件中坐标为(0,0)的元素
    screen.fill(skin.get_at((0,0)))

    # 设置窗口标题显示的内容
    pygame.display.set_caption('Sokoban')

    # 创建推箱子游戏对象，并初始化窗口界面
    skb = Sokoban()
    skb.draw(screen,skin)

    #
    clock = pygame.time.Clock()
    pygame.key.set_repeat(200,50)

    # 游戏主循环
    while True:
        clock.tick(60)

        # 获取游戏事件
        for event in pygame.event.get():
            # 退出游戏操作
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # 键盘操作
            elif event.type == KEYDOWN:
                # 向左移动
                if event.key == K_LEFT:
                    # 移动操作，并重新画图
                    skb.move('l')
                    skb.draw(screen,skin)
                # 向上移动   
                elif event.key == K_UP:
                    skb.move('u')
                    skb.draw(screen,skin)
                # 向右移动
                elif event.key == K_RIGHT:
                    skb.move('r')
                    skb.draw(screen,skin)
                # 向下移动
                elif event.key == K_DOWN:
                    skb.move('d')
                    skb.draw(screen,skin)
                # 撤销操作
                elif event.key == K_BACKSPACE:
                    skb.undo()
                    skb.draw(screen,skin)
                # 重做操作
                elif event.key == K_SPACE:
                    skb.redo()
                    skb.draw(screen,skin)

        # 每次操作后都要更新窗口界面的显示内容
        pygame.display.update()

        # 设置窗口的标题显示的内容：显示已操作的步数及推箱子的步数
        pygame.display.set_caption(skb.solution.__len__().__str__() + '/' + skb.push.__str__() + ' - Sokoban')

# 主函数
if __name__ == '__main__':
    main()