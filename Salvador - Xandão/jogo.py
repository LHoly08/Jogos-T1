import pygame as pg
import math
from random import randint
#Inicio
pg.init()

fonte = pg.font.SysFont(None, 36)
som_ponto = pg.mixer.Sound("audio_ponto.mp3")
fim = pg.mixer.Sound("end.mp3")
relogio = pg.time.Clock()



def escrever_texto(texto,cor,x,y):
    escrever_text = fonte.render(texto, True, cor)
    jogo.blit(escrever_text, (x,y))
#Tamanho da janela
largura, altura = 700, 900
jogo = pg.display.set_mode((largura, altura))
pg.display.set_caption("Bubble Shooter Simples")

def menu():
    fim.play()
   
    while True:
        jogo.fill((200, 180, 170)) # cor de fundo do menu
        escrever_texto("ACABOU O TEMPO", (0, 0, 0),largura//2 - 226//2, 200)
        escrever_texto("Pressione ENTER para Jogar DE NOVO", (0, 100, 0),largura//2 - 456//2, 300)
        escrever_texto("Pressione ESC para Sair", (150, 0, 0),largura//2 - 284//2, 350)

        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()
            elif evento.type == pg.KEYDOWN:
                if evento.key == pg.K_RETURN:
                    fim.stop()
                    return "jogo"
                elif evento.key == pg.K_ESCAPE:
                    pg.quit()
                    quit()

        pg.display.flip()
def main():
    imagens = [
        "alvaro.png",
        "br.png",
        "g.png",
        "h.png",
        "r.png",
        "s.png",
        "t.png",
        "ze.png",
        "bola.png",
        "bola2.png",
        "jon.png",
        "pedlo.png",
        "xan.png"
    ]
    #Cores
    FUNDO = (245, 232, 227)
    COR_Base = (100,150,130)
    COR_LINHA = (194, 197, 204)

    #Variáveis do controlo da seta e da bola
    x_tiro = largura // 2
    y_tiro = altura - 80
    vel_tiro = 10
    pontos = 0
    angulo = 90

    atirando = False #saber quANDO está a atirar
    bolas = []

    #Função para converter ângulo em dx e dy
    def calcular_movimento(angulo_graus, velocidade):
        rad = math.radians(angulo_graus)
        dx = math.cos(rad) * velocidade
        dy = -math.sin(rad) * velocidade
        return dx, dy

    #
    # Cesto
    x_cesto = largura // 2 - 40
    y_cesto = 60
    largura_cesto = 80
    altura_cesto = 20
    vel_cesto = 2
    direcao_cesto = 1

    imagem = pg.image.load(imagens[randint(0,len(imagens)-1)])



    time_in = pg.time.get_ticks() # isto ira servir para dar meio que reset no pg.time.get_ticks depois de ser chamado a função menu
    while True:
        jogo.fill(FUNDO)
   
        time = pg.time.get_ticks()
        time_seg = (time - time_in)//1000
        if time_seg >= 60:
            return "menu"
           
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()
            elif evento.type == pg.KEYDOWN:
                if evento.key == pg.K_LEFT or evento.key == pg.K_a:
                    angulo += 5
                    if angulo > 160:
                        angulo = 160
                elif evento.key == pg.K_RIGHT or evento.key == pg.K_d:
                    angulo -= 5
                    if angulo < 20:
                        angulo = 20
                elif evento.key == pg.K_SPACE and not atirando:
                    dx, dy = calcular_movimento(angulo, vel_tiro)
                    bolas.append([x_tiro, y_tiro, dx, dy])
                    atirando = True
       

        jogo.blit(imagem, (81,51))
        #Desenhar a seta
        dx_mira, dy_mira = calcular_movimento(angulo, 50)
        pg.draw.line(jogo, COR_Base, (x_tiro, y_tiro), (x_tiro + dx_mira, y_tiro + dy_mira), 5)
        pg.draw.circle(jogo, COR_Base, (x_tiro, y_tiro), 12)

        #Mover e desenhar bolas
        novas_bolas = []
        for bola in bolas:
            bola[0] += bola[2]
            bola[1] += bola[3]

            #Ricochete nas laterais
            if bola[0] <= 80 or bola[0] >= largura - 80:
                bola[2] *= -1

            #Verificar colisão com o cesto
            if (x_cesto <= bola[0] <= x_cesto + largura_cesto) and (y_cesto <= bola[1] <= y_cesto + altura_cesto):
                pontos += 1
                imagem = pg.image.load(imagens[randint(0,len(imagens)-1)])
                som_ponto.play()
                continue

            if bola[1] > 0:
                novas_bolas.append(bola)
                pg.draw.circle(jogo, (50,130,200), (int(bola[0]), int(bola[1])), 10)
        bolas = novas_bolas

        if not bolas:
            atirando = False

        #Bordas
        pg.draw.line(jogo, COR_Base, (80, altura - 50), (80, 50), 5)
        pg.draw.circle(jogo, COR_Base, (80, altura - 50), 2)
        pg.draw.circle(jogo, COR_Base, (80, 50), 2)

        pg.draw.line(jogo, COR_Base, (largura - 80, altura - 50), (largura - 80, 50), 5)
        pg.draw.circle(jogo, COR_Base, (largura - 80, 50), 2)
        pg.draw.circle(jogo, COR_Base, (largura - 80, altura - 50), 2)

        pg.draw.line(jogo, COR_Base, (80, altura - 50), (largura - 80, altura - 50), 5)
        pg.draw.line(jogo, COR_Base, (80, 50), (largura - 80, 50), 5)
        pg.draw.line(jogo, COR_LINHA, (83, altura - 180), (largura - 83, altura - 180), 5)

        #Atualizar posição do cesto
        x_cesto += vel_cesto * direcao_cesto
        if x_cesto <= 80 or x_cesto + largura_cesto >= largura - 80:
            direcao_cesto *= -1 # inverter direção

        #Desenhar o cesto no topo
        pg.draw.rect(jogo, (100, 100, 200), (x_cesto, y_cesto, largura_cesto, altura_cesto), border_radius=10)
        #mostar tempo
        escrever_texto(f'Tempo atual: {time_seg} s', (0, 0, 0),480, 20)

        #Mostrar pontuação
        escrever_texto(f"Pontos: {pontos}", (0, 0, 0),30, 20)
   
        #Atualizar a tela
        pg.display.flip()

        relogio.tick(60)
opção = "jogo"
variaçao_opçao = {
    "jogo":main,
    "menu":menu
}
while True:
    opção = variaçao_opçao[opção]()