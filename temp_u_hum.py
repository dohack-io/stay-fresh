import requests
from bs4 import BeautifulSoup


class TempHum:
    def __init__(self):
        self.temp = 0
        self.hum = 0
        # list = []
        self.session_requests = requests.session()
        self.url = 'https://www.wetteronline.de/wetter/dortmund#'
        self.url2 = 'https://www.wetteronline.de/aktuelles-wetter?gid=10416'

    def get_data(self):
        logRes = self.session_requests.get(self.url)
        logRes2 = self.session_requests.get(self.url2)

        loSoup = BeautifulSoup(logRes.text, features='html.parser')
        inpData = loSoup.find_all('div')

        loSoup2 = BeautifulSoup(logRes2.text, features='html.parser')
        # Liefert alle Daten (container)
        inpData2 = loSoup2.find_all('div',{"id":"humidity"})

        # Definieren der Daten, die man holen will
        for i in inpData:
            if i.get('id') == 'nowcast-card-temperature':
                n = str(i.find_all('div')[0].text).strip()
                self.temp = n
                #drucken der Information

        for m in inpData2:
            #m = inpData22.div.table.tbody.tr
            k = m.findAll('td')
            data = str(k[1].text)
            self.hum = data[:-1]

        return {'temp': self.temp, 'hum': self.hum}
