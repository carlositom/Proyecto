#Importamos librerias
import paho.mqtt.client as mqtt
import time

#Pedimos valores iniciales
ip = input("ip: ")
user = input("Username: ")
topic = input("Topico: ")
port = 1883

#Definimos funciones callback
def on_connect(client,userdata,flags,rc):
    print("Conexion Exitosa")
def on_message(client,userdata,message):
    msg = str(message.payload.decode("utf-8"))
    print(msg)

#Agregamos funciones del cliente mqtt
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#Conectamos el cliente
client.connect(ip,port)

#Agregamos pausa
time.sleep(1)

#Comenzamos loop
client.loop_start()

#Nos suscribimos al topico
client.subscribe(topic)

#Agregamos pausa
time.sleep(1)

#Agregamos funcionalidad para mandar mensajes
while True:
    msg = input("")
    chat = user + ": " + msg
    client.publish(topic,chat)
    #Stop para terminar con el loop
    if msg == "Stop" or msg == "stop":
        break

#Desconexion del cliente
client.disconnect()
client.loop_stop()

