import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

from config import DATABASE_PATH, EXPORT_FOLDER, REPORT_FOLDER


def export_csv():

    conn = sqlite3.connect(DATABASE_PATH)

    data = pd.read_sql_query(
        "SELECT * FROM invoices",
        conn
    )

    os.makedirs(EXPORT_FOLDER, exist_ok=True)

    path = os.path.join(
        EXPORT_FOLDER,
        "Invoice_Report.csv"
    )

    data.to_csv(path, index=False)

    conn.close()

    print("\nCSV Report Generated Successfully!")
    print(path)


def export_excel():

    conn = sqlite3.connect(DATABASE_PATH)

    data = pd.read_sql_query(
        "SELECT * FROM invoices",
        conn
    )

    os.makedirs(EXPORT_FOLDER, exist_ok=True)

    path = os.path.join(
        EXPORT_FOLDER,
        "Invoice_Report.xlsx"
    )

    data.to_excel(path, index=False)

    conn.close()

    print("\nExcel Report Generated Successfully!")
    print(path)


def generate_graph():

    conn = sqlite3.connect(DATABASE_PATH)

    data = pd.read_sql_query(
        "SELECT * FROM invoices",
        conn
    )

    conn.close()

    if len(data) == 0:
        print("\nNo data available.")
        return

    plt.figure(figsize=(6,4))

    plt.bar(
        data["invoice_number"],
        data["amount"]
    )

    plt.title("Invoice Amounts")

    plt.xlabel("Invoice")

    plt.ylabel("Amount")

    os.makedirs(REPORT_FOLDER, exist_ok=True)

    path = os.path.join(
        REPORT_FOLDER,
        "Invoice_Graph.png"
    )

    plt.savefig(path)

    plt.show()

    print("\nGraph Generated Successfully!")