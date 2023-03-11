# Simple HTTP client example.

import network, socket
from machine import Pin
import time

# AP info
SSID='' # Network SSID
KEY=''  # Network key

# Use the actual port and host ip from your Express server
PORT = 80
HOST = "192.168.1.100"

# Init wlan module and connect to network
print("Trying to connect. Note this may take a while...")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, KEY)

# We should have a valid IP now via DHCP
print("WiFi Connected ", wlan.ifconfig())

# Get addr info via DNS
addr = socket.getaddrinfo(HOST, PORT)[0][4]
print(addr)

# Create a new socket and connect to addr
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

# Set timeout
client.settimeout(3.0)

# Send HTTP request and recv response
client.send("GET /node/?command=on HTTP/1.1\r\nHost: %s\r\n\r\n"%(HOST))
print(client.recv(1024))

# Close socket
client.close()


led = Pin(6, Pin.OUT)
button = Pin(21, Pin.IN)

led.value(0)
logic_state = True

def toggle_state(state):
    current_state = not state
    if current_state == True:
        command = 'on'
    else:
        command = 'off'
    print(command)
    client.connect(addr)
    client.settimeout(3.0)
    client.send("GET /node/?command=%s HTTP/1.1\r\nHost: %s\r\n\r\n"%(command,HOST))
    print(client.recv(1024))
    client.close()
    time.sleep(1)
    return current_state


while True:

  button_state = button.value()
  if button_state == True:     # if push_button pressed
      led.value(1)             # led will turn ON
      logic_state = toggle_state(logic_state) #call the url to toggle the Smart Plug
  else:                       # if push_button not pressed
      led.value(0)             # led will turn OFF