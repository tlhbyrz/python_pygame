import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))

pygame.display.set_caption("2D OYUN TASARIMI")

clock = pygame.time.Clock()

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

x = 50
y = 400
width = 64
heigth = 64
vel = 10

jumpCount = 10
isJump = False

left = False
right = False
walkCount = 0

def draw_the_game():
    global walkCount
    screen.blit(bg, (0,0))
    if walkCount > 26:  #27 fps de oynuyoruz cunku
        walkCount =0
    
    if right:
        screen.blit(walkRight[walkCount//3],(x,y))
    elif left:
        screen.blit(walkLeft[walkCount//3],(x,y))
    else:
        screen.blit(char,(x,y))
    pygame.display.update()

run = True
while run:
    #fps yi ayarliyor
    clock.tick(27) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel
        left = False
        true = True
        walkCount += 1

    elif keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        true = False
        walkCount += 1

    else:
        left = False
        true = False
        walkCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            true = False

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

    draw_the_game()    

pygame.quit()



