repetir = True

while repetir == True:
    base = float(input("ingrese la base: "))
    altura = float(input("ingrese la altura: "))

    if base != 0 and altura != 0:
        area_triangulo = (base * altura) / 2
        print("El area del triangulo es: ",area_triangulo)
    else:
        repetir = False        

    
