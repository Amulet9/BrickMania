from pygame.font import SysFont
from pygame.display import flip
from pygame import event, KEYDOWN, K_UP, K_DOWN, K_RETURN, K_q, QUIT, quit
from models import FallingTile
from models import Color
from sys import exit

def main_menu(scale, screen, HEIGHT, WIDTH, clock):
    title_font = SysFont(None, int(72 * scale))
    menu_font = SysFont(None, int(48 * scale))

    tiles = [FallingTile() for _ in range(20)]

    options = ["Main Game", "Demo Game"]
    selected_option = 0

    while True:
        screen.fill(Color.BLACK)

        for tile in tiles:
            tile.move()
            tile.draw()

        title_text = title_font.render("BRICKMANIA", True, Color.YELLOW)
        screen.blit(title_text, ((WIDTH // 2 - title_text.get_width() // 2) * scale, (HEIGHT // 2 - 150) * scale))

        for i, option in enumerate(options):
            color = Color.YELLOW if i == selected_option else Color.WHITE
            option_text = menu_font.render(option+[" [PRESS ENTER]",''][color!=Color.YELLOW], True, color)
            screen.blit(option_text, ((WIDTH // 2 - option_text.get_width() // 2) * scale,
                                      (HEIGHT // 2 + i * 60) * scale))

        quit_text = menu_font.render("Press Q to Quit", True, Color.WHITE)
        screen.blit(quit_text, ((WIDTH // 2 - quit_text.get_width() // 2) * scale, (HEIGHT // 2 + 150) * scale))

        flip()
        for event in event.get():
            if event.type == QUIT:
                quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == K_RETURN:
                    return selected_option
                elif event.key == K_q:
                    quit()
                    exit()

        clock.tick(60)