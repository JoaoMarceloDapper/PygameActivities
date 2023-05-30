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
    pygame.draw.line( display, preto, (40, 40), (700, 40),2 )
    pygame.draw.line( display, preto, (40, 40), (400, 400),2 )
    pygame.draw.line( display, preto, (700, 40), (400, 400),2 )
    pygame.display.update()

pygame.quit()