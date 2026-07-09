from database import create_database
from extractor import process_invoices
from report_generator import (
    export_csv,
    export_excel,
    generate_graph
)

create_database()

while True:

    print("\n" + "=" * 55)
    print(" SMART INVOICE PROCESSING SYSTEM")
    print("=" * 55)

    print("1. Process PDF Invoices")
    print("2. Export CSV Report")
    print("3. Export Excel Report")
    print("4. Generate Graph")
    print("5. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        process_invoices()

    elif choice == "2":
        export_csv()

    elif choice == "3":
        export_excel()

    elif choice == "4":
        generate_graph()

    elif choice == "5":
        print("\nThank you!")
        break

    else:
        print("\nInvalid Choice.")