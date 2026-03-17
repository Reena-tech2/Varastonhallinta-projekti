
#tuote class
class Tietokone:
    def __init__(self, merkki, malli, hinta):
        self.merkki = merkki
        self.malli = malli
        self.hinta = hinta
    def nayta_tiedot(self):
       print(f"Merkki:{self.merkki}")
       print(f"Malli:{self.malli}")
       print(f"Hinta:{self.hinta}")
       
        
class Komponentti:
    def __init__(self, nimi, maara, hinta):
        self.nimi = nimi
        self.maara = maara
        self.hinta = hinta
    def nayta_tiedot(self):
        print(f"komponentti_nimi:{self.nimi}")
        print(f"komponentti_maara:{self.maara}")
        print(f"komponentti_hinta:{self.hinta}")
        
 #Jos haluamme lisätä uusia tuotetyyppejä,voimme tehdä uuden luokan

class Varasto:
    def __init__(self, varasto_nimi):
        self.varasto_nimi = varasto_nimi
        self.tuotteet= []
        
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
