# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:32:55 2019

@author: Benjamin Weber
"""

import requests
from bs4 import BeautifulSoup
#import getpass

AB = 0

list = []
session_requests = requests.session()
url = 'https://www.wetteronline.de/luftqualitaet/nordrhein-westfalen?day=28&gid=10416&metparaid=PM10&month=09&year=2019'


logRes = session_requests.get(url)

loSoup = BeautifulSoup(logRes.text)
inpData = loSoup.find('table')
d2 = inpData.contents[3]

k = d2.find_all('tr')


for i in k:
    i.find_all('a')
    ort = str(i.find_all('a')[0].text)
    AB = ort
    ort = ort.replace("\n","")
    ort = ort.replace("\t","")
    ort = ort.strip()
    wert = str(i.find_all('a')[1].text)
    wert = wert.replace("\n","")
    wert = wert.replace("\t","")
    wert = wert.replace(" ","")
    list.append((ort,wert))
    #if (tex.find('Diagramm') == -1 and tex.find('Feinstaub') == -1):
    #print(tex)
#print(i.contents[1].text)
#    for n in i.children:
#        k2 = n.find('td')
#        AB = n
    

#for i in inpData:
    
    
#    str1 = str(i.get('href'))
#    if str1.find('PM10') != -1:
#        if str(i.text).isnumeric():
#            print (i.text)
#        if i.text.isnumeric():
#            print (i.text)
            #print(i.previous_element.text)
    #if i.get('href') == '/ozonwerte/ratingen?metparaid=PM10':
     #   print ('HURRRAA!!!')

        
"""
for i in inpData:
    #print (i.get('name'))
    if i.get('name') == 'execution':
       execution = i.get('value')
        print (execution)
        
print ('Token: ' + token)


pl = {"username" : "g027501", "password" : "********", "warn" : "true"}

#soup = BeautifulSoup(result.text)
#print(soup.find_all('input'))


"""
