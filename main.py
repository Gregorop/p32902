from pygame import *

class Hero:
    def __init__(self,x,y,w,h,filename,heath):
        self.heath = heath
        self.rect = Rect(x,y,w,h) #270 - ширина, 300 - высота
        self.image = transform.scale(image.load(filename),(w,h))
        self.x_speed, self.y_speed = 0, 0

    def draw(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

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

W,H = 1000, 1000
#win = display.set_mode((1000,500),flags=FULLSCREEN) 
win = display.set_mode((W,H))
display.set_caption('Моя игра....')

background = image.load('bg.jpg')
background = transform.scale(background,(W,H))

cat = Hero(x=400,y=200,w=100,h=100,filename='cat.jpg',heath=100)
dragon = Hero(x=500,y=600,w=400,h=400,filename='dragon.png',heath=100)

while True:
    win.blit(background,(0,0))
    cat.update()
    
    dragon.draw()

    for e in event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            exit()

        if e.type == KEYDOWN and e.key == K_RIGHT:
            cat.x_speed += 1
        
        if e.type == KEYDOWN and e.key == K_LEFT:
            cat.x_speed -= 1

        if e.type == MOUSEBUTTONDOWN:
            dragon.attack(cat)

    display.update()