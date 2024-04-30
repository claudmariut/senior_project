# File with different functions to retrieve entities id based on user searches.
import entitiesDB
import os
from tinydb import TinyDB, Query
import lightSwitchRESTAPI

def search_entities_by_domain(domain, db):
    # Initialize an empty list to store matching entity IDs
    matching_entity_ids = []

    # Query the database for entries with the specified entity_type
    Entity = Query()
    results = db.search(Entity.domain == domain)

    # Extract the entity IDs from the results
    for entry in results:
        matching_entity_ids.append(entry["entity_id"])

    return matching_entity_ids

def main():
    path = "entities_db.json"
    # Check if Database exists first
    if not os.path.exists(path):
        entitiesDB.main()
    else:
        db = TinyDB(path)
        entities = db.all()

        # Extract unique domains
        domains = set(entity['domain'] for entity in entities)
        domain_list = list(domains)

        # Create dictionary for selection helper (domains)
        entity_dictionary = {}
        for i in range(len(domains)):
            entity_dictionary[i + 1] = domain_list[i]

        # Prompt for user selection (Simulating phone drop-down menu)
        print("Select one type of entity: (1 - {})".format(len(domain_list)))
        for key, value in entity_dictionary.items():
            print("{}: {}".format(key, value))
        sel = input()

        # Call function to return all entities of the selected type.
        entities_of_domain = search_entities_by_domain(entity_dictionary[int(sel)], db)

        # Create dictionary for selection helper (entities id)
        entity_id_dict = {}
        for i in range(len(entities_of_domain)):
            entity_id_dict[i + 1] = entities_of_domain[i]

        # Prompt for user selection (Simulating phone drop-down menu)
        print("Select one entity: (1 - {})".format(len(entities_of_domain)))
        for key, value in entity_id_dict.items():
            print("{}: {}".format(key, value))
        sel = input()

        # Execute toggle service on light (assuming light type for exper)
        lightSwitchRESTAPI.toggle(entity_id_dict[int(sel)])

        db.close()

main()
