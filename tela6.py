import pygame
pygame.init()
tamanho = (800,600)
display = pygame.display.set_mode(tamanho)
branco = (255, 255, 255)
preto = (0, 0, 0)
clock = pygame.time.Clock( )
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.fill(branco)
    pygame.draw.circle( display, preto, (50, 50), 30 )
    pygame.draw.line( display, preto, (50, 50), (150, 400), 2 )
    pygame.draw.circle( display, preto, (150, 400), 30 )
    pygame.draw.line( display, preto, (150, 400), (400, 250), 2 )
    pygame.draw.circle( display, preto, (400, 250), 30 )
    pygame.draw.line( display, preto, (400, 250), (600, 250), 2 )
    pygame.draw.circle( display, preto, (600, 250), 30 )
    pygame.display.update()

pygame.quit()