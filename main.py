#bibliotecas
import pygame
import random

#iniciar
pygame.init()

#janela do jogo
janela_largura = 400
janela_altura =  600
tela = pygame.display.set_mode((janela_largura, janela_altura)) # criar uma janela
pygame.display.set_caption('doodle jump') # nome do jogo
musica_de_fundo = pygame.mixer.music.load('sapo_nao_lava.mp3') #música de fundo
pygame.mixer.music.play(-1)

#frame
clock = pygame.time.Clock()
FPS = 60

rodar = 200
gravidade = 1 # quão rápido a sapa cai (1 pixel)
maximo_plataformas = 10 # máximo de plataformas na tela
rolagem = 0
background_rolagem = 0

# cores
branco = (255, 255, 255)

#imagens
sapa_imagem = pygame.image.load('sapa.png') # imagem da sapa
background_imagem = pygame.image.load('ceu.png') # imagem do background
background_imagem = pygame.transform.scale(background_imagem, (janela_largura, janela_altura)) # escala do background
plataforma_imagem = pygame.image.load('platform.png') # imagem da plataforma

# função para aparecer o background 
def draw_background(rolagem):
    tela.blit(background_imagem, (0, 0 + background_rolagem))
    tela.blit(background_imagem, (0, -600 + background_rolagem)) # dois backgrounds, um atrás do outro

# jogador (sapa)
class Jogador():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(sapa_imagem, (140, 140)) # escala da imagem
        self.largura = 43 # largura do retângulo
        self.altura = 45 # altura do retângulo
        self.rect = pygame.Rect(0, 0, self.largura, self.altura) # criar um retângulo 
        self.rect.center = (x, y) # centralizar o retângulo na sapa
        self.vel_y = 0 # velocidade do eixo y

    def move(self): # movimento da sapa
        # resetar variáveis 
        rolagem = 0 # movimento de rolagem da tela
        dx = 0 
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_a]: 
            dx = -10 # mover 10 pixels para a esquerda
        if key[pygame.K_d]:
            dx = 10 # mover 10 pixels para a direita

        self.vel_y += gravidade # acelerar o pulo
        dy += self.vel_y

        # colisão da tela (para a sapa não conseguir ir além da borda da janela do jogo) 
        if self.rect.left + dx < 0: # se a sapa for além da janela do lado esquerdo
            dx = - self.rect.left # parar quando alcançar a tela
        if self.rect.right + dx > janela_largura: # se a sapa for além da janela do lado direito
            dx = janela_largura - self.rect.right 


        # colisão com as plataformas
        for plataforma in platafroma_grupo:
            if plataforma.rect.colliderect(self.rect. x, self.rect.y + dy, self.largura, self. altura):
                if self.rect.bottom < plataforma.rect.centery:
                    if self.vel_y > 0:
                        self.rect.bottom = plataforma.rect.top # se o fundo da sapa tocar no topo da plataforma
                        dy = 0
                        self.vel_y = -20


        # colisão com a parte de baixo da tela
        if self.rect.bottom + dy > janela_altura: # se a sapa for além do chão dao janela
            dy = 0
            self.vel_y = -20

        if self.rect.top <= rodar:
            if self.vel_y < 0:
                rolagem = -dy # rolagem é o contrário do movimento da sapa

        # recentralizar o retângulo
        self.rect.x += dx
        self.rect.y += dy + rolagem

        return rolagem

    def draw(self): # 
        tela.blit(self.image, (self.rect.x - 50, self.rect.y - 70))
        

#platafroma
class Plataforma(pygame.sprite.Sprite): 

    def __init__(self, x, y, largura):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(plataforma_imagem, (largura, 50)) # escala da plataforma
        self.largura = largura # largura do retângulo
        self.altura = 30 # altura do retângulo
        self.rect = pygame.Rect(0, 0, self.largura, self.altura) # criar um retângulo 
        self.rect.center = (x, y) # centralizar o retângulo na sapa
        
        self.rect.x = x
        self.rect.y = y

    def update(self, rolagem):
        self.rect.y += rolagem # update a posição das plataformas enquanto a tela rola

        if self.rect.top > janela_altura:
            self.kill() # excluir as plataformas que saem ta tela


platafroma_grupo = pygame.sprite.Group()

sapa = Jogador(janela_largura // 2, janela_altura - 150) # posição da sapa

# plataforma inicial
plataforma = Plataforma(janela_largura // 2 - 23, janela_altura - 100, 50)
platafroma_grupo.add(plataforma)

# loop do jogo
loop = True
while loop:

    clock.tick(FPS)

    rolagem = sapa.move()

    background_rolagem += rolagem
    if background_rolagem >+ 600:
        background_rolagem = 0 # resetar a posição dos dois backgrounds, para ser infinito
    draw_background(background_rolagem) # fazer com que o background apareça na tela

    if len(platafroma_grupo) < maximo_plataformas:
        plataforma_largura = random.randint(60, 100) # largura das plataformas (entre 60 e 100)
        plataforma_x = random.randint(0, janela_largura - plataforma_largura) # posição no eixo x
        plataforma_y = plataforma.rect.y - random.randint(100, 190) # posição no eixo y
        plataforma = Plataforma(plataforma_x, plataforma_y, plataforma_largura) # gerar a plataforma
        platafroma_grupo.add(plataforma)

    platafroma_grupo.update(rolagem)

    platafroma_grupo.draw(tela) # adicionar as plataformas à tela
    sapa.draw()

    for event in pygame.event.get(): # sair do jogo
        if event.type == pygame.QUIT:
            loop = False

    pygame.display.update() 

pygame.quit()