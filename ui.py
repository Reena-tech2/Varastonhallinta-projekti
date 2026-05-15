import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import varastosovellus
import sqlite3
CONN = sqlite3.connect("varasto.db")
varastosovellus.CONN = CONN
cursor = CONN.cursor()
root = tk.Tk()
root.title("Varastohallinta sovellus")
root.geometry("1000x150")
root.configure(bg="#2c3e50")
text_box = tk.Text(root, height=20, width=70, bg="#1e1e1e", fg="white",)
text_box.pack(pady=10)


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
    CONN = sqlite3.connect("varasto.db")
    cur = CONN.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        text_box.insert(tk.END, str(row) + "\n")


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
    CONN = sqlite3.connect("varasto.db")
    cur = CONN.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        text_box.insert(tk.END, str(row) + "\n")


def tulosta_varasto():

    text_box.delete("1.0", tk.END)

    text_box.insert(tk.END, "TIETOKONEET:\n")
    cursor.execute("SELECT * FROM tietokone")
    for row in cursor.fetchall():
        text_box.insert(tk.END, str(row) + "\n")

    text_box.insert(tk.END, "\nKOMPONENTIT:\n")
    cursor.execute("SELECT * FROM komponentti")
    for row in cursor.fetchall():
        text_box.insert(tk.END, str(row) + "\n")


btn = tk.Button(root, text="Tulosta varasto", command=tulosta_varasto)
btn.pack(pady=5)


def lisaa_tuote_ui():
    tyyppi = combo_lisaa.get()
    merkki = merkki_entry.get().strip()
    malli = malli_entry.get().strip()
    hinta_str = hinta_entry.get().strip()
    maara_str = maara_entry.get().strip()

    if tyyppi == "tietokone":
        if not all([merkki, malli, hinta_str, maara_str]):
            messagebox.showerror("Virhe", "Kaikki kentät ovat pakollisia.")
            return
    else:
        if not all([merkki, hinta_str, maara_str]):
            messagebox.showerror("Virhe", "Kaikki kentät ovat pakollisia.")
            return
    try:
        hinta = float(hinta_str)
    except ValueError:
        messagebox.showerror("Virhe", "Hinta täytyy olla numero.")
        return
    try:
        maara = int(maara_str)
    except ValueError:
        messagebox.showerror("Virhe", "Määrä täytyy olla kokonaisluku.")
        return
    if hinta < 0:
        messagebox.showerror("Virhe", "Hinta ei voi olla negatiivinen.")
        return
    if maara < 0:
        messagebox.showerror("Virhe", "Määrä ei voi olla negatiivinen.")
        return
    try:
        if tyyppi == "Tietokone":
            varastosovellus.lisaa_tietokone(merkki, malli, hinta, maara)
            messagebox.showinfo(
                "Onnistui", f"Tietokone '{merkki} {malli}' lisätty varastoon.")
        else:
            varastosovellus.lisaa_komponentti(merkki, hinta, maara)
            messagebox.showinfo(
                "Onnistui", f"Komponentti '{merkki}' lisätty varastoon.")
    except Exception as e:
        messagebox.showerror("Tietokantavirhe", str(e))
        return
    merkki_entry.delete(0, tk.END)
    malli_entry.delete(0, tk.END)
    hinta_entry.delete(0, tk.END)
    maara_entry.delete(0, tk.END)


# Lisää tuote
add_frame = tk.Frame(root)
add_frame.pack(pady=10)

ttk.Label(add_frame, text="Tyyppi").grid(row=0, column=0)
combo_lisaa = ttk.Combobox(
    add_frame, values=["Tietokone", "Komponentti"], width=15)
combo_lisaa.grid(row=0, column=1)
combo_lisaa.current(0)

ttk.Label(add_frame, text="Merkki").grid(row=0, column=2)
merkki_entry = ttk.Entry(add_frame, width=15)
merkki_entry.grid(row=0, column=3)

ttk.Label(add_frame, text="Malli").grid(row=0, column=4)
malli_entry = ttk.Entry(add_frame, width=15)
malli_entry.grid(row=0, column=5)

