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

+ [Arduino RP2040 Connect.](https://www.amazon.com/dp/B095J4KFVT?ref_=cm_sw_r_cp_ud_dp_387K0K6BBVZGKR0QMGEA&_encoding=UTF8&tag=intgus-20&linkCode=ur2&linkId=bd27108f0f5c903fb113a58d52f1a4f3&camp=1789&creative=9325) It can be done with a Raspberry Pico W using the appropiate libraries
+ [Arcade buttons.](https://www.amazon.com/dp/B01N11BDX9?psc=1&amp;ref=ppx_yo2ov_dt_b_product_details&_encoding=UTF8&tag=intgus-20&linkCode=ur2&linkId=b82fe38182984dcbda0799d0f07b67bf&camp=1789&creative=9325) Adafruit sells individual buttons if you want different colors
+ [Dupont Connectors.](https://www.amazon.com/dp/B07QGBKFYZ?psc=1&amp;ref=ppx_yo2ov_dt_b_product_details&_encoding=UTF8&tag=intgus-20&linkCode=ur2&linkId=15daff3f17e82b56dc52221f9eb01f99&camp=1789&creative=9325) This is for the breadboard end of the cable and soldered on the button connectors.
+ [A TP-Link Smart Bulb](https://www.amazon.com/gp/product/B08TB6VXFL/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&amp;th=1&_encoding=UTF8&tag=intgus-20&linkCode=ur2&linkId=e89f14f99190cdd48077d8c55ecef0e4&camp=1789&creative=9325) (I'm using the KL125)
+ NodeJS with npm for the Express server (I'm using a Raspberry Pi 4 but any computer with NodeJS will work)