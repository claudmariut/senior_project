import requests
import time

# HA IP Address and TOKEN
HA_API_BASE_URL = "http://homeassistant.local:8123/api"
HA_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI5ZDY0ZmMzYWU2ZDY0ZTQ5YjMwMWMzZDgxNTc3ZDYzMiIsImlhdCI6MTcxMzIxMTA3OSwiZXhwIjoyMDI4NTcxMDc5fQ.2MKu1g03LlhzOHHOgFwJdeW78G0Vsv_fE34MQGYqKFI"

# Function to call a service
def call_service(entity_id, domain, service_call):
    headers = {
        "Authorization": f"Bearer {HA_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    data = {
        "entity_id": entity_id
    }


    url = f"{HA_API_BASE_URL}/services/{domain}/{service_call}"

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Service executed succesfully!")
    else:
        print(f"Fail to execute service. Status code: {response.status_code}, Response: {response.text}")
