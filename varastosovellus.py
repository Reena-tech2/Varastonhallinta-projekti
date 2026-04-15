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
        # Lisämme koodia tuotteen lisäämiseksi
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


def tulosta_yksi_tietokone(merkki):
    sql = """SELECT * FROM tietokone WHERE merkki = ? COLLATE NOCASE"""
    cur = CONN.cursor()
    cur.execute(sql, (merkki,))
    row = cur.fetchone()
    if row:
        print(
            f"ID: {row[0]}, Merkki: {row[1]}, Malli: {row[2]}, Hinta: {row[3]}€, Määrä: {row[4]} kpl")
    else:
        print(f"Tietokonetta merkillä '{merkki}' ei löytynyt.")
    cur.close()


def tulosta_yksi_komponentti(nimi):
    sql = """SELECT * FROM komponentti WHERE nimi = ? COLLATE NOCASE"""
    cur = CONN.cursor()
    cur.execute(sql, (nimi,))
    row = cur.fetchone()
    if row:
        print(
            f"ID: {row[0]}, Nimi: {row[1]}, Hinta: {row[2]}€, Määrä: {row[3]} kpl")
    else:
        print(f"Komponenttia nimellä '{nimi}' ei löytynyt.")
    cur.close()


def lisaa_tietokone(merkki, malli, hinta, maara):
    cursor = CONN.cursor()

    merkki = merkki.strip().lower()
    malli = malli.strip().lower()
    hinta = float(hinta)
    maara = int(maara)

    # check if exists
    cursor.execute("""
        SELECT maara FROM tietokone
        WHERE merkki = ? AND malli = ?
    """, (merkki, malli))

    result = cursor.fetchone()

    if result:
        uusi_maara = result[0] + maara

        cursor.execute("""
            UPDATE tietokone
            SET maara = ?, hinta = ?
            WHERE merkki = ? AND malli = ?
        """, (uusi_maara, hinta, merkki, malli))

        print("Tietokone päivitetty")

    else:
        cursor.execute("""
            INSERT INTO tietokone (merkki, malli, hinta, maara)
            VALUES (?, ?, ?, ?)
        """, (merkki, malli, hinta, maara))

        print("Tietokone lisätty")

    CONN.commit()


def lisaa_komponentti(nimi, hinta, maara):
    cursor = CONN.cursor()

    nimi = nimi.strip().lower()
    hinta = float(hinta)
    maara = int(maara)

    # check if exists
    cursor.execute("""
        SELECT maara FROM komponentti
        WHERE nimi = ? COLLATE NOCASE
    """, (nimi,))

    result = cursor.fetchone()

    if result:
        uusi_maara = result[0] + maara

        cursor.execute("""
            UPDATE komponentti
            SET maara = ?, hinta = ?
            WHERE nimi = ? COLLATE NOCASE
        """, (uusi_maara, hinta, nimi))

        print("Komponentti päivitetty")

    else:
        cursor.execute("""
            INSERT INTO komponentti (nimi, hinta, maara)
            VALUES (?, ?, ?)
        """, (nimi, hinta, maara))

        print("Komponentti lisätty")

    CONN.commit()


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
    cursor.execute(sql, values)
    CONN.commit()

    if cursor.rowcount == 0:
        print(f"Tuotetta '{nimi}' ei löytynyt tietokannasta.")
    else:
        print(
            f"{nimi} päivitetty onnistuneesti: hinta={uusi_hinta}, määrä={uusi_maara}")


def main():
    """
    Main function for the program
    """
    global CONN
    os.system("cls")
    try:
        # Muutetaan tietokannan polku suhteelliseksi, jotta se toimii millä tahansa tietokoneella
        database = "varasto.db"

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
                print("1. Tulosta kaikki tuotteet")
                print("2. Hae tietty tietokone")
                print("3. Hae tietty komponentti")
                valinta = input("Valitse toiminto: ")

                if valinta == "1":
                    os.system("cls")
                    print("TIETOKONEET:")
                    tulosta_tietokone()
                    print("\nKOMPONENTIT:")
                    tulosta_komponentti()

                elif valinta == "2":
                    merkki = input("Anna tietokoneen merkki: ")
                    if not merkki.strip():
                        print("Merkki ei voi olla tyhjä")
                        continue
                    os.system("cls")
                    print("TIETOKONE:")
                    tulosta_yksi_tietokone(merkki)

                elif valinta == "3":
                    nimi = input("Anna komponentin nimi: ")
                    if not nimi.strip():
                        print("Nimi ei voi olla tyhjä")
                        continue
                    os.system("cls")
                    print("KOMPONENTTI:")
                    tulosta_yksi_komponentti(nimi)

                else:
                    os.system("cls")
                    print("Väärä valinta")

            if user_input == "2":
                os.system("cls")
            luokka = input(
                "1. Tietokone \n2. Komponentti \nValitse numerolla lisättävän tuotteen luokka: ")

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
                luokka = input(
                    "1. Tietokone \n2. Komponentti \nValitse numerolla poistettavan tuotteen luokka: ")
                id = int(input("Anna poistettavan tuotteen ID: "))

                if luokka == "1":
                    os.system("cls")
                    poista_tietokone(id)
                if luokka == "2":
                    os.system("cls")
                    poista_komponentti(id)

            if user_input == "4":
                os.system("cls")
                luokka = input(
                    "1. Tietokone \n2. Komponentti \nValitse numerolla päivitettävän tuotteen luokka: ")
                nimi = input("Anna tuotteen nimi: ")
                if not nimi.strip():
                    print("Nimi ei voi olla tyhjä")
                    continue
                hinta_input = input("Anna uusi hinta : ")
                maara_input = input("Anna uusi määrä : ")

                uusi_hinta = float(hinta_input) if hinta_input else None
                uusi_maara = int(maara_input) if maara_input else None

                if luokka == "1":
                    paivita_tuotteen_tiedot(
                        nimi, uusi_hinta, uusi_maara, luokka="tietokone")
                elif luokka == "2":
                    paivita_tuotteen_tiedot(
                        nimi, uusi_hinta, uusi_maara, luokka="komponentti")

            if user_input == "5":
                os.system("cls")
                print("Suljetaan ohjelma")
                os._exit(0)

            elif user_input not in ["1", "2", "3", "4", "5"]:
                os.system("cls")
                print("Väärä valinta")
    finally:
        if CONN:
            CONN.close()


if __name__ == "__main__":
    main()
