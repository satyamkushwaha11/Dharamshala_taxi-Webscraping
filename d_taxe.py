

import  requests
from bs4 import BeautifulSoup
import json

from requests.models import encode_multipart_formdata

url="https://www.dharamshalataxi.com/packages/"
re=requests.get(url)
soup=BeautifulSoup(re.text,"html.parser")
s=soup.find('div',class_="container")
s=s.find('table',class_="table")
h=s.find_all('th')
lt=[i.text for i in h]
# print(lt)
b=s.find("tbody")
bs=b.find_all('tr')
final=[]
for  i  in bs:
    asa=i.text.split('\n')[1:-2]
    z=zip(lt,asa)
    d=dict(z)
    final.append(d)
print(json.dumps(final,indent=4)) 
