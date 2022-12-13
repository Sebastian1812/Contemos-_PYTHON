from sys import*
from FS_button import *
from FS_player import *

init()

# M U S I C A  Y  S O N I D O
mixer.init()
mixer.music.load("Musica/musciakids.mp3")
mixer.music.set_volume(.1)
mixer.music.play(900)

# V E N T A N A
alto = 700
ancho = 1106
root = display.set_mode((ancho, alto))
display.set_caption("¡Contemos!")
ico = image.load("Imagenes/gato.ico")
display.set_icon(ico)

# C O L O R E S
naranja = Color(212, 139, 11)
negro = Color(0, 0, 0)

# F U E N T E S
font1 = font.SysFont("estandar", 30)
font2 = font.Font('Fuentes/Golden Age Shad.ttf', 50)
font3 = font.Font('Fuentes/Golden Age Shad.ttf', 80)
font4 = font.Font('Fuentes/Golden Age Shad.ttf', 40)

# I M A G E N E S
logo = image.load("Imagenes/Contemos_log.png")
fond = image.load("Imagenes/Fondo/background.png")
bjugar = [image.load("Imagenes/Botones/b1_jugar.png").convert_alpha(),
          image.load("Imagenes/Botones/b1_5_jugar.png").convert_alpha(),
          image.load("Imagenes/Botones/b2_jugar.png").convert_alpha()]
bsalir = [image.load("Imagenes/Botones/b1_salir.png").convert_alpha(),
          image.load("Imagenes/Botones/b1_5_salir.png").convert_alpha(),
          image.load("Imagenes/Botones/b2_salir.png").convert_alpha()]
fond_prins = [image.load("Imagenes/Fondo/1.png"),
              image.load("Imagenes/Fondo/2.png")]
b_pausa = [image.load("Imagenes/Botones/pause_1.png").convert_alpha(),
           image.load("Imagenes/Botones/pause_1_1.png").convert_alpha(),
           image.load("Imagenes/Botones/pause_2.png").convert_alpha()]
pausafond = image.load("Imagenes/Fondo/pausa.png")
gameoverfond = [image.load("Imagenes/Fondo/game_over.png"),
                image.load("Imagenes/Fondo/Ganaste.png"),
                image.load("Imagenes/Fondo/Continuar.png")]
tutorial = image.load("Imagenes/Fondo/tutorial.png")


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
bflecha = [image.load("Imagenes/Botones/b1_flecha.png").convert_alpha(),
       image.load("Imagenes/Botones/b1_5_flecha.png").convert_alpha(),
       image.load("Imagenes/Botones/b2_flecha.png").convert_alpha()]


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
flecha_button = Button(783, 520, bflecha)

# V A R I A B L E S
# Enteros
x = 20
y = 380
puntajes = []

# Booleanos
game = True
game_start = False
game_pause = False
game_over = False
game_restart = 0
game_continuar = False
game_tutorial = False
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


def archiPuntos(lista):
    with open("puntaje.txt", "a") as f:
        for i in range(len(lista)):
            f.write(str(lista[i])+'\n')


def leerArchivo():
    with open("puntaje.txt","r") as f:
        listaArchivo = f.readlines()
    listaArchivo.sort()
    return listaArchivo

def juegomain(evento):
    global game_pause, game_over, game, game_restart, game_continuar, puntajes
    if not game_pause:
        jugador = player.handle_event(root, fond_prins, evento, x, game_restart)
        saltjugador = jugador[0]
        game_over = jugador[1]
        meta = jugador[2]
        puntaje = [jugador[3], jugador[4]]
        describ = [font4.render("Empiezas", 1, negro),
                   font4.render("en", 1, negro),
                   font4.render("Cuenta", 1, negro),
                   font4.render("hasta", 1, negro),
                   font4.render("Llegaste", 1, negro),
                   font4.render("al", 1, negro)]
        if pause_button.draw(root):
            game_pause = True
        imprinNum(saltjugador)
        root.blit(player.image, player.rect)
        root.blit(describ[0], (180, 169))
        root.blit(describ[1], (255, 209))
        root.blit(describ[2], (475, 169))
        root.blit(describ[3], (500, 209))
        root.blit(describ[4], (725, 169))
        root.blit(describ[5], (800, 209))
        game_restart = 0
        if meta == 50:
            if game_continuar:
                root.blit(gameoverfond[2], (0, 0))
                if si_button[1].draw(root):
                    game_restart = 2
                    game_continuar = False
                if no_button[1].draw(root):
                    puntajes.append(puntaje[0]*puntaje[1])
                    game = False
                    game_continuar = False
            else:
                txt = [font2.render(str(puntaje[1]), 1, negro),
                       font2.render("x"+str(puntaje[0]), 1, negro),
                       font3.render(str(puntaje[0]*puntaje[1]), 1, negro)]

                root.blit(gameoverfond[1], (0, 0))
                root.blit(txt[0], (336, 194))
                root.blit(txt[1], (336, 262))
                root.blit(txt[2], (336, 400))
                if ok_button.draw(root):
                    game_continuar = True

        else:
            if game_over:
                root.blit(gameoverfond[0], (0, 0))
                if si_button[0].draw(root):
                    puntajes.append(puntaje[1])
                    game_restart = 1
                if no_button[0].draw(root):
                    puntajes.append(puntaje[1])
                    game = False

    else:
        root.blit(pausafond, (0, 0))
        if sal_button[1].draw(root):
            game = False
        if reanud_button.draw(root):
            game_pause = False


def juegomenu():
    global x, game, game_start, game_over, game_tutorial, puntajes

    evento = event.get()
    while game:
        root.blit(fond, (0, 0))
        root.blit(logo, (24, -20))

        for evento in event.get():
            if evento.type == QUIT:
                game = False

        if game_start:
            if not game_tutorial:
                root.blit(tutorial, (0, 0))
                if flecha_button.draw(root):
                    game_tutorial = True
            else:
                juegomain(evento)

        else:
            if jug_button.draw(root):
                game_start = True

            if sal_button[0].draw(root):
                game = False


        display.update()
    archiPuntos(puntajes)
    listaPuntajes = leerArchivo()
    quit()
    exit()

juegomenu()
