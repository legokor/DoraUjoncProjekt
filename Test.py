import threading
import time

from MqttSender import MqttSender


class Test:
    def runTest(self):
        testSendProcess = threading.Thread(target=self.test1)
        testSendProcess.start()

    def test1(self):
        sender = MqttSender("mqtt_connect_sender")
        sender.run()
        num = 100
        while True:
            sender.send(f"{num}")
            num -= 5
            if num < 50:
                num = 100
            time.sleep(2)
