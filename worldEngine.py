import pygame

pygame.init()

size = width, height = 1000, 800

white = pygame.Color(255, 255, 255)
blue = pygame.Color(0, 0, 255)

screen = pygame.display.set_mode(size)

pygame.draw.rect(screen, blue, (200, 200, 50, 25))

def alternateBackground(currentBackground):
    pygame.time.wait(2500)
    if currentBackground == "blue":
        screen.fill(white)
        return "white"
    else:
        screen.fill(blue)
        return "blue"


bgColour = "blue"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    bgColour = alternateBackground(bgColour)
    pygame.display.update()
