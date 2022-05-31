try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'FiberHGW_TP959C_2.4GHz'
password = 'jPDhjhXr'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

M1_forward = Pin(26, Pin.OUT)
M1_backward = Pin(27,Pin.OUT)
M2_forward = Pin(12,Pin.OUT)
M2_backward =Pin(14,Pin.OUT)
M3_forward = Pin(25,Pin.OUT) 
M3_backward = Pin(33,Pin.OUT)
M4_forward = Pin(32,Pin.OUT)
M4_backward = Pin(13,Pin.OUT)
