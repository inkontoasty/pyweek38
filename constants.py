import pygame
from pygame.locals import *
from os.path import join as pathjoin

SCENE_INTRO = 0
SCENE_GAME = 1
IMG_FINLAND = pygame.image.load(pathjoin('assets','finland.jpg'))
IMG_BULGARIA = pygame.image.load(pathjoin('assets','bulgaria.jpg'))
IMG_ITALY = pygame.image.load(pathjoin('assets','italy.jpg'))
COL_BG = (0, 84, 119)
COL_TITLE = (255, 100, 100)
COL_TXT = (0, 84, 119)
COL_TXT2 = (0, 119, 84)
COL_CHOICE = (255,255,255)
COL_SELBORDER = (0, 255, 255)
COUNTRIES = ['finland', 'germany', 'italy', 'serbia', 'bulgaria', 'romania', 'ukraine', 'belarus', 'lithuania', 'latvia', 'estonia', 'uzbekistan', 'krygyzstan', 'georgia', 'azerbaijian', 'turkmenistan', 'tajikstan', 'russia', 'kazakthstan']
COUNTRYCOLS = [(1, 7, 11), (0, 0, 0), (3, 10, 2), (6, 12, 10), (15, 15, 3), (10, 12, 14), (9, 4, 10), (11, 11, 13), (15, 8, 11), (15, 9, 9), (15, 12, 14), (13, 6, 4), (12, 5, 3), (14, 8, 7), (10, 5, 2), (9, 3, 6), (15, 6, 4), (12, 3, 3), (11, 1, 2)]
class Country:
    def __init__(self,money,troops,mindex):
        self.money = money
        self.troops = troops
        self.mindex = mindex
        self.allies = []
        self.war = []
        self.takenover = []
        self.owner = None
MUSIC1 = 0
getfont = lambda x: pygame.font.Font(pathjoin('assets','bebasnue.ttf'),x)

