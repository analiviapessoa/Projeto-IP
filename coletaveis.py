import pygame
import constantes


class Vitoriaregia(pygame.sprite.Sprite):

    def __init__(self, plataforma):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(constantes.VITORIA_REGIA_IMAGEM, (60, 45))
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
        self.image = pygame.transform.scale(constantes.MOSCA_IMAGEM, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, rolagem, janela_altura):
        self.rect.y += rolagem

        if self.rect.top > janela_altura:
            self.kill()

class Sal(pygame.sprite.Sprite) :
    def __init__(self, plataforma) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(constantes.SAL_IMAGEM, (35, 45))
        self.rect = self.image.get_rect()
        self.rect.center = (plataforma.rect.center)
        self.rect.y -= 40

    def update(self, rolagem, janela_altura)  :
        self.rect.y += rolagem

        if self.rect.top > janela_altura :
            self.kill()
