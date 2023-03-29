import pygame
pygame.init()

screen = pygame.display.set_mode((600, 200))
pygame.display.set_caption("Music Player")

font=pygame.font.Font('fonts/Tilt_Neon/static/TiltNeon-Regular.ttf',25)
text = ["'s' - to start play music","'space' - to pause/unpause music","'p' - to play previous music","'n' - to play next music"]
list1 = []
for line in text:
    line1 = font.render(f'{line}', False, 'green')
    list1.append(line1)

playlist = ["Playlist/Arctic Monkeys - Do I Wanna Know.mp3",
            "Playlist/Maneskin - Beggin.mp3",
            "Playlist/The Weeknd-Die For You.mp3"]

check = True
i = 0

while check:
    y=10
    for line1 in list1:
        screen.blit(line1, (10, y))
        y+=30

    pygame.display.update()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            check = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == pygame.K_s:
                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play()

            elif event.key == pygame.K_n:
                if i <= 1:
                    i += 1
                else:
                    i = 2
                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play()

            elif event.key == pygame.K_p:
                if i >=1:
                    i-=1
                else:
                    i = 0
                pygame.mixer.music.load(playlist[i])
                pygame.mixer.music.play()