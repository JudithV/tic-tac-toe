### Descripción
Implementación del juego del TIC TAC TOE (tres en raya) usando el lenguaje de programación Python.

### Setup
Para jugar a esta versión del tres en raya hay que asegurarse de instalar primero los requerimientos usando el comando:

`pip install -r requirements.txt`

Pues, para el desarrollo de este pequeño juego, he utilizado la librería de python Tkinter, que aporta las herramientas necesarias para que gráficamente la aplicación sea "jugable". Por tanto, esta librería tiene que estar instalada.

### Ejecución
Una vez instalados los requerimientos necesarios, se juega lanzando desde la terminal en la carpeta en la que se encuentra el archivo `tictactoe.py` el siguiente comando:

`python tictactoe.py`

Esto ejecutaría el script que contiene el código del juego. Esto haría que se nos abra una ventana emergente como esta:
<img width="200" alt="image" src="https://github.com/JudithV/tic-tac-toe/assets/42940890/2ff736b3-bb50-4c88-b6de-021335df244d">

Bastaría con hacer click en una casilla para insertar en ella la ficha del jugador que tiene el turno. Luego, sería el turno del siguiente jugador. La partida siempre comienza siendo el turno del jugador uno, y luego se le pasa el turno al jugador dos y así sucesivamente. 
Si el otro jugador intentase poner su ficha en una casilla ocupada del tablero, no ocurriría nada. Sigue siendo su turno hasta que introduzca un movimiento válido.
Una vez haya ganado un jugador o bien se haya acabado en empate (todas las casillas se encuentran rellenadas pero no ha ganado nadie), dándole al botón de "Reiniciar" se puede iniciar una nueva partida con el tablero limpio.
