import pygame 
pygame.init()

def temporizador(tempo_atual, tempo_inicial):
    return (tempo_atual - tempo_inicial)//1000

# Ecrã

largura, altura = 700, 800
ecra = pygame.display.set_mode((largura, altura))
letra = pygame.font.Font("Minecraft.ttf", 40)
letra_game_over = pygame.font.Font("Minecraft.ttf", 80)
pygame.display.set_caption(("Ping-Pong"))

# Musicas e Sound Effects

pygame.mixer.music.load("musica_minecraft.mp3")
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)
menos_vida = pygame.mixer.Sound("vida-1.wav")
game_over = pygame.mixer.Sound("game_over.wav")
click = pygame.mixer.Sound("click.wav")
start_game = pygame.mixer.Sound("start_game.wav")
select_skin = pygame.mixer.Sound("select_skin.wav")
colisao_paredes = pygame.mixer.Sound("colisao_paredes.wav")
colisao_raquete = pygame.mixer.Sound("colisao_raquete.wav")

# Texto

ping_pong = letra.render("Ping-Pong", True, (255, 86, 0))
ping_pong_rect = ping_pong.get_rect()
ping_pong_rect.center = (ecra.get_width()/2, 180)

play = letra.render("Play", True, (255, 178, 0))
play_rect = play.get_rect()
play_rect.center = (ecra.get_width()/2, 280)

quit = letra.render("Quit", True, (255, 178, 0))
quit_rect = quit.get_rect()
quit_rect.center = (ecra.get_width()/2, 600)

go_back = letra.render("Go back", True, (255, 178, 0))
go_back_rect = go_back.get_rect()
go_back_rect.center = (ecra.get_width()/2, 300)

game_over_text = letra_game_over.render("Game Over", True, (255, 255, 255))
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (ecra.get_width()/2, 100)

menu_game_over = letra.render("Menu", True, (255, 255, 255))
menu_game_over_rect = menu_game_over.get_rect()
menu_game_over_rect.center = (ecra.get_width()/2, 500)

quit_game_over = letra.render("Quit", True, (255, 255, 255))
quit_game_over_rect = quit_game_over.get_rect()
quit_game_over_rect.center = (ecra.get_width()/2, 650)

# Jogo

bola_parada = pygame.image.load("bola_laranja.xcf")
hitbox_bola_parada = bola_parada.get_rect()
hitbox_bola_parada.center = (ecra.get_width()/2, 440)
x_raquete, y_raquete = 255, 650
x_bola, y_bola = 325, 195
pontuacao = 0
recorde = 0
tempo_inicial = 0
recorde_tempo = 0

# Criação de Bolas diferentes 

bola_basket = pygame.image.load("bola_basket.xcf")
bola_basket_rect = bola_basket.get_rect()
bola_basket_rect.center = (200, 380)

bola_laranja = pygame.image.load("bola_laranja.xcf")
bola_laranja_rect = bola_laranja.get_rect()
bola_laranja_rect.center = (350, 380)

bola_futebol = pygame.image.load("bola_futebol.xcf")
bola_futebol_rect = bola_futebol.get_rect()
bola_futebol_rect.center = (505, 380)

bola_tenis = pygame.image.load("bola_tenis.xcf")
bola_tenis_rect = bola_tenis.get_rect()
bola_tenis_rect.center = (200, 515)

bola_volei = pygame.image.load("bola_volei.xcf")
bola_volei_rect = bola_volei.get_rect()
bola_volei_rect.center = (350, 515)

bola_boling = pygame.image.load("bola_boling.xcf")
bola_boling_rect = bola_boling.get_rect()
bola_boling_rect.center = (505, 515)

bola_bilhar = pygame.image.load("bola_bilhar.xcf")
bola_bilhar_rect = bola_bilhar.get_rect()
bola_bilhar_rect.center = (200, 630)

