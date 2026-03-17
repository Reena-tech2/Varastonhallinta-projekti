import sqlite3

# Connect to your database
conn = sqlite3.connect("varasto.db")
cur = conn.cursor()

# --- Tietokone table fix ---
cur.execute("ALTER TABLE tietokone RENAME TO tietokone_old;")

cur.execute("""
CREATE TABLE tietokone (
    id INTEGER PRIMARY KEY,
    merkki TEXT,
    malli TEXT,
    hinta REAL,
    maara INTEGER
);
""")

cur.execute("""
INSERT INTO tietokone (id, merkki, malli, hinta, maara)
SELECT id, merkki, malli, CAST(hinta AS REAL), maara
FROM tietokone_old;
""")

cur.execute("DROP TABLE tietokone_old;")

# --- Komponentti table fix ---
cur.execute("ALTER TABLE komponentti RENAME TO komponentti_old;")

cur.execute("""
CREATE TABLE komponentti (
    id INTEGER PRIMARY KEY,
    nimi TEXT,
    hinta REAL,
    maara INTEGER
);
""")

cur.execute("""
INSERT INTO komponentti (id, nimi, hinta, maara)
SELECT id, nimi, CAST(hinta AS REAL), maara
FROM komponentti_old;
""")

cur.execute("DROP TABLE komponentti_old;")

conn.commit()
conn.close()

print("Tables fixed: 'hinta' is now REAL in both tables.")