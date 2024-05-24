import json
import requests

# URL del endpoint de ThingSpeak
url = "https://api.thingspeak.com/channels/2560312/feeds.json"  # Reemplaza <channel_id> con el ID de tu canal

# Parámetros de la solicitud GET (opcional)
params = {
    "api_key": "ZB4A4W0YSS4NJ0HZ",  # Si tu canal es privado, necesitas la clave de API de lectura
    "results": 10  # Número de entradas para recuperar (hasta 8000)
}

# Realizar la solicitud GET
response = requests.get(url, params=params)

# Verificar la respuesta
if response.status_code == 200:
    data = response.json()
    print("Datos recuperados con éxito!")
    # Guardar los datos en un archivo JSON
    with open('datosRecuperados.json', 'w') as file:
        json.dump(data, file)
    
    print("Datos guardados en 'datos.json'")
else:
    print("Error al recuperar los datos")
    print(response.status_code)
    print(response.text)