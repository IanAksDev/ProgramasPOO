X=10
a=-5
x=6.0
print(type(X))
print(type(a))
print(type(x))
print(type(True))
print(type("Hola"))
class Persona:
    def __init__(self):
        print ("Constructor Persona")
dejah=Persona()
print(type(dejah))

a="10"
b=5
c="Hola"
d="adios"
print(b)
print(c+d)
print(a*5)
print(b*5)
cadena="dejah@email.com"
print(cadena[::2])
print(cadena [1::2])
for i in range (0,15):
    print(cadena[::2])
for i in range (1):
    print(cadena[1::2])
for i in [0,2,4,6,8,10,12,14]:
        print(cadena[i])123