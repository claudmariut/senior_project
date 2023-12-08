import requests

# Replace these variables with your Home Assistant details
HA_API_BASE_URL = "http://172.16.0.1:8123/api"
HA_ACCESS_TOKEN = "TOKEN-KEY-HERE"

# Function to toggle a switch
def switchOn(entity_id, turn_on=True):
    headers = {
        "Authorization": f"Bearer {HA_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    data = {
        "entity_id": entity_id,
        "state": "on" if turn_on else "off",
    }

    url = f"{HA_API_BASE_URL}/services/switch/turn_on" if turn_on else f"{HA_API_BASE_URL}/services/switch/turn_off"

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Switch {entity_id} turned {'on' if turn_on else 'off'} successfully.")
    else:
        print(f"Failed to toggle switch {entity_id}. Status code: {response.status_code}, Response: {response.text}")

# Replace "your_switch_entity_id" with the actual entity ID of your switch
switchOn("switch.ihome_ww117_smart_plug_socket_1", turn_on=True)