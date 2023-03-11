## Express Server to control a TP-Link Smart Plug

Quick prototype using the HTTP client example, a simple Express server and this [Python Script](https://github.com/softScheck/tplink-smartplug) to control a TP-Link Smart Plug

The Arduino RP 2040 Connect just have a momentary switch with a 10K resistor.

Using the following:

+ Arduino RP2040 Connect (it can be done with a Raspberry Pico W using the appropiate wireless library)
+ A TP-Link Smart Plug (I'm using the HS103)
+ NodeJS with npm for the Express server (I'm using a Raspberry Pi 4 but any computer with NodeJS will work)
