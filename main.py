from constants import *
from opening import IntroScene
from mixer import Mixer

class GameScene:
    def __init__(self, app):
        self.app = app
        self.mapimg = pygame.image.load(pathjoin("assets","map.png"))
        self.selfont = getfont(32)
        self.selimg = None
        self.moneyimg = None
        self.troopsimg = None
        self.mindeximg = None
        self.maprect = Rect(234, 85, 1046, 636)
        self.stats = STARTINGSTATS

    def reset(self, selected):
        self.selected = selected
        self.hovering = None
        self.updatetopbar()

    def updatetopbar(self):
        if self.hovering:
            self.selimg = self.selfont.render(self.hovering, True, COL_TXT)
            stats = self.stats[COUNTRIES.index(self.hovering)]
        else:
            stats = self.stats[COUNTRIES.index(self.selected)]
            self.selimg = self.selfont.render(f"you are {self.selected}", True, COL_TXT)
        self.moneyimg = self.selfont.render(f"money: ${stats[1]}K", True, COL_TXT2)
        self.troopsimg = self.selfont.render(f"troops: {stats[0]} units", True, COL_TXT2)
        self.mindeximg = self.selfont.render(f"military index: {stats[2]}%", True, COL_TXT2)

    def event(self, event):
        if event.type == MOUSEMOTION:
            if self.maprect.collidepoint(event.pos):
                col = self.mapimg.get_at(event.pos)
                col = (col[0]//16, col[1]//16, col[2]//16)
                if col in COUNTRYCOLS:
                    self.hovering = COUNTRIES[COUNTRYCOLS.index(col)]
                    self.updatetopbar()
                elif self.hovering:
                    self.hovering = None
                    self.updatetopbar()
            elif self.hovering:
                self.hovering = None
                self.updatetopbar()

    def update(self):
        pass

    def draw(self):
        self.app.screen.blit(self.mapimg, (0, 0))
        self.app.screen.blit(self.selimg, (250, 10))
        self.app.screen.blit(self.moneyimg, (250, 40))
        self.app.screen.blit(self.troopsimg, (450, 10))
        self.app.screen.blit(self.mindeximg, (450, 40))

class App:
    def __init__(self):
        pygame.init()
        self.mixer = Mixer()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720))
        self.scenes = [IntroScene(self), GameScene(self)]
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
            self.clock.tick(60)

app = App()
app.run()
