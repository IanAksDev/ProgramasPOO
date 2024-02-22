""""
Nombre: Ian Aksel Hernandez Mendieta
Matricula: 1723110389
Grupo: 21
Fecha: 18/01/2024
Descripción: 
Programa para definir un objeto de la clase Alumno y sus atributos como nombre y matricula, ademas de acceder a la funcion sumar, que suma dos numeros.

"""

class Alumno:  #donde se crea  la clase
    matricula: None #creacion del atributo matricula
    nombre: None #creaciion del atributo nombre
    def __init__(self, matricula, nombre): #creacion del constructor
        self.matricula = matricula #pasa el valor de la variable matricula al init
        self.nombre = nombre #pasa el valor de la variable nombre al init
        print("Objeto Alumno")#imprime el texto objeto alumno
    def estudiar (self): #creacion de la funcion estudiar
        print(f"{self.nombre} estudia") #imprime el valor guardado de nombre y estudia
    def sumar (self,numero1, numero2):#creacion de la funcion sumar
        suma=numero1+numero2#suma los valores de numero1 y numero2
        print(f"{numero1} + {numero2} = {suma}")#realiza la suma y la imprime
dejah=Alumno(111, "dejah")#crea un objeto de la clase alumno
dejah.estudiar()#inovoca la funcion estudiar de la clase
dejah.sumar(10,5)#invoca  la funcion sumar de la clase
  