from webbrowser import BackgroundBrowser
import pygame

#Dimencoes:
dimX = 400
dimY = 600

# background
bgImg = pygame.image.load('img/backgraund.jpg')

# iniciar fonte
pygame.font.init()
fonteH1 = pygame.font.SysFont('Kdam Thmor Pro', 30)
fonteH2 = pygame.font.SysFont('Kdam Thmor Pro', 22)
fonteH3 = pygame.font.SysFont('Kdam Thmor Pro', 16)

# inicializar o pygame
pygame.init()
TAM_TELA = (dimX,dimY)
tela = pygame.display.set_mode(TAM_TELA)
pygame.display.set_caption("ValmiDrama - Snakers!")

# cronômetro/tempo
tempo = pygame.time.Clock()

# players
nomePlayer = 'Player'
pontuacaoPlayer = 0
nivel = 5
pontuacao = pontuacaoPlayer

