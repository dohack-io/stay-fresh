from urllib import request
import ssl; ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.lanuv.nrw.de/fileadmin/lanuv/luft/immissionen/aktluftqual/eu_luftqualitaet.csv"
url2 = "https://www.opengeodata.nrw.de/produkte/umwelt_klima/luftqualitaet/luqs/konti_nach_station/OpenKontiLUQS_VDOM_aktuell.csv"

# Retrieve the webpage as a string
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1)'}
res = request.Request(url=url2, headers=headers)

response = request.urlopen(res)
csv = response.read()

# Save the string to a file
csvstr = str(csv).strip("b'")

lines = csvstr.split("\\n")
for line in lines:
    print(line.split(";"))
        