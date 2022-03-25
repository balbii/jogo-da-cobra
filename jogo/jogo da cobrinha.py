#Joguinho do Rafa e do José...

import pygame, random
from pygame.locals import *

#Definindo onde a maça ira aparecer no jogo
def on_grid_random():
    x = random.randint(0,107)
    y = random.randint(0,71)
    return (x * 10, y * 10)

def collision(c1, c2): #definindo colisões
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

#definindo teclas
w = 0
d = 1
s = 2
a = 3

#é aqui que a magica acontece
pygame.init()
screen = pygame.display.set_mode((1080, 720))#tamanho de tela padrao ne
pygame.display.set_caption('Jogo da Cobrinha')#nome criativo

cobra = [(200, 200), (210, 200), (220,200)] 
cobra_skin = pygame.Surface((10,10))
cobra_skin.fill((255,255,255)) 

maça_pos = on_grid_random()
maça = pygame.Surface((10,10))
maça.fill((255,255,255))


my_direction = a

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 50)
score = 0

game_over = False
while not game_over:
    clock.tick(35)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == KEYDOWN:
            if event.key == K_w and my_direction != s:
                my_direction = w
            if event.key == K_s and my_direction != w:
                my_direction = s
            if event.key == K_a and my_direction != d:
                my_direction = a
            if event.key == K_d and my_direction != a:
                my_direction = d

    if collision(cobra[0], maça_pos):
        maça_pos = on_grid_random()
        cobra.append((0,0))
        score = score + 1
        
    if cobra[0][0] == 1080 or cobra[0][1] == 720 or cobra[0][0] < 0 or cobra[0][1] < 0:
        game_over = True
        break
    
    for i in range(1, len(cobra) - 1):
        if cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]:
            game_over = True
            break

    if game_over:
        break
    
    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])
        
    if my_direction == w:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if my_direction == s:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if my_direction == d:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if my_direction == a:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])
    
    screen.fill((0,0,0))
    screen.blit(maça, maça_pos)
    
    for x in range(0, 1080, 10): 
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 1080))
    for y in range(0, 1080, 10):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (1080, y))
    
    score_font = font.render('Pontos: %s' % (score), True, (255, 255, 255))
    score_rect = score_font.get_rect()
    score_rect.topleft = (100 - 100, 0)
    screen.blit(score_font, score_rect)
    
    for pos in cobra:
        screen.blit(cobra_skin,pos)

    pygame.display.update()

while True:
    game_over_font = pygame.font.Font('freesansbold.ttf', 75)
    game_over_screen = game_over_font.render('Você Perdeu', True, (255, 255, 255))
    game_over_rect = game_over_screen.get_rect()
    game_over_rect.midtop = (1080 / 2, 250)
    screen.blit(game_over_screen, game_over_rect)
    pygame.display.update()
    pygame.time.wait(500)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
