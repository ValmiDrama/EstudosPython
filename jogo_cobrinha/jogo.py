# pip install pygame
import pygame
import sys
from cobrinha import Cobra
from comida import Comida
import time
from configuracao import *


cobra = Cobra()
comida = Comida()
posicao_comida = comida.posicao

jogando = True
while jogando:
    # RGB - Red, Green, Blue - (255,255,255)
    tela.fill((119,136,153))    
    tela.blit(bgImg, (0,0))
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # se uma tecla for pressionada (control)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                 cobra.muda_direcao('DIREITA')
            if event.key == pygame.K_UP:
                 cobra.muda_direcao('CIMA')
            if event.key == pygame.K_DOWN:
                 cobra.muda_direcao('BAIXO')
            if event.key == pygame.K_LEFT:
                 cobra.muda_direcao('ESQUERDA')

    posicao_comida = comida.gera_nova_comida()

    # se a cobra comeu
    if cobra.move(posicao_comida):
        comida.devorada = True
        pontuacao += 1
        
    
    if cobra.verifica_colisao():
        gamer_over = fonteH1.render('GAME OVER', True, (255,255,255))
        tela.blit(gamer_over, (140,250))
        
        pontos = fonteH2.render(f'Pontuação: {pontuacao}', True, (255,255,255))
        tela.blit(pontos, (150,280))

        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    # texto da pontuacao
    pontos = fonteH3.render(f'{nomePlayer} Pontuação: {pontuacao}', True, (255,255,255))
    tela.blit(pontos, (220,10))
    # desenha cobra
    for pos in cobra.corpo:
        pygame.draw.rect(tela, pygame.Color(200,200,200),
                               # esquerda, cima, largura, altura
                               pygame.Rect(pos[0], pos[1], 10, 10))

    # desenha comida
    pygame.draw.rect(tela, pygame.Color(242,79,0),
                     pygame.Rect(posicao_comida[0],posicao_comida[1],10,10))

    # atualiza a tela
    pygame.display.update()

    # FPS - Frames por Segundo - +1 nivelc+    
    tempo.tick((10+nivel))
