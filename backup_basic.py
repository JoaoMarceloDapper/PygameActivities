import pygame
pygame.init()
tamanho = (800,600)
display = pygame.display.set_mode(tamanho)
branco = (255, 255, 255)
preto = (0, 0, 0)
clock = pygame.time.Clock( )
running = True
posicaobolina = 40
direcaobolina = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.fill(branco)
    pygame.draw.circle( display, preto, (400, 300), 10 )
    pygame.draw.line( display, preto, (200, 150), (600, 150), 2 )

    pygame.draw.circle( display, preto, ( posicaobolina, 500 ), 30 )
    if posicaobolina>800:
        direcaobolina = False
    elif posicaobolina <=0 :
        direcaobolina = True
    
    if direcaobolina:
        posicaobolina = posicaobolina +10
    else:
        posicaobolina = posicaobolina -10

    pygame.display.update()
    clock.tick(60)
pygame.quit()