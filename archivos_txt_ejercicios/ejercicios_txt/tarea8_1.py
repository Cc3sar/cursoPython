fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    ordenar = line.split()
    for palabras in ordenar:
        if palabras in lst: continue
        lst.append(palabras)
lst.sort()
print(lst)
