import pygame
import sys

WIDTH, HEIGHT = 800, 600
FPS = 60

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = HEIGHT - 100
        self.vel_y = 0
        self.on_ground = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if self.on_ground and keys[pygame.K_SPACE]:
            self.vel_y = -15
            self.on_ground = False

        self.vel_y += 1
        self.rect.y += self.vel_y
        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.vel_y = 0
            self.on_ground = True


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mazu Adventure")
    clock = pygame.time.Clock()

    player = Player()
    all_sprites = pygame.sprite.Group(player)

    running = True
    frame_count = 0
    while running and frame_count < FPS * 5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update()
        screen.fill((135, 206, 250))
        pygame.draw.rect(screen, (34, 139, 34), (0, HEIGHT - 50, WIDTH, 50))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
        frame_count += 1

    pygame.quit()

if __name__ == "__main__":
    main()
