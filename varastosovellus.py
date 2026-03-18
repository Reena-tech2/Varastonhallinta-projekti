import sqlite3
import os
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
        
def tulosta_tietokone():
    """
    Fetch data from the "tietokone" table and print it into the terminal\n
    Paremeters:\n
        None\n
    Returns:\n
        None
    Example:\n
        tulosta_tietokone()
    """    
    sql = """SELECT * FROM tietokone"""
    cur = CONN.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def tulosta_komponentti():
    """
    Fetch data from the "komponentti" table and print it into the terminal\n
    Paremeters:\n
        None\n
    Returns:\n
        None
    Example:\n
        tulosta_komponentti()
    """    
    sql = """SELECT * FROM komponentti"""
    cur = CONN.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def lisaa_tietokone(merkki, malli, hinta, maara):
    """
    Adds data to the database with given values.\n
    Parameters:\n
        merkki (string)\n
        malli (string)\n
        hinta (string)\n
        maara (integer)\n
    Returns:\n
        None\n
    Example:\n
        lisaa_tietokone(HP, model666, 666, 66)
    """
    sql = """INSERT INTO tietokone (merkki, malli, hinta, maara) VALUES (?, ?, ?, ?)"""
    cursor = CONN.cursor()
    cursor.execute(sql, (merkki, malli, hinta, maara))
    CONN.commit()
    print("Tietokone lisätty")

def lisaa_komponentti(nimi, hinta, maara):
    """
    Adds data to the database with given values.\n
    Parameters:\n
        nimi (string)\n
        hinta (string)\n
        maara (integer)\n
    Returns:\n
        None\n
    Example:\n
        lisaa_komponentti(muistikampa 8Gb, 123, 12)
    """
    sql = """INSERT INTO komponentti (nimi, hinta, maara) VALUES (?, ?, ?)"""
    cursor = CONN.cursor()
    cursor.execute(sql, (nimi, hinta, maara))
    CONN.commit()
    print("Komponentti lisätty")

def poista_tietokone(id):
    """
    Remove data from database based on the given ID.\n
    Parameters:\n
        ID (integer)
    Returns:\n
        None\n
    Example:\n
        poista_tietokone(3)
    """

    sql = """DELETE FROM tietokone WHERE id = ?"""
    cur = CONN.cursor()
    cur.execute(sql, (id, ))
    CONN.commit()
    print("Tietokone poistettu")

def poista_komponentti(id):
    """
    Remove data from database based on the given ID.\n
    Parameters:\n
        ID (integer)
    Returns:\n
        None\n
    Example:\n
        poista_komponentti(3)
    """

    sql = """DELETE FROM komponentti WHERE id = ?"""
    cur = CONN.cursor()
    cur.execute(sql, (id, ))
    CONN.commit()
    print("Komponentti poistettu")

def main ():
    """
    Main function for the program
    """
    global CONN
    os.system("cls")
    try:
        database = r"C:\Users\satuh\Documents\GitHub\Varastonhallinta-projekti\varasto.db"
        CONN = sqlite3.connect(database)
        while 1:
            print("VARASTONHALLINTA")
            print("----------")
            print("PÄÄVALIKKO")
            print("1: Tulosta varasto")
            print("2: Lisää tuote")
            print("3: Poista tuote")
            print("4: Sulje ohjelma")

            user_input = input("Value: ")
            if user_input == "1":
                os.system("cls")
                print("TIETOKONEET:")
                tulosta_tietokone()
                print("\nKOMPONENTIT:")
                tulosta_komponentti()

            if user_input == "2":
                os.system("cls")
                luokka = input("1. Tietokone \n2. Komponentti \nValitse numerolla lisättävän tuotteen luokka: ")

                if luokka == "1":
                    os.system("cls")
                    merkki = input("Merkki: ")
                    malli = input("Malli: ")
                    hinta = input("Hinta €: ")
                    maara = input("Määrä: ")
                    os.system("cls")
                    lisaa_tietokone(merkki, malli, hinta, int(maara))
                if luokka == "2":
                    os.system("cls")
                    nimi = input("Tuotenimi: ")
                    hinta = input("Hinta €: ")
                    maara = input("Määrä: ")
                    os.system("cls")
                    lisaa_komponentti(nimi, hinta, int(maara))

            if user_input == "3":
                os.system("cls")
                os.system("cls")
                luokka = input("1. Tietokone \n2. Komponentti \nValitse numerolla poistettavan tuotteen luokka: ")
                id = int(input("Anna poistettavan tuotteen ID: "))

                if luokka == "1":
                    os.system("cls")
                    poista_tietokone(id)
                if luokka == "2":
                    os.system("cls")
                    poista_komponentti(id)

            if user_input == "4":
                os.system("cls")
                print("Suljetaan ohjelma")
                os._exit(0)

            elif user_input not in ["1", "2", "3", "4"]:
                os.system("cls")
                print("Väärä valinta")    
    finally:
        if CONN:
            CONN.close()

if __name__ == "__main__":
    main()
        
    


    
    
    #def paivita_hinta(self,uusi_hinta):
    #Lisämme koodia päivittääkse hinnan
    
    
    #Lisämme enemmän function tähän
