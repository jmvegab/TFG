import paho.mqtt.client as mqtt

# Configuración de la conexión MQTT
mqtt_host = "mqtt3.thingspeak.com"
mqtt_port = 1883
mqtt_api_key = "LUxPl3UJALswHx0VOxSU5T/x"  # API Key para autenticación MQTT
mqtt_channel_id = "2560312"  # Reemplaza con el ID de tu canal ThingSpeak
mqtt_topic = f"channels/{mqtt_channel_id}/publish"

# Función para manejar la conexión MQTT
def on_connect(client, userdata, flags, rc):
    print("Conectado al broker MQTT con resultado: " + mqtt.connack_string(rc))
    # Una vez conectado, publicar el mensaje
    publish_message()

# Función para manejar la publicación exitosa
def on_publish(client, userdata, mid):
    print("Mensaje publicado correctamente.")

# Función para publicar el mensaje
def publish_message():
    # Payload para publicar
    payload = "field1=45&field2=60&field3=75&status=MQTTPUBLISH"
    # Publicar el mensaje en el tema correspondiente
    client.publish(topic=mqtt_topic, payload=payload, qos=0, retain=False)

# Crear un cliente MQTT
client = mqtt.Client()

# Establecer las funciones de callback
client.on_connect = on_connect
client.on_publish = on_publish

# Establecer la API Key como contraseña
client.username_pw_set(username="JwETAzQXDRg0DxsiODQlCCg", password=mqtt_api_key)

# Conectar al broker MQTT
client.connect(mqtt_host, mqtt_port)

# Mantener la conexión activa
client.loop_forever()
