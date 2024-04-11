import os
class Soko:
    mapa = [] # mapa del juego
    personaje_columna = 0
    personaje_fila = 0

    def __init__(self):
        # Define el mapa de juego
        self.mapa =[
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,],
            [3,4,4,4,2,2,4,4,4,2,2,2,4,4,4,4,4,3,],
            [3,4,0,1,2,4,2,4,4,2,2,2,4,4,4,4,4,3,],
            [3,4,4,4,2,2,2,4,4,4,4,1,4,4,4,2,4,3,],
            [3,4,4,4,4,4,4,4,4,4,4,2,4,4,4,4,4,3,],
            [3,4,4,4,4,4,4,4,4,4,4,2,2,2,4,4,4,3,],
            [3,4,4,4,4,4,4,4,4,4,4,2,2,2,4,4,4,3,],
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]
        ]

        self.personaje_columna = 2
        self.personaje_fila = 2

    def imprimirMapa(self):
        for filas in self.mapa:
            print(filas)

    def movimiento1(self):#moverse a la derecha en espacio

        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0

        self.personaje_columna += 1

    def movimientoC(self): #mover la caja a la derecha

        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1

        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0

        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.personaje_columna += 1

    def movimientoM(self):#meter personaje en meta
        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5

        self.personaje_columna += 1

    def movimientoM2(self):#moverse personaje en meta
        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5

        self.personaje_columna += 1

    def movimientoMS(self):# personaje sale de meta
        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0

        self.personaje_columna += 1


    def movimientoCM(self):#personaje empuja caja y  caja entra en meta
        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0

        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6

        self.personaje_columna += 1

    def movimientoCM2(self):#personaje empuja caja y personaje entra en meta
        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5

        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
        
        self.personaje_columna += 1

    def movimientoCM3(self):#personaje empuja caja y se mueve en meta
        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5

        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
        
        self.personaje_columna += 1

    def movimientoCM4(self):#personaje empuja caja fuera de meta y saca caja
        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5

        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1

        self.personaje_columna += 1

    def movimientoCM5(self):#personaje empuja caja fuera de meta y sale personaje
        
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0

        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1

        self.personaje_columna += 1

    def movimientoCM6(self):#personaje en espacio empuja caja meta hacia espacio
        self.mapa[self.personaje_fila][self.personaje_columna] = 4#en la posicion del personaje se cambia a 4
        
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5 #un paso delante del personaje se cambia a 5

        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1#dos pasos delante del personaje se cambia a 1

        self.personaje_columna += 1 #actualiza la posicion en el mapa

    def movimientoCM7(self):#personaje meta empuja caja hacia meta
        
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0

        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6

        self.personaje_columna += 1



    def derecha(self): #verifiva la posicion del personaje
        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            self.movimiento1() #en la posicion del personaje debe haber un 0 y un paso adelante del personaje hay un 4

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
            self.movimientoM() #en la posicion del personaje debe haber un 0 y un paso adelante del personaje hay un 2

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
            self.movimientoM2() #en la posicion del personaje debe haber un 5 y un paso adelante del personaje hay un 2

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            self.movimientoMS() #en la posicion del personaje debe haber un 5 y un paso adelante del personaje hay un 4

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
            self.movimientoCM() #en la posicion del personaje debe haber un 0, un paso adelante del personaje hay un 1 y dos paso delante del personaje hay un 2

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
            self.movimientoCM2() #en la posicion del personaje debe haber un 0, un paso adelante del personaje hay un 6 y dos paso delante del personaje hay un 2
        
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
            self.movimientoCM3() #en la posicion del personaje debe haber un 5, un paso adelante del personaje hay un 6 y dos paso delante del personaje hay un 2

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
            self.movimientoCM4() #en la posicion del personaje debe haber un 5, un paso adelante del personaje hay un 6 y dos paso delante del personaje hay un 4

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1  and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
            self.movimientoCM5() #en la posicion del personaje debe haber un 5, un paso adelante del personaje hay un 1 y dos paso delante del personaje hay un 4

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
            self.movimientoCM6() #en la posicion del personaje debe haber un 0, un paso adelante del personaje hay un 6 y dos paso delante del personaje hay un 4

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
            self.movimientoCM7()

        elif self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
            self.movimientoC() #un paso adelante del personaje debe haber un 1 y dos paso adelante del personaje hay un 4


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

    def movimientoCMI(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0

        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6

        self.personaje_columna -= 1

    def movimientoCMI2(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5

        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
        
        self.personaje_columna -= 1

    def movimientoCMI3(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5

        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
        
        self.personaje_columna -= 1

    def movimientoCMI4(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5

        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1

        self.personaje_columna -= 1

    def movimientoCMI5(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0

        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1

        self.personaje_columna -= 1

    def movimientoCMI6(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4#en la posicion del personaje se cambia a 4
        
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5 #un paso delante del personaje se cambia a 5

        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1#dos pasos delante del personaje se cambia a 1

        self.personaje_columna -= 1 #actualiza la posicion en el mapa

    def movimientoCMI7(self):#personaje meta empuja caja hacia meta
        
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0

        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6

        self.personaje_columna -= 1

    def izquierda(self):
        if self.mapa[self.personaje_fila][self.personaje_columna - 1 ] == 4 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
            self.movimiento2()

        elif self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
            self.movimientoMI2()

        elif self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna] == 5:
            self.movimientoMI()

        elif self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4 and self.mapa[self.personaje_fila][self.personaje_columna] == 5:
            self.movimientoMIS()

        elif self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
            self.movimientoCMI()

        elif self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
            self.movimientoCMI2()

        elif self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna] == 5:
            self.movimientoCMI3()

        elif self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna] == 5:
            self.movimientoCMI4()
        
        elif self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna] == 5:
            self.movimientoCMI5()

        elif self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6  and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
            self.movimientoCMI6() #en la posicion del personaje debe haber un 0, un paso adelante del personaje hay un 6 y dos paso delante del personaje hay un 4

        elif self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna] == 5:
            self.movimientoCMI7()

        elif self.mapa[self.personaje_fila][self.personaje_columna - 2 ] == 4 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1:
            self.movimientoC2()


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

    def movimientoCMA(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0

        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6

        self.personaje_fila -= 1

    def movimientoCMA2(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5

        self.mapa[self.personaje_fila  - 2][self.personaje_columna] = 6
        
        self.personaje_fila -= 1


    def movimientoCMA3(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5

        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        
        self.personaje_fila -= 1

    def movimientoCMA4(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5

        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1

        self.personaje_fila -= 1

    def movimientoCMA5(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0

        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1

        self.personaje_fila -= 1

    def movimientoCMA6(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4#en la posicion del personaje se cambia a 4
        
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5 #un paso delante del personaje se cambia a 5

        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1#dos pasos delante del personaje se cambia a 1

        self.personaje_fila -= 1 #actualiza la posicion en el mapa

    def movimientoCMA7(self):#personaje meta empuja caja hacia meta
        
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0

        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6

        self.personaje_fila -= 1

    def arriba(self):

        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
            self.movimiento3()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2:
            self.movimientoMA2()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2:
            self.movimientoMA()
        
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
            self.movimientoMAS()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.movimientoCMA()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.movimientoCMA2()
        
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.movimientoCMA3()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
            self.movimientoCMA4()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
            self.movimientoCMA5()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6  and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
            self.movimientoCMA6()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.movimientoCMA7()

        elif self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
            self.movimientoC3()


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

    def movimientoCMAB(self):

        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6

        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0

        self.mapa[self.personaje_fila][self.personaje_columna] = 4

        self.personaje_fila += 1

    def movimientoCMAB2(self):

        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6

        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5

        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.personaje_fila += 1

    def movimientoCMAB3(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5

        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        
        self.personaje_fila += 1

    def movimientoCMAB4(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 2

        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5

        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1

        self.personaje_fila += 1

    def movimientoCMAB5(self):

        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0

        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1

        self.personaje_fila += 1

    def movimientoCMAB6(self):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4#en la posicion del personaje se cambia a 4
        
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5 #un paso delante del personaje se cambia a 5

        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1#dos pasos delante del personaje se cambia a 1

        self.personaje_fila += 1 #actualiza la posicion en el mapa

    def movimientoCMAB7(self):#personaje meta empuja caja hacia meta
        
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0

        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6

        self.personaje_fila += 1


    def abajo(self):

        if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
            self.movimiento4()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2:
            self.movimientoMAB2()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2:
            self.movimientoMAB()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
            self.movimientoMABS()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
            self.movimientoCMAB()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
            self.movimientoCMAB2()
        
        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
            self.movimientoCMAB3()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
            self.movimientoCMAB4()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
            self.movimientoCMAB5()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6  and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
            self.movimientoCMAB6()

        elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
            self.movimientoCMAB7()

        elif self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
            self.movimientoC4()

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def jugar(self):
        while True:
            self.limpiar_pantalla()
            # Imprime el mapa
            self.imprimirMapa()

            print("Su posicion es:")
            print((self.personaje_columna,self.personaje_fila))
            # Pide al usuario el movimiento
            movimiento = input("Selecciona el movimiento: ")
            # Moverse a la derecha
            if movimiento == 'd':
                self.derecha()
            elif movimiento == 'a':
                self.izquierda()
            elif movimiento == 'w':
                self.arriba()
            elif movimiento == 's':
                self.abajo()
            elif movimiento == 'r':
                self.__init__()
                
soko = Soko()
soko.jugar()