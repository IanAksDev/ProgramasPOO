"""
0=personaje
1=caja
2=metas
3=pared
4=piso
5=personaje-meta
6=caja-meta
"""

Mapa= [3, 4, 4, 0, 4, 4, 3] #Define el mapa del juego
#definimos la posicion inicia del personaje
posicion_columna = 3

while True:

    print(Mapa)#imprime el mapa

    movimiento = input("Selecciona el movimiento: ") #Pide al usuario el movimiento


    if movimiento == "d":
        if Mapa [posicion_columna] == 0 and Mapa [posicion_columna +1] == 4:
    #donde estaba el personaje pone un piso
            Mapa[posicion_columna] = 4
    #donde estaba un piso pone el personaje
            Mapa [posicion_columna +1] = 0
    #actualiza la posicion del personaje
            posicion_columna+=1

    if movimiento == "a":

        if Mapa [posicion_columna -1] == 4 and Mapa[posicion_columna] == 0:
            Mapa[posicion_columna -1] = 0
            Mapa[posicion_columna] = 4
            posicion_columna-=1 
    print(Mapa)