ttk.Label(add_frame, text="Hinta").grid(row=0, column=6)
hinta_entry = ttk.Entry(add_frame, width=10)
hinta_entry.grid(row=0, column=7)

ttk.Label(add_frame, text="Määrä").grid(row=0, column=8)
maara_entry = ttk.Entry(add_frame, width=10)
maara_entry.grid(row=0, column=9)

ttk.Button(add_frame, text="Lisää", command=lisaa_tuote_ui).grid(
    row=0, column=10, padx=10)




# Poista tuote
def poista_tietokone(id_value):
    try:
        cur = CONN.cursor()
        cur.execute("DELETE FROM tietokone WHERE id = ?", (id_value,))
        CONN.commit()
        print("Tietokone poistettu")
    except Exception as e:
        print("ERROR (tietokone):", e)

def poista_komponentti(id_value):
    try:
        cur = CONN.cursor()
        cur.execute("SELECT * FROM komponentti WHERE id = ?", (id_value,))
        CONN.commit()
        print("Komponentti poistettu")
    except Exception as e:
        print("ERROR:", e)

def delete_ui():
    try:
        print("BUTTON CLICKED")

        id_value = int(id_entry.get())
        tyyppi = combo_poista.get()

        print("TYPE:", tyyppi)
        print("ID:", id_value)

        if tyyppi == "Tietokone":
            poista_tietokone(id_value)
        elif tyyppi == "Komponentti":
            poista_komponentti(id_value)

    except ValueError:
        print("ERROR: ID must be a number")
    except Exception as e:
        print("ERROR:", e)






del_frame = tk.Frame(root)
del_frame.pack(pady=10)

# DROPDOWN MENU
ttk.Label(del_frame, text="Tyyppi").grid(row=0, column=0)
combo_poista = ttk.Combobox(del_frame, values=["Tietokone", "Komponentti"], width=15)
combo_poista.grid(row=0, column=1)
combo_poista.current(0)

# id
ttk.Label(del_frame, text="Id").grid(row=0, column=2)
id_entry = ttk.Entry(del_frame, width=15)
id_entry.grid(row=0, column=3)
# Button
btn = ttk.Button(del_frame, text="Poista", command=delete_ui)
btn.grid(row=0, column=6, padx=10)




# päivitettävän
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
    luokka = luokka.lower().strip()
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


def paivita_tuote_ui():
    try:
        print("UPDATE CLICKED")

        nimi = nimi_entry.get()
        luokka = combo_paivita.get()

        hinta = uusihinta_entry.get()
        maara = uusimaara_entry.get()

        if hinta == "":
            hinta = None
        else:
            hinta = float(hinta)

        if maara == "":
            maara = None
        else:
            maara = int(maara)

        paivita_tuotteen_tiedot(nimi, hinta, maara, luokka)

    except Exception as e:
        print("ERROR:", e)




paivita_frame = tk.Frame(root)
paivita_frame.pack(pady=10)

ttk.Label(paivita_frame, text="Tyyppi").grid(row=0, column=0)
combo_paivita = ttk.Combobox(paivita_frame, values=[
                     "Tietokone", "Komponentti"], width=15)
combo_paivita.grid(row=0, column=1)
combo_paivita.current(0)

ttk.Label(paivita_frame, text="Nimi").grid(row=0, column=2)
nimi_entry = ttk.Entry(paivita_frame, width=15)
nimi_entry.grid(row=0, column=3)


ttk.Label(paivita_frame, text="UusiHinta").grid(row=0, column=6)
uusihinta_entry = ttk.Entry(paivita_frame, width=10)
uusihinta_entry.grid(row=0, column=7)

ttk.Label(paivita_frame, text="UusiMäärä").grid(row=0, column=8)
uusimaara_entry = ttk.Entry(paivita_frame, width=10)
uusimaara_entry.grid(row=0, column=9)

ttk.Button(paivita_frame, text="paivita", command=paivita_tuote_ui).grid(row=0, column=10, padx=10)


def sulje_ohjelma():
    root.destroy()   # closes the window + ends program


btn = tk.Button(root, text="Sulje", command=sulje_ohjelma)
btn.pack(pady=20)

root.mainloop()
