import paho.mqtt.publish as publish
import psutil

# Definir las variables para la comunicación con ThingSpeak
channel_ID = "2560312"  # Reemplazar con el ID de tu canal ThingSpeak
mqtt_host = "mqtt3.thingspeak.com"
mqtt_client_ID = "JwETAzQXDRg0DxsiODQlCCg"  # Reemplazar con tu ID de cliente MQTT
mqtt_username = "JwETAzQXDRg0DxsiODQlCCg"  # Reemplazar con tu nombre de usuario MQTT
mqtt_password = "LUxPl3UJALswHx0VOxSU5T/x"  # Reemplazar con tu contraseña MQTT

# Definir el tipo de conexión y el puerto
t_transport = "websockets"
t_port = 80

# Crear el tema MQTT
topic = "channels/" + channel_ID + "/publish"

# Ejecutar el bucle principal
while True:
    cpu_percent = 80
    ram_percent = 90
    payload = "field1=" + str(cpu_percent) + "&field2=" + str(ram_percent)
    try:
        publish.single(topic, payload, hostname=mqtt_host, transport=t_transport, port=t_port, client_id=mqtt_client_ID, auth={'username': mqtt_username, 'password': mqtt_password})
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
