from urllib import request
import ssl


class NoPm:
    def __init__(self):
        pass
    def get_data(self):
        ssl._create_default_https_context = ssl._create_unverified_context

        url = "https://www.lanuv.nrw.de/fileadmin/lanuv/luft/immissionen/aktluftqual/eu_luftqualitaet.csv"
        url2 = "https://www.opengeodata.nrw.de/produkte/umwelt_klima/luftqualitaet/luqs/konti_nach_station/OpenKontiLUQS_VDOM_aktuell.csv"

        # Umgehung, um Daten von der Webseite zu holen
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1)'}
        res = request.Request(url=url, headers=headers)

        response = request.urlopen(res)
        csv = response.read()

        # definieren der csv-Datei als String
        csvstr = str(csv).strip("b'")

        # Ausgabe der Daten
        lines = csvstr.split("\\n")
        for line in lines:
            # if "\\xd" in line

            if 'Dortmund' in line:
                data = line.split(";")
                if data[1] == 'VDOR':
                    return {'no2': data[4], 'pm10': data[5]}
