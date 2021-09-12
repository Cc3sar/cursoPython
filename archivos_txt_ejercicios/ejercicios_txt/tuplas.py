name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
correos = dict()
lista = list()

for read in handle:
    if read.startswith("From:"): continue
    if read.startswith("From"):
        linea = read.split()
        hora = linea[5]
        h = str(hora).split(":")
        h = h[0]
        correos[h] = correos.get(h, 0) + 1

for clave, valor in list(correos.items()):
    lista.append((clave, valor))

lista.sort()

for clave, valor in lista:
    print(clave, valor)