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
COL_CHOICE = (255,255,255)
COL_SELBORDER = (0, 255, 255)
FINLAND = 1
BULGARIA = 2
ITALY = 3
MUSIC1 = 0
getfont = lambda x: pygame.font.Font(pathjoin('assets','bebasnue.ttf'),x)

