# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from datetime import datetime
import paho.mqtt.subscribe as subscribe
import json

try:
    pass
except :
    print("Error de conexión")
while True:
    try:
        m = subscribe.simple(topics=['#'],
                             hostname="192.168.0.250",
                             port=1883,
                             auth={
                                 'username': "cif-lora-bogota",
                                 'password': "NNSXS.U647VXOIMRH3BECSCGARXK2RSUPNDIUMTK2QEZA.XRBGL6VQKVKHHYK3AT2ZUCWXUV662WSAI5Z4UOHQ3M3BYDYXPLVA"},
                            msg_count=10)
        for a in m:
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            print(f"Topic: {a.topic}")
            print()
            payload = a.payload.decode("utf-8")
            jsonData = f"{payload}"
            jsonToPython = json.loads(jsonData)
            if f"{a.topic}"[-3:] == "/up":
                a, b, c, d, e = jsonToPython['uplink_message']['decoded_payload']['bytes']
                print(f"{(a + b * 256 + c * 65536 + d * 16777216)/10} Kw/h")
                print(jsonToPython['uplink_message']['decoded_payload']['bytes'])
                print()
                #print(jsonToPython)
                print()
                time.sleep(2)
            else:
                print(jsonToPython)
                print()
    except:
        print("Error de lectura")
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))