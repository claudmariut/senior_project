import requests
import time

# HA IP Address and TOKEN
HA_API_BASE_URL = "http://raspberrypi.local:8123/api"
HA_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIwMmQ3YWJlNTA4Yzc0MmMwYTc1Yjc0ZDViNTliM2RhYSIsImlhdCI6MTcwOTE0NzQ5NSwiZXhwIjoyMDI0NTA3NDk1fQ.hmawkNeOI0UjnMkFRgoCshv8qmxuTJMy1NNsbnjHuDM"

# Function to toggle a light on
def turn_on(entity_id):
    headers = {
        "Authorization": f"Bearer {HA_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    data = {
        "entity_id": entity_id,
    }

    url = f"{HA_API_BASE_URL}/services/light/turn_on"

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Switch {entity_id} turned on successfully.")
    else:
        print(f"Failed to toggle switch {entity_id}. Status code: {response.status_code}, Response: {response.text}")

def turn_off(entity_id):
    headers = {
        "Authorization": f"Bearer {HA_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    data = {
        "entity_id": entity_id,
    }

    url = f"{HA_API_BASE_URL}/services/light/turn_off"

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Switch {entity_id} turned off successfully.")
        time.sleep(2)
    else:
        print(f"Failed to toggle switch {entity_id}. Status code: {response.status_code}, Response: {response.text}")

def toggle(entity_id):
    headers = {
        "Authorization": f"Bearer {HA_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    data = {
        "entity_id": entity_id,
    }

    url = f"{HA_API_BASE_URL}/services/light/toggle"

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Switch {entity_id} turned off successfully.")
        time.sleep(2)
    else:
        print(f"Failed to toggle switch {entity_id}. Status code: {response.status_code}, Response: {response.text}")


