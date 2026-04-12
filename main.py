from pygame import*

display.init()
mixer.init()
font.init()

clock = time.Clock()
mwWidth = 700
mwHigth = 500

end_game = False
finish = False

mw = display.set_mode((mwWidth, mwHigth))
display.set_caption('Ping pong')

# background = transform.scale(image.load('galaxy.jpg'), (mwWidth,mwHigth))
# mixer.music.load('space.ogg')
# mixer.music.set_volume(0.1)
# strike_effect = mixer.Sound('fire.ogg')
# strike_effect.set_volume(0.1)
# mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, ppicture, xcor, ycor, speed=0, width=20, height=75):
        super().__init__()
        self.ppicture = transform.scale(image.load(ppicture), (width, height))
        self.rect = self.ppicture.get_rect()
        self.rect.x = xcor
        self.rect.y = ycor
        self.speed = speed
    
    def reset(self):
        mw.blit(self.ppicture, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def go1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < mwWidth-75:
            self.rect.y += self.speed

    def go2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < mwWidth-75:
            self.rect.y += self.speed

player1 = Player('racket.png', 0, 213, 5)
player2 = Player('racket.png', 680, 213, 5)
ball = GameSprite('tenis_ball.png', 330, 230, 2, 40, 40)

while not end_game:
    for e in event.get():
        if e.type == QUIT:
            end_game = True

    if not finish:
        mw.fill((200, 255, 255))

    clock.tick(60)
    display.update()            