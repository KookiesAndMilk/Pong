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
#Definir alto y ancho de jugadores
player_h = 100
player_w = 15
#Pantalla
screen_size = (800,600)

#Coordenadas de jugadores y velocidad
player1_x= 50
player1_y= 300 - 50
player1_speed_y = 0

#P2
player2_x= 750 - player_w
player2_y= 300 - 50
player2_speed_y = 0

#Definir velocidad de pelota
pelota_x= 400
pelota_y = 300
pelota_speed_x = 3
pelota_speed_y = 3

#definir FPS
clock = pygame.time.Clock()

screen = pygame.display.set_mode(screen_size)

#Game over
game_over = False

paused = False

max_speed = 10

def reset_game():
    global pelota_x, pelota_y, pelota_speed_x, pelota_speed_y, paused
    pelota_x=400
    pelota_y = 300
    pelota_speed_x = 3
    pelota_speed_y = 3
    paused = True

def resume_game():
    global pelota_speed_x, pelota_speed_y
    pelota_speed_x = 3
    pelota_speed_y = 3

while not game_over:
    for event in pygame.event.get():
        #print (event)
        if event.type == pygame.QUIT:
            game_over == True
            sys.exit()
    #Definir teclas del jugador 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w :
                player1_speed_y = -3
            if event.key == pygame.K_s :
                player1_speed_y = 3
            #Definir teclas del jugador 2
            if event.key == pygame.K_UP:
                player2_speed_y = -3
            if event.key == pygame.K_DOWN:
                player2_speed_y = 3
            if event.key == pygame.K_RETURN and paused:
                paused = False
                resume_game()
        if event.type == pygame.KEYUP:
            #Player1
            if event.key == pygame.K_w:
                player1_speed_y = 0
            if event.key == pygame.K_s:
                player1_speed_y = 0
            #Player2
            if event.key == pygame.K_UP:
                player2_speed_y = 0
            if event.key == pygame.K_DOWN:
                player2_speed_y = 0
    
    if not paused:
        player1_y += player1_speed_y
        player2_y += player2_speed_y

        if player1_y < 0:
            player1_y = 0
        if player1_y > 600 - player_h:
            player1_y = 600 - player_h
        if player2_y < 0:
            player2_y = 0
        if player2_y > 600 - player_h:
            player2_y = 600 - player_h


    #Hacer que la pelota rebote
    if pelota_y > 590 or pelota_y < 10:
        pelota_speed_y *= -1
    # Reiniciar el juego si la pelota sale de la pantalla
    if pelota_x > 800 or pelota_x < 0:
        reset_game()

    #Hacer que la pelota aparezca de nuevo
    if pelota_x > 800:
        pelota_x = 400
        pelota_y = 300
         #Invertir el lado de la pelota
        pelota_speed_x *= -1
        pelota_speed_y *= -1
        
    if pelota_x <0:
        pelota_x = 400
        pelota_y = 300
    
        #Invertir el lado de la pelota
        pelota_speed_x *= -1
        pelota_speed_y *= -1


    #Movimiento de pelota y jugadores
    player1_y += player1_speed_y
    player2_y += player2_speed_y
    
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y

    

    #Color de fondo
    screen.fill(BLACK)
    
    ###------- zona de dibujo
    player1 = pygame.draw.rect(screen, WHITE, (player1_x, player1_y, player_w, player_h))
    player2 = pygame.draw.rect(screen, WHITE, (player2_x, player2_y, player_w, player_h))
    pelota = pygame.draw.circle(screen, WHITE,(pelota_x, pelota_y), 10)

    ''' for x in range (100,700,100):
        pygame.draw.rect(screen, WHITE, (x, 230, 50, 50 ))
        pygame.draw.line(screen, GREEN, (x,0), (x,100), 5) '''
    #pygame.draw.line(screen, RED, [0,100], [500, 100], 5)
    #pygame.draw.rect(screen, RED, (100, 100, 80, 80))
    #pygame.draw.circle(screen,BLUE, (500, 500), 50 )
    #pygame.draw.circle(screen, BLACK, center, outer_radius)
    ###------- zona de dibujo
    #Colisión de pelota
    if pelota.colliderect(player1) or pelota.colliderect(player2) :
        pelota_speed_x *= -1

        if abs(pelota_speed_x) < max_speed:
            pelota_speed_x *= 1.1  # Incrementa la velocidad gradualmente
            pelota_speed_y *= 1.1

    #Actualizar pantalla
    pygame.display.flip() 
    clock.tick(60)
    pass