bola_andebol = pygame.image.load("bola_andebol.xcf")
bola_andebol_rect = bola_andebol.get_rect()
bola_andebol_rect.center = (505, 630)

# Lista de todas as bolas 

lista_bolas = [pygame.image.load("bola_laranja.xcf"),
               pygame.image.load("bola_basket.xcf"),
               pygame.image.load("bola_futebol.xcf"), 
               pygame.image.load("bola_tenis.xcf"),
               pygame.image.load("bola_volei.xcf"),
               pygame.image.load("bola_boling.xcf"),
               pygame.image.load("bola_bilhar.xcf"),
               pygame.image.load("bola_andebol.xcf")
]

# Corações vermelhos e pretos 

heart_1 = pygame.image.load("Coracao.xcf")
heart_2 = pygame.image.load("Coracao.xcf")
heart_3 = pygame.image.load("Coracao.xcf")
preto_1 = pygame.image.load("coracao_preto.xcf")
preto_2 = pygame.image.load("coracao_preto.xcf")
preto_3 = pygame.image.load("coracao_preto.xcf")

# Fisica da bola 

hitbox_bola = lista_bolas[1].get_rect()
t_x, t_y = 7, 7
direita = True
retangulo_d = True
retangulo_e = False
velocidade = 0
vidas = 3
relogio = pygame.time.Clock()

# Menus

menu = True
menu_bolas = False
game_over_tela = False
x_bola_menu, y_bola_menu = 40, 30
bola = 0

