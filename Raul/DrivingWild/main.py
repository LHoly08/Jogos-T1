import pygame
import random
import os
import json

pygame.init()
dpsize=pygame.display.get_desktop_sizes()
screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("DrivingWild")
clock = pygame.time.Clock()
#pygame.display.set_icon()

if os.path.exists("Resources/Data.json"):
    Highscore = json.load(open("Resources/Data.json"))["Highscore"]
else:
    Highscore=0

#Facilitar o carregamento das imagens
def load_image(filename, size):
    path = os.path.join("Resources", filename)
    if os.path.exists(path):
        image = pygame.image.load(path).convert_alpha()
        image = pygame.transform.scale(image, size)
        return image
    else:
        error = pygame.Surface(size)
        error.fill(255,0,0)
        return error

#Heranca de sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image("player.png", (70, 140))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_width() // 2
        self.rect.bottom = screen.get_height() - 30
        self.speed_x = 0

    def update(self):
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.speed_x = -8
        if keys[pygame.K_d]:
            self.speed_x = 8
        self.rect.x += self.speed_x
        # Limites da pista
        if self.rect.left < 200:
            self.rect.left = 200
        if self.rect.right > 800:
            self.rect.right = 800

    def get_hitbox(self):
        return self.rect.inflate(-self.rect.width * 0.2, -self.rect.height * 0.2)

#Heranca de sprite
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imagelist=[]
        i=1
        for file in sorted(os.listdir("Resources/Obstacles")):
            if file.endswith(".png"):
                img = load_image(f"Obstacles/obstacle{i}.png", (70, 140))
                i+=1
                self.imagelist.append(img)
        self.reset()

    def reset(self):
        self.image=self.imagelist[random.randint(0, len(self.imagelist)-1)]
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(200, 800 - self.rect.width)
        self.rect.y = random.randrange(-600, -140)
        self.speed = random.randint(4, 15)
        #for o in pygame.sprite.spritecollide(self, obstacles, False):
        #    if o != self:
        #        self.reset()

    def update(self):
        if random.randint(0,150) == 0:
            self.speed = random.randint(4, 15)
        if self.rect.top < -200:
            self.rect.y += 2
        else:
            self.rect.y += self.speed
        if self.rect.top > 900:
            self.reset()

    def check_collision(self,obs):
        for o in pygame.sprite.spritecollide(self, obs, False):
            if o != self:
                self.reset()
                break
    
    def get_hitbox(self):
        return self.rect.inflate(-self.rect.width * 0.2, -self.rect.height * 0.2)
    
class Road:
    def __init__(self):
        self.image = load_image("road.png", (1000, 800))
        self.y1 = 0
        self.y2 = -800
        self.speed = 10

    def update(self):
        self.y1 += self.speed
        self.y2 += self.speed
        if self.y1 >= 800:
            self.y1 = self.y2 - 800
        if self.y2 >= 800:
            self.y2 = self.y1 - 800

    def draw(self, surface):
        surface.blit(self.image, (0, self.y1))
        surface.blit(self.image, (0, self.y2))

class Menu:
    def __init__(self,font=pygame.font.Font(None, 40)):
        ########################################################
        video = []
        for filename in sorted(os.listdir("Resources/MenuBackgroundFrames")):
            if filename.endswith(".png"):
                img = pygame.image.load(os.path.join("Resources/MenuBackgroundFrames", filename)).convert()
                img = pygame.transform.scale(img, (1000, 800))
                video.append(img)
        self.Background = video
        ########################################################
        title=pygame.image.load("Resources/MenuTitle.png")
        self.Title=title
        ########################################################
        button_width=200
        button_height =60
        button_x = (screen.get_width() - button_width) // 2
        button_y = title.get_rect().bottom + 200 
        button1 = pygame.Rect(button_x, button_y, button_width, button_height)
        text1 = font.render("Jogar", True, (255, 255, 255))
        self.StartButton=[button1,text1]
        ########################################################

def draw_text(surface, text, size, x, y, color=(255, 255, 255)):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, color)
    surface.blit(text, text.get_rect(center=(x, y)))

