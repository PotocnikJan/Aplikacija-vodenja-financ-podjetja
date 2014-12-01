import sqlite3
datoteka_baze = "Podjetje.sqlite"

def izracunajPromet():
    #Za začetek izračunajmo dosedanji promet podjetja
    promet = 0
    c = baza.cursor
    c.execute("""SELECT SUM(skupna_cena) FROM izdani_racuni""")
    c.fetchone()
    promet += c
    c.close()
    return promet

def izracunajStroski():
    #izračunajmo še stroške
    stroski = 0
    c = baza.cursor
    c.execute("""SELECT SUM(cena) FROM stroski""")
    c.fetchone()
    stroski += c
    c.close()
    return stroski
def zasluzek():
    return (izracunajPromet() - izracunajSroski())


###################################################################
#Povežemo se z bazo

baza = sqlite3.connect(datoteka_baze,isolation_level=None)
#bottle.run(host='localhost', port=8080)
