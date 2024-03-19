import pygame
pygame.init()

W,H = 600,400
WHITE = (255,255,255)
RED = (255,0,0)

sc = pygame.display.set_mode((W,H), pygame.RESIZABLE)

clock = pygame.time.Clock()
FPS = 60

x = W // 2
y = H //2
speed = 5
circle_radius = 25

flUp = flDown =flLeft = flRight = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                flLeft = True
            elif event.key == pygame.K_RIGHT:
                flRight = True
            elif event.key == pygame.K_UP:
                flUp = True
            elif event.key == pygame.K_DOWN:
                flDown = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]:
                flUp = flDown = flLeft = flRight = False
        elif event.type == pygame.VIDEORESIZE:
            W, H = event.size 
            x = W // 2 
            y = H // 2
            sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)

    if flLeft and x > 0:
        x -= speed
    elif flRight and x < W:
        x += speed
    if flUp and y > 0:
        y -= speed
    elif flDown and y < H:
        y += speed


    sc.fill(WHITE)
    pygame.draw.circle(sc, RED, (x, y), circle_radius)
    pygame.display.update()
            

    clock.tick(FPS)