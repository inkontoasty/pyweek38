import pygame
from pygame.locals import *
from os.path import join as pathjoin
import time

SCENE_INTRO = 0

class IntroScene:
    def __init__(self, app):
        self.app = app
        self.img = pygame.image.load(pathjoin('assets','opening.png'))
        self.rect = self.img.get_rect()
        self.now = time.time()

    def event(self, event):
        pass

    def update(self):
        if time.time()-self.now > 1/60:
            self.rect.y += 1
            self.now = time.time()


    def draw(self):
        self.app.screen.blit(self.img, (0,0), self.rect)

class App:
    def __init__(self):
        pygame.mixer.init()
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.scenes = [IntroScene(self)]
        self.scene = SCENE_INTRO

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                self.scenes[self.scene].event(event)
            self.scenes[self.scene].update()
            self.scenes[self.scene].draw()
            pygame.display.flip()

app = App()
app.run()
