import sys
from FS_button import *
from FS_player import *

init()

# M U S I C A  Y  S O N I D O
mixer.init()
mixer.music.load("Musica/musciakids.mp3")
mixer.music.set_volume(.2)
mixer.music.play(900)

# V E N T A N A
alto = 700
ancho = 1106
root = display.set_mode((ancho, alto))
display.set_caption("¡Contemos!")
ico = image.load("gato.ico")
display.set_icon(ico)

# C O L O R E S
naranja = Color(212, 139, 11)
negro = Color(0, 0, 0)
rojo = Color(234,32,0)

# F U E N T E S
font1 = font.SysFont('Fuentes/Golden Age Shad', 30)
font2 = font.SysFont('Fuentes/Golden Age Shad', 70)
font3 = font.SysFont('Fuentes/Golden Age Shad', 100)
font4 = font.SysFont('Fuentes/Golden Age Shad', 60)

# I M A G E N E S
logo = image.load("Imagenes/Contemos_log.png")
fond = image.load("Imagenes/Fondo/background.png")
bjugar = [image.load("Imagenes/Botones/b1_jugar.png").convert_alpha(),
          image.load("Imagenes/Botones/b1_5_jugar.png").convert_alpha(),
          image.load("Imagenes/Botones/b2_jugar.png").convert_alpha()]
bsalir = [image.load("Imagenes/Botones/b1_salir.png").convert_alpha(),
          image.load("Imagenes/Botones/b1_5_salir.png").convert_alpha(),
          image.load("Imagenes/Botones/b2_salir.png").convert_alpha()]
fond_prins = [image.load("Imagenes/Fondo/juego/1.png"),
              image.load("Imagenes/Fondo/juego/2.png")]
b_pausa = [image.load("Imagenes/Botones/pause_1.png").convert_alpha(),
           image.load("Imagenes/Botones/pause_1_1.png").convert_alpha(),
           image.load("Imagenes/Botones/pause_2.png").convert_alpha()]
pausafond = image.load("Imagenes/Fondo/pausa.png")
gameoverfond = [image.load("Imagenes/Fondo/game_over.png"),
                image.load("Imagenes/Fondo/Ganaste.png"),
                image.load("Imagenes/Fondo/Continuar.png")]

breanudar = [image.load("Imagenes/Botones/b1_reanudar.png").convert_alpha(),
             image.load("Imagenes/Botones/b1_5_reanudar.png").convert_alpha(),
             image.load("Imagenes/Botones/b2_reanudar.png").convert_alpha()]

bsi = [image.load("Imagenes/Botones/b1_si.png").convert_alpha(),
       image.load("Imagenes/Botones/b1_5_si.png").convert_alpha(),
       image.load("Imagenes/Botones/b2_si.png").convert_alpha()]
bno = [image.load("Imagenes/Botones/b1_no.png").convert_alpha(),
       image.load("Imagenes/Botones/b1_5_no.png").convert_alpha(),
       image.load("Imagenes/Botones/b2_no.png").convert_alpha()]
bok = [image.load("Imagenes/Botones/b1_ok.png").convert_alpha(),
       image.load("Imagenes/Botones/b1_5_ok.png").convert_alpha(),
       image.load("Imagenes/Botones/b2_ok.png").convert_alpha()]


# B O T O N E S
jug_button = Button(701, 398, bjugar)
sal_button = [Button(701, 529, bsalir),
              Button(408, 401, bsalir)]
pause_button = Button(10, 125, b_pausa)
reanud_button = Button(408, 231, breanudar)
si_button = [Button(408, 294, bsi),
             Button(408, 244, bsi)]
no_button = [Button(408, 441, bno),
             Button(408, 391, bno)]
ok_button = Button(408, 500, bok)

# V A R I A B L E S
# Enteros
x = 20
y = 380

# Booleanos
game = True
game_start = False
game_pause = False
game_over = False
game_restart = 0
game_continuar = False
# Otros
clock = time.Clock()
player = Gato((x, y))


def imprinNum(saltjugador):
    i = 5 * saltjugador

    txt1 = [font1.render(str(i - 4), 0, negro),
            font1.render(str(i - 3), 0, negro),
            font1.render(str(i - 2), 0, negro),
            font1.render(str(i - 1), 0, negro),
            font1.render(str(i), 0, negro)]

    if i < 10:
        root.blit(txt1[0], (108, 648))
        root.blit(txt1[1], (312, 648))
        root.blit(txt1[2], (510, 648))
        root.blit(txt1[3], (708, 648))
        root.blit(txt1[4], (912, 648))
    else:
        root.blit(txt1[0], (103, 648))
        root.blit(txt1[1], (305, 648))
        root.blit(txt1[2], (503, 648))
        root.blit(txt1[3], (706, 648))
        root.blit(txt1[4], (908, 648))



def juegomain(evento):
    global game_pause, game_over, game, game_restart, game_continuar
    if not game_pause:

        jugador = player.handle_event(root, fond_prins, evento, x,game_restart)
        saltjugador = jugador[0]
        game_over = jugador[1]
        meta = jugador[2]
        puntaje = [jugador[3], jugador[4]]
        describ = [font4.render("Empiezas", 1, rojo),
                   font4.render("en", 1, rojo),
                   font4.render("Cuenta", 1, rojo),
                   font4.render("hasta", 1, rojo),
                   font4.render("Llegaste", 1, rojo),
                   font4.render("al", 1, rojo)]
        if pause_button.draw(root):
            game_pause = True
        imprinNum(saltjugador)
        root.blit(player.image, player.rect)
        root.blit(describ[0], (180, 169))
        root.blit(describ[1], (255, 209))
        root.blit(describ[2], (475, 169))
        root.blit(describ[3], (500, 209))
        root.blit(describ[4], (749, 169))
        root.blit(describ[5], (815, 209))
        game_restart = 0
        if meta == 50:
            if game_continuar:
                root.blit(gameoverfond[2], (0, 0))
                if si_button[1].draw(root):
                    game_restart = 2
                    game_continuar = False
                if no_button[1].draw(root):
                    game = False
                    game_continuar = False
            else:
                txt = [font2.render(str(puntaje[1]), 1, negro),
                       font2.render("*"+str(puntaje[0]), 1, negro),
                       font3.render(str(puntaje[0]*puntaje[1]), 1, negro)]

                root.blit(gameoverfond[1], (0, 0))
                root.blit(txt[0], (595, 235))
                root.blit(txt[1], (595, 308))
                root.blit(txt[2], (595, 400))
                if ok_button.draw(root):
                    print(f"vidas = {puntaje[0]}\npuntos = {puntaje[1]}")
                    game_continuar = True

        else:
            if game_over:
                root.blit(gameoverfond[0], (0, 0))
                if si_button[0].draw(root):
                    game_restart = 1
                if no_button[0].draw(root):
                    game = False

    else:
        root.blit(pausafond, (0, 0))
        if sal_button[1].draw(root):
            game = False
        if reanud_button.draw(root):
            game_pause = False


def juegomenu():
    global x, game, game_start, game_over

    evento = event.get()
    while game:
        root.blit(fond, (0, 0))
        root.blit(logo, (24, -20))

        for evento in event.get():
            if evento.type == QUIT:
                game = False

        if game_start:
            juegomain(evento)
        else:
            if jug_button.draw(root):
                game_start = True

            if sal_button[0].draw(root):
                quit()
                exit()

        display.update()
        # pygame.display.flip()


juegomenu()
