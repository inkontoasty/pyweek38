from constants import *
from opening import IntroScene
from mixer import Mixer
from game import GameScene



class App:
    def __init__(self):
        pygame.init()
        self.mixer = Mixer()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1280, 720))
        self.scenes = [IntroScene(self), GameScene(self)]
        # self.map=CountryMap
        self.scene = SCENE_INTRO
        



    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                self.scenes[self.scene].event(event)

                if self.scene:
                    if event.type==cooldown_time:
                        
                        self.scenes[self.scene].country_attack()

            
            self.scenes[self.scene].update()
            self.scenes[self.scene].draw()
            
            if pygame.key.get_just_pressed()[pygame.K_a]:
                
                self.scenes[self.scene].attack()
            
            
            
            
            
            
            pygame.display.flip()
            self.clock.tick(60)
            

app = App()
app.run()
