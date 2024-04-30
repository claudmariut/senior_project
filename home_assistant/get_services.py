import requests


# HA IP Address and TOKEN
HA_API_BASE_URL = "http://homeassistant.local:8123/api"
HA_ACCESS_TOKEN = "YOUR_TOKEN_API_KEY"

# Function to get services from HA Server
def get_services():
    headers = {
        "Authorization": f"Bearer {HA_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    url = f"{HA_API_BASE_URL}/services"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Returns a list of domains with all services associated with that domain.
        return response.json()
    else:
        print(f"Failed to connect! .Status code: {response.status_code}, Response: {response.text}")

# Function to format each service provided by each domain to only display service type, name of service and description.
def format_entry(entry):
    # Iterate through the services dictionary of the entry
    for service_name, service_info in entry['services'].items():
        # Keep only 'name' and 'description' keys for each service
        entry['services'][service_name] = {'name': service_info['name'], 'description': service_info['description']}
    return entry


def main():
    response = get_services()
    formatted_response = []
    for r in response:
        formatted_response.append(format_entry(r))
    return formatted_response
