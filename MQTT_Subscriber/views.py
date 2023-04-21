import random
from paho.mqtt import client as mqtt_client
from django.shortcuts import render
import datetime
import time

data = 'Empty'


def datacal():
    broker = 'broker.emqx.io'
    port = 1883
    topic = "python/mqtt"
    # generate client ID with pub prefix randomly
    client_id = f'python-mqtt-{random.randint(0, 1000)}'
    username = 'emqx'
    password = 'public'

    def connect_mqtt() -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(client_id)
        client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.connect(broker, port)
        return client

    def subscribe(client: mqtt_client):
        def on_message(client, userdata, msg):
            global data
            data = msg.payload.decode('utf8')
            # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            # print("Position = ", data)
            print(data)

        client.subscribe(topic)
        client.on_message = on_message

    def run():
        client = connect_mqtt()
        subscribe(client)
        client.loop_forever()

    if __name__ == '__main__':
        run()


datacal()


def output(request):
    datacal()
    now = datetime.datetime.now()
    person = "MQTT Results" + data
    context = {
        'person': person,
        'current_date': now.date(),
    }
    return render(request, 'mytemp.html', context)
