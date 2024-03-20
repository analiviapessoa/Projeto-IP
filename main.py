#bibliotecas
import pygame
import random
import os
 
#iniciar
pygame.init()

#janela do jogo
janela_largura = 400
janela_altura =  600
tela = pygame.display.set_mode((janela_largura, janela_altura)) # criar uma janela
pygame.display.set_caption('flying froggy') # nome do jogo

#músicas e efeitos sonoros
musica_de_fundo = pygame.mixer.music.load('audios/sapo_nao_lava.mp3') #música de fundo
pygame.mixer.music.play(-1,1.5)
pygame.mixer.music.set_volume(1.5)

morte = pygame.mixer.Sound('audios/morte.mp3')
morte.set_volume(0.5)

som_vitoriaregia = pygame.mixer.Sound('audios/som_vr.mp3')
som_vitoriaregia.set_volume(0.5)

som_mosca = pygame.mixer.Sound('audios/som_mosca.mp3')
som_mosca.set_volume(0.5)

som_sal = pygame.mixer.Sound('audios/sal.mp3')
som_sal.set_volume(0.5)

#imagens
sapa_imagem = pygame.image.load('imagens/sapa.png') # imagem da sapa
background_imagem = pygame.image.load('imagens/ceu.png') # imagem do background
background_imagem = pygame.transform.scale(background_imagem, (janela_largura, janela_altura)) # escala do background
game_over_imagem = pygame.image.load('gameover.png') # imagem da tela final
game_over_imagem = pygame.transform.scale(game_over_imagem, (janela_largura, janela_altura)) # escala da tela final
plataforma_imagem = pygame.image.load('imagens/platform.png') # imagem da plataforma
mosca_imagem = pygame.image.load('imagens/fly.png') # imagem da mosca
vitoriaregia_imagem = pygame.image.load('imagens/vitoria_regia.png') # imagem da vitória-régia
sal_imagem = pygame.image.load('imagens/sal.png') # imagem do sal
tela_inicial_imagem = pygame.image.load('imagens/telainicial.jpeg') # imagem da tela inicial
tela_inicial_imagem = pygame.transform.scale(tela_inicial_imagem, (janela_largura, janela_altura))
vida_imagem = pygame.image.load('imagens/vida.webp').convert_alpha()

#frame
clock = pygame.time.Clock()
FPS = 50

#variáveis do jogo 
rodar = 200
gravidade = 1 # quão rápido a sapa cai (1 pixel)
maximo_plataformas = 10 # máximo de plataformas na tela
rolagem = 0
background_rolagem = 0
placar = 0 
efeito_fim_de_jogo = 0 #efeito tela fechando 
contador_mosca = 0
pos_icone_mosca = (janela_largura - 180, 8.5)
contador_sal = 0
contador_vr = 0
vidas_restantes = 3
pos_icone_vida1 = (janela_largura - 90, 8)
pos_icone_vida2 = (janela_largura - 60, 8)
pos_icone_vida3 = (janela_largura - 30, 8)

# cores
branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 100, 120)
azul_claro = (80, 200, 230)

#fontes
fonte1 = pygame.font.SysFont(None, 35)

#função para escrever na tela
def escrever_texto(texto, fonte, cor_texto, x, y):
    imagem = fonte.render(texto, True, cor_texto)
    tela.blit(imagem, (x,y))

def desenhar_painel():
    pygame.draw.rect(tela, azul_claro, (0,0, janela_largura, 30))
    pygame.draw.line(tela, azul, (0, 30), (janela_largura, 30 ), 3) #placar em cima da tela 
    escrever_texto('SCORE: ' + str(placar), fonte1, azul, 10, 10) # pontuação 
    #exibir contador de moscas
    escrever_texto (': ' + str(contador_mosca), fonte1, azul, janela_largura - 148, 10)
    #exibir ícone da mosca
    tela.blit(pygame.transform.scale(mosca_imagem, (30, 20)), pos_icone_mosca)

