#bibliotecas
import pygame
import random
import os
import constantes
from jogador import *
from coletaveis import *


#iniciar
pygame.init()

 # criar uma janela
pygame.display.set_caption(constantes.TITULO_JOGO) # nome do jogo

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




background_rolagem = 0
placar = 0 
efeito_fim_de_jogo = 0 #efeito tela fechando 
contador_mosca = 0
contador_sal = 0
contador_vr = 0
vidas_restantes = 3


#fontes
fonte1 = pygame.font.SysFont(None, 35)

#função para escrever na tela
def escrever_texto(texto, fonte, cor_texto, x, y):
    imagem = fonte.render(texto, True, cor_texto)
    constantes.TELA.blit(imagem, (x,y))

def desenhar_painel():
    pygame.draw.rect(constantes.TELA, constantes.AZUL_CLARO, (0,0, constantes.LARGURA, 30))
    pygame.draw.line(constantes.TELA, constantes.AZUL, (0, 30), (constantes.LARGURA, 30 ), 3) #placar em cima da tela 
    escrever_texto('SCORE: ' + str(placar), fonte1, constantes.AZUL, 10, 10) # pontuação 
    #exibir contador de moscas
    escrever_texto (': ' + str(contador_mosca), fonte1, constantes.AZUL, constantes.LARGURA - 148, 10)
    #exibir ícone da mosca
    constantes.TELA.blit(pygame.transform.scale(constantes.MOSCA_IMAGEM, (30, 20)), constantes.POS_ICONE_MOSCA)

def desenhar_vidas():
    if vidas_restantes >= 1:
        constantes.TELA.blit(pygame.transform.scale(constantes.VIDA_IMAGEM, (20, 20)), constantes.POS_ICONE_VIDA1)
    if vidas_restantes >= 2:
        constantes.TELA.blit(pygame.transform.scale(constantes.VIDA_IMAGEM, (20, 20)), constantes.POS_ICONE_VIDA2)
    if vidas_restantes >= 3:
        constantes.TELA.blit(pygame.transform.scale(constantes.VIDA_IMAGEM, (20, 20)), constantes.POS_ICONE_VIDA3)

# função para aparecer o background 
def draw_background(rolagem):
    constantes.TELA.blit(constantes.BACKGROUND_IMAGEM, (0, 0 + background_rolagem))
    constantes.TELA.blit(constantes.BACKGROUND_IMAGEM, (0, -600 + background_rolagem)) # dois backgrounds, um atrás do outro

#checar recorde
if os.path.exists('placar.txt'):
    with open('placar.txt','r') as file:
        recorde = int(file.read())    
else:
    recorde = 0

#platafroma
class Plataforma(pygame.sprite.Sprite): 

    def __init__(self, x, y, largura, move):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(constantes.PLATAFORMA_IMAGEM, (largura, 50)) # escala da plataforma
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
        if self.contador_movimentos>=100 or self.rect.left < 0 or self.rect.right > constantes.LARGURA:
            self.direcao *= -1
            self.contador_movimentos = 0

        # update a posição das plataformas enquanto a tela rola
        self.rect.y += rolagem 

         # excluir as plataformas que saem ta tela
        if self.rect.top > constantes.ALTURA:
            self.kill() 
    
platafroma_grupo = pygame.sprite.Group()
vitoriaregia_grupo = pygame.sprite.Group()
mosca_grupo = pygame.sprite.Group()
sal_grupo = pygame.sprite.Group()