correr = True
while correr:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correr = False
    rato = pygame.mouse.get_pos()
    rato_click = pygame.mouse.get_pressed()
    if menu:

        # Menu principal 

        vidas = 3 
        ecra.fill((40, 0, 200))

        # Ambiente do menu 

        pygame.draw.rect(ecra,(255, 255, 255),(350, 0, 10, 800))
        pygame.draw.rect(ecra,(255, 255, 255),(0, 400, 800, 10))
        pygame.draw.rect(ecra,(255, 255, 255),(0, 0, 10, 800))
        pygame.draw.rect(ecra,(255, 255, 255),(690, 0, 10, 800))
        pygame.draw.rect(ecra,(255, 255, 255),(0, 0, 900, 10))
        pygame.draw.rect(ecra,(255, 255, 255),(0, 790, 900, 10))
        pygame.draw.rect(ecra,(100, 100, 100),(140, 115, 430, 570))
        pygame.draw.rect(ecra,(200, 200, 200), ping_pong_rect)
        pygame.draw.rect(ecra,(200, 200, 200), play_rect)
        pygame.draw.rect(ecra,(200, 200, 200), quit_rect)
        ecra.blit(lista_bolas[bola], hitbox_bola_parada)
        ecra.blit(quit, quit_rect)
        ecra.blit(play, play_rect)
        ecra.blit(ping_pong, ping_pong_rect)
        ecra.blit(lista_bolas[bola], (x_bola_menu, y_bola_menu))

        # Bola de decoração que mexe 

        if x_bola_menu == 40 and 30 < y_bola_menu <=710:
            y_bola_menu = y_bola_menu - 5
        elif x_bola_menu <= 600 and y_bola_menu == 710:
            x_bola_menu = x_bola_menu - 5
        elif x_bola_menu == 600:
            y_bola_menu = y_bola_menu + 5
        elif x_bola_menu >= 40 and y_bola_menu == 30:
            x_bola_menu = x_bola_menu + 5

        # Verificação de botões

        if rato_click[0]:
            if play_rect.collidepoint(rato):
                tempo_inicial = pygame.time.get_ticks()
                start_game.play()
                menu = False
            elif quit_rect.collidepoint(rato):
                correr = False
            elif hitbox_bola_parada.collidepoint(rato):
                click.play()
                menu = False
                menu_bolas = True
    elif menu_bolas: 

        # Menu de skins da bola 

        ecra.fill((40, 0, 200))

        # Ambiemte de menu de skins de bola 

        pygame.draw.rect(ecra,(255, 255, 255),(350, 0, 10, 800))
        pygame.draw.rect(ecra,(255, 255, 255),(0, 400, 800, 10))
        pygame.draw.rect(ecra,(255, 255, 255),(0, 0, 10, 800))
        pygame.draw.rect(ecra,(255, 255, 255),(690, 0, 10, 800))
        pygame.draw.rect(ecra,(255, 255, 255),(0, 0, 900, 10))
        pygame.draw.rect(ecra,(255, 255, 255),(0, 790, 900, 10))
        pygame.draw.rect(ecra,(100, 100, 100),(140, 115, 430, 570))
        pygame.draw.rect(ecra,(200, 200, 200), ping_pong_rect)
        pygame.draw.rect(ecra,(200, 200, 200), go_back_rect)
        ecra.blit(ping_pong, ping_pong_rect)
        ecra.blit(go_back, go_back_rect)
        ecra.blit(bola_laranja, bola_laranja_rect)
        ecra.blit(bola_basket, bola_basket_rect)
        ecra.blit(bola_futebol, bola_futebol_rect)
        ecra.blit(bola_tenis, bola_tenis_rect)
        ecra.blit(bola_volei, bola_volei_rect)
        ecra.blit(bola_boling, bola_boling_rect)
        ecra.blit(bola_bilhar, bola_bilhar_rect)
        ecra.blit(bola_andebol, bola_andebol_rect)
        if rato_click[0]:
            if go_back_rect.collidepoint(rato):
                click.play()
                menu = True
                menu_bolas = False
            if bola_basket_rect.collidepoint(rato):
                select_skin.play()
                bola = 1
                menu = True
                menu_bolas = False
            if bola_laranja_rect.collidepoint(rato):
                select_skin.play()
                bola = 0
                menu = True
                menu_bolas = False
            if bola_futebol_rect.collidepoint(rato):
                select_skin.play()
                bola = 2
                menu = True
                menu_bolas = False
            if bola_tenis_rect.collidepoint(rato):
                select_skin.play()
                bola = 3
                menu = True
                menu_bolas = False
            if bola_volei_rect.collidepoint(rato):
                select_skin.play()
                bola = 4
                menu = True
                menu_bolas = False
            if bola_boling_rect.collidepoint(rato):
                select_skin.play()
                bola = 5
                menu = True
                menu_bolas = False
            if bola_bilhar_rect.collidepoint(rato):
                select_skin.play()
                bola = 6
                menu = True
                menu_bolas = False
            if bola_andebol_rect.collidepoint(rato):
                select_skin.play()
                bola = 7
                menu = True
                menu_bolas = False
    elif game_over_tela:
        ecra.fill((175, 0, 0))
        ecra.blit(game_over_text, game_over_text_rect)
        pygame.draw.rect(ecra, (255, 255, 255),(0, 150, 800, 10))
        pygame.draw.rect(ecra, (0, 0, 0), quit_game_over_rect)
        pygame.draw.rect(ecra, (0, 0, 0), menu_game_over_rect)
        ecra.blit(menu_game_over, menu_game_over_rect)
        ecra.blit(quit_game_over, quit_game_over_rect)
        ecra.blit(letra.render("Score", True, (0, 0, 0)), (130, 190))
        ecra.blit(letra.render(str(pontuacao), True, (255, 255, 255)), (125, 270))
        ecra.blit(letra.render(str(tempo)+"s", True, (255, 255, 255)), (220, 270))
        ecra.blit(letra.render("Record", True, (0, 0, 0)), (470, 190))
        ecra.blit(letra.render(str(recorde), True, (255, 255, 255)), (480, 270))
        ecra.blit(letra.render(str(recorde_tempo)+"s", True, (255, 255, 255)), (560, 270))
        if rato_click[0]:
            if menu_game_over_rect.collidepoint(rato):
                pontuacao = 0
                menu = True
                game_over_tela = False
            if quit_game_over_rect.collidepoint(rato):
                correr = False
    else:
        if vidas == 0:
            if pontuacao > recorde:
                recorde = pontuacao
            if tempo > recorde_tempo:
                recorde_tempo = tempo
            game_over.play()
            game_over_tela = True
        y_bola = y_bola + t_y
        x_bola = x_bola + t_x
        ecra.fill((40,0,200))
        ecra.blit(heart_1, (20, 20))
        ecra.blit(heart_2, (100, 20))
        ecra.blit(heart_3, (180, 20))
        if vidas <= 2:
            ecra.blit(preto_3, (180, 20))
        if vidas <=1:
            ecra.blit(preto_2, (100, 20))
        tempo = temporizador(pygame.time.get_ticks(), tempo_inicial)
        rect_meio_h = pygame.draw.rect(ecra,(255, 255, 255),(350, 0, 10,800 ))
        rect_meio_v = pygame.draw.rect(ecra,(255, 255, 255),(0, 400, 800, 10))
        rect_esquerda = pygame.draw.rect(ecra,(255, 255, 255),(0, 0, 10, 800))
        rect_direita = pygame.draw.rect(ecra,(255, 255, 255),(690, 0, 10, 800))
        rect_cima = pygame.draw.rect(ecra,(255, 255, 255),(0, 0, 900, 10))
        rect_baixo = pygame.draw.rect(ecra,(255, 255, 255),(0, 790, 900, 10))
        raquete = pygame.draw.rect(ecra,(0, 0, 0),(x_raquete, y_raquete, 200, 40))
        ecra.blit(lista_bolas[bola], (x_bola, y_bola))
        ecra.blit(letra.render("Score:", True, (0, 0, 0)), (380, 30))
        ecra.blit(letra.render(str(pontuacao), True, (255, 0, 0)), (540, 32))
        ecra.blit(letra.render(str(tempo)+"s", True, (255, 255, 255)), (630, 32))
        movimento = pygame.key.get_pressed()
        m = pygame.key.get_pressed()
        posicao = x_raquete
        if movimento[pygame.K_a]:
            x_raquete = x_raquete - 5
            retangulo_e = True
            retangulo_d = False
        elif movimento[pygame.K_d]:
            x_raquete = x_raquete + 5
            retangulo_d = True
            retangulo_e = False
        if posicao == x_raquete:
            retangulo_d = False 
            retangulo_e = False
        hitbox_bola.topleft = (x_bola, y_bola)   
        if hitbox_bola.colliderect(rect_baixo):
            X_bola, y_bola = 325, 195
            t_x, t_y = 7, 7
            velocidade = 0
            vidas = vidas - 1 
            if vidas > 0:
                menos_vida.play()
        if hitbox_bola.colliderect(raquete):
            colisao_raquete.play()
            if retangulo_e:
                direita = False
            elif retangulo_d:
                direita = True
            if velocidade == 10:
                velocidade = velocidade - 1
            velocidade = velocidade + 1
            t_x = abs(t_x) + velocidade//10
            t_y = abs(t_y) + velocidade//10
            t_y = - abs(t_y)
        elif hitbox_bola.colliderect(rect_cima):
            pontuacao = pontuacao + 1
            colisao_paredes.play()
            t_y = abs(t_y) 
        if hitbox_bola.colliderect(rect_esquerda):
            colisao_paredes.play()
            direita = True
        if hitbox_bola.colliderect(rect_direita):
            colisao_paredes.play()
            direita = False
        if direita:
            t_x = abs(t_x)
        else:
            t_x = - abs(t_x)
        if raquete.colliderect(rect_esquerda):
            x_raquete = x_raquete + 5
        elif raquete.colliderect(rect_direita):
            x_raquete = x_raquete - 5
        if m[pygame.K_m]:
            game_over.play()
            pontuacao = 0
            menu = True    
    relogio.tick(60)
    pygame.display.update()   
pygame.quit()         