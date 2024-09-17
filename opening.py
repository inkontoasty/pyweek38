from constants import *

class IntroScene:
    def __init__(self, app):
        self.app = app
        self.img = pygame.image.load(pathjoin('assets','opening.png')).convert(24)
        self.rect = self.img.get_rect()
        self.introdone = False
        self.imgalpha = 256
        self.txttitle = getfont(72).render("hearts of betrayal",True,COL_TITLE)
        self.txtchoice = getfont(48).render("choose your country",True,COL_CHOICE)
        self.finlandrect = IMG_FINLAND.get_rect()
        self.bulgariarect = IMG_BULGARIA.get_rect()
        self.italyrect = IMG_ITALY.get_rect()
        self.titlerect = self.txttitle.get_rect()
        self.choicerect = self.txtchoice.get_rect()
        self.finlandrect.center = (250,500)
        self.bulgariarect = self.finlandrect.move((400, 0)) 
        self.italyrect = self.bulgariarect.move((400, 0)) 
        self.titlerect.center = (640, 100) 
        self.choicerect.center = (640, 250) 
        self.selrect = self.finlandrect 
        self.selected = ''

    def event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE and self.rect.top < self.rect.height-720:
                self.introdone = True #skip intro scene
        elif self.imgalpha == 0:
            if event.type == MOUSEMOTION: #country selection
                if self.finlandrect.collidepoint(event.pos):
                    self.selected = 'Finland'
                    self.selrect = self.finlandrect
                elif self.bulgariarect.collidepoint(event.pos):
                    self.selected = 'Bulgaria'
                    self.selrect = self.bulgariarect
                elif self.italyrect.collidepoint(event.pos):
                    self.selected = 'Italy'
                    self.selrect = self.italyrect
                else:
                    self.selected = ''
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and self.selected:
                    self.app.scene = SCENE_GAME
                    self.app.scenes[SCENE_GAME].reset(self.selected) #give it selected country

    def update(self):
        if not self.introdone:
            self.rect.y += 1
            if self.rect.top > self.rect.height-720:
                 self.introdone = True
        else:
            if self.imgalpha:
                self.imgalpha -= 2
                self.img.set_alpha(self.imgalpha)
                if not self.imgalpha:
                    self.app.mixer.play(MUSIC1, loop=True)

    def draw(self):
        self.app.screen.fill(COL_BG)
        if self.imgalpha:
            self.app.screen.blit(self.img, (0,0), self.rect)
        else:
            self.app.screen.blit(self.txttitle, self.titlerect)
            self.app.screen.blit(self.txtchoice, self.choicerect)
            self.app.screen.blit(IMG_FINLAND, self.finlandrect)
            self.app.screen.blit(IMG_BULGARIA, self.bulgariarect)
            self.app.screen.blit(IMG_ITALY, self.italyrect)
            if self.selected:
                pygame.draw.rect(self.app.screen, COL_SELBORDER, self.selrect, 20)

