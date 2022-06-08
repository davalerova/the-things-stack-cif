import paho.mqtt.publish as publish
from datetime import datetime
publish.single("v3/cif-lora-bogota/devices/luminaria-bog-002/down/push",
               '{"downlinks":[{"f_port": 2,"frm_payload":"MA==", "confirmed": true, "priority": "NORMAL"}]}',
               hostname="192.168.0.250",
               port=1883,
               auth={'username':"cif-lora-bogota",'password':"NNSXS.U647VXOIMRH3BECSCGARXK2RSUPNDIUMTK2QEZA.XRBGL6VQKVKHHYK3AT2ZUCWXUV662WSAI5Z4UOHQ3M3BYDYXPLVA"})
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))