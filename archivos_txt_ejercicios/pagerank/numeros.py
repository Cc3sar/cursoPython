numero = int(input("Ingrese un numero comprendido entre 1 y 10: "))
numero_romano = "El numero en romano es: "

if numero >= 1 and numero <= 10:
    if numero == 1:
        print(numero_romano,"I")

    if numero == 2:
        print(numero_romano,"II")

    if numero == 3:
        print(numero_romano,"III")
    
    if numero == 4:
        print(numero_romano,"IV")
    
    if numero == 5:
        print(numero_romano,"V")
    
    if numero == 6:
        print(numero_romano,"VI")
    
    if numero == 7:
        print(numero_romano,"VII")
    
    if numero == 8:
        print(numero_romano,"VIII")
    
    if numero == 9:
        print(numero_romano,"IX")
    
    if numero == 10:
        print(numero_romano,"X")

else:
    print("Numero fuera del rango")