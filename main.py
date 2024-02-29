from pygame import *
from random import randint

class Baza:
    def __init__(self,x,y,w,h,filename,heath):
        self.heath = heath
        self.rect = Rect(x,y,w,h) #270 - ширина, 300 - высота
        self.image = transform.scale(image.load(filename),(w,h))
        self.x_speed, self.y_speed = 0, 0

    def draw(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

class Hero(Baza):
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        self.draw()

    def attack(self,aim):
        dx = abs(self.rect.x - aim.rect.x)
        dy = abs(self.rect.y - aim.rect.y)
        if dx > 100 and dy > 100:
            print('слишком далеко')
        else:
            print('удар')

class Enemy(Baza):
    def update(self):
        if self.rect.right > W:
            self.x_speed = -1
        
        if self.rect.x < 0:
            self.x_speed = 1

        self.rect.x += self.x_speed
        self.draw()

class Enemy_finder(Baza):
    def update(self,player):
        if self.rect.x > player.rect.x:
            self.x_speed = -1
        if self.rect.x < player.rect.x:
            self.x_speed = 1
        if self.rect.x == player.rect.x:
            self.x_speed = 0

        self.rect.x += self.x_speed
        self.draw()

class Wall_picture(Baza):
    def update(self):
        #мб тут проверки стокновений?
        self.draw()

class Wall_color:
    def __init__(self,x,y,w,h,color):
        self.rect = Rect(x,y,w,h)
        self.color = color

    def draw(self):
        draw.rect(win,self.color,self.rect)
    
    def update(self):
        self.draw()

W,H = 1000, 1000
#win = display.set_mode((1000,500),flags=FULLSCREEN) 
win = display.set_mode((W,H))
display.set_caption('Моя игра....')

background = image.load('bg.jpg')
background = transform.scale(background,(W,H))

cat = Hero(x=400,y=200,w=100,h=100,filename='cat.jpg',heath=100)
dragon = Enemy_finder(x=500,y=600,w=400,h=400,filename='dragon.png',heath=100)
#dragon.x_speed = -1

wall1 = Wall_color(x=100,y=100,w=50,h=500,color=(255,255,255))
wall2 = Wall_picture(x=300,y=100,w=50,h=500,filename='bricks.jpg',heath=1)
wall3 = Wall_picture(x=300,y=100,w=500,h=50,filename='bricks.jpg',heath=1)

while True:
    win.blit(background,(0,0))
    cat.update()
    
    dragon.update(cat)

    wall1.update()
    wall2.update()
    wall3.update()

    for e in event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            exit()

        if e.type == KEYDOWN and e.key == K_RIGHT:
            cat.x_speed += 3
        
        if e.type == KEYDOWN and e.key == K_LEFT:
            cat.x_speed -= 3

        if e.type == KEYDOWN and e.key == K_UP:
            cat.y_speed -= 3
        
        if e.type == KEYDOWN and e.key == K_DOWN:
            cat.y_speed += 3

        

    display.update()
