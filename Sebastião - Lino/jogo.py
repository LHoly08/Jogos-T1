import pygame
import time 

pygame.init()

# Janela
largura, altura = 800, 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("FUGITIVO PROFISSIONAL")

# Imagens e som
player1 = pygame.image.load("carinho.webp")
player1 = pygame.transform.scale(player1, (70, 30))  
meta = pygame.image.load("meta.jpg")
sob = pygame.transform.scale(meta, (70, 30))
ganha_img = pygame.image.load("parabens.png")
ganha_img = pygame.transform.scale(ganha_img, (300, 200))
pre_img = pygame.image.load("policia.png")
pre_img = pygame.transform.scale(pre_img, (400, 300))
but_img = pygame.image.load("tntn.png")
but_img = pygame.transform.scale(but_img, (400, 300))

# Sons
explo_som = pygame.mixer.Sound("explo.mp3")
vito_som = pygame.mixer.Sound("ponto.mp3")
vit_def_som = pygame.mixer.Sound("vitoriadef.mp3")
perder_som = pygame.mixer.Sound("preso.mp3")

# Música de fundo
pygame.mixer.music.load("fundo.mp3")
pygame.mixer.music.play(-1)

# Estado do jogo
x_inicial, y_inicial = 200, 300
x, y = x_inicial, y_inicial
velocidade = 0.2
car_largura, car_altura = 70, 30
metax, metay = 700, 300
count = 0
vit = 0
ajogar = True
musica_toca = True
fim_mostrado = False

# Loop principal
correr = True
while correr:
    rato_click = pygame.mouse.get_pressed()
    rato = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correr = False

    janela.fill((244, 164, 96))

    if ajogar:
        if not musica_toca:
            pygame.mixer.music.load("fundo.mp3")
            pygame.mixer.music.play(-1)
            musica_tocando = True

        carro_rect = pygame.Rect(x, y, car_largura, car_altura)

        # Obstáculos
        hitbox = pygame.draw.rect(janela, (255, 0, 0), (325, 225, 150, 150))
        hitbox1 = pygame.draw.circle(janela, (0, 255, 0), (100, 450), 50)
        hitbox2 = pygame.draw.circle(janela, (0, 255, 0), (700, 450), 50)
        hitbox3 = pygame.draw.circle(janela, (0, 255, 0), (100, 100), 50)
        hitbox4 = pygame.draw.circle(janela, (0, 255, 0), (700, 100), 50)
        metacar = pygame.Rect(metax, metay, 100, 100)

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            x -= velocidade
        if teclas[pygame.K_RIGHT]:
            x += velocidade
        if teclas[pygame.K_UP]:
            y -= velocidade
        elif teclas[pygame.K_DOWN]:
            y += velocidade

        # Colisões
        for obstaculo in [hitbox, hitbox1, hitbox2, hitbox3, hitbox4]:
            if carro_rect.colliderect(obstaculo):
                explo_som.play()
                count += 1
                x, y = x_inicial, y_inicial

        if carro_rect.colliderect(metacar):
            vito_som.play()
            vit += 1
            x, y = x_inicial, y_inicial

        if count >= 3 or vit >= 5:
            ajogar = False
            pygame.mixer.music.stop()
            musica_toca = False
            fim_mostrado = False  

        janela.blit(player1, (x, y))
        janela.blit(sob, (metax, metay))

    else:
        if not fim_mostrado:
            if vit >= 5:
                vit_def_som.play()
            else:
                perder_som.play()
            fim_mostrado = True

        if vit >= 5:
            janela.blit(ganha_img, (250, 100))
            janela.blit(but_img, (200, 350))
        else:
            janela.blit(pre_img, (200, 100))
            janela.blit(but_img, (200, 350))

        if rato_click[0] and 200 <= rato[0] <= 600 and 350 <= rato[1] <= 650:
            # Reset jogo
            x, y = x_inicial, y_inicial
            count = 0
            vit = 0
            ajogar = True
            fim_mostrado = False
            musica_tocando = False  # música reinicia no próximo ciclo

    pygame.display.flip()

pygame.quit()