import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_691953.xml"

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

tree = ET.fromstring(data)

counts = tree.findall('.//count')

lista = list()

for read in counts:
    element = read.text
    element = int(element)
    lista.append(element)
print(sum(lista))