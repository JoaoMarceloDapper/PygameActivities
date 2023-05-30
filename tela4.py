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
    pygame.draw.line( display, preto, (0, 300), (800, 300), 2 )
    pygame.draw.line( display, preto, (20, 150), (20, 500), 2 )
    pygame.draw.line( display, preto, (22, 150), (100, 400), 2 )
    pygame.draw.line( display, preto, (150, 180), (100, 400), 2 )
    pygame.draw.line( display, preto, (150, 180), (150, 500), 2 )
    pygame.draw.line( display, preto, (300, 40), (150, 500),2 )
    pygame.draw.line( display, preto, (300, 40), (400, 400),2 )
    pygame.display.update()

pygame.quit()