# pip install pygame
import pygame
import sys
from cobrinha import Cobra
from comida import Comida
import time
from configuracao import *

# iniciar fonte
pygame.font.init()
minha_fonte = pygame.font.SysFont('Comic Sans MS', 30)

# inicializar o pygame
pygame.init()
TAM_TELA = (dimX,dimY)
tela = pygame.display.set_mode(TAM_TELA)

# cronômetro | tempo
tempo = pygame.time.Clock()

pontuacao = pontuacaoPlayer

cobra = Cobra()
comida = Comida()
posicao_comida = comida.posicao


while True:
    # RGB - Red, Green, Blue - (255,255,255)
    tela.fill((119,136,153)) 

    for event in pygame.event.get():
        # listener - mouse ou teclado
        if event.type == pygame.QUIT:
            # interrompe pygame
            pygame.quit()
            # fechar script (janela)
            sys.exit()

        # se uma tecla foi pressionada
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

    # se a cobra comeu a comida
    if cobra.move(posicao_comida):
        comida.devorada = True
        pontuacao += 1

    if cobra.verifica_colisao():
        pontos = minha_fonte.render(f'Pontuação: {pontuacao}', True, (255,255,255))
        tela.blit(pontos, (10,10))

        voce_perdeu = minha_fonte.render('VOCÊ PERDEU!', True, (255,255,255))
        tela.blit(voce_perdeu, (80,180))

        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    # texto da pontuacao
    pontos = minha_fonte.render(f'{nomePlayer} Pontuação: {pontuacao}', True, (255,255,255))
    tela.blit(pontos, (10,10))
    # desenha cobra
    for pos in cobra.corpo:
        pygame.draw.rect(tela, pygame.Color(200,200,200),
                               # esquerda, cima, largura, altura
                               pygame.Rect(pos[0], pos[1], 10, 10))

    # desenha comida
    pygame.draw.rect(tela, pygame.Color(242,79,0),
                     pygame.Rect(posicao_comida[0],posicao_comida[1],10,10))

    # atualiza a tela a cada frame
    pygame.display.update()

    # FPS - Frames por Segundo
    tempo.tick(20)
