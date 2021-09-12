fname = input("Enter file name: ")

fh = open(fname)
count = 0
for read in fh:
    if read.find("From:"): continue
    if read.startswith("From"):
        partes = read.split()
        print(partes[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")