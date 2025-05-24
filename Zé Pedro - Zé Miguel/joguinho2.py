import pygame

#Class do Jogador
class Jogador:
    x=100
    y=354
    def __init__(self, sprites):
        self.imagem=sprites[0]
        self.sprites=sprites
        self.go_up=False
        self.moving=False
        self.anim=0
        self.go_down=False
        self.hitbox=(self.imagem).get_rect()
        self.hitbox.topleft=(self.x, self.y)
        self.cabeça=pygame.rect.Rect(self.x, self.y-10, self.hitbox[2], 10)
        self.pontos=0
        self.posição=(self.x, self.y)

    def salto(self, gravity):
        if self.go_up:
            if self.y<300:
                self.go_down=True
            if self.y>300 and not self.go_down:
                self.y-=gravity
            elif self.y>=354:
                self.y=354
                self.go_up=False
                self.go_down=False
            else:
                self.y+=gravity

    def imagens(self, anim_atual):
        if self.moving:
            if anim_atual-self.anim<200:
                self.imagem=self.sprites[1]
            elif anim_atual-self.anim<400:
                self.imagem=self.sprites[2]
            else:
                self.anim=pygame.time.get_ticks()
        else:
            self.imagem=self.sprites[0]
            self.anim=pygame.time.get_ticks()
        if self.go_up:
            self.imagem=self.sprites[3]
        self.hitbox=(self.imagem).get_rect()
        (self.hitbox).topleft=(self.x, self.y) 
        self.cabeça=pygame.rect.Rect(self.x, self.y-5, self.hitbox[2], 5)

class Bola:
    x, y = 364, 474
    def __init__(self, imagem):
        self.bola_salta=False
        self.imagem=imagem
        self.hitbox=self.imagem.get_rect()
        self.salta=False
        self.baixo=False
        self.anda=False
        self.hitbox.topleft=(self.x, self.y)

    def gravidadebola(self, gravity, limite):
        if self.salta:
                if self.y<limite:
                    self.baixo=True
                if self.y>limite and not self.baixo:
                    self.y-=gravity
                elif self.y>474:
                    self.y=474
                    self.salta=False
                    self.baixo=False
                    self.anda=False
                else:
                    self.y+=gravity
                if self.y!=474:
                    self.anda=True

    def bola_lados(self, direção):
        global reset
        if self.x<0 or self.x>800:
            reset()
        elif  self.anda:
            self.x+=direção

    def hitbox_change(self):
        self.hitbox.topleft=(self.x, self.y)

pygame.init()

LARGURA, ALTURA = 800, 600
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("HeadSoccer")

# Posições iniciais dos jogadores
x, y = 20, 100

#lista de sprites
jogador1_sprites=[
    pygame.image.load("alienBlue_stand.png"),
    pygame.image.load("alienBlue_walk1.png"),
    pygame.image.load("alienBlue_walk2.png"),
    pygame.image.load("alienBlue_jump.png")
]
jogador2_sprites=[
    pygame.image.load("alienGreen_stand.png"),
    pygame.image.load("alienGreen_walk1.png"),
    pygame.image.load("alienGreen_walk2.png"),
    pygame.image.load("alienGreen_jump.png")
]

#jogadores
jogador1=Jogador(jogador1_sprites)
jogador2=Jogador(jogador2_sprites)
jogador2.x=LARGURA-228

# Fontes
fonte_tempo = pygame.font.Font(None, 74)
fonte_mensagem = pygame.font.Font(None, 50)
inicio_tempo = pygame.time.get_ticks()
duracao = 60000
mostrar_mensagem = False
tempo_mensagem_inicio = 0
duracao_mensagem = 3000

# Gravidade
GRAVITY = 5


# Bola
bola_img = pygame.image.load("ball_soccer4.png")
bola=Bola(bola_img)
sentido_bola=0
altura_max=0

#Fonte dos pontos
fontepontos = pygame.font.Font(None, 40)
texto_pontos2 = fontepontos.render(f"Player2:{jogador2.pontos}", True, (255, 255, 255))
texto_pontos1 = fontepontos.render(f" Player1:{jogador1.pontos}" ,True, (255, 255, 0))
# Nuvens
nuvemesquerda1 = pygame.image.load("tile_0153.png")
nuvemesquerda1 = pygame.transform.scale(nuvemesquerda1, (40, 40))
nuvemmeio1 = pygame.image.load("tile_0154.png")
nuvemmeio1 = pygame.transform.scale(nuvemmeio1, (40, 40))
nuvemdireita1 = pygame.image.load("tile_0155.png")
nuvemdireita1 = pygame.transform.scale(nuvemdireita1, (40, 40))

pygame.mixer.music.load("Kazzio - Safira (online-audio-converter.com).ogg") 
pygame.mixer.music.play(-1) 

vai_cima1=False
vai_cima2=False
# Variáveis de controle do jogo
running = True
relogio=pygame.time.Clock()
# Função para aplicar a gravidade e o salto

