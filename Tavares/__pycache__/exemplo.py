import pygame
import sys
# Iniciar o Pygame
pygame.init()
# Definir tamanho da janela
largura = 800
altura = 600
ecra = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Detetar Colisão com
Pygame")
# Cor de fundo
cor_fundo = (30, 30, 30)
# Carregar imagens
imagem1 = pygame.image.load("nave1.png")
imagem2 = pygame.image.load("nave2.png")
# Redimensionar se necessário
imagem1 = pygame.transform.scale(imagem1, (50, 50))
imagem2 = pygame.transform.scale(imagem2, (50, 50))
# Obter retângulos (para posição e colisão)
rect1 = imagem1.get_rect()
rect2 = imagem2.get_rect()
# Posição inicial
rect1.topleft = (100, 100)
rect2.topleft = (300, 300)
COLÉGIO
INTERNATO
DOS CARVALHOS MATERIAL DE APOIO
Disciplina IP Ano/Turma: 10T1 Docente Nuno Couto
velocidade = 5
while True:
# Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
        pygame.quit()
    sys.exit()
    # Teclas pressionadas
    teclas = pygame.key.get_pressed()
    # Movimento imagem1 (Setas)
    if teclas[pygame.K_LEFT]:
    rect1.x -= velocidade
    if teclas[pygame.K_RIGHT]:
    rect1.x += velocidade
    if teclas[pygame.K_UP]:
    rect1.y -= velocidade
    if teclas[pygame.K_DOWN]:
    rect1.y += velocidade
    # Movimento imagem2 (WASD)
    if teclas[pygame.K_a]:
    rect2.x -= velocidade
    if teclas[pygame.K_d]:
    rect2.x += velocidade
    if teclas[pygame.K_w]:
    rect2.y -= velocidade
    if teclas[pygame.K_s]:
    rect2.y += velocidade
    COLÉGIO
    INTERNATO
    DOS CARVALHOS MATERIAL DE APOIO
    Disciplina IP Ano/Turma: 10T1 Docente Nuno Couto
    # Verificar colisão
    if rect1.colliderect(rect2):
    print("COLISÃO DETETADA!")
    cor_fundo = (255, 0, 0) # Muda cor do ecrã
    para vermelho
    else:
    cor_fundo = (30, 30, 30)
    # Desenhar
    ecra.fill(cor_fundo)
    ecra.blit(imagem1, rect1)
    ecra.blit(imagem2, rect2)
    # Atualizar ecrã
    pygame.display.flip()