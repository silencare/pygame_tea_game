import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

#tworzenie klasy
class Block(pygame.sprite.Sprite):
    #konstruktor
    def __init__(self):
        #użycie konstruktora klasy rodzica Sprite
        pygame.sprite.Sprite.__init__(self)

        #załadowanie obrazu jako obraz klasy
        self.image = pygame.image.load(f'img/strzalka_lewo/strzalka_lewo1.png').convert_alpha()

        #użycie kształtu obrazu jako hitboxów
        self.rect = self.image.get_rect()

    def update(self):
        self.x +=100


grupa = pygame.sprite.Group()

strzalka1 = Block()

grupa.add(strzalka1)

fps = 60
clock = pygame.time.Clock()

running = True
while running:
    grupa.draw(screen)

    pygame.display.update()
    clock.tick(fps)
