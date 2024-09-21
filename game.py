from random import randint , randrange 
import random
from time import time
from constants import *

class GameScene:  # to be refactored
    def __init__(self, app):
        self.app = app
        self.tick = time() + 3  # update countries every 3 seconds
        self.mapimg = pygame.image.load(pathjoin("assets","map.png"))  # the background
        self.font = getfont(32)  # see constants.py
        self.selimg = None  # text surfaces to be rendered later
        self.moneyimg = None
        self.troopsimg = None
        self.mindeximg = None
        self.editingmindex = False  # hovering on miliray index text?
        self.alliesimg = self.font.render("allies:", True, COL_TXT)  # constant text
        self.warimg = self.font.render("war: ", True, COL_TXT2)
        self.maprect = Rect(234, 85, 1046, 636)  # area on background image not blank
        # give random countries for now - will be changed to be more realistic
        self.countries = {
                country:Country(randint(1,5000),randint(1,500),randint(1,45))
                for country in COUNTRIES
            }
        self.globaleconomy = 20  # money all countries earn every tick

        


    def reset(self, selected):  # runs after opening screen
        self.selected = selected  # our chosen country

        NATIONS.pop(NATIONS.index(self.selected))
        self.hovering = None
        self.updatetopbar()

    def updatetopbar(self):  # display stats
        if self.hovering and self.hovering != self.selected:
            self.selimg = self.font.render(self.hovering, True, COL_TXT)
            stats = self.countries[self.hovering]
        else:
            stats = self.countries[self.selected]
            self.selimg = self.font.render(f"{self.selected} (you)", True, COL_TXT)
        self.moneyimg = self.font.render(f"money: ${stats.money}M", True, COL_TXT2)
        self.troopsimg = self.font.render(f"troops: {stats.troops}K units", True, COL_TXT2)
        if self.editingmindex:
            self.mindeximg = self.font.render(f"scroll to edit: {stats.mindex}%", True, COL_TITLE)
        else:
            self.mindeximg = self.font.render(f"military index: {stats.mindex}%", True, COL_TXT)

    def event(self, event):
        if event.type == MOUSEMOTION:
            # update top bar based on country hovering on
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

            # updating your military index?
            if not self.hovering and Rect(450,40,250,30).collidepoint(event.pos):
                self.editingmindex = True
                self.updatetopbar()
            elif self.editingmindex:
                self.editingmindex = False
                self.updatetopbar()
        elif event.type == MOUSEWHEEL:
            self.countries[self.selected].mindex = max(0,min(100,self.countries[self.selected].mindex+event.y))
            self.updatetopbar()
    
    
    def attack(self):

        if self.hovering and self.hovering != self.selected :
            player_country=self.countries[self.selected]
            attackrd_country=self.countries[self.hovering]

            if player_country.troops>attackrd_country.troops:

                player_country.troops=player_country.troops-attackrd_country.troops+(attackrd_country.troops)//3
                player_country.money+=attackrd_country.money//3

                attackrd_country.owner=self.selected

                player_country.takenover.append(self.hovering)

                attackrd_country.troops = 0
                attackrd_country.money = 0
                attackrd_country.mindex = 0

                attackrd_country.allies.clear()
                attackrd_country.war.clear()

                

                self.updatetopbar()
            
            else:
                lost_troops = attackrd_country.troops // 2  
                player_country.troops -= lost_troops
                player_country.troops = max(player_country.troops, 0)
        

    

    def country_attack(self):

        
        

        
    #created a new list identical to COUNTRIES to use here 

        random_cont1=NATIONS[randrange(0,11)]
        random_cont2=COUNTRIES[randrange(0,12)]

        

        attacking_country=self.countries[random_cont1]
        

        defending_country=self.countries[random_cont2]
        

        if attacking_country!=defending_country:
            

            if attacking_country.troops>defending_country.troops:
                

                if random.random()<=0.469:
                    
                    
                    #attack a neighbouring country if probability is correct 

                    attacking_country.troops=attacking_country.troops-defending_country.troops+(defending_country.troops)//3
                    attacking_country.money+=defending_country.money//3

                    defending_country.owner=attacking_country

                    attacking_country.takenover.append(defending_country)

                    defending_country.troops = 0
                    defending_country.money = 0
                    defending_country.mindex = 0

                    defending_country.allies.clear()
                    defending_country.war.clear()

                    self.updatetopbar()

                    #rest of the function is same as the attack function , needs a bit more optimization
                    
            



   
    








    def update(self):
        if time() > self.tick:
            self.tick = time() + 3
            for name,country in self.countries.items():  # update their troops/economy
                country.money += int(country.money*self.globaleconomy/100)
                country.money -= int(country.money*country.mindex/100)
                country.troops += int(country.money * country.mindex / 1000)
                if randint(1, 10) == 1:  # randomly update their index
                    country.mindex = max(0,min(100,country.mindex + randint(-2,2)))
            self.updatetopbar()


    def draw(self):
        self.app.screen.blit(self.mapimg, (0, 0))
        self.app.screen.blit(self.selimg, (250, 10))
        self.app.screen.blit(self.moneyimg, (250, 40))
        self.app.screen.blit(self.troopsimg, (450, 10))
        self.app.screen.blit(self.mindeximg, (450, 40))
        self.app.screen.blit(self.alliesimg, (700, 10))
        self.app.screen.blit(self.warimg, (700, 40))

