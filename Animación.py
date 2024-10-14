import pygame, sys
pygame.init ()

#Colores
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

#center = (200, 200)
#outer_radius = 100
#inner_radius = 80

#Pantalla
screen_size = (800,600)

#Coordenadas del cuadro
cord_x = 400
cord_y = 200

#Definir velocidad
speed_x = 3
speed_y = 3

#definir FPS
clock = pygame.time.Clock()

screen = pygame.display.set_mode(screen_size)


while True:
    for event in pygame.event.get():
        #print (event)
        if event.type == pygame.QUIT:
    
            sys.exit()

    if ( cord_x > 720 or cord_x < 0):
        speed_x *= -1
    if (cord_y >520 or cord_y < 0):
        speed_y *= -1
        
    cord_x += speed_x
    cord_y += speed_y
    #Color de fondo
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (cord_x,cord_y,80,80))
    ###------- zona de dibujo
    ''' for x in range (100,700,100):
        pygame.draw.rect(screen, WHITE, (x, 230, 50, 50 ))
        pygame.draw.line(screen, GREEN, (x,0), (x,100), 5) '''
    #pygame.draw.line(screen, RED, [0,100], [500, 100], 5)
    #pygame.draw.rect(screen, RED, (100, 100, 80, 80))
    #pygame.draw.circle(screen,BLUE, (500, 500), 50 )
    #pygame.draw.circle(screen, BLACK, center, outer_radius)
    ###------- zona de dibujo

    #Actualizar pantalla
    pygame.display.flip() 
    clock.tick(60)
    pass


