"""
Programa: eva01.py
Alumno: Ian Aksel Hernandez Mendieta
Matricula: 1723110389
Fecha: 1/29/2024
"""
class profesores(): #definimos la clace profesores
  id = None # definimos el la variable ID
  nombre = "" # definimos la variable Nombre
  materias = [] # definimos la variable Materias

  def __init__(self, id, nombre):# definimos el constructor
      self.id = id # accedemos a la variable ID
      self.nombre = nombre # accedemos a la variable nombre
      print("ClaceProfesor") # imprimimos el texto solicitado

  def califica(self): # definimos el metodo califica
      print("El profesor {} califica evaluaciones de la materia {}".format(self.nombre, self.materias[0])) # imprimimos el texto solicitado

  def pasaAsistencia(self):# definimos el metodo pasaAsistencia
      print(f"El profesor {self.nombre} pasa asistencia")
    # imprimimos el texto solicitado


profesor1 = profesores("111", "Profesor 1") # creamos el objeto profesores
profesor1.materias.append("Materia 1") # invocamos el metodo materias 1
profesor1.materias.append("Materia 2") # invocamos el metodo materias 2
profesor1.califica()# invocamos el metodo califica
profesor1.pasaAsistencia() # invocamos el metodo pasaAsistencia