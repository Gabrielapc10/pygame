import pygame
import random 


pygame.init()

largura = 1000
altura = 800
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Desvie do bloco!")

rosa = (20, 5, 0)
laranja = (200, 100, 0)
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
azul = (0, 110, 200)
verde = (0, 255, 0)
roxo = (150, 10, 100)

player_x = largura // 2
player_y = altura - 50
player_vel = 5
player_tam = 40

obs_x = random.randint(0, largura - 40)
obs_y = - 40
obs_vel = 5
obs_tam = 20
pontos = 0

obs2_x = random.randint(0, largura - 40)
obs2_y = - 50
obs2_vel = 10
obs2_tam = 30
pontos2 = 0

obs3_x = random.randint(0, largura - 40)
obs3_y = - 60
obs3_vel = 15
obs3_tam = 40
pontos3 = 0

obs4_x = random.randint(0, largura - 40)
obs4_y = - 70
obs4_vel = 20
obs4_tam = 50
pontos4 = 0

obs5_x = random.randint(0, largura - 40)
obs5_y = - 80
obs5_vel = 25
obs5_tam = 60
pontos5 = 0

fonte = pygame.font.SysFont(None, 40)

relogio = pygame.time.Clock()

rodando = True
while rodando:
      relogio.tick(60)

      for evento in pygame.event.get():
          if evento.type == pygame.QUIT:
             rodando = False

      teclas = pygame.key.get_pressed()
      if teclas[pygame.K_LEFT] and player_x > 0:
         player_x += player_vel
      if teclas[pygame.K_RIGHT] and player_x < largura - player_tam: 
         player_x -= player_vel
      if teclas[pygame.K_UP] and player_y > 0 :
          player_y += player_vel
      if teclas[pygame.K_DOWN] and player_y < largura - player_tam:
          player_y -= player_vel
      

      obs_y += obs_vel
      obs2_y += obs2_vel
      obs3_y += obs3_vel
      obs4_y += obs4_vel
      obs5_y += obs5_vel
      
      if obs_y > altura:
          obs_y = -obs_tam
          obs_x = random.randint(0, largura - obs_tam)
          pontos += 1
          obs_vel += 0.2

      if obs2_y > altura:
          obs2_y = -obs_tam
          obs2_x = random.randint(0, largura - obs_tam)
          pontos2 += 1
          obs2_vel += 0.2
          
      if obs3_y > altura:
          obs3_y = -obs_tam
          obs3_x = random.randint(0, largura - obs_tam)
          pontos3 += 1
          obs3_vel += 0.2

      if obs4_y > altura:
          obs4_y = -obs_tam
          obs4_x = random.randint(0, largura - obs_tam)
          pontos4 += 1
          obs4_vel += 0.2
          
      if obs5_y > altura:
          obs5_y = -obs_tam
          obs5_x = random.randint(0, largura - obs_tam)
          pontos5 += 1
          obs5_vel += 0.2

      jogador = pygame.Rect(player_x, player_y, player_tam, player_tam)   
      obstaculo = pygame.Rect(obs_x, obs_y, obs_tam, obs_tam)
      obstaculo2 = pygame.Rect(obs2_x, obs2_y, obs2_tam, obs2_tam)
      obstaculo3 = pygame.Rect(obs3_x, obs3_y, obs3_tam, obs3_tam)
      obstaculo4 = pygame.Rect(obs4_x, obs4_y, obs4_tam, obs4_tam)
      obstaculo5 = pygame.Rect(obs5_x, obs5_y, obs5_tam, obs5_tam)
      
      if jogador.colliderect(obstaculo):
         print("Game Over!")
         rodando = False
      if jogador.colliderect(obstaculo2):
         print("Game Over!")
         rodando = False
      if jogador.colliderect(obstaculo3):
         print("Game Over!")
         rodando = False
      if jogador.colliderect(obstaculo4):
         print("Game Over!")
         rodando = False
      if jogador.colliderect(obstaculo5):
         print("Game Over!")
         rodando = False

      tela.fill(preto)
      pygame.draw.rect(tela, azul, jogador)
      pygame.draw.rect(tela, vermelho, obstaculo)
      pygame.draw.rect(tela, verde, obstaculo2)
      pygame.draw.rect(tela, roxo, obstaculo3)
      pygame.draw.rect(tela, laranja, obstaculo4)
      pygame.draw.rect(tela, rosa, obstaculo5)
      texto = fonte.render(f"Pontos: {pontos+pontos2+pontos3,pontos4,pontos5}", True, branco)
      tela.blit(texto, (10, 10))

      pygame.display.update()

pygame.quit()