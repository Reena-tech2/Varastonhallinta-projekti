
# tuote class
class Tietokone:
    def __init__(self, merkki, malli, hinta, maara):
        self.merkki = merkki
        self.malli = malli
        self.hinta = hinta
        self.maara = maara
    def nayta_tiedot(self):
       print(f"Merkki: {self.merkki}")
       print(f"Malli: {self.malli}")
       print(f"Hinta: {self.hinta}")
       print(f"Määrä: {self.maara}")
       
        
class Komponentti:
    def __init__(self, nimi, maara, hinta):
        self.nimi = nimi
        self.hinta = hinta
        self.maara = maara
    def nayta_tiedot(self):
        print(f"Nimi: {self.nimi}")
        print(f"Hinta: {self.hinta}")
        print(f"Määrä: {self.maara}")

 # Jos haluamme lisätä uusia tuotetyyppejä,voimme tehdä uuden luokan


class Varasto:
    def __init__(self, varasto_nimi):
        self.varasto_nimi = varasto_nimi
        self.tuotteet = []

    def lisaa_tuote(self, tuote):
    #Lisämme koodia tuotteen lisäämiseksi
         self.tuotteet.append(tuote)
         print(f"{tuote} lisätty {self.varasto_nimi}")
    
    def poista_tuote(self, nimi):
        for tuote in self.tuotteet:
            if tuote.nimi == nimi:
                self.tuotteet.remove(tuote)
                print("Tuote poistettu.")
                return
        print("Tuotetta ei löytynyt.")
        

        
    


    
    
    #def paivita_hinta(self,uusi_hinta):
    #Lisämme koodia päivittääkse hinnan
    
    
    #Lisämme enemmän function tähän
