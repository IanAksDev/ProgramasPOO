# ProgramasPOO
Programas que se hicieron en clases
# Sokoba
## 0. Objetivo 

programar el juego de sokoba en una version retro para consola.

## 1. Reglas del juego

El juego sokoba consiste en acomodar cajas en puntos determinados por las metas.

1. El personaje se puede mover hacia arriba, abajo , izquierda y derecha.
2. El personaje solo puede empujar 1 caja en cualquier sentido.
3. El personae se movera en un mapa predefinido.
4. Para terminar el nivel se tiene que acomodar todas las cajas sobre las metas.

## 2. Elementos del juego

### 2.0  Mapa del juego

Cada nivel del juego se colocara dentro de un array bidimencional, colocando números para representar elementos de juego, a continuacion se tiene un ejemplo basico de nivel.

Mapa=[3,4,4,0,4,4,3]

## 2.1 lista elementos del juego

0. Personaje
1. Caja
2. Metas
3. Pared
4. Piso
5. Personaje-meta
6. Caja-meta

## 3. Controles 
- a=Izquierda
- d=Derecha
- w=Arriba
- s=Abajo

### 4.Lista de movimientos

 | No. | Sentido | Movimiento | Inicio | Fin | Fecha  |
 | --- | ------- | ---------- | ------ | --- | ------ |
 | 1 | derecha | personaje, piso | [0,4] | [4,0] | Succesfull |
 | 2 | izquierda | piso, personaje | [4,0] | [0,4] | Succesfull |  
 | 3 | derecha | caja, piso | [0,1,4] | [4,0,1] | Done |
 | 4 | izquierda | caja, piso | [4,1,0] | [1,0,4] | Done |
 | 5 | derecha | personaje, meta | [0,2] | [4,5] | ToDo |
 | 6 | izquierda | personaje, meta | [2,0] | [5,4] | ToDo |
 | 7 | derecha | personaje_meta,piso | [5,4] | [2,0] | ToDo |
 | 8 | izquierda | personaje_meta,piso | [4,5] | [0,2] | ToDo 
 | 9 | derecha | personaje_meta,meta | [5,2] | [2,5] | ToDo |
 | 10 | izquierda | personaje_meta,meta | [2,5] | [5,2] | ToDo |
 | 11 | derecha | personaje_meta,caja, piso | [5,1,4] | [2,0,1] | ToDo |
 | 12 | izquierda | personaje_meta,caja,piso | [4,1,5] | [1,0,2] | ToDo |  
 | 13 | derecha | personaje,caja,meta | [0,1,2] | [4,0,6] | ToDo |
 | 14 | izquierda | personaje,caja,meta | [2,1,0] | [6,0,4] | ToDo |
 | 15 | derecha | personaje,caja_meta,meta | [0,6,2] | [4,5,6] | ToDo |
 | 16 | izquierda | personaje,caja_meta,meta | [2,6,0] | [6,5,4] | ToDo |
 | 17 | derecha | personaje_meta,caja_meta,piso | [5,6,4] | [2,5,1] | ToDo |
 | 18 | izquierda | personaje_meta,caja_meta,piso | [4,6,5] | [1,5,2] | ToDo 
 | 19 | derecha | personaje,piso,pared | [0,4,3] | [4,0,3] | Succesfull |
 | 20 | izquierda | personaje,piso,pared | [3,4,0] | [3,0,4] | Succesfull |
 | 21 | derecha | personaje_meta,caja,meta | [5,1,2] | [2,0,6] | ToDo |
 | 22 | izquierda | personaje_meta,caja,meta | [2,1,5] | [6,0,2] | ToDo |
 | 23 | derecha | personaje,caja_meta,piso | [0,6,4] | [4,5,1] | ToDo |
 | 24 | izquierda | personaje,caja_meta,piso | [4,6,0] | [1,5,4] | ToDo |
 | 25 | derecha | personaje_meta,caja_meta,meta | [5,6,2] | [2,5,6] | ToDo |
 | 26 | izquierda | personaje_meta,caja_meta,meta | [2,6,5] | [6,5,2] | ToDo |
 | 27 | derecha | personaje,caja,pared | [0,1,3] | [0,1,3] | Done |
 | 28 | izquierda | personaje, caja,pared | [3,1,0] | [3,1,0] | Done |