def reset():
    bola.y=364
    bola.x=474
    jogador1.x=100
    jogador1.y=354 
    jogador2.x=LARGURA-228
    jogador2.y=354


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

       
    # Atualizar a tela
    janela.fill((76, 152, 228))

    texto_pontos2 = fontepontos.render(f"Player2:{jogador2.pontos}", True, (255, 255, 255))
    texto_pontos1 = fontepontos.render(f" Player1:{jogador1.pontos}" ,True, (255, 255, 0))

    # Temporizador
    tempo_atual = pygame.time.get_ticks()
    tempo_decorrido = tempo_atual - inicio_tempo
    if tempo_decorrido >= duracao:
        if not mostrar_mensagem:
            mostrar_mensagem = True
            tempo_mensagem_inicio = tempo_atual
        tempo_passado_mensagem = tempo_atual - tempo_mensagem_inicio
        if tempo_passado_mensagem >= duracao_mensagem:
            running = False
        texto = fonte_mensagem.render("FIM DO JOGO", True, (255, 0, 0))
        janela.blit(texto, ( LARGURA // 2 - texto.get_width() // 2,  ALTURA // 2 - texto.get_height()))
    else:
        segundos = (tempo_decorrido // 1000) % 60
        minutos = (tempo_decorrido // 60000) % 60
        horas = (tempo_decorrido // 3600000)
        texto_tempo = f"{minutos:02}:{segundos:02}"
        texto = fonte_tempo.render(texto_tempo, True, (255, 255, 255))
        janela.blit(texto, (1350// 2 - texto.get_width() // 2, 100 // 2 - texto.get_height() // 2))
    

    # Movimentação dos jogadores
    jogador1.posição=(jogador1.x, jogador1.y)
    jogador2.posição=(jogador2.x, jogador2.y)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and not jogador1.go_up:  # Salto jogador 1
       jogador1.go_up=True
    if teclas[pygame.K_a]:
        jogador1.x -= 5
    if teclas[pygame.K_d]:
        jogador1.x += 5

    if teclas[pygame.K_UP] and not jogador2.go_up:  # Salto jogador 2
        jogador2.go_up=True
    if teclas[pygame.K_LEFT]:
        jogador2.x -= 5
    if teclas[pygame.K_RIGHT]:
        jogador2.x += 5
    
    if jogador1.posição!=(jogador1.x, jogador1.y):
        jogador1.moving=True
    else:
        jogador1.moving=False
    
    if jogador2.posição!=(jogador2.x, jogador2.y):
        jogador2.moving=True
    else:
        jogador2.moving=False

    # Aplicar a gravidade e movimento dos jogadores
    jogador1.salto(GRAVITY)
    jogador2.salto(GRAVITY)

    #Mudar Imagem
    jogador1.imagens(pygame.time.get_ticks())
    jogador2.imagens(pygame.time.get_ticks())

    # Desenhar as nuvens
    janela.blit(nuvemesquerda1, (x, y))
    janela.blit(nuvemmeio1, (x + 35, y))
    janela.blit(nuvemdireita1, (x + 65, y))

    # Chão e balizas
    pygame.draw.rect(janela, (0, 255, 0), (0, 510, 800, 300))  # Chão
    baliza_d = pygame.draw.rect(janela, (255, 255, 255), (0, 340, 90, 170))  # Baliza Direita
    baliza_e = pygame.draw.rect(janela, (255, 255, 255), (710, 340, 90, 170))  # Baliza Esquerda
    
    # Desenhar os jogadores
    janela.blit(jogador1.imagem, (jogador1.x, jogador1.y))
    janela.blit(jogador2.imagem, (jogador2.x, jogador2.y))

    # Desenhar a bola
    janela.blit(bola.imagem, (bola.x, bola.y))

    bola.hitbox_change()
    #colisoes
    if (bola.hitbox).colliderect(baliza_e):
        jogador1.pontos+=1 
        reset()
        
            
    if (bola.hitbox).colliderect(baliza_d): 
        jogador2.pontos+=1
        reset()
    
    if (jogador1.hitbox).colliderect(bola.hitbox):
        bola.salta=True
        sentido_bola=5
        altura_max=250
    if (jogador2.hitbox).colliderect(bola.hitbox):
        bola.salta=True
        sentido_bola=-5
        altura_max=250
    if (jogador1.cabeça).colliderect(bola.hitbox):
        bola.salta=True
        sentido_bola=5
        altura_max=150
    if (jogador1.cabeça).colliderect(bola.hitbox):
        bola.salta=True
        sentido_bola=-5
        altura_max=150

    bola.bola_lados(sentido_bola)
    bola.gravidadebola(GRAVITY, altura_max)
        
    rect_cima =texto_pontos1.get_rect(center=(500// 2,100 // 2))
    rect_meio =texto_pontos2.get_rect(center=(1000 // 2, 100// 2))
    janela.blit(texto_pontos1, rect_cima)
    janela.blit(texto_pontos2, rect_meio)

    pygame.display.flip()
    pygame.display.update()
    relogio.tick(60)

pygame.quit()

