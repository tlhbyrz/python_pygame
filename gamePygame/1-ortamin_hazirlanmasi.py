import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))

pygame.display.set_caption("pygame deneme")

x = 50
y = 50
width = 60
heigth = 60
vel = 10

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_LEFT]:
        x -= vel    

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, heigth))
    pygame.display.update()

pygame.quit()
