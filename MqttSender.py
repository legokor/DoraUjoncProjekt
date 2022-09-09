import json

import paho.mqtt.client as mqtt


class MqttSender:
    def __init__(self, name):
        self.name = name
        self.data = self.initFile(name)

        self.client = self.connect()

        self.running = False

    def connect(self):
        client = mqtt.Client(self.name)
        client.username_pw_set(self.data["username"], self.data["password"])
        client.on_connect = self.on_connect
        try:
            client.connect(self.data["broker"], self.data["port"])
        except Exception as e:
            print(f"Failed to connect to MQTT Broker: {e}")
        return client

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Failed to connect to MQTT Broker, return code {rc}")

    def run(self):
        if not self.running:
            print("-------MQTT SENDER STARTED-------")


    def stop(self):
        if self.running:
            print("-------MQTT SENDER STOPPED-------")

    def send(self, message):
        result = self.client.publish(self.data["topic"], message)
        status = result[0]
        if status == 0:
            pass
            # print(f"Send `{message}` to topic `{self.data['topic']}`")
        else:
            print(f"Failed to send message: '{message}' to topic '{self.data['topic']}'")

    def initFile(self, name) -> dict:
        try:
            with open(f"./{name}.json") as f:
                rec = json.load(f)
        except:
            rec = None
        return rec
