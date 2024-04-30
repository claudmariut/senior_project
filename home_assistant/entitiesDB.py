import get_entities
from tinydb import TinyDB

def main():
    # Retrieve entities and update database
    entities = get_entities.main()
    db = TinyDB("entities_db.json")

    # Dump contents of database simulating an update.
    db.truncate()

    # Insert entries into database
    for entity in entities:
        db.insert(entity)

    db.close()

