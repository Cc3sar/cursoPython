fname = input("Ingrese el nombre del archivo: ")
try:
    openfile = open(fname)
except:
    print("El archivo no existe o el nombre es incorrecto")
    exit()
for read in openfile:
    print(read.upper())