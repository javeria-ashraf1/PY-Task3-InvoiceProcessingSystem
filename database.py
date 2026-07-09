import sqlite3
from config import DATABASE_PATH

def create_database():

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS invoices(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        invoice_number TEXT,

        company TEXT,

        amount REAL,

        date TEXT

    )
    """)

    conn.commit()

    conn.close()


def insert_invoice(invoice_number, company, amount, date):

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO invoices

    (invoice_number,company,amount,date)

    VALUES(?,?,?,?)

    """,(invoice_number,company,amount,date))

    conn.commit()

    conn.close()