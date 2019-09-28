#Hier wird HTML request angefordert von wetter.online
import requests

url_hauptseite = "https://www.wetteronline.de/?period=101&date=&pid=p_luft_observation&pcid=pc_luft_data&sid=StationDiagram&g"

url_station = ["d=a4457&iid ", "id=a4457&iid"]

url_tageszeit = ["=j101&day=28&month=9&year=2019"]

url_messwert = ["&metparaid=PM10", "&metparaid=NO" ]

r = requests.get(url_hauptseite.format(url_station[0]).format(url_tageszeit[0]).format(url_messwert[0]))

print(r.text)