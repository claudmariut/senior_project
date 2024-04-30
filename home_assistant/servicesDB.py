import get_services
from tinydb import TinyDB

def main():
    # Retrieve entities and update database
    services = get_services.main()
    db = TinyDB("services_db.json")

    # Dump contents of database simulating an update.
    db.truncate()

    # Insert entries into database
    for domain in services:
        db.insert(domain)

    db.close()

