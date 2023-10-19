from tkinter import *
import random

def main():
    ventana = Tk()
    ventana.title("3 en raya")

    # Dos jugadores: El primero marca sus casillas con X, el segundo con O
    global jugadores
    jugadores = ["X", "O"]

    # Se escoge un jugador aleatorio entre los dos para comenzar el juego
    global jugador
    jugador = random.choice(jugadores)

    # Se inicializa un tablero vacío de 3x3
    global tablero
    tablero = [[0,0,0],[0,0,0],[0,0,0]]

    # Se muestra encima del tablero quién tiene el turno
    global etiqueta
    etiqueta = Label(text="Turno del jugador " + str(jugadores.index(jugador) + 1), font=('rockwell',20))
    etiqueta.pack(side="top")

    boton_reinicio = Button(text="Reiniciar", font=("rockwell",20), command=nueva_partida)
    boton_reinicio.pack(side="bottom")

    frame = Frame(ventana)
    frame.pack()

    for i in range(3):
        for j in range(3):
            tablero[i][j] = Button(frame, text="", font=("rockwell", 20), width=5, height=2,
                                   command= lambda fila=i, columna=j: turno_siguiente(fila,columna))
            tablero[i][j].grid(row=i, column=j)
    ventana.mainloop()

# Función que devuelve True si ya hay ganador en el turno en el que se la invoca, teniendo en cuenta
# el estado del tablero en dicho turno
def comprobar_ganador():
    global tablero
    # Si una fila ha sido rellenada por el mismo jugador
    for i in range(3):
        if tablero[i][0]['text'] == tablero[i][1]['text'] == tablero[i][2]['text'] != "":
            tablero[i][0].config(bg="green")
            tablero[i][1].config(bg="green")
            tablero[i][2].config(bg="green")
            return True

    # Si una columna ha sido rellenada por el mismo jugador
    for j in range(3):
        if tablero[0][j]['text'] == tablero[1][j]['text'] == tablero[2][j]['text'] != "":
            tablero[0][j].config(bg="green")
            tablero[1][j].config(bg="green")
            tablero[2][j].config(bg="green")
            return True

    # Si la diagonal ha sido rellenada por el mismo jugador
    if tablero[0][0]['text'] == tablero[1][1]['text'] == tablero[2][2]['text'] != "":
        tablero[0][0].config(bg="green")
        tablero[1][1].config(bg="green")
        tablero[2][2].config(bg="green")
        return True

    # Si la diagonal inversa ha sido rellenada por el mismo jugador
    elif tablero[0][2]['text'] == tablero[1][1]['text'] == tablero[2][0]['text'] != "":
        tablero[0][2].config(bg="green")
        tablero[1][1].config(bg="green")
        tablero[2][0].config(bg="green")
        return True

    elif espacios_en_blanco() is False: # Si todo el tablero se ha rellenado pero no hay ganador...
        for i in range(3):
            for j in range(3):
                tablero[i][j].config(bg="yellow")
        return "Empate"

    else:
        return False

# Función que devuelve True si todos los espacios del tablero ya se han rellenado
def espacios_en_blanco():
    global tablero
    ocupados = 0
    for i in range(3):
        for j in range(3):
            if tablero[i][j]['text'] != "":
                ocupados += 1

    if ocupados == 9: # Si el tablero de 3x3 está completo
        return False
    else:
        return True

def nueva_partida():
    global jugador, jugadores, etiqueta
    jugador = random.choice(jugadores)

    etiqueta.config(text=("Turno del jugador "+ str(jugadores.index(jugador) + 1) +"."))

    for i in range(3):
        for j in range(3):
            tablero[i][j].config(text="",bg="#F0F0F0")

def turno_siguiente(fila, columna):
    global jugador, jugadores, tablero, etiqueta
    if tablero[fila][columna]['text'] == "" and comprobar_ganador() is False:

        if jugador == jugadores[0]:

            tablero[fila][columna]['text'] = jugador

            if comprobar_ganador() is False:
                jugador = jugadores[1]
                etiqueta.config(text=("Turno del jugador 2."))

            elif comprobar_ganador() is True:
                etiqueta.config(text=("Ha ganado el jugador 1. ¡Enhorabuena!"))

            elif comprobar_ganador() == "Empate":
                etiqueta.config(text="¡Ha habido un empate!")

        else:

            tablero[fila][columna]['text'] = jugador

            if comprobar_ganador() is False:
                jugador = jugadores[0]
                etiqueta.config(text=("Turno del jugador 1."))

            elif comprobar_ganador() is True:
                etiqueta.config(text=("Ha ganado el jugador 2. ¡Enhorabuena!"))

            elif comprobar_ganador() == "Empate":
                etiqueta.config(text="¡Ha habido un empate!")

if __name__ == '__main__':
    main()