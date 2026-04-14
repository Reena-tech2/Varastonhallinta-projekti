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

 # Jos haluamme lisätä uusia tuotetyyppejä, voimme tehdä uuden luokan


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
        
    def paivita_tuotteen_tiedot(self, nimi, uusi_hinta=None, uusi_maara=None):
        for tuote in self.tuotteet:
            if hasattr(tuote, "nimi") and tuote.nimi == nimi:
                if uusi_hinta is not None:
                    if uusi_hinta < 0:
                        print("Virhe: Hinta ei voi olla negatiivinen")
                        return
                    tuote.hinta = uusi_hinta
                if uusi_maara is not None:
                    if uusi_maara < 0:
                        print("Virhe: Määrä ei voi olla negatiivinen")
                        return
                    tuote.maara = uusi_maara
                print(
                    f"{nimi} päivitetty onnistuneesti: hinta={tuote.hinta}€, määrä={tuote.maara} kpl")
                return
        print(f"Tuotetta '{nimi}' ei löytynyt varastosta")
        
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
    
    
def paivita_tuotteen_tiedot(nimi, uusi_hinta=None, uusi_maara=None, luokka="tietokone"):
    """
    Update product information directly in the database.
    
    Parameters:
        nimi (str): Name of the product (merkki for tietokone, nimi for komponentti)
        uusi_hinta (float, optional): New price
        uusi_maara (int, optional): New quantity
        luokka (str): "tietokone" or "komponentti"
    
    Returns:
        None
    """
    # Choose table and column for name
    if luokka == "tietokone":
        table = "tietokone"
        name_col = "merkki"
    elif luokka == "komponentti":
        table = "komponentti"
        name_col = "nimi"
    else:
        print("Virhe: tuntematon tuoteluokka")
        return

    # Build SQL dynamically depending on which fields to update
    fields = []
    values = []
    if uusi_hinta is not None:
        if uusi_hinta < 0:
            print("Virhe: Hinta ei voi olla negatiivinen")
            return
        fields.append("hinta = ?")
        values.append(uusi_hinta)
    if uusi_maara is not None:
        if uusi_maara < 0:
            print("Virhe: Määrä ei voi olla negatiivinen")
            return
        fields.append("maara = ?")
        values.append(uusi_maara)

    if not fields:
        print("Ei muutettavia tietoja.")
        return

    # Add the name for WHERE clause
    values.append(nimi)

    sql = f"UPDATE {table} SET {', '.join(fields)} WHERE {name_col} = ? COLLATE NOCASE"
    
    cursor = CONN.cursor()
    cursor.execute(sql,values)
    CONN.commit()

    if cursor.rowcount == 0:
        print(f"Tuotetta '{nimi}' ei löytynyt tietokannasta.")
    else:
        print(f"{nimi} päivitetty onnistuneesti: hinta={uusi_hinta}, määrä={uusi_maara}")

def main ():
    """
    Main function for the program
    """
    global CONN
    os.system("cls")
    try:
        database = "varasto.db" #Muutetaan tietokannan polku suhteelliseksi, jotta se toimii millä tahansa tietokoneella

        CONN = sqlite3.connect(database)
        while 1:
            print("VARASTONHALLINTA")
            print("----------")
            print("PÄÄVALIKKO")
            print("1: Tulosta varasto")
            print("2: Lisää tuote")
            print("3: Poista tuote")
            print("4: Päivitä tuotteen tiedot")
            print("5: Sulje ohjelma")

            user_input = input("Value: ")
            if user_input == "1":
                os.system("cls")
                print("TIETOKONEET:")
                tulosta_tietokone()
                print("\nKOMPONENTIT:")
                tulosta_komponentti()

            if user_input == "2":
                os.system("cls")
                luokka = input("1. Tietokone \n2. Komponentti \nValitse lisättävän tuotteen luokka numerolla: ")
                
                if luokka not in ["1", "2"]:
                        print("Virhe: Valitse 1 tai 2")
                        continue

                if luokka == "1":
                    os.system("cls")
                    merkki = input("Merkki: ")
                    if not merkki.strip():
                        print("Merkki ei voi olla tyhjä")
                        continue
                    malli = input("Malli: ")
                    hinta = input("Hinta €: ")
                    maara = input("Määrä: ")
                    os.system("cls")
                    lisaa_tietokone(merkki, malli, hinta, int(maara))
                if luokka == "2":
                    os.system("cls")
                    nimi = input("Tuotenimi: ")
                    if not nimi.strip():
                        print("Nimi ei voi olla tyhjä")
                        continue
                    hinta = input("Hinta €: ")
                    maara = input("Määrä: ")
                    os.system("cls")
                    lisaa_komponentti(nimi, hinta, int(maara))

            if user_input == "3":
                os.system("cls")
                os.system("cls")
                luokka = input("1. Tietokone \n2. Komponentti \nValitse poistettavan tuotteen luokka numerolla: ")
                
                if luokka not in ["1", "2"]:
                        print("Virhe: Valitse 1 tai 2")
                        continue
                    
                id = int(input("Anna poistettavan tuotteen ID: "))

                if luokka == "1":
                    os.system("cls")
                    poista_tietokone(id)
                if luokka == "2":
                    os.system("cls")
                    poista_komponentti(id)
                    
            if user_input == "4":
                    os.system("cls")
                    luokka = input("1. Tietokone \n2. Komponentti \nValitse päivitettävän tuotteen luokka numerolla: ")
                    
                    if luokka not in ["1", "2"]:
                        print("Virhe: Valitse 1 tai 2")
                        continue
                   
                    nimi = input("Anna tuotteen nimi: ")
                    if not nimi.strip():
                        print("Nimi ei voi olla tyhjä")
                        continue
                    hinta_input = input("Anna uusi hinta : ")
                    maara_input = input("Anna uusi määrä : ")

                    uusi_hinta = float(hinta_input) if hinta_input else None
                    uusi_maara = int(maara_input) if maara_input else None

                    if luokka == "1":
                      paivita_tuotteen_tiedot(nimi, uusi_hinta, uusi_maara, luokka ="tietokone")
                    elif luokka == "2":
                      paivita_tuotteen_tiedot(nimi, uusi_hinta, uusi_maara, luokka ="komponentti")
                       
            

            if user_input == "5":
                os.system("cls")
                print("Suljetaan ohjelma")
                os._exit(0)

            elif user_input not in ["1", "2", "3", "4","5"]:
                os.system("cls")
                print("Väärä valinta")    
    finally:
        if CONN:
            CONN.close()

if __name__ == "__main__":
    main()
        
    


   

   
