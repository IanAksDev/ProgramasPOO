"""
Nombre: Ian Aksel Hernandez Mendieta
Matricula: 1723110389
Grupo: 21
Fecha: 18/01/2024
Descripción: Es un programa que crea a la clase y sus atributos, e imprime el nombre, la matricula y Objetos Alumnos.
"""
class Alumnos:#Crea la clase Alumnos
  matricula=None#crea el atributo matricula
  nombre=None#crea el atributo nombre
  def __init__ (self, matricula, nombre):#define al constructor de la clase Alumnos
    self.matricula=matricula#pasa el valor del atributo matricula al init
    self.nombre=nombre#pasa el valor del atributo nombre al init
print("Objetos Alumnos")#imprime objetos alumnos
objetoAlumnos=Alumnos(1723110389, "Aksel")#crea instancia  de la clase Alumnos
print(objetoAlumnos.matricula, objetoAlumnos.nombre)#imprime los atributos matricula y nombre