def desenhar_vidas():
    if vidas_restantes >= 1:
        tela.blit(pygame.transform.scale(vida_imagem, (20, 20)), pos_icone_vida1)
    if vidas_restantes >= 2:
        tela.blit(pygame.transform.scale(vida_imagem, (20, 20)), pos_icone_vida2)
    if vidas_restantes >= 3:
        tela.blit(pygame.transform.scale(vida_imagem, (20, 20)), pos_icone_vida3)

# função para aparecer o background 
def draw_background(rolagem):
    tela.blit(background_imagem, (0, 0 + background_rolagem))
    tela.blit(background_imagem, (0, -600 + background_rolagem)) # dois backgrounds, um atrás do outro

#checar recorde
if os.path.exists('placar.txt'):
    with open('placar.txt','r') as file:
        recorde = int(file.read())    
else:
    recorde = 0

class Vitoriaregia(pygame.sprite.Sprite):

    def __init__(self, plataforma):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(vitoriaregia_imagem, (60, 45))
        self.rect = self.image.get_rect()
        self.rect.center = (plataforma.rect.center)
        self.rect.y -= 30

    def update(self, rolagem, janela_altura):
        self.rect.y += rolagem 

        if self.rect.top > janela_altura:
            self.kill()

class Mosca(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(mosca_imagem, (30, 30))  
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  

    def update(self, rolagem, janela_altura):
        self.rect.y += rolagem

        if self.rect.top > janela_altura:
            self.kill()  

class Sal(pygame.sprite.Sprite) :
    def __init__(self, plataforma) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(sal_imagem, (35, 45))
        self.rect = self.image.get_rect()
        self.rect.center = (plataforma.rect.center)
        self.rect.y -= 40

    def update(self, rolagem, janela_altura)  :
        self.rect.y += rolagem

        if self.rect.top > janela_altura :
            self.kill()

# jogador (sapa)
class Jogador():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(sapa_imagem, (140, 140)) # escala da imagem
        self.largura = 43 # largura do retângulo
        self.altura = 45 # altura do retângulo
        self.rect = pygame.Rect(0, 0, self.largura, self.altura) # criar um retângulo 
        self.rect.center = (x, y) # centralizar o retângulo na sapa
        self.vel_y = 0 # velocidade do eixo y
        self.poder_ativo = False

    def ativar_poder(self) :
        self.poder_ativo = True
        if self.poder_ativo :
            self. gravidade = 0.4 
            FPS = 100

    def desativar_poder(self) :
        self.poder_ativo = False


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
            if plataforma.rect.colliderect(self.rect.x, self.rect.y + dy, self.largura, self.altura):
                if self.rect.bottom < plataforma.rect.centery:
                    if self.vel_y > 0:
                        self.rect.bottom = plataforma.rect.top # se o fundo da sapa tocar no topo da plataforma
                        dy = 0
                        self.vel_y = -20

        if self.rect.top <= rodar:
            if self.vel_y < 0:
                rolagem = -dy # rolagem é o contrário do movimento da sapa

        # recentralizar o retângulo
        self.rect.x += dx
        self.rect.y += dy + rolagem

        return rolagem
    
    def ativar_poder(self):
        self.poder_ativo = True
        if self.poder_ativo:
            self.vel_y = -30  # Impulso vertical alto

    def desativar_poder(self):
        self.poder_ativo = False

    def draw(self): # 
        tela.blit(self.image, (self.rect.x - 50, self.rect.y - 70))        

#platafroma
class Plataforma(pygame.sprite.Sprite): 

    def __init__(self, x, y, largura, move):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(plataforma_imagem, (largura, 50)) # escala da plataforma
        self.mover = move
        self.contador_movimentos = random.randint(0,50)
        self.direcao = random.choice([-1,1])
        self.velocidade = random.randint(1,2)
        self.largura = largura # largura do retângulo
        self.altura = 30 # altura do retângulo
        self.rect = pygame.Rect(0, 0, self.largura, self.altura) # criar um retângulo 
        self.rect.center = (x, y) # centralizar o retângulo
        
        self.rect.x = x
        self.rect.y = y

    def update(self, rolagem):

        #mover a plataforma
        if self.mover == True:
            self.contador_movimentos += 1
            self.rect.x += self.direcao * self.velocidade
        
        #mudar a direção da plataforma
        if self.contador_movimentos>=100 or self.rect.left < 0 or self.rect.right > janela_largura:
            self.direcao *= -1
            self.contador_movimentos = 0

        # update a posição das plataformas enquanto a tela rola
        self.rect.y += rolagem 

         # excluir as plataformas que saem ta tela
        if self.rect.top > janela_altura:
            self.kill() 
    
platafroma_grupo = pygame.sprite.Group()
vitoriaregia_grupo = pygame.sprite.Group()
mosca_grupo = pygame.sprite.Group()
sal_grupo = pygame.sprite.Group()

sapa = Jogador(janela_largura // 2, janela_altura - 150) # posição da sapa inicial 

# plataforma inicial
plataforma = Plataforma(janela_largura // 2 - 23, janela_altura - 100, 50, False)
platafroma_grupo.add(plataforma)

# loop do jogo
game_over = False
loop = True

tela.blit(tela_inicial_imagem, (0, 0))  # desenho  da imagem na tela inicial
pygame.display.update()  

iniciou_jogo = False
while not iniciou_jogo:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            iniciou_jogo = True  

while loop:

    clock.tick(FPS)

    if game_over == False:
        FPS += 0.01
        rolagem = sapa.move()

        #desenhar tela de fundo
        background_rolagem += rolagem
        if background_rolagem >+ 600:
            background_rolagem = 0 # resetar a posição dos dois backgrounds, para ser infinito
        draw_background(background_rolagem) # fazer com que o background apareça na tela

        #gerar plataforma
        if len(platafroma_grupo) < maximo_plataformas:
            plataforma_largura = random.randint(60, 100) # largura das plataformas (entre 60 e 100)
            plataforma_x = random.randint(0, janela_largura - plataforma_largura) # posição no eixo x
            plataforma_y = plataforma.rect.y - random.randint(100, 190) # posição no eixo y
            
            #plataformas que se movem
            plataforma_tipo = random.randint(1,2)
            if plataforma_tipo==1 and placar > 3000:
                plataforma_movendo = True
            else:
                plataforma_movendo = False
            
            plataforma = Plataforma(plataforma_x, plataforma_y, plataforma_largura,plataforma_movendo) # gerar a plataforma
            platafroma_grupo.add(plataforma)

        #atualizar plataforma
        platafroma_grupo.update(rolagem)

        #gerar vitória-régia
        if len(vitoriaregia_grupo) == 0 and placar > 100:
            vitoriaregia = Vitoriaregia(plataforma)
            vitoriaregia_grupo.add(vitoriaregia)

        #atualizar vitória-régia
        vitoriaregia_grupo.update(rolagem, janela_altura)

        for vitoriaregia in vitoriaregia_grupo :
            if pygame.sprite.collide_rect(sapa, vitoriaregia):
                    # acionar o boost quando toca na vitória régia
                    if pygame.sprite.collide_rect(sapa, vitoriaregia):
                        sapa.ativar_poder()  # Ativa o impulso ao colidir com a vitória-régia
                        som_vitoriaregia.play()  # Toca o som de upgrade
                        contador_vr += 1 #Adiciona 1 ao contador de vitórias-régias
    
        if len(mosca_grupo) == 0 and placar > 100: 
            plataforma_x = random.randint(0, janela_largura - plataforma_largura)  # posição no eixo x da plataforma
            plataforma_y = plataforma.rect.y - random.randint(100, 190)  # posição no eixo y da plataforma

            # Garantir que a mosca seja gerada a pelo menos 20 pixels de distância das bordas das plataformas
            mosca_x = random.randint(max(plataforma_x + 20, 20), min(plataforma_x + plataforma_largura - 20, janela_largura - 20))
            mosca_y = plataforma_y

            mosca = Mosca(mosca_x, mosca_y)
            mosca_grupo.add(mosca)
        #atualizar mosca
        mosca_grupo.update(rolagem, janela_altura)
        #desenhar mosca
        mosca_grupo.draw(tela)

        for mosca in mosca_grupo:
            if pygame.sprite.collide_rect(sapa, mosca): #verifica se a sapa colidiu com a mosca 
                mosca.kill()  # Tira a mosca da tela
                som_mosca.play()  # Toca a música da mosca
                contador_mosca += 1 # Adiciona 1 ao contador de mosca
         
        if len(sal_grupo) == 0 and contador_mosca >= 1:
            sal = Sal(plataforma) 
            sal_grupo.add(sal)   

        sal_grupo.update(rolagem, janela_altura)
        sal_grupo.draw(tela)  

        for sal in sal_grupo :
                if pygame.sprite.collide_rect(sapa, sal) : # Verifica se a sapa colidiu com o saleiro
                    sal.kill() # Tira o saleiro da tela
                    som_sal.play() # Toca o som para o saleiro
                    vidas_restantes -= 1 # Elimina 1 das 3 vidas da sapa
                    contador_sal += 1 # Adiciona 1 ao contador de saleiro

        for mosca in mosca_grupo:
            if pygame.sprite.collide_rect(sapa, mosca): #verifica se a sapa colidiu com a mosca 
                mosca.kill() # Tira a mosca da tela
                som_mosca.play() # Toca o som da mosca  
                contador_mosca += 1 # Adiciona 1 ao contador de mosca
                if contador_mosca %5 == 0: #Verifica se ja tem 5 (ou um múltiplo de 5) moscas
                    if vidas_restantes<3: #Verifica se a sapa já perdeu alguma vida
                        vidas_restantes+=1 #Adiciona 1 vida

        if rolagem > 0:
            placar += rolagem

        #desenhar linha abaixo do recorde
            pygame.draw.line(tela, preto, (0, placar - recorde + rolagem), (janela_largura, placar - recorde + rolagem), 3)
            escrever_texto('RECORDE', fonte1, preto, janela_largura - 130, placar - recorde + rolagem)

        # adicionar as plataformas à tela
        platafroma_grupo.draw(tela) 
        vitoriaregia_grupo.draw(tela)
        sapa.draw()

        #desenhar painel 
        desenhar_painel()

        #desenhar vidas 
        desenhar_vidas()

        if vidas_restantes <= 0 :
            game_over = True
            morte.play()
            vidas_restantes = 3
            
        
        #ver se a sapa caiu 
        if sapa.rect.top > janela_altura:
            game_over = True
            morte.play()

        if sapa.rect.top > janela_altura and vidas_restantes>0:
            game_over = True
            morte.play()
            vidas_restantes = 3

    #se a sapinha cair      
    else:
        tela.blit(game_over_imagem, (0,0))
        escrever_texto(str(placar), fonte1, branco, 190, 198)
        escrever_texto(str(contador_mosca), fonte1, branco, 210, 230)
        escrever_texto(str(contador_vr), fonte1, branco, 315, 265)
        escrever_texto(str(contador_sal), fonte1, branco, 215, 300)
        pygame.mixer.music.set_volume(0)
        
        #atualizar recorde
        if placar>recorde:
            recorde=placar
            with open ('placar.txt','w') as file:
                file.write(str(recorde))

        key = pygame.key.get_pressed() #para identificar que a barra de espaço foi precionada
        if key[pygame.K_SPACE]:
            
            #reiniciar as variaveis para recomeçar o jogo 
            game_over = False
            placar = 0 
            rolagem = 0
            
            #reposicionar a sapinha  
            sapa.rect.center = (janela_largura // 2, janela_altura - 150) # posição da sapa inicial 
            
            #resetar as plataformas
            platafroma_grupo.empty()
            
            #cria a plataforma de início (de novo)
            plataforma = Plataforma(janela_largura // 2 - 23, janela_altura - 100, 50, plataforma_movendo)
            platafroma_grupo.add(plataforma)
            
            #reiniciar musica 
            musica_de_fundo = pygame.mixer.music.load('audios/sapo_nao_lava.mp3') #música de fundo
            pygame.mixer.music.play(-1,1.5)
            pygame.mixer.music.set_volume(1.5)

            #reiniciar velocidade do jogo 
            FPS = 50 

    for event in pygame.event.get(): # sair do jogo
        if event.type == pygame.QUIT:
            #atualizar recorde
            if placar>recorde:
                recorde=placar
                with open ('placar.txt','w') as file:
                    file.write(str(recorde))
            loop = False

    pygame.display.update() 

pygame.quit()