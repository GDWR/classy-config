import pygame

from classy_config import ClassyConfig, ConfigParam

# Define configuration file
ClassyConfig(filepath="config.toml")


screen_width = ConfigParam("window.width", int)
screen_height = ConfigParam("window.height", int)
screen_size = screen_width, screen_height

pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption(ConfigParam("window.name", str))


class Logo(pygame.sprite.Sprite):

    def __init__(
        self,
        size=ConfigParam("logo.size", int),
        x_speed=ConfigParam("logo.x_speed", int),
        y_speed=ConfigParam("logo.y_speed", int),
    ) -> None:

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size, size))
        self.image.fill((255, 255, 255))

        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2
        self.rect.y = screen_height // 2

        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        if (self.rect.x + self.rect.width >= screen_width) or (self.rect.x <= 0):
            self.x_speed = -self.x_speed

        if (self.rect.y + self.rect.height >= screen_height) or (self.rect.y <= 0):
            self.y_speed = -self.y_speed

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed


clock = pygame.time.Clock()
logo = Logo()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(0)

    logo.update()
    screen.blit(logo.image, logo.rect)

    pygame.display.flip()
    clock.tick(60)
