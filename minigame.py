#Mini Game Python / TONYTPDG 

import pygame
import random
import sys

# Iniciando o jogo
pygame.init()

# configuração da tela
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird - Mini")
clock = pygame.time.Clock()

# cores (pode mudar)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235)  # Cor do céu
GREEN = (34, 139, 34)   # Cor dos canos
YELLOW = (255, 215, 0)  # Cor do pássaro

# algumas variáveis do jogo
bird_x = 50
bird_y = HEIGHT // 2
bird_velocity = 0
gravity = 0.5
jump_strength = -8

pipe_width = 70
pipe_gap = 150
pipe_x = WIDTH
pipe_height = random.randint(100, 400)
pipe_velocity = 4

score = 0
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 24)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

running = True
game_over = False

# loop principal do jogo (não errar nada aqui!!!!!)
while running:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                # pulo do pássaro (espaço)
                bird_velocity = jump_strength
            if event.key == pygame.K_SPACE and game_over:
                # reiniciar o jogo (sempre que perder, reinicia )
                bird_y = HEIGHT // 2
                bird_velocity = 0
                pipe_x = WIDTH
                pipe_height = random.randint(100, 400)
                score = 0
                game_over = False

    if not game_over:
        # física do pássaro (gravidade e velocidade)
        bird_velocity += gravity
        bird_y += bird_velocity

        # movimento dos obstaculos do mapa
        pipe_x -= pipe_velocity
        if pipe_x < -pipe_width:
            pipe_x = WIDTH
            pipe_height = random.randint(100, 400)
            score += 1

        # desenho do passaro 
        bird_rect = pygame.Rect(bird_x, int(bird_y), 30, 30)
        pygame.draw.ellipse(screen, YELLOW, bird_rect)

        # desenho dos obstaculos
        top_pipe = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
        bottom_pipe = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, HEIGHT - pipe_height - pipe_gap)
        pygame.draw.rect(screen, GREEN, top_pipe)
        pygame.draw.rect(screen, GREEN, bottom_pipe)

        # checar colisão 
        if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
            game_over = True
        if bird_y > HEIGHT or bird_y < 0:
            game_over = True

        # placar (canto superior )
        draw_text(f"Score: {score}", font, WHITE, screen, 10, 10)
    else:
        # tela de game ouver (caso perca no jogo)
        draw_text("GAME OVER", font, BLACK, screen, 90, HEIGHT // 2 - 50)
        draw_text("Pressione ESPAÇO para reiniciar", small_font, BLACK, screen, 65, HEIGHT // 2 + 10)

    # atualizar a tela
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()