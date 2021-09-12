import re 

f = open("regex_sum_691949.txt")
values = list()
number = list()

for read in f:
    read = read.rstrip()
    x = re.findall('\S*[0-9]\S*', read)

    if len(x) > 0:
        for n in x:
            number.append(n)
for val in number:
    try:
        n = int(val)
        values.append(n)
    except:
        continue
print(sum(values))