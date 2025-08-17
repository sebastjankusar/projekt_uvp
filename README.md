# <p align="center">ANALIZA FILMOV</p>
V svoji projektni nalogi za predmet **Uvod v programiranje** sem se odločil analizirati vse filme, ki so med 1981 in 2020 pristali na prvem mestu v prodaji vstopnic (angleško box office). Podatke sem dobil s spletne strani https://www.listchallenges.com/every-number-1-movie-in-the-usa-box-office.
## <p align="center">NAVODILA</p>
Če želite sami pridobiti podatke iz interneta in jih pretvoriti v csv datoteko, samo poženite main.py. Če s tem ne želite naresti html datotek za strani seznama, ko v terminalu požene main.py zraven dopišite ne_poberi.<br>
Analiza filmov je dostopna v datoteki `analiza.ipynb`.
## <p align="center">PRIDOBIVANJE PODATKOV</p>
- V datoteki `dobivanje_spletnih_strani.py` je funkcija, ki iz vseh strani seznama iz interneta shrani html datoteko v računalnik.
- Funkcija v datoteki `izluscenje_podatkov.py` nato z regularnimi izrazi naredi slovar filmov z naslovom, letom izdaje, oceno, ki jo je film dosegel na Rotten Tomatoes, ter oceno, ki jo je dosegel na IMDb. 
- Nazadnje funkcija v datoteki `naredi_csv.py` slovar filmov prepiše v datoteko `filmi.csv`. 
## <p align="center">ANALIZA</p>
V analizi, vidni v datoteki `analiza.ipynb`, lahko vidite razne tabele in grafične prikaze, ki prikazujejo, kateri filmi so najboljše in kateri najslabše ocenjeni, ter druge zanimive ugotovitve.<br>
Nekatere funkcije, uporabljene pri analizi, so shranjene v datoteki `analiza_funkcije.py`, da je v glavni datoteki manj vidne kode.