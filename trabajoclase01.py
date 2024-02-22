a=10
b=9
c=18


if a>b:
    print(a) 
elif b>c:
    print(b) 
else: a>c
print(a) 

print("            ")

#este es un if anidado
if a>b:
    if a>c:
        print(a)
else:
    print(c)
    
print("")

if a>b and a>c:
    print(a)
else:
    print(c)

print("")

if a>b or a>c:
    print(a)
else:
    print(c)

print("")

cadena= "hola mundo python" 
vocalA= "a"
vocalE= "e"
vocalI= "i"
vocalO= "o"
vocalU= "u"
contadorA= 0
contadorE= 0
contadorI= 0
contadorO= 0
contadorU= 0
for letra in cadena.lower():
    if letra in vocalA:
        contadorA += 1
    if letra in vocalE:
        contadorE += 1
    if letra in vocalI:
        contadorI += 1
    if letra in vocalO:
        contadorO += 1
    if letra in vocalU:
        contadorU += 1

print("vocalesA: ", contadorA)
print("vocalesE: ", contadorE)
print("vocalesI: ", contadorI)
print("vocalesO: ", contadorO)
print("vocalesU: ", contadorU)



