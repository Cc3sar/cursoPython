fh = open("romeo.txt")
lst = dict()
valor = 0
for line in fh:
    ordenar = line.split()
    for palabras in ordenar:
        if palabras in lst: continue
        valor += 1
        lst[palabras] = valor
print(lst)    