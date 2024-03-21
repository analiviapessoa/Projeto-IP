import pygame

#dimensões da tela
LARGURA = 400
ALTURA = 600

#título do jogo 
TITULO_JOGO = 'Flying Froggy'

#frames por segundos 
FPS = 60

# cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 100, 120)
AZUL_CLARO = (80, 200, 230)

TELA = pygame.display.set_mode((LARGURA, ALTURA))

#frame
CLOCK = pygame.time.Clock()

#imagens

SAPA_IMAGEM = pygame.image.load('imagens/sapa.png') # imagem da sapa
BACKGROUND_IMAGEM = pygame.image.load('imagens/ceu.png') # imagem do background
BACKGROUND_IMAGEM = pygame.transform.scale(BACKGROUND_IMAGEM, (LARGURA, ALTURA)) # escala do background
GAME_OVER_IMAGEM = pygame.image.load('imagens/gameover.png') # imagem da tela final
GAME_OVER_IMAGEM = pygame.transform.scale(GAME_OVER_IMAGEM, (LARGURA, ALTURA)) # escala da tela final
PLATAFORMA_IMAGEM = pygame.image.load('imagens/platform.png') # imagem da plataforma
MOSCA_IMAGEM = pygame.image.load('imagens/fly.png') # imagem da mosca
VITORIA_REGIA_IMAGEM = pygame.image.load('imagens/vitoria_regia.png') # imagem da vitória-régia
SAL_IMAGEM = pygame.image.load('imagens/sal.png') # imagem do sal
TELA_INICIAL_IMAGEM = pygame.image.load('imagens/ntelainicial.png') # imagem da tela inicial
TELA_INICIAL_IMAGEM = pygame.transform.scale(TELA_INICIAL_IMAGEM, (LARGURA, ALTURA))
VIDA_IMAGEM = pygame.image.load('imagens/vida.webp').convert_alpha()


#variáveis do jogo 
RODAR = 200
GRAVIDADE = 1 # quão rápido a sapa cai (1 pixel)
MAXIMO_PLATAFORMAS = 10 # máximo de plataformas na tela
ROLAGEM = 0
BACKGROUND_ROLAGEM = 0
PLACAR = 0 
EFEITO_FIM_DE_JOGO = 0 #efeito tela fechando 
CONTADOR_MOSCA = 0
POS_ICONE_MOSCA = (LARGURA - 180, 8.5)
CONTADOR_SAL = 0
CONTADOR_VR = 0
VIDAS_RESTANTES = 3
POS_ICONE_VIDA1 = (LARGURA - 90, 8)
POS_ICONE_VIDA2 = (LARGURA - 60, 8)
POS_ICONE_VIDA3 = (LARGURA - 30, 8)


