import dobivanje_spletnih_strani
import izluscenje_podatkov
import naredi_csv

import sys

argumenti = sys.argv
poberi = True
if len(argumenti) > 1 and argumenti[1] == "ne_poberi":
    poberi = False

if poberi:
    dobivanje_spletnih_strani.naredi_html_strani()

filmi = izluscenje_podatkov.naredi_seznam_filmov()

naredi_csv.shrani_filme(filmi)

