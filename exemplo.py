import pygame
import sys

# inicializa o pygame
pygame.init()

#define tamanho da janela
largura, altura = 1000, 800
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Exemplo Pygame - Movendo um Quadrado")

#define propriedades do jogador
x = 500
y = 400
velocidade = 1
tamanho = 50

#loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # Preenche a tela com preto
    janela.fill((50, 0, 50))

    # Desenha o quadrado (vermelho)
    pygame.draw.rect(janela, (200, 0, 255), (x, y, tamanho, tamanho))

    # Atualiza a tela
    pygame.display.update()
