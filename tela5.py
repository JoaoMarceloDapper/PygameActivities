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
    pygame.draw.line( display, preto, (0, 600), (800, 0), 2 )
    pygame.draw.circle( display, preto, (400, 300), 70 )
    pygame.display.update()

pygame.quit()