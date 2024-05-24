import requests
import json

# URL del endpoint de ThingSpeak
url = "https://api.thingspeak.com/channels/2560312/bulk_update.json"

# Leer el archivo JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Enviar datos a ThingSpeak
response = requests.post(url, json=data)

# Verificar la respuesta
if response.status_code == 200:
    print(response.json())
else:
    print(response.json())
