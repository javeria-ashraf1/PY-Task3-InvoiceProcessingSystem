import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_PATH = os.path.join(BASE_DIR, "database", "invoice.db")

INVOICE_FOLDER = os.path.join(BASE_DIR, "invoices")

EXPORT_FOLDER = os.path.join(BASE_DIR, "exports")

REPORT_FOLDER = os.path.join(BASE_DIR, "reports")

LOG_FOLDER = os.path.join(BASE_DIR, "logs")

LOG_FILE = os.path.join(LOG_FOLDER, "system.log")