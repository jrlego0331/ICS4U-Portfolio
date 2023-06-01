import pygame as pg

pg.mixer.init()

pg.mixer.music.load('BGM.mp3')
pg.mixer.music.play(-1)

match_sound = pg.mixer.Sound('resources/mixkit-arcade-video-game-bonus-2044.wav')
penalty_sound = pg.mixer.Sound('resources/mixkit-small-hit-in-a-game-2072.wav')

pg.mixer.Sound.play(match_sound)
pg.mixer.Sound.play(penalty_sound)


#Or:
class gameSound():
    def __init__(self):
        pg.mixer.init()
        self.match_sound = pg.mixer.Sound('resources/mixkit-arcade-video-game-bonus-2044.wav')
        self.penalty_sound = pg.mixer.Sound('resources/mixkit-small-hit-in-a-game-2072.wav')

    def setBGM(self, music):
        pg.mixer.music.load(music)
        pg.mixer.music.play(-1)

    def scoreUpSound(self):
        pg.mixer.Sound.play(self.match_sound)

    def scoreDeductSound(self):
        pg.mixer.Sound.play(self.penalty_sound)


sound = gameSound()
sound.setBGM('resources/8-bit-dream-land-142093.mp3')
sound.scoreUpSound()
sound.scoreDeductSound()