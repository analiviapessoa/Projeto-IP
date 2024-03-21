import pygame
import constantes
from coletaveis import *
from main import *

# jogador (sapa)
class Jogador():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(constantes.SAPA_IMAGEM , (140, 140)) # escala da imagem
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
            constantes.FPS = 100

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

        self.vel_y += constantes.GRAVIDADE # acelerar o pulo
        dy += self.vel_y

        # colisão da tela (para a sapa não conseguir ir além da borda da janela do jogo)
        if self.rect.left + dx < 0: # se a sapa for além da janela do lado esquerdo
            dx = - self.rect.left # parar quando alcançar a tela
        if self.rect.right + dx > constantes.LARGURA: # se a sapa for além da janela do lado direito
            dx = constantes.LARGURA - self.rect.right


        # colisão com as plataformas
        from main import platafroma_grupo

        for plataforma in platafroma_grupo:
            if plataforma.rect.colliderect(self.rect.x, self.rect.y + dy, self.largura, self.altura):
                if self.rect.bottom < plataforma.rect.centery:
                    if self.vel_y > 0:
                        self.rect.bottom = plataforma.rect.top # se o fundo da sapa tocar no topo da plataforma
                        dy = 0
                        self.vel_y = -20

        if self.rect.top <= (constantes.RODAR):
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
        constantes.TELA.blit(self.image, (self.rect.x - 50, self.rect.y - 70))

