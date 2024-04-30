# File with different functions to retrieve entities id based on user searches.
import entitiesDB
import servicesDB
import callServices
import os
from tinydb import TinyDB, Query

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

def search_services_by_domain(domain, db):
    services_list = []

    query = Query()
    entries = db.search(query.domain == domain)

    # Iterate through each entry in the query result
    for entry in entries:
        for service_name, service_data in entry['services'].items():
            service_dict = {'name': service_data['name'], 'description': service_data['description']}
            services_list.append({service_name: service_dict})

    return services_list

def select_domain(entities):
    # Extract unique domains
    domains = set(entity['domain'] for entity in entities)
    domain_list = list(domains)

    # Create dictionary for selection helper (domains)
    entity_dictionary = {}
    for i in range(len(domains)):
        entity_dictionary[i + 1] = domain_list[i]

    # Prompt for user selection (Simulating phone drop-down menu)
    print("Select one domain: (1 - {})".format(len(domain_list)))
    for key, value in entity_dictionary.items():
        print("{}: {}".format(key, value))
    sel = input()

    return entity_dictionary[int(sel)]

def select_entity(domain, db_ent):
    # Call function to return all entities of the selected type.
    entities_of_domain = search_entities_by_domain(domain, db_ent)

    # Create dictionary for selection helper (entities id)
    entity_id_dict = {}
    for i in range(len(entities_of_domain)):
        entity_id_dict[i + 1] = entities_of_domain[i]

    # Prompt for user selection (Simulating phone drop-down menu)
    print("Select one or more entities separated by a comma: (1 - {})".format(len(entities_of_domain)))
    for key, value in entity_id_dict.items():
        print("{}: {}".format(key, value))
    sel = input()

    entities = []
    for entity in sel.split(","):
        entities.append(entity_id_dict[int(entity)])

    return ",".join(entities)

def select_service(domain, db_ser):
    # Call function to return list of services for that particular domain
    domain_services = search_services_by_domain(domain, db_ser)

    # Create dictionary for selection helper (domain services)
    domain_services_dict = {}
    for i in range(len(domain_services)):
        domain_services_dict[i + 1] = domain_services[i]

    # Prompt for user selection (Simulating phone drop-down menu)
    print("Select one service: (1 - {})".format(len(domain_services)))
    for key, value in domain_services_dict.items():
        print("{}: {}".format(key, value))
    sel = input()

    return next(iter(domain_services_dict[int(sel)].keys()))

def main():
    path_ent = "entities_db.json"
    path_ser = "services_db.json"
    # Check if Database exists first
    if not os.path.exists(path_ent):
        entitiesDB.main()
    elif not os.path.exists(path_ser):
        servicesDB.main()

    db_ent = TinyDB(path_ent)
    entities = db_ent.all()
    db_ser = TinyDB(path_ser)
    services = db_ser.all()

    # Call function to select domain, entity_id and service
    domain = select_domain(entities)
    entity_id = select_entity(domain, db_ent)
    service = select_service(domain, db_ser)

    # Execute Service, we could also prompt the user to associate this service to a gesture.
    callServices.call_service(entity_id, domain, service)

    # Close Databases
    db_ent.close()
    db_ser.close()

main()
