#!/usr/bin/env python
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import threading
import random

import logging

temp = 30.0

def getit():
    global temp
    threading.Timer(0.25, printit).start()
    tmp = random.randint(0,100)+random.randint(0,100)+random.randint(0,100)
    if tmp >+ 150:
        temp += tmp/3000
        rq = client.write_coils(1, [True]*8)
        rr = client.read_coils(1,8)
    else:
        temp -= (tmp+100)/3000
        rq = client.write_coils(1, [False]*8)
        rr = client.read_coils(1,8)

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


client = ModbusClient('172.20.0.2', port=502)

client.connect()

print('ModbusClient started')

rr = client.read_coils(1, 1, unit=0x02)

getit()

client.close()
