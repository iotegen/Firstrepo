
import pygame
from random import randrange
from time import sleep
import psycopg2

size = width, height = 1050, 650
block = 25

x, y = randrange(0, width, block), randrange(0, height, block)
apple = randrange(0, width, block), randrange(0, height, block)
orange = randrange(0, width, block), randrange(0, height, block)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
score = 0
level = 0
snake = [(x, y)]
dx, dy = 0, 0
fps = 10
walls = []

pygame.init()
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_level = pygame.font.SysFont('Arial', 26, bold=True)
font_menu = pygame.font.SysFont('Arial', 85,bold=True)
game_background = pygame.image.load('background.jpg')
menu_background = pygame.image.load('menu_background.jpg')


def login(name):
    cur.execute("SELECT name, score, level FROM snake")
    row = cur.fetchall()
    for rows in row:
        if name == rows[0]:
            print(f'You have successfully logged into your account {name}. \nYour data: Score: {rows[1]}\nLevel: {rows[2]}.')
            return False
    return True


def record(name):
    cur.execute("SELECT name, score, level from snake")
    row = cur.fetchall()
    for rows in row:
        if name == rows[0]:
            if result[1] >= int(rows[2]) and result[0] > int(rows[1]):
                cur.execute(f"UPDATE snake set score = {str(result[0])}, level = {str(result[1])} where name = '{name}'")
                con.commit()
                return True
    return False


global con, cur

con = psycopg2.connect(
    database='Snake',
    user='postgres',
    password='Iliyas2004',
    host="localhost",
)

cur = con.cursor()


name = input('Input your name: ')

if login(name):
    cur.execute(f'''INSERT INTO snake (name, score, level) VALUES('{name}', 0, 0)''')
    con.commit()
    print('Welcome, new player!')
    
con.commit()



def main_menu():
    menu = True
    while menu:
        screen.blit(menu_background, (0, 0))
        
        # menu text
        render_menu = font_menu.render('CLICK', True, pygame.Color('black'))
        screen.blit(render_menu, (430, 550))

        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and 430 <= mx <= 550 and 570 <= my <= 600:
                menu = False

        pygame.display.flip()

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]: # K_RETURN - нажатие на Enter
            break

main_menu()
working = True
while working:
    screen.blit(game_background, (0, 0))

    # drawing snake, apple, walls
    for i, j in snake:
        pygame.draw.rect(screen, (255, 255, 255), (i, j, block - 1, block - 1))
    pygame.draw.rect(screen, (255, 0, 0), (*apple, block, block))
    if score % 3 == 0 and score > 0:
        pygame.draw.rect(screen, (255, 20, 190), (*orange,block,block))
    for i, j in walls:
        pygame.draw.rect(screen, (255, 255, 0), (i, j, block - 1, block - 1))

    # show score
    render_score = font_score.render(f'SCORE: {score}', True, pygame.Color('orange'))
    screen.blit(render_score, (5, 5))    
    render_level = font_level.render(f'LEVEL: {level}', True, pygame.Color('aqua'))
    screen.blit(render_level, (880,5))
    
    # snake movement
    x += dx * block
    y += dy * block
    snake.append((x, y))
    snake = snake[-length:]
    

    # game over
    if x < 0 or x > width - block or y < 0 or y > height - block or len(snake) > len(set(snake)) or snake[-1] in walls:
        while working:
            render_end = font_end.render('GAME OVER', True, pygame.Color('orange'))
            screen.blit(render_end, (335, 300))
            pygame.display.flip()
            result = [score, level]
            if record(name):
                print(f'New record: {score}.')
            sleep(2)
            working = False
                
    # eating apple
    if snake[-1] == apple:
        while apple in snake or apple in walls:
            apple = randrange(0, width, block), randrange(0, height, block)
        length += 1
        score += 1
        fps += 0.5
        if score % 3 == 0 and score > 0:
            level += 1
        if level > 3:
            score += 3
            length += 2
        wall = randrange(0, width, block), randrange(0, width, block)
        walls.append(wall)
    if snake[-1] == orange:
        while orange in snake or orange in walls:
            orange = randrange(0, width, block), randrange(0, height, block)
        length += 2
        score += 2
        fps += 1
        if score % 3 == 0 and score > 0:
            level += 1
        if level > 3:
            score += 3
            length += 2
        wall = randrange(0, width, block), randrange(0, width, block)
        walls.append(wall)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            working = False

    pygame.display.flip()
    clock.tick(fps)

    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}


con.commit()
cur.close()
con.close()