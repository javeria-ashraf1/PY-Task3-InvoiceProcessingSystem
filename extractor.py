import os
import pdfplumber

from database import insert_invoice
from logger import write_log
from config import INVOICE_FOLDER


def process_invoices():

    files = os.listdir(INVOICE_FOLDER)

    if len(files) == 0:
        print("\nNo PDF invoices found inside invoices folder.")
        return

    processed = 0

    for file in files:

        if file.endswith(".pdf"):

            path = os.path.join(INVOICE_FOLDER, file)

            try:

                with pdfplumber.open(path) as pdf:

                    text = ""

                    for page in pdf.pages:
                        text += page.extract_text() or ""

                invoice_number = file.replace(".pdf", "")
                company = "Unknown Company"
                amount = 0
                date = "Not Available"

                for line in text.split("\n"):

                    if "Invoice" in line:
                        invoice_number = line

                    if "Total" in line:
                        try:
                            amount = float(line.split()[-1])
                        except:
                            pass

                    if "Date" in line:
                        date = line

                insert_invoice(
                    invoice_number,
                    company,
                    amount,
                    date
                )

                write_log(f"Processed {file}")

                processed += 1

            except Exception as e:

                write_log(str(e))

    print("\n================================")
    print("Invoice Processing Completed")
    print("Processed Files :", processed)
    print("================================")