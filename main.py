def web_page():
  if M1_forward.value() & M2_forward.value() & M3_forward.value() & M4_forward.value() == 1:
    gpio_state="Forward"
  elif M1_backward.value() & M2_backward.value() & M3_backward.value() & M4_backward.value() ==1:
    gpio_state="Backward"
  elif M1_forward.value() & M3_forward.value() & M2_backward.value() & M4_backward.value() ==1:
    gpio_state="Right"
  elif M1_backward.value() & M3_backward.value() & M2_backward.value() & M4_backward.value() ==1:
    gpio_state="Left"
  elif  M1_forward.value() & M1_backward.value() & M2_backward.value() & M2_forward.value() & M3_backward.value() & M3_forward.value() & M4_backward.value() & M4_forward.value() == 0:
    gpio_state="Stop"
  
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



</style>
</head>
<body>
<p>GPIO state: <strong>""" + gpio_state + """</strong></p>
<button class="buttonx button6">LeftUPP</button>
<button class="buttonx button7">LeftDWN</button>
<a href="/?forward"><button class="buttony button1">Forwardd</button></a>
<button class="buttonx button8">RightUP</button>
<button class="buttonx button9">RightDW</button>
<a href="/?left"><br><button class="button button3">Leftt</button></a>
<a href="/?stop"><button class="buttons button5">Stop</button></a>
<a href="/?right"><button class="button button4">Right</button></br></a>
<button class="buttonx button10">LeftUPP</button>
<button class="buttonx button11">LeftDWN</button>
<a href="/?backward"><button class="buttony button2">Backward</button></a>
<button class="buttonx button12">RightUP</button>
<button class="buttonx button13">RightDW</button>





</body>
</html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.40', 80))
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
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()