running=True
menu=True
gameoverSound=pygame.mixer.Sound("Resources/SomGameover.mp3")
gameoverSound.set_volume(1.0)
while running:
    if menu:
        frame_index=0
        menuProperties=Menu()
        while menu:
            title_rect = menuProperties.Title.get_rect()
            title_rect.centerx = screen.get_width() // 2
            title_rect.top = 50

            #StartButton
            startButton=menuProperties.StartButton[0]
            startText=menuProperties.StartButton[1]  
            if startButton.collidepoint(pygame.mouse.get_pos()):
                button_color = (120, 120, 120)
            else:
                button_color = (70, 70, 70)             

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    menu = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if startButton.collidepoint(event.pos):
                        menu = False


            screen.blit(menuProperties.Background[frame_index], (0, 0))  
            screen.blit(menuProperties.Title, title_rect)  
            pygame.draw.rect(screen, button_color, startButton, border_radius=12)
            screen.blit(startText, startText.get_rect(center=startButton.center))
            draw_text(screen, f"Highscore: {Highscore}", 40, startButton.centerx, startButton.centery+60, (50, 50, 50))

            frame_index = (frame_index + 1) % len(menuProperties.Background)
            clock.tick(20)  
            pygame.display.flip()
    else:
        player = Player()
        road = Road()
        obstacles = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)   
        for _ in range(10):
            o = Obstacle()
            all_sprites.add(o)
            obstacles.add(o)    
        score = 0
        game_over = False

        pygame.mixer.music.load("Resources/GameSound.mp3")
        pygame.mixer.music.play(-1) 

        while not menu and running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu = True
                        pygame.mixer.music.unload()
                    if event.key == pygame.K_w and not game_over:
                        if road.speed < 40:
                            road.speed += 2
                            for o in obstacles:
                                o.speed += 2
                    if event.key == pygame.K_s and not game_over:
                        road.speed = max(2, road.speed - 2)
                        for o in obstacles:
                            o.speed -= max(2, o.speed - 2)
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and not game_over and road.speed < 50:
                road.speed += 0.1
                for o in obstacles:
                    o.speed += 0.1
            if keys[pygame.K_s] and not game_over:
                road.speed = max(2, road.speed - 0.5)
                for o in obstacles:
                    o.speed -= 0.5

            if not game_over:
                all_sprites.update()
                for o in obstacles:
                    if o is Obstacle:
                        o.check_collision(obstacles)
                obs_list = []
                for o in obstacles:
                    overlap = False
                    for other in obs_list:
                        if o.rect.colliderect(other.rect.inflate(50, 50)):
                            o.speed = other.speed
                            overlap = True
                            break
                    if not overlap:
                        obs_list.append(o)

                road.update()
                score += road.speed * 0.01
                if score>1500 and len(obstacles)<15:
                    o = Obstacle()
                    all_sprites.add(o)
                    obstacles.add(o)
                if score>3000 and len(obstacles)<20:
                    o = Obstacle()
                    all_sprites.add(o)
                    obstacles.add(o)
                # Colisão
                for o in obstacles:
                    if player.get_hitbox().colliderect(o.get_hitbox()):
                        gameoverSound.play()
                        pygame.mixer.music.stop()                       
                        game_over = True

            # Desenhar
            road.draw(screen)
            all_sprites.draw(screen)
            draw_text(screen, f"Pontuação: {int(score)}", 36, screen.get_width() // 2, 30, (255, 255, 255))

            if game_over:
                if score > Highscore:
                    Highscore = int(score)
                draw_text(screen, "GAME OVER", 80, screen.get_width() // 2, screen.get_height() // 2, (255, 0, 0))
                draw_text(screen, "Pressione 'ESC' para voltar ao menu", 40, screen.get_width() // 2, screen.get_height() // 2 + 70, (255, 255, 255))

            pygame.display.flip()
            clock.tick(30)


if os.path.exists("Resources/Data.json"):
    with open("Resources/Data.json") as f:
        data = json.load(f)
    data["Highscore"] = Highscore
    with open("Resources/Data.json", "w") as f:
        json.dump(data, f)
else:
    data = {"Highscore": Highscore}
    with open("Resources/Data.json", "w") as f:
        json.dump(data, f)


pygame.quit()