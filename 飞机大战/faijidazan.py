import pygame
from random import randint
import math

print("按下空格建发射子弹")
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("飞机大战")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
bgimg = pygame.image.load('bg.png')
enemyimg = pygame.image.load('enemy.png')

pygame.mixer.music.load('bg.wav')
pygame.mixer.music.play(-1)

bomb_sound = pygame.mixer.Sound('exp.wav')

playerimg = pygame.image.load('player.png')
playerX = 400
playerY = 500
playStep = 0

score = 0
font = pygame.font.Font('freesansbold.ttf', 35)

def show_score():
    text = f"score:{score}"
    score_render = font.render(text, True, (0, 200, 255))
    screen.blit(score_render, (10, 10))

is_over = False
over_font = pygame.font.Font('freesansbold.ttf', 64)
def check_is_over():
    if is_over:
        text = "Game Over"
        render = over_font.render(text, True, (255, 50, 10))
        screen.blit(render, (230, 250))

number_of_enemies = 10
class Enemy():
    def __init__(self):
        self.img = pygame.image.load('enemy.png')
        self.x = randint(100, 600)
        self.y = randint(50, 250)
        self.step = randint(2, 5)
    def reset(self):
        self.x = randint(100, 600)
        self.y = randint(50, 250)

Enemies = []
for i in range(number_of_enemies):
    Enemies.append(Enemy())

def show_enemy():
    global is_over
    for e in Enemies:
        screen.blit(e.img, (e.x, e.y))
        e.x += e.step
        if (e.x > 736 or e.x < 0):
            e.step *= -1
            e.y += 40
            if e.y > 450:
                is_over = True
                print("游戏结束啦！")
                Enemies.clear()


def distance(bx, by, ex, ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a*a + b*b)

bullets = []

class Bullet():
    def __init__(self):
        self.img = pygame.image.load('bullet.png')
        self.x = playerX
        self.y = playerY + 10
        self.step = 10
    def hit(self):
        global score
        for e in Enemies:
            if (distance(self.x, self.y, e.x, e.y) < 40):
                bomb_sound.play()
                bullets.remove(self)
                e.reset()
                score += 1

def show_bullet():
    for bull in bullets:
        screen.blit(bull.img, (bull.x, bull.y))
        bull.hit()
        bull.y -= bull.step
        if bull.y < 0:
            bullets.remove(bull)

def distance_two(bx, by, ex, ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a*a + b*b)

bullets_two = []

class Bullet_two():
    def __init__(self):
        self.img = pygame.image.load('bullet.png')
        self.x = playerX + 30
        self.y = playerY + 10
        self.step = 10
    def hit_two(self):
        for d in Enemies:
            if (distance_two(self.x, self.y, d.x, d.y) < 40):
                bomb_sound.play()
                bullets_two.remove(self)
                d.reset()

def show_bullet_two():
    for b in bullets_two:
        screen.blit(b.img, (b.x, b.y))
        b.hit_two()
        b.y -= b.step
        if b.y < 0:
            bullets_two.remove(b)

def move_player():
    global playerX
    playerX += playStep
    while playerX > 736:
        playerX -= 6
    while playerX < 0:
        playerX +=6

running = True
while running:
    screen.blit(bgimg, (0, 0))
    show_score()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playStep = 6
            elif event.key == pygame.K_LEFT:
                playStep = -6
            elif event.key == pygame.K_SPACE:
                print("发射子弹....")
                bullets.append(Bullet())
                bullets_two.append(Bullet_two())
        if event.type == pygame.KEYUP:
                playStep = 0
    screen.blit(playerimg, (playerX, playerY))
    move_player()
    show_bullet()
    show_bullet_two()
    show_enemy()
    check_is_over()
    pygame.display.update()
