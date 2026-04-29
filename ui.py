import tkinter as tk
import varastosovellus
import sqlite3
CONN = sqlite3.connect("varasto.db")
cursor = CONN.cursor()
root = tk.Tk()
root.title("Varastohallinta sovellus")
root.geometry("600x500")
text_box = tk.Text(root, height=20, width=70)
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
btn.pack(pady=60)



root.mainloop()