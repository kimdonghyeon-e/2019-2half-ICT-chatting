import time, json, ssl
import paho.mqtt.client as mqtt
import random
from datetime import datetime


ENDPOINT = 'a3kb109oy8xa3g-ats.iot.us-west-2.amazonaws.com'
THING_NAME = 'GameClient1'

sub = 'chatting/1'

def on_connect(mqttc, obj, flags, rc):
        if rc == 0:
                print('connected!!')
                mqttc.subscribe(sub, qos=0)

def on_message(mqttc, obj, msg):
        if msg.topic == sub:
                payload = msg.payload.decode('utf-8')
                j = json.loads(payload)
                if j['sender'] != 'pc1':
                    print(j['sender'],':',j['message'])

mqtt_client = mqtt.Client(client_id=THING_NAME)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.tls_set('C:\Users\b0198\OneDrive\Documents\수업\ICT융합공학\GCT2', certfile='C:\Users\b0198\OneDrive\Documents\수업\ICT융합공학\GCT2',
        keyfile='C:\Users\b0198\OneDrive\Documents\수업\ICT융합공학\GCT2', tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
mqtt_client.connect(ENDPOINT, port=8883)
mqtt_client.loop_start() # threaded network loop

while True:
        test=input()
        now = datetime.now()
        nowtime = '%s-%s-%s %s:%s:%s' % (now.year,now.month,now.day,now.hour,now.minute,now.second)
        payload = json.dumps({'message': test, 'sender':'pc1', 'time':nowtime})
        mqtt_client.publish('chatting/1', payload, qos=1)
