import tkinter as tk
from tkinter import ttk
import varastosovellus
import sqlite3
CONN = sqlite3.connect("varasto.db")
cursor = CONN.cursor()
root = tk.Tk()
root.title("Varastohallinta sovellus")
root.geometry("1000x150")
root.configure(bg="#2c3e50")
text_box = tk.Text(root, height=20, width=70,bg="#1e1e1e",fg="white",)
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

btn = tk.Button(root,text = "Tulosta varasto",command= tulosta_varasto)
btn.pack(pady=5)


# Lisää tuote
add_frame = tk.Frame(root)
add_frame.pack(pady=10)

ttk.Label(add_frame, text="Tyyppi").grid(row=0, column=0)
combo = ttk.Combobox(add_frame, values=["Tietokone", "Komponentti"], width=15)
combo.grid(row=0, column=1)
combo.current(0)

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

ttk.Button(add_frame, text="Lisää").grid(row=0, column=10, padx=10)

# Poista tuote 
del_frame = tk.Frame(root)
del_frame.pack(pady=10)

# DROPDOWN MENU
ttk.Label(del_frame, text="Tyyppi").grid(row=0, column=0)
combo = ttk.Combobox(del_frame, values=["Tietokone", "Komponentti"], width=15)
combo.grid(row=0, column=1)
combo.current(0)

# id
ttk.Label(del_frame, text="Id").grid(row=0, column=2)
id_entry = ttk.Entry(del_frame, width=15)
id_entry.grid(row=0, column=3)
# Button
btn = ttk.Button(del_frame, text="Poista")
btn.grid(row=0, column=6, padx=10)

# päivitettävän


pävitä_frame = tk.Frame(root)
pävitä_frame.pack(pady=10)

ttk.Label(pävitä_frame, text="Tyyppi").grid(row=0, column=0)
combo = ttk.Combobox(pävitä_frame, values=["Tietokone", "Komponentti"], width=15)
combo.grid(row=0, column=1)
combo.current(0)

ttk.Label(pävitä_frame, text="Nimi").grid(row=0, column=2)
nimi_entry = ttk.Entry(pävitä_frame, width=15)
nimi_entry.grid(row=0, column=3)


ttk.Label(pävitä_frame, text="UusiHinta").grid(row=0, column=6)
uusihinta_entry = ttk.Entry(pävitä_frame, width=10)
uusihinta_entry.grid(row=0, column=7)

ttk.Label(pävitä_frame, text="UusiMäärä").grid(row=0, column=8)
uusimaara_entry = ttk.Entry(pävitä_frame, width=10)
uusimaara_entry.grid(row=0, column=9)

ttk.Button(pävitä_frame, text="Pävitä").grid(row=0, column=10, padx=10)


def sulje_ohjelma():
    root.destroy()   # closes the window + ends program

btn = tk.Button(root, text="Sulje", command=sulje_ohjelma)
btn.pack(pady=20)

root.mainloop()