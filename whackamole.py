import pygame
import random


def main():
    line_color = (0, 0, 0)
    location = (0,0)
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        def draw_grid():
            for i in range (20):
                pygame.draw.line(screen, line_color, (i*32, 0), (i*32, 640))
            for i in range(16):
                pygame.draw.line(screen, line_color, (0, i*32), (640, i*32))


        while running:
            screen.fill("light green")
            draw_grid()
            screen.blit(mole_image, mole_image.get_rect(topleft=(location[0] * 32, location[1] * 32)))
            pygame.display.flip()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = event.pos[0]
                    mouse_y = event.pos[1]
                    print(f"Mouse X: {mouse_x //32} and Mouse y {mouse_y//32}")
                    print(f"Location {location}")
                    print(f"EQ :{(mouse_x //32 == location[0]) and (mouse_y // 32 == location[1])}")
                    if (mouse_x //32 == location[0]) and (mouse_y // 32 == location[1]):
                        random_range1 = (random.randrange(0, 480)//32) *32
                        random_range2 = (random.randrange(0, 608)//32)*32
                        print(f"Random 1: {random_range1} and random 2: {random_range2}")
                        location = (random_range2//32),(random_range1//32)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
