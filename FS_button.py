from pygame import *

#S O N I D O
mixer.init()
soundbot = mixer.Sound("Musica/boton.wav")


class Button:
    def __init__(self, x, y, imagenes):
        self.image = imagenes
        self.rect = self.image[0].get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, root):
        action = False
        root.blit(self.image[0], (self.rect.x, self.rect.y))
        pos = mouse.get_pos()
        if self.rect.collidepoint(pos):
            root.blit(self.image[1], (self.rect.x, self.rect.y))
            if mouse.get_pressed()[0] == 1 and not self.clicked:
                root.blit(self.image[2], (self.rect.x, self.rect.y))
                mixer.Sound.play(soundbot)
                self.clicked = True
                action = True
        if mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action
