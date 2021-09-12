import sqlite3
import re

conn = sqlite3.connect('DB1.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)

comparation = list()

for line in fh:
    line = line.rstrip()
    if not line.startswith("From: "): continue
    origin = re.findall('From: .*@([a-z]*)', line)
    
    if str(origin) in comparation or len(str(origin)) <= 2: continue
    comparation.append(str(origin))

    cur.execute('INSERT INTO Counts (org, count) VALUES (?, 0)', (str(origin),))
conn.commit()
  
for line2 in fh:
    print("ya me ejecute")
    line2 = line2.rstrip()
    if not line2.startswith("From: "): continue
    origin = re.findall('From: .*@([a-z]*)', line)
    try:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (str(origin),))
    except:
        continue
    
    


         
cur.close()