temperatura = int(input("Ingrese la temperatura en grados Fahrenheit: "))
celsius = 0
apropiado = "Temperatura apropiada, la conversión a celsius es: "
inapropiado = "La temperatura en Fahrenheit debe ser "
celsius = (temperatura - 32) * 5/9

print("1. Natacion")
print("2. Tenis")
print("3. Golf")
print("4. Esqui")
print("5. Ajedrez")

opcion = int(input("Elija una opcion: "))

if opcion >=1 and opcion <= 5: 

    if opcion == 1:
        
        if temperatura > 85:
            print(apropiado, celsius)
        
        else:
            print(inapropiado, "mayor que 85")
    
    if opcion == 2:

        if temperatura > 70 and temperatura <= 85:
            print(apropiado, celsius)
        
        else:
            print(inapropiado, "mayor que 70 y menor o igual a 85")
    
    if opcion == 3:

        if temperatura > 32 and temperatura <= 70:
            print(apropiado, celsius)
        
        else:
            print(inapropiado, "mayor que 32 y menor o igual a 70")
    
    if opcion == 4:

        if temperatura > 10 and temperatura <= 32:
            print(apropiado, celsius)
        
        else:
            print(inapropiado, "mayor que 10 y menor o igual a 32")

    if opcion == 5:

        if temperatura <= 10:
            print(apropiado, celsius)
        
        else:
            print(inapropiado, "menor o igual a 10")
else:
    print("opcion fuera de rango")
