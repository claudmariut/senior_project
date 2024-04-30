import requests


# HA IP Address and TOKEN
HA_API_BASE_URL = "http://homeassistant.local:8123/api"
HA_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI5ZDY0ZmMzYWU2ZDY0ZTQ5YjMwMWMzZDgxNTc3ZDYzMiIsImlhdCI6MTcxMzIxMTA3OSwiZXhwIjoyMDI4NTcxMDc5fQ.2MKu1g03LlhzOHHOgFwJdeW78G0Vsv_fE34MQGYqKFI"

# Function to get entities from HA Server
def get_entities():
    headers = {
        "Authorization": f"Bearer {HA_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    url = f"{HA_API_BASE_URL}/states"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Returns a list of dictionaries with all entities and their states and attributes
        return response.json()
    else:
        print(f"Failed to connect! .Status code: {response.status_code}, Response: {response.text}")


# Function to format a single dictionary entry
def format_entry(entry):
    # Extract the entity_id and split it by the dot
    entity_id_parts = entry['entity_id'].split('.')

    # Create a new dictionary with the desired format
    formatted_entry = {
        'entity_id': entry['entity_id'],
        'domain': entity_id_parts[0]  # Extract the first part of entity_id
    }
    return formatted_entry


def main():
    response = get_entities()
    formatted_response = []
    for entry in response:
        formatted_response.append(format_entry(entry))
    return formatted_response
