import pygame

pygame.init()


# creating the game window
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 500
game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("test game")


# colors
black = (0,0,0)
white =(255,255,255)
# game specific variables
ball_x = 250
ball_y = 250
ball_radius = 8
ball_vel_x = 5
ball_vel_y = 5

player_paddle_x = 0
player_paddle_y = 200
player_paddle_height = 70
player_paddle_width = 5
player_paddle_vel = 7
player_score = 0 

computer_paddle_width = player_paddle_width
computer_paddle_x = SCREEN_WIDTH - computer_paddle_width
computer_paddle_y = 250
computer_paddle_height = player_paddle_height
opponent_speed = 5
opponent_score = 0

clock = pygame.time.Clock()
fps = 60

font = pygame.font.SysFont(None, 30)
def show_text(text, color, x_pos, y_pos):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x_pos, y_pos])

# creating a gameloop
run_game = True

while run_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False   

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and player_paddle_y > 0:
        player_paddle_y -= player_paddle_vel    

    if keys[pygame.K_DOWN] and player_paddle_y < SCREEN_HEIGHT - player_paddle_height:
        player_paddle_y += player_paddle_vel

    ball_x += ball_vel_x
    ball_y += ball_vel_y

    game_window.fill(black)

    show_text("Opponent Score: " + str(opponent_score), white, 500, 10)

    ball = pygame.draw.circle(game_window, white, (ball_x, ball_y), ball_radius)

    player_paddle = pygame.draw.rect(game_window, white, (player_paddle_x, player_paddle_y, player_paddle_width, player_paddle_height))

    opponent = pygame.draw.rect(game_window, white, (computer_paddle_x, computer_paddle_y, computer_paddle_width, computer_paddle_height))

    middle_line = pygame.draw.rect(game_window, white, (SCREEN_WIDTH/2, 0, 2, SCREEN_HEIGHT))


    # ball animation
    

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_vel_y *= -1

    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_vel_x *= -1

    if ball.colliderect(player_paddle) or ball.colliderect(opponent):
        ball_vel_x *= -1
    
    if opponent.top < ball_y -10:
        computer_paddle_y += opponent_speed
    if opponent.bottom > ball_y + 10:
        computer_paddle_y -= opponent_speed

    if computer_paddle_y <= 0:
        computer_paddle_y = 0

    if computer_paddle_y >= SCREEN_HEIGHT:
        computer_paddle_y = SCREEN_HEIGHT - computer_paddle_height
    
    if ball.left <= 0:
        opponent_score += 1

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
