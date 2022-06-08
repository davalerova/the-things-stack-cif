import argparse
import time
import paho.mqtt.publish as publish
from datetime import datetime


parser = argparse.ArgumentParser(description='Enciende o apaga una luminaria')
parser.add_argument('-l', '--luminaria', type=str, help='Código luminaria')
parser.add_argument('-v', '--varias', type=str, help='Código luminaria')
parser.add_argument('-o', '--operacion',
                    type=str,
                    choices=['encender', 'apagar'],
                    default='encender', required=False,
                    help='Operación a realizar con la luminaria')

args = parser.parse_args()
if args.luminaria:
    if args.operacion == 'encender':
        publish.single(f"v3/cif-lora-bogota/devices/luminaria-bog-{args.luminaria}/down/push",
                       '{"downlinks":[{"f_port": 2,"frm_payload":"MQ==", "confirmed": true, "priority": "NORMAL"}]}',
                       hostname="192.168.0.250",
                       port=1883,
                       auth={'username': "cif-lora-bogota",
                             'password': "NNSXS.U647VXOIMRH3BECSCGARXK2RSUPNDIUMTK2QEZA.XRBGL6VQKVKHHYK3AT2ZUCWXUV662WSAI5Z4UOHQ3M3BYDYXPLVA"})
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), args.luminaria, "encender")
    elif args.operacion == 'apagar':
        publish.single(F"v3/cif-lora-bogota/devices/luminaria-bog-{args.luminaria}/down/push",
                       '{"downlinks":[{"f_port": 2,"frm_payload":"MA==", "confirmed": true, "priority": "NORMAL"}]}',
                       hostname="192.168.0.250",
                       port=1883,
                       auth={'username': "cif-lora-bogota",
                             'password': "NNSXS.U647VXOIMRH3BECSCGARXK2RSUPNDIUMTK2QEZA.XRBGL6VQKVKHHYK3AT2ZUCWXUV662WSAI5Z4UOHQ3M3BYDYXPLVA"})
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),args.luminaria, "apagar")
elif args.varias:
    min, max = map(int, args.varias.split(":"))
    if args.operacion == 'encender':
        for i in range(min, max+1):
            if i == min:
                publish.single(f"v3/cif-lora-bogota/devices/luminaria-bog-{str(i).rjust(3, '0')}/down/replace",
                               '{"downlinks":[{"f_port": 2,"frm_payload":"MQ==", "confirmed": true, "priority": "NORMAL"}]}',
                               hostname="192.168.0.250",
                               port=1883,
                               auth={'username': "cif-lora-bogota",
                                     'password': "NNSXS.U647VXOIMRH3BECSCGARXK2RSUPNDIUMTK2QEZA.XRBGL6VQKVKHHYK3AT2ZUCWXUV662WSAI5Z4UOHQ3M3BYDYXPLVA"})
                print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str(i).rjust(3, '0'), "encender")
                time.sleep(0.25)
            else:
                publish.single(f"v3/cif-lora-bogota/devices/luminaria-bog-{str(i).rjust(3, '0')}/down/push",
                               '{"downlinks":[{"f_port": 2,"frm_payload":"MQ==", "confirmed": true, "priority": "NORMAL"}]}',
                               hostname="192.168.0.250",
                               port=1883,
                               auth={'username': "cif-lora-bogota",
                                     'password': "NNSXS.U647VXOIMRH3BECSCGARXK2RSUPNDIUMTK2QEZA.XRBGL6VQKVKHHYK3AT2ZUCWXUV662WSAI5Z4UOHQ3M3BYDYXPLVA"})
                print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str(i).rjust(3, '0'), "encender")
                time.sleep(0.25)



    elif args.operacion == 'apagar':
        for i in range(min, max + 1):
            if i == min:
                publish.single(f"v3/cif-lora-bogota/devices/luminaria-bog-{str(i).rjust(3, '0')}/down/replace",
                               '{"downlinks":[{"f_port": 2,"frm_payload":"MA==", "confirmed": true, "priority": "NORMAL"}]}',
                               hostname="192.168.0.250",
                               port=1883,
                               auth={'username': "cif-lora-bogota",
                                     'password': "NNSXS.U647VXOIMRH3BECSCGARXK2RSUPNDIUMTK2QEZA.XRBGL6VQKVKHHYK3AT2ZUCWXUV662WSAI5Z4UOHQ3M3BYDYXPLVA"})
                print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str(i).rjust(3, '0'), "apagar")
                time.sleep(0.25)
            else:
                publish.single(f"v3/cif-lora-bogota/devices/luminaria-bog-{str(i).rjust(3, '0')}/down/push",
                               '{"downlinks":[{"f_port": 2,"frm_payload":"MA==", "confirmed": true, "priority": "NORMAL"}]}',
                               hostname="192.168.0.250",
                               port=1883,
                               auth={'username': "cif-lora-bogota",
                                     'password': "NNSXS.U647VXOIMRH3BECSCGARXK2RSUPNDIUMTK2QEZA.XRBGL6VQKVKHHYK3AT2ZUCWXUV662WSAI5Z4UOHQ3M3BYDYXPLVA"})
                print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str(i).rjust(3, '0'), "apagar")
                time.sleep(0.25)

        #time.sleep(5)