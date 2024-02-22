"""
Nombre: Ian Aksel Hernandez Mendieta
Matricula: 1723110389
Grupo: 21
Fecha: 18/01/2024
Descripción: Es un programa que crea a la clase y sus atributos, e imprime el nombre y matricula de uno o mas objetos.
"""
class Alumnos:#Crea la clase Alumnos
  matricula=None#crea el atributo de la clase, matricula
  nombre=None#crea el atributo de la clase, nombre
  def __init__ (self, matricula, nombre):#define al constructor de la clase Alumnos
    self.matricula=matricula #pasa el valor del atributo matricula al init
    self.nombre=nombre#pasa el valor del atributo nombre al init
objetoAlumnos=Alumnos(1723110389, "Aksel")#crea instancia  de laclase Alumnos
objetoAlumnos2=Alumnos(nombre="John",matricula=222)#crea segunda instancia de la clase alumnos
print(objetoAlumnos.nombre, objetoAlumnos.matricula)#imprime los atributos matricula y nombre