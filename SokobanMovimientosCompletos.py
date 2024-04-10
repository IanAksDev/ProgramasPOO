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
            [3,4,0,1,2,2,2,4,3],
            [3,4,4,4,2,2,2,4,3],
            [3,4,4,1,4,4,4,4,3],
            [3,3,3,3,3,3,3,3,3]
        ]

        self.personaje_columna = 2
        self.personaje_fila = 2

    def imprimirMapa(self):
        for filas in self.mapa:
            print(filas)

    def movimiento1(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0

        self.personaje_columna += 1

    def movimientoC(self):

        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1

        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0

        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.personaje_columna += 1

    def movimientoM2(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5

        self.personaje_columna += 1

    def movimientoM(self):
    # Mover al personaje-meta a la derecha y actualizar su posición
        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5

        self.personaje_columna += 1

    def movimientoMS(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0

        self.personaje_columna += 1

    def derecha(self): 
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            self.movimiento1()

        elif self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
            self.movimientoC()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
            self.movimientoM2()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
            self.movimientoM()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            self.movimientoMS()


    def movimiento2(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila][self.personaje_columna - 1 ] = 0

        self.personaje_columna -= 1

    def movimientoC2(self):

        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1

        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0

        self.personaje_columna -= 1

    def movimientoMI2(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5

        self.personaje_columna -= 1

    def movimientoMI(self):
    # Mover al personaje-meta a la derecha y actualizar su posición
        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5

        self.personaje_columna -= 1

    def movimientoMIS(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0

        self.personaje_columna -= 1

    def izquierda(self):
        if self.mapa[self.personaje_fila][self.personaje_columna - 1 ] == 4 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
            self.movimiento2()

        elif self.mapa[self.personaje_fila][self.personaje_columna - 2 ] == 4 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1:
            self.movimientoC2()

        elif self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
            self.movimientoMI2()

        elif self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna] == 5:
            self.movimientoMI()

        elif self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4 and self.mapa[self.personaje_fila][self.personaje_columna] == 5:
            self.movimientoMIS()


    def movimiento3(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0

        self.personaje_fila -= 1

    def movimientoC3(self):

        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1

        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0

        self.personaje_fila -= 1

    def movimientoMA2(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5

        self.personaje_fila -= 1

    def movimientoMA(self):
    # Mover al personaje-meta a la derecha y actualizar su posición
        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5

        self.personaje_fila -= 1

    def movimientoMAS(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0

        self.personaje_fila -= 1

    def arriba(self):

        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
            self.movimiento3()

        elif self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
            self.movimientoC3()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2:
            self.movimientoMA2()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2:
            self.movimientoMA()
        
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
            self.movimientoMAS()

    def movimiento4(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0

        self.personaje_fila += 1

    def movimientoC4(self):

        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1

        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0

        self.personaje_fila += 1

    def movimientoMAB2(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5

        self.personaje_fila += 1

    def movimientoMAB(self):
    # Mover al personaje-meta a la derecha y actualizar su posición
        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5

        self.personaje_fila += 1
    
    def movimientoMABS(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0

        self.personaje_fila += 1


    def abajo(self):

        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
            self.movimiento4()

        elif self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
            self.movimientoC4()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2:
            self.movimientoMAB2()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2:
            self.movimientoMAB()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
            self.movimientoMABS()

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