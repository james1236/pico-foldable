# pico-foldable
A small ds-style foldable Raspberry Pi Pico console with a buzzer, a joystick, a display and some buttons. You can easily create and add new games as seperate files in /creations/ and a game picking menu/autorun system lets you play them (hold both buttons to get to the menu). The 3D printed case prints in 4 seperate parts and has a print-in-place hinge.

It is powered by a 3.7v LiPo battery through the adafruit Powerboost 500c recharger/power supply board. The EN (enable) pin on this board allows a circuit across the magnets between both displays to turn the whole device on when opened. A MicroUSB breakout board is installed to direct power to the Powerboost 500c while directing the data lines straight to the Pico's test pads, allowing you to plug it in as usual to upload code or debug.

### Parts
|Part|Quantity|
|---|---|
|Raspberry Pi Pico (RP2040)|1|
|Passive Piezo Electric Buzzer|1|
|<a href="https://www.adafruit.com/product/1944">Adafruit Powerboost 500C</a>|1|
|Female MicroUSB Breakout Board|1|
|~~FFC (Flexible flat cable) from RPI camera module~~|0|
|10 out flexible rainbow ribbon cable|1|
|3mm dia x 1mm thick Neodynium magnets with 0.13kg pull|4|
|<a href="https://www.waveshare.com/1.5inch-OLED-Module.htm">128x128, Waveshare 1.5inch OLED display Module I2C Mode SSD1327</a>|1|
|<a href="https://www.sparkfun.com/products/9426">Joystick - Sparkfun COM-09426</a>|1|
|Momentary Tactile PCB Push Buttons 6mm x 6mm|2|
|500mAh 3.7V LiPo Battery|1|
|500 Ohm Resistor (for reducing buzzer volume)|1|

### Ribbon Cable Wires
|Num|Color|Connection|
|---|---|---|
|1|brown|bat 3.7|
|2|red|GND|
|3|orange|buzzer|
|4|yellow|left button|
|5|green|right button|
|6|blue|joystick X|
|7|purple|joystick Y|
|8|gray|VCC|

### Bottom Half Wires
|Output|Input|
|---|---|
|Magnet|GND (ribbon wire 2)|
|Left Button|GND (ribbon wire 2)|
|Right Button|GND (ribbon wire 2)|
|Joystick GND|GND (ribbon wire 2)|
|Buzzer -|GND (ribbon wire 2)|
|LiPo Battery negative (black) wire|GND (ribbon wire 2)|
|LiPo Battery positive (red) wire|bat 3.7 (ribbon wire 1)|
|Buzzer +|buzzer wire (ribbon wire 3)|
|Left Button (opposite half)|left button wire (ribbon wire 4)|
|Right Button (opposite half)|right button wire (ribbon wire 5)|
|Joystick X|joystick X wire (ribbon wire 6)|
|Joystick Y|joystick Y wire (ribbon wire 7)|
|Joystick VCC|VCC (ribbon wire 8)|

### Top Half Wires
|Output|Input|
|---|---|
|Powerboost 500c EN (enable)|Magnet|
|Powerboost 500c BAT|Battery positive (ribbon wire 1)|
|Powerboost 500c USB|USB Breakout VCC positive|
|Pico pin 28 (GND)|USB Breakout GND negative|
|Pico pin 40 (VBUS)|Powerboost 500c USB positive pad|
|Pico pin 33 (GND)|Powerboost 500c USB negative pad|
|Pico TP2 (Test pad 2)|USB Breakout Data Minus (DM or D-)|
|Pico TP3 (Test pad 3)|USB Breakout Data Plus (DP or D+)|
|Pico pin 13 (GND)|Bottom half GND (ribbon wire 2)|
|Pico pin 1 (GP0)|500 ohm resistor -> buzzer (ribbon wire 3)|
|Pico pin 19 (GP14)|Left button (ribbon wire 4)|
|Pico pin 20 (GP15)|Right button (ribbon wire 5)|
|Pico pin 33 (ADC0)|Joystick X (ribbon wire 6)|
|Pico pin 34 (ADC1)|Joystick Y (ribbon wire 7)|
|Pico pin 39 (VSYS)|VCC (ribbon wire 8)|
|Pico pin 21 (GP16)|Display SDA (DIN)|
|Pico pin 22 (GP17)|Display SCK (CLK)|
|Pico pin 36 (3V3 OUT)|Display VCC|
|Pico pin 18 (GND)|Display GND|
