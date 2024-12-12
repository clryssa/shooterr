#Create your own shooter
from pygame import*
from random import randint

#musik
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()


clock = time.Clock()
run = True
finish = False
fps = 60
score = 0

#mengatur ukuran sprite di game
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width,height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

#mengerakan roket
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
#menembak peluru
    def fire(self):
        bullet = Bullet('lsr warna.png',self.rect.centerx, self.rect.top, 10,35,30)
        bullets.add(bullet)

#class musuh memunculkn alien 
miss = 0
class Enemy (GameSprite):
    def update (self):
        global miss
        self.rect.y += self.speed
        if self.rect.y >= win_height:
            self.rect.y = 2 
            self.rect.x = randint(5, win_width - 40)
            self.speed = randint(1,5)
            miss += 1

class Asteroid (GameSprite):
    def update (self):
        self.rect.y += self.speed
        if self.rect.y >= win_height:
            self.rect.y = 2 
            self.rect.x = randint(5, win_width - 40)
            self.speed = randint(1,5)

#clas peluru
class Bullet (GameSprite):
    def update (self):
        self.rect.y -= self.speed


#game scene:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('shoooter Game')
background = transform.scale(image.load('bg angkasa.jpg'),(700, 500))

#game karakter roket
player = Player ('astroboy.png', 5, win_height - 139,5, 100,150)

#memunculkan alien tanpa batas
enemy = sprite.Group()
for i in range(5):
    ufo = Enemy('meteoroid.png', randint(5,win_width - 60 ),randint(-4,-2),randint(1,5),150,100)
    enemy.add(ufo)
mixer.music.set_volume(0.3)

teor = sprite.Group()
for i in range(5):
    aste = Asteroid('asteroid.png', randint(5,win_width - 60 ),randint(-4,-2),randint(1,5),100,50)
    teor.add(aste)

#memunculkan tulisan 
font.init()
font1 = font.SysFont('Arial', 26)
font2 = font.SysFont('Arial', 66)
you_lose = font2.render('YOU LOSE', 1,(255,255,255))
you_win = font2.render('YOU WIN', 1,(255,255,255))


#memunculkn variabel pluru
bullets = sprite.Group()

#variabel score
score = 0

finish = False

#jika proyek dijlankan
while run:
#membuat tanda exit
    for e in event.get():
        if e.type == QUIT:
            run = False
#saat spsi d tkn plru klar
        if e.type == KEYDOWN:
            keys = key.get_pressed()
            if keys[K_SPACE]:
                player.fire()

        if not finish:

            text_lose = font1.render('Alien terlewat: ' + str(miss),1,(255,255,255))
            text_score = font1.render('Score: ' + str(score),1,(255,255,255))
            window.blit((background),(0,0))
            window.blit(text_lose,(5,20))
            window.blit(text_score,(5,40))

            if miss > 5:
                finish = True
                window.blit(you_lose,(win_width/3.3, win_height/2))

            if score > 5:
                finish = True
                window.blit(you_win,(win_width/3.3, win_height/2))

            collides = sprite.groupcollide(enemy, bullets, True, True)
            collides_teor = sprite.groupcollide(teor, bullets, False, True)
            if collides:
                ufo = Enemy('meteoroid.png', randint(5, win_width - 40), 2, randint(1,5),150,100)
                enemy.add(ufo)
                score += 1

            player.reset()
            player.update()

            enemy.draw(window)
            enemy.update()

            teor.draw(window)
            teor.update()

            bullets.draw(window)

            bullets.update()

            display.update()
            clock.tick(fps)
            

