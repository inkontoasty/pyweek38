from constants import *
import time

class Mixer:
    def __init__(self):
        pygame.mixer.init()
        self.musicplaying = -1
        self.musicdone = 0
        self.sounds = [pygame.mixer.Sound(pathjoin("assets","music1.mp3"))]

    def play(self, sound, loop=False):
        self.sounds[sound].play()
        self.musicdone = time.time() + self.sounds[sound].get_length() if loop else 1e9
        self.musicplaying = MUSIC1

    def update(self):
        if self.musicplaying>=0 and time.time() > self.musicdone:
            self.play_music1()
