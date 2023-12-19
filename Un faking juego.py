import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de Plataformas con Monedas")

# Colores
white = (255, 255, 255)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Jugador
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10
player_speed = 5
jump = False
jump_count = 10

# Gravedad
gravity = 1
fall_speed = 0

# Plataforma
platform_width = 200
platform_height = 20
platform_x = screen_width // 2 - platform_width // 2
platform_y = screen_height - 100

# Monedas
coin_radius = 15
coins = [{'x': random.randint(50, screen_width - 50), 'y': random.randint(50, screen_height - 200)} for _ in range(5)]

# Contador de monedas
coin_count = 0
font = pygame.font.Font(None, 36)

# Bucle principal del juego
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

    # Verificar si la barra espaciadora se presiona para saltar
    if not jump:
        if keys[pygame.K_SPACE] and fall_speed == 0:
            jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jump = False
            jump_count = 10

    # Simular la gravedad y la caída del jugador
    fall_speed += gravity
    player_y += fall_speed

    # Restringir al jugador dentro de la pantalla
    player_x = max(0, min(screen_width - player_width, player_x))
    player_y = max(0, min(screen_height - player_height, player_y))

    # Verificar colisión con la plataforma
    if (
        player_x < platform_x + platform_width
        and player_x + player_width > platform_x
        and player_y < platform_y + platform_height
    ):
        if fall_speed > 0:  # Solo si está cayendo (hacia abajo)
            player_y = platform_y - player_height
            fall_speed = 0

    # Verificar colisión con las monedas
    for coin in coins:
        if (
            player_x < coin['x'] + coin_radius
            and player_x + player_width > coin['x'] - coin_radius
            and player_y < coin['y'] + coin_radius
            and player_y + player_height > coin['y'] - coin_radius
        ):
            coin_count += 1
            coins.remove(coin)
            coins.append({'x': random.randint(50, screen_width - 50), 'y': random.randint(50, screen_height - 200)})

    # Dibujar en la pantalla
    screen.fill(white)
    pygame.draw.rect(screen, blue, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(
        screen, blue, (platform_x, platform_y, platform_width, platform_height)
    )
    
    # Dibujar monedas
    for coin in coins:
        pygame.draw.circle(screen, yellow, (coin['x'], coin['y']), coin_radius)

    # Mostrar el contador de monedas
    text = font.render(f'Monedas: {coin_count}', True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
