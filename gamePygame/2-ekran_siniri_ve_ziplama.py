import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))

pygame.display.set_caption("pygame deneme")

x = 50
y = 50
width = 60
heigth = 60
vel = 10

jumpCount = 10
isJump = False

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_LEFT]:
        x -= vel

    if not isJump:
        if keys[pygame.K_UP]:
            y -= vel

        if keys[pygame.K_DOWN]:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True

    #bu kismi stackoverflowdan aldim.Pek anlamadim.Ama calisiyor.
    else:
        if jumpCount >= -10:
            isJump = True
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.3 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, heigth))
    pygame.display.update()

pygame.quit()



