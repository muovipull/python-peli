'''
import datetime
aika = datetime.datetime.now()
print(aika.strftime("%d.%m.%Y %H:%M:%S"))

import time
alku = time.time()   # ajan mittaus alkaa
tulos = int(input("Paljonko on 13 * 19? "))
loppu = time.time()  # ajan mittaus päättyy
if tulos == 247:
    print("Oikein!")
else:
    print("Väärin!")
print("Aika:", round(loppu - alku, 1), "s")
'''
import time
import datetime

while True:

    aika = datetime.datetime.now()


    print(aika.hour,".",aika.minute,".",aika.second)
    time.sleep(1)

'''
import urllib.request
osoite = "https://www.ohjelmointiputka.net/oppaat/opas.php?tunnus=python3_09"
sivu = urllib.request.urlopen(osoite)
data = sivu.read()
try:
	teksti = data.decode("UTF-8")
	print(teksti)
except:
	try:
		teksti = data.decode("Latin-1")
		print(teksti)
	except:
		print("Merkistökoodaus ei ole UTF-8 eikä Latin-1.")
		print("Tulostetaan data ilman dekoodausta:")
		print(data)
'''