sapa = Jogador(constantes.LARGURA // 2, constantes.ALTURA - 150) # posição da sapa inicial 

# plataforma inicial
plataforma = Plataforma(constantes.LARGURA // 2 - 23, constantes.ALTURA - 100, 50, False)
platafroma_grupo.add(plataforma)

# loop do jogo
game_over = False
loop = True

constantes.TELA.blit(constantes.TELA_INICIAL_IMAGEM, (0, 0))  # desenho  da imagem na tela inicial
pygame.display.update()  

iniciou_jogo = False
while not iniciou_jogo:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                iniciou_jogo = True 

while loop:

    constantes.CLOCK.tick(constantes.FPS)

    if game_over == False:
        constantes.FPS += 0.01
        rolagem = sapa.move()

        #desenhar tela de fundo
        background_rolagem += rolagem
        if background_rolagem >+ 600:
            background_rolagem = 0 # resetar a posição dos dois backgrounds, para ser infinito
        draw_background(background_rolagem) # fazer com que o background apareça na tela

        #gerar plataforma
        if len(platafroma_grupo) < constantes.MAXIMO_PLATAFORMAS:
            plataforma_largura = random.randint(60, 100) # largura das plataformas (entre 60 e 100)
            plataforma_x = random.randint(0, constantes.LARGURA - plataforma_largura) # posição no eixo x
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
        vitoriaregia_grupo.update(rolagem, constantes.ALTURA)

        for vitoriaregia in vitoriaregia_grupo :
            if pygame.sprite.collide_rect(sapa, vitoriaregia):
                    # acionar o boost quando toca na vitória régia
                    if pygame.sprite.collide_rect(sapa, vitoriaregia):
                        sapa.ativar_poder()  # Ativa o impulso ao colidir com a vitória-régia
                        som_vitoriaregia.play()  # Toca o som de upgrade
                        contador_vr += 1 #Adiciona 1 ao contador de vitórias-régias
    
        if len(mosca_grupo) == 0 and placar > 100: 
            plataforma_x = random.randint(0, constantes.LARGURA - plataforma_largura)  # posição no eixo x da plataforma
            plataforma_y = plataforma.rect.y - random.randint(100, 190)  # posição no eixo y da plataforma

            # Garantir que a mosca seja gerada a pelo menos 20 pixels de distância das bordas das plataformas
            mosca_x = random.randint(max(plataforma_x + 20, 20), min(plataforma_x + plataforma_largura - 20, constantes.LARGURA - 20))
            mosca_y = plataforma_y

            mosca = Mosca(mosca_x, mosca_y)
            mosca_grupo.add(mosca)
        #atualizar mosca
        mosca_grupo.update(rolagem, constantes.ALTURA)
        #desenhar mosca
        mosca_grupo.draw(constantes.TELA)
         
        if len(sal_grupo) == 0 and contador_mosca >= 1:
            sal = Sal(plataforma) 
            sal_grupo.add(sal)   

        sal_grupo.update(rolagem, constantes.ALTURA)
        sal_grupo.draw(constantes.TELA)  

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
                if contador_mosca %4 == 0: #Verifica se ja tem 5 (ou um múltiplo de 5) moscas
                    if vidas_restantes<3: #Verifica se a sapa já perdeu alguma vida
                        vidas_restantes+=1 #Adiciona 1 vida



        if rolagem > 0:
            placar += rolagem

        #desenhar linha abaixo do recorde
            pygame.draw.line(constantes.TELA, constantes.PRETO, (0, placar - recorde + rolagem), (constantes.LARGURA, placar - recorde + rolagem), 3)
            escrever_texto('RECORDE', fonte1, constantes.PRETO, constantes.LARGURA - 130, placar - recorde + rolagem)

        # adicionar as plataformas à tela
        platafroma_grupo.draw(constantes.TELA) 
        vitoriaregia_grupo.draw(constantes.TELA)
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
        if sapa.rect.top > constantes.ALTURA:
            game_over = True
            morte.play()

        if sapa.rect.top > constantes.ALTURA and vidas_restantes>0:
            game_over = True
            morte.play()
            vidas_restantes = 3

    #se a sapinha cair      
    else:
        constantes.TELA.blit(constantes.GAME_OVER_IMAGEM, (0,0))
        escrever_texto(str(placar), fonte1, constantes.BRANCO, 190, 198)
        escrever_texto(str(contador_mosca), fonte1, constantes.BRANCO, 210, 230)
        escrever_texto(str(contador_vr), fonte1, constantes.BRANCO, 315, 265)
        escrever_texto(str(contador_sal), fonte1, constantes.BRANCO, 215, 300)
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
            contador_mosca = 0
            contador_vr = 0
            contador_sal = 0
            
            #reposicionar a sapinha  
            sapa.rect.center = (constantes.LARGURA // 2, constantes.ALTURA - 150) # posição da sapa inicial 
            
            #resetar as plataformas
            platafroma_grupo.empty()
            
            #cria a plataforma de início (de novo)
            plataforma = Plataforma (constantes.LARGURA // 2 - 23, constantes.ALTURA - 100, 50, plataforma_movendo)
            platafroma_grupo.add(plataforma)
            
            #reiniciar musica 
            musica_de_fundo = pygame.mixer.music.load('audios/sapo_nao_lava.mp3') #música de fundo
            pygame.mixer.music.play(-1,1.5)
            pygame.mixer.music.set_volume(1.5)

            #reiniciar velocidade do jogo 
            constantes.FPS = 50 

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