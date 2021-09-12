import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_691954.json"

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

data = data.decode()

info = json.loads(data)

suma = 0

for read in info['comments']:
    values = int(read['count'])
    suma += values
print(suma)