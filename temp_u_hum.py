import requests
from bs4 import BeautifulSoup
#import getpass

AB = 0

list = []
session_requests = requests.session()
url = 'https://www.wetteronline.de/wetter/dortmund#'
url2 = 'https://www.wetteronline.de/aktuelles-wetter?gid=10416'


logRes = session_requests.get(url)
logRes2 = session_requests.get(url2)

loSoup = BeautifulSoup(logRes.text, features='html.parser')
inpData = loSoup.find_all('div')

loSoup2 = BeautifulSoup(logRes2.text, features='html.parser')
#Liefert alle Daten (container)
inpData2 = loSoup2.find_all('div',{"id":"humidity"})

#Definieren der Daten, die man holen will
for i in inpData:
    if i.get('id') == 'nowcast-card-temperature':
        n = str(i.find_all('div')[0].text).strip()
        print(n)
        #drucken der Information
        
for m in inpData2:
    #m = inpData22.div.table.tbody.tr
    AB = m
    k = AB.findAll('td')
    print(str(k[1].text))