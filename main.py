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

M1_up = Pin(16,Pin.OUT)
M2_up = Pin(17,Pin.OUT)
M3_up = Pin(18,Pin.OUT)
M4_up = Pin(5,Pin.OUT)



def web_page():
  if M1_forward.value() & M2_forward.value() & M3_forward.value() & M4_forward.value() == 1:
    gpio_state="Forward"
  elif M1_backward.value() & M2_backward.value() & M3_backward.value() & M4_backward.value() ==1:
    gpio_state="Backward"
  elif M1_forward.value() & M3_forward.value() & M2_backward.value() & M4_backward.value() ==1:
    gpio_state="Right"
  elif M1_backward.value() & M3_backward.value() & M2_forward.value() & M4_forward.value() ==1:
    gpio_state="Left"
  elif  M1_forward.value() & M1_backward.value() & M2_backward.value() & M2_forward.value() & M3_backward.value() & M3_forward.value() & M4_backward.value() & M4_forward.value() == 0:
    gpio_state="Stop"
  elif M1_up.value() & M2_up.value() == 1:
    gpio_state="FrontUP"
  elif M3_up.value() & M4_up.value() == 1:
    gpio_state="BackUP"
  elif M1_up.value() == 1:
    gpio_state="FrontLeftUp"
  elif M2_up.value() ==1 :
    gpio_state="FronRightUp"
  elif M3_up.value() ==1 :
    gpio_state="BackLeftUp"
  elif M4_up.value() == 1:
    gpio_state="BackRightUp"
  elif M3_up.value() & M4_up.value() == 0:
    gpio_state="BackDown"
  elif M1_up.value() & M2_up.value() == 0:
    gpio_state="FrontDown"
  elif M1_up.value() == 0:
    gpio_state="FrontLeftDown"
  elif M2_up.value() ==0 :
    gpio_state="FronRightDown"
  elif M3_up.value() ==0 :
    gpio_state="BackLeftDown"
  elif M4_up.value() == 0:
    gpio_state="BackRightDown"
    
  html = """<html>
<head>
<style>
.button {
  border: none;
  color: white;
  padding: 16px 120px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 2px 4px;
  transition-duration: 0.4s;
  cursor: pointer;
}

.buttony {
  border: none;
  color: white;
  padding: 64px 16px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 2px 4px;
  transition-duration: 0.4s;
  cursor: pointer;
}
.buttonx {
  border: none;
  color: white;
  padding: 32px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 2px 4px;
  transition-duration: 0.4s;
  cursor: pointer;
}
.buttons {
  border: none;
  color: white;
  padding: 20px 26px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 2px 4px;
  transition-duration: 0.4s;
  cursor: pointer;
}

.button1 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button1:hover {
  background-color: #008CBA;
  color: white;
}

.button2 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button2:hover {
  background-color: #008CBA;
  color: white;
}

.button3 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button3:hover {
  background-color: #008CBA;
  color: white;
}
.button4 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button4:hover {
  background-color: #008CBA;
  color: white;
}

}
.button5 {
  background-color: white;
  color: black;
  border: 2px solid #ff0000;
}

.button5:hover {
  background-color: #ff0000;
  color: white;
}
}
.button6 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button6:hover {
  background-color: #008CBA;
  color: white;
}

}
.button7 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button7:hover {
  background-color: #008CBA;
  color: white;
}

}
.button8 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button8:hover {
  background-color: #008CBA;
  color: white;
}
}
.button9 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button9:hover {
  background-color: #008CBA;
  color: white;
}

}
.button10 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button10:hover {
  background-color: #008CBA;
  color: white;
}
}
.button11 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button11:hover {
  background-color: #008CBA;
  color: white;
}
}
.button12 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button12:hover {
  background-color: #008CBA;
  color: white;
}
}
.button13 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button13:hover {
  background-color: #008CBA;
  color: white;
}
}
.button14 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button14:hover {
  background-color: #008CBA;
  color: white;
}
}
.button15 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button15:hover {
  background-color: #008CBA;
  color: white;
}
}
.button16 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button16:hover {
  background-color: #008CBA;
  color: white;
}
}
.button17 {
  background-color: white;
  color: black;
  border: 2px solid #008CBA;
}

.button17:hover {
  background-color: #008CBA;
  color: white;
}


</style>
</head>
<body>
<p>GPIO state: <strong>""" + gpio_state + """</strong></p>
<a href="/?solup"><button class="buttonx button6">LeftUPP</button></a>
<a href="/?soldown"><button class="buttonx button7">LeftDWN</button></a>
<a href="/?forward"><button class="buttony button1">Forwardd</button></a>
<a href="/?sagup"><button class="buttonx button8">RightUP</button></a>
<a href="/?sagdown"><button class="buttonx button9">RightDW</button></a>
<a href="/?frontup"><button class="buttony button14">FrontUP</button></a>
<a href="/?frontdown"><button class="buttony button17">FrontDown</button></a>
<a href="/?left"><br><button class="button button3">Leftt</button></a>
<a href="/?stop"><button class="buttons button5">Stop</button></a>
<a href="/?right"><button class="button button4">Right</button></br></a>
<a href="/?soleftupback"><button class="buttonx button10">LeftUPP</button></a>
<a href="/?soleftdownback"><button class="buttonx button11">LeftDWN</button></a>
<a href="/?backward"><button class="buttony button2">Backward</button></a>
<a href="/?saupback"><button class="buttonx button12">RightUP</button></a>
<a href="/?sadownback"><button class="buttonx button13">RightDW</button></a>
<a href="/?backup"><button class="buttony button15">BackUP</button></a>
<a href="/?arkadown"><button class="buttony button16">BackDown</button></a>


</body>
</html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.37', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  forwardd = request.find('/?forward')
  backwardd = request.find('/?backward')
  right = request.find('/?right')
  left = request.find('/?left')
  stop = request.find('/?stop')
  leftup = request.find('/?solup')
  leftdown = request.find('/?soldown')
  rightup = request.find('/?sagup')
  rightdown = request.find('/?sagdown')
  frontup = request.find('/?frontup')
  leftupback = request.find('/?soleftupback')
  leftdownback = request.find('/?soleftdownback')
  rightupback = request.find('/?saupback')
  rightdownback = request.find('/?sadownback')
  backup = request.find('/?backup')
  backdown = request.find('/?arkadown')
  frontdown = request.find('/?frontdown')
  if forwardd == 6:
    print('Forward')
    M1_forward.value(1)
    M1_backward.value(0)
    M2_forward.value(1)
    M2_backward.value(0)
    M3_forward.value(1)
    M3_backward.value(0)
    M4_forward.value(1)
    M4_backward.value(0)
  if backwardd == 6:
    print('Backward')
    M1_forward.value(0)
    M1_backward.value(1)
    M2_forward.value(0)
    M2_backward.value(1)
    M3_forward.value(0)
    M3_backward.value(1)
    M4_forward.value(0)
    M4_backward.value(1)
  if right == 6:
    M1_forward.value(1)
    M1_backward.value(0)
    M2_forward.value(0)
    M2_backward.value(1)
    M3_forward.value(1)
    M3_backward.value(0)
    M4_forward.value(0)
    M4_backward.value(1)
  if left == 6:
    M1_forward.value(0)
    M1_backward.value(1)
    M2_forward.value(1)
    M2_backward.value(0)
    M3_forward.value(0)
    M3_backward.value(1)
    M4_forward.value(1)
    M4_backward.value(0)
  if stop == 6:
    M1_forward.value(0)
    M1_backward.value(0)
    M2_forward.value(0)
    M2_backward.value(0)
    M3_forward.value(0)
    M3_backward.value(0)
    M4_forward.value(0)
    M4_backward.value(0)
  if leftup == 6:
    M1_up.value(1)
  if leftdown == 6:
    M1_up.value(0)
  if rightup == 6:
    M2_up.value(1)
  if rightdown == 6:
    M2_up.value(0)
  if frontup == 6:
    M1_up.value(1)
    M2_up.value(1)
  if leftupback == 6:
    M3_up.value(1)
  if leftdownback == 6:
    M3_up.value(0)
  if rightupback == 6:
    M4_up.value(1)
  if rightdownback == 6:
    M4_up.value(0)
  if backup == 6:
    M3_up.value(1)
    M4_up.value(1)
  if frontdown == 6:
    M1_up.value(0)
    M2_up.value(0)
  if backdown == 6:
    M3_up.value(0)
    M4_up.value(0)
  
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()













