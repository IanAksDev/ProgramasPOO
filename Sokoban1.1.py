import os
class Soko:
    mapa = [] # mapa del juego
    personaje_columna = 0
    personaje_fila = 0

    def __init__(self):
        # Define el mapa de juego
        self.mapa =[
            [3,3,3,3,3,3,3,3,3],
            [3,4,4,4,4,4,4,4,3],
            [3,4,0,1,4,4,4,4,3],
            [3,4,4,4,4,4,3,3],
            [3,3,3,3,3,3,3]
        ]

        # Definimos la posicion inicial del personaje
        self.personaje_columna = 2
        self.personaje_fila = 2

    def imprimirMapa(self):
        for filas in self.mapa:
            print(filas)

    def movimiento1(self):
        # Donde estaba el persona pone un piso
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        # Donde estaba el piso pone al personaje
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        # Actualiza la posicion del personaje
        self.personaje_columna+=1

    def derecha(self):
        # Movimiento 1: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            self.movimiento1()

    def movimiento2(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila][self.personaje_columna - 1 ] = 0

        self.personaje_columna-=1

    def izquierda(self):
        if self.mapa[self.personaje_fila][self.personaje_columna -1 ] == 4 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
            self.movimiento2()

    def movimiento3(self):
        # Donde estaba el personaje pone un piso
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        # Donde estaba el piso pone al personaje
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        # Actualiza la posicion del personaje
        self.personaje_fila -= 1

    def arriba(self):
        # Movimiento 1: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
            self.movimiento3()

    def movimiento4(self):
        # Donde estaba el personaje pone un piso
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        # Donde estaba el piso pone al personaje
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        # Actualiza la posicion del personaje
        self.personaje_fila += 1

    def abajo(self):
        # Movimiento 1: [0,4] -> [4,0]
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
            self.movimiento4()

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def jugar(self):
        while True:
            self.limpiar_pantalla()
            # Imprime el mapa
            self.imprimirMapa()
            # Pide al usuario el movimiento
            movimiento = input("Selecciona el movimiento: ")
            # Moverse a la derecha
            if movimiento == 'd':
                self.derecha()
            if movimiento == 'a':
                self.izquierda()
            if movimiento == 'w':
                self.arriba()
            if movimiento == 's':
                self.abajo()


soko = Soko()
soko.jugar()