## Express Server to control a TP-Link Smart Plug

Prototype using the HTTP client example, a simple Express server and this [NPM Package](https://github.com/konsumer/tplink-lightbulb) to control a TP-Link Smart Bulb

The Arduino RP 2040 Connect is using five Arcade Buttons with embeded LED lights (with resistors  included). 

### Installing and running

```bash
git clone https://github.com/intGus/light-server.git
cd light-server
npm install
node index.js
```

Python code (main.py) for the Arduino Nano can be found in the /Arduino directory

For the connections inside the box I used this [tutorial](https://learn.adafruit.com/arcade-button-control-box)

### I'm using the following:
<sup>(includes paid links)</sup>

+ Arduino RP2040 Connect - It can be done with a Raspberry Pico W using the appropiate libraries
+ Arcade buttons - Adafruit sells individual buttons if you want different colors
+ A TP-Link Smart Bulb - I'm using the KL125
+ NodeJS with npm for the Express server (I'm using a Raspberry Pi 4 but any computer with NodeJS will work)
