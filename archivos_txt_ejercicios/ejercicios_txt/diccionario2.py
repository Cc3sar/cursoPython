name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
correos = dict()
mayor = 0

for read in handle:
    if read.find("From:"): continue
    if read.startswith("From"):
        correo = read.split()
        c = correo[1]
        correos[c] = correos.get(c, 0) + 1
        if correos[c] > mayor: 
            mayor = correos[c] 
            m = c
print(m, mayor)