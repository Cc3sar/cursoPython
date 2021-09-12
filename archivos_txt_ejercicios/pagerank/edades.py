contador = 0
menores = 0
mayores = 0

for contador in range(10):
    edad = int(input("Ingrese la edad de la persona: "))
    if edad >= 18:
        mayores += 1
    else:
        menores += 1

print("La cantidad de personas mayores es: ",mayores)
print("La cantidad de personas menores es: ",menores)