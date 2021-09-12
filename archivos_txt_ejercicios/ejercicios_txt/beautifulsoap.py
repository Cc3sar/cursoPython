from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_691951.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
values = list()

for tag in tags:
    search = str(tag)
    number = re.findall('>([0-9]+)</', search)
    for x in number:
        values.append(int(x))
    
print(sum(values))