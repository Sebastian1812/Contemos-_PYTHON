from pygame import *
from random import *

init()

#V A R I A B L E S
bg = 1
xbackground = 0
n1 = 0
n2 = 0
res = 0
meta =50

#S O N I D O
mixer.init()
saltoson = mixer.Sound("Musica/Salto_sonido.wav")
correcto = mixer.Sound("Musica/correcto.wav")
incorrecto = mixer.Sound("Musica/incorrecto.wav")

# C O L O R E S
naranja = Color(212, 139, 11)
negro = Color(0, 0, 0)

# F U E N T E S
font1 = font.Font('Fuentes/Golden Age Shad.ttf', 60)

# I M A G E N E S
life_bar = [image.load("Imagenes/Gato/Lifes/0.png"),
            image.load("Imagenes/Gato/Lifes/1.png"),
            image.load("Imagenes/Gato/Lifes/2.png"),
            image.load("Imagenes/Gato/Lifes/3.png"),
            image.load("Imagenes/Gato/Lifes/4.png"),
            image.load("Imagenes/Gato/Lifes/5.png"),
            image.load("Imagenes/Gato/Lifes/6.png"),
            image.load("Imagenes/Gato/Lifes/7.png")]


def resultado(n1, n2, resul):
    check = n1 + n2
    puntos = 10
    if resul == check:
        mixer.Sound.play(correcto)
        return True
    else:
        mixer.Sound.play(incorrecto)
        return False


class Gato(sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.sheet = image.load("Imagenes/Gato/spriteSheet.png")
        self.sheet.set_clip(Rect(830, 0, 254, 200))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.resul = 1
        self.puntos = 0
        self.vidas = 7
        self.game_over = False
        self.game_restart = False
        self.problem = True
        self.frame = 0
        self.right_states = {0: (830, 0, 254, 200),
                             1: (1124, 0, 260, 200),
                             2: (1410, 0, 250, 200),
                             3: (1707, 0, 250, 200),
                             4: (2015, 0, 227, 200),
                             5: (0, 0, 280, 200),
                             6: (295, 0, 202, 200),
                             7: (581, 0, 210, 200)}
        self.buton = False

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(Rect(clipped_rect))
        return clipped_rect


    def retry(self, x, root, band):
        global bg, xbackground, res
        bg = 1
        self.resul = 1
        self.problem = True
        self.rect.x = x
        xbackground = x
        if band == 0:
            self.vidas -= 1
            if self.vidas == 0:
                self.game_over = True
        elif band == 1:
            self.vidas = 7
            self.puntos = 0
            res = 0
        elif band == 2:
            self.puntos = self.puntos*self.vidas
            res = 0


    def movimientos(self, x):
        global xbackground, bg
        if self.resul < 50:
            mixer.Sound.play(saltoson)
            self.clip(self.right_states)
            self.rect.x += 200
            self.resul += 1
            xbackground += 200
            if self.rect.x >= 946:
                self.rect.x = x
                bg += 1
            if xbackground >= 1892:
                xbackground = x

    def handle_event(self, root, f1, evento, x, band):
        global xbackground, bg, fond, n1, n2, res

        #REVISA COMO VOLVERA A JUGAR EL USUARIO
        if band == 1:
            self.retry(x, root, 1)
            self.game_over = False
        elif band == 2:
            self.retry(x, root, 2)
            self.game_over = False

        # CAMBIO DE ESCENARIO
        if xbackground < 948:
            root.blit(f1[0], (0, 0))
        else:
            root.blit(f1[1], (0, 0))

        root.blit(life_bar[self.vidas], (588, 10))

        if self.problem:
            n1 = self.resul
            n2 = randrange(1, 10)
            while n1+n2 > meta:
                n2 = randrange(1, 10)
            self.problem = False


        # T E X T O S
        txt = [font1.render(str(n1), 1, negro),
               font1.render(str(n2), 1, negro),
               font1.render(str(self.resul), 1, negro)]
        points = font1.render(str(self.puntos), 1, negro)

        # IMPRIMIR TEXTOS A LA VENTANA
        root.blit(txt[0], (270, 315))
        root.blit(txt[1], (543, 315))
        root.blit(txt[2], (815, 315))
        root.blit(points, (50, 50))

        # MOVIMIENTO DE LAS FLECHAS
        if evento.type == KEYDOWN and self.buton == False:
            if not self.buton:
                self.buton = True
                if evento.key == K_RIGHT:
                    self.movimientos(x)
                elif evento.key == K_ESCAPE:
                    quit()
                    exit()

                elif evento.key == K_RETURN:
                    if resultado(n1, n2, self.resul):
                        self.puntos += 10
                        res = self.resul
                        if res == meta:
                            self.game_over = True
                        else:
                            self.problem = True
                    else:
                        self.retry(x, root, 0)


        if evento.type == KEYUP:
            if evento.key == K_RIGHT:
                self.clip(self.right_states[0])
            self.buton = False

        self.image = self.sheet.subsurface(self.sheet.get_clip())

        return bg, self.game_over, res, self.vidas, self.puntos
