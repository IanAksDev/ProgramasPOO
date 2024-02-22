"""
Nombre: Ian Aksel Hernandez Mendieta
Matricula: 1723110389
Grupo: 21
Fecha: 18/01/2024
Descripción: Es un programa que crea a la clase y sus variables, e imprime el nombre y el constructor de la clase.
"""
class A:#crea la clase A
  matricula=None#crea el atributo matricula
  nombre=None#crea el atributo nombre
  def __init__ (self):#define al constructor de la clase A
    print("Constructor de la clase A")#imprime constructor de la clase A
objetoA=A()#Es la instancia de la clase A
print(objetoA.nombre)#imprime el atributo nombre
