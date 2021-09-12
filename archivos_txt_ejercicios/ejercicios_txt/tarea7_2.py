fname = input("Enter file name: ")
fh = open(fname)
contador = 0
result = 0
try:
    fh = open(fname)
except:
    print("El archivo no existe o el nombre es incorrecto")
    exit()
for read in fh:
    if not read.startswith("X-DSPAM-Confidence:") : continue 

    search_number = read.find("X-DSPAM-Confidence:")
    sn = read[search_number:]
    number = sn.find(":")
    n = sn[number+2:]
    number_convert = float(n)
    result = result + number_convert
    contador += 1
print("Average spam confidence:",result/contador)
  
    #convert_nr = float(nr.strip())
    #result += convert_nr
    