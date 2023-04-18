from machine import Pin
import network, socket
import time

try:
    from secrets import secrets
except ImportError:
    print("WiFi info is kept in secrets.py!")
    raise

print('Running')

#IO config part

button_white = Pin(27, Pin.IN, Pin.PULL_UP)
button_yellow = Pin(28, Pin.IN, Pin.PULL_UP)
button_green = Pin(29, Pin.IN, Pin.PULL_UP)
button_blue = Pin(12, Pin.IN, Pin.PULL_UP)
button_red = Pin(13, Pin.IN, Pin.PULL_UP)

led_white = Pin(18, Pin.OUT)
led_yellow = Pin(25, Pin.OUT)
led_green = Pin(15, Pin.OUT)
led_blue = Pin(16, Pin.OUT)
led_red = Pin(17, Pin.OUT)

buttons = [button_white, button_yellow, button_green, button_blue, button_red]
leds = [led_white, led_yellow, led_green, led_blue, led_red]
#list of hue & saturation values for white, yellow, green, blue, red
colors = [[0,0 ], [30, 100], [120, 100], [240, 100], [0, 100]]

# webclient portion

PORT = 3000
HOST = "192.168.1.100"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets["ssid"], secrets["password"])

print("WiFi Connected ", wlan.ifconfig())
addr = socket.getaddrinfo(HOST, PORT)[0][4]
print(addr)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send_command(hue, sat):
    client.connect(addr)
    client.settimeout(3.0)
    client.send("GET /?command=1&hue=%s&saturation=%s HTTP/1.1\r\nHost: %s\r\n\r\n"%(hue, sat,HOST))
    #print(client.recv(1024))
    client.close()

# main loop

while True:
    for button in buttons:
        if not button.value():
            i = buttons.index(button)
            print(leds[i])
            leds[i].value(True)
            send_command(*colors[i])

            while not button.value():
                pass
            leds[i].value(False)
    time.sleep(0.05)
