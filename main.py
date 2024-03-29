from pygame import *
from random import randint

class Baza(sprite.Sprite):
    def __init__(self,x,y,w,h,heath,filename):
        super().__init__()
        self.heath = heath
        self.rect = Rect(x,y,w,h)
        self.image = transform.scale(image.load(filename),(w,h))
        self.x_speed, self.y_speed = 0, 0

    def draw(self):
        win.blit(self.image, (self.rect.x,self.rect.y))    

class Hero(Baza):
    def update (self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        #print(self.x_speed,self.y_speed)
        touched = sprite.spritecollide(self,walls,False)
        if self.x_speed > 0:
            for wall in touched:
                self.rect.right = min(wall.rect.x,self.rect.right)
            
            if self.rect.right > W: self.rect.right = W #правый край экрана

        if self.x_speed < 0:  
            for wall in touched:  #проверка стен (4 раза в разных условиях)
                self.rect.x = max(wall.rect.right,self.rect.x)
            
            if self.rect.x < 0: self.rect.x = 0 #левый край экрана

        if self.y_speed > 0:
            for wall in touched:
                self.rect.bottom = min(wall.rect.y,self.rect.bottom)

        if self.y_speed < 0:    
            for wall in touched:
                self.rect.y = max(wall.rect.bottom,self.rect.y)

        touched = sprite.spritecollide(self,enemies,False)
        if touched:
            global game_mode
            game_mode = 'sad finish'

        self.draw()

class Enemy(Baza):
    def update(self):
        if self.rect.right > W:
            self.x_speed = -2

        if self.rect.x < 0:
            self.x_speed = 2
        
        self.rect.x += self.x_speed
        self.draw()

class Wall_picture(Baza):
    def __init__(self,x,y,w,h,heath,filename):
        super().__init__(x,y,w,h,heath,filename)
        walls.add(self)

    def update(self):
        self.draw()

class Wall_color(sprite.Sprite):
    def __init__(self,x,y,w,h,color):
        super().__init__()
        self.rect = Rect(x,y,w,h)
        self.color = color
        walls.add(self)

    def draw(self):
        draw.rect(win,self.color,self.rect)
    
    def update(self):
        self.draw()

W,H = 1400, 800
win = display.set_mode((W,H))
display.set_caption('Apex')

backgroung = image.load('fon.jpg')
backgroung = transform.scale(backgroung,(W,H))

sad_backgroung = image.load('sad_finish.jpg')

enemies = sprite.Group()
drow_range = Enemy(x=200,y=200,w=300,h=250,filename ='drowka.png',heath=100)
enemies.add(drow_range)

dragon_knight = Hero(x=700,y=200,w=200,h=250,filename ='dkmodel.png',heath=150)
drow_range.x_speed = -1

walls = sprite.Group()
Wall_color(x=100,y=100,w=50,h=500,color =(255,255,255))
Wall_color(x=500,y=100,w=50,h=500,color =(255,255,255))
Wall_color(x=100,y=100,w=800,h=50,color =(255,255,255))

game_mode = 'game'

while True:
    if game_mode == 'game':
        win.blit(backgroung,(0,0))

        dragon_knight.update()
        drow_range.update()

        walls.update()
    
    if game_mode == 'sad finish':
        win.blit(sad_backgroung,(0,0))

    for e in event.get():
        if e.type == QUIT:
            exit()

        if e.type == KEYDOWN and e.key == K_RIGHT:
            dragon_knight.x_speed = 1
            dragon_knight.y_speed = 0

        if e.type == KEYDOWN and e.key == K_LEFT:
            dragon_knight.x_speed = -1
            dragon_knight.y_speed = 0

        if e.type == KEYDOWN and e.key == K_UP:
            dragon_knight.y_speed = -1
            dragon_knight.x_speed = 0

        if e.type == KEYDOWN and e.key == K_DOWN:
            dragon_knight.y_speed = 1
            dragon_knight.x_speed = 0

        if e.type == KEYUP:
            if e.key == K_DOWN or e.key == K_UP:
                dragon_knight.y_speed = 0
            
            if e.key == K_RIGHT or e.key == K_LEFT:
                dragon_knight.x_speed = 0


    display.update()
