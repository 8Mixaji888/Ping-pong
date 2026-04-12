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

while not end_game:
    for e in event.get():
        if e.type == QUIT:
            end_game = True

    if not finish:
        mw.fill((200, 255, 255))

    clock.tick(60)
    display.update()            