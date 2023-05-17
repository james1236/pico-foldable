# pico-foldable
A small ds-style foldable raspberry pi pico console with a buzzer, a joystick, a display and some buttons. Battery powered, turns on when opened.

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

### Top Half Wires
|Output|Input|
|---|---|
|Pico TP2 (Test pad 2)|USB Breakout Data Minus (DM or D-)|
|Pico TP3 (Test pad 3)|USB Breakout Data Plus (DP or D+)|
|Pico pin 1 (GP0)|500 ohm resistor -> buzzer (ribbon wire 3)|
|Pico pin 21 (GP16)|Display SDA (DIN)|
|Pico pin 22 (GP17)|Display SCK (CLK)|
|Pico pin 40 (VBUS)|Powerboost 500c USB positive pad|
|Pico pin 36 (3V3 OUT)|Display VCC|
|Pico pin 33 (GND)|Powerboost 500c USB negative pad|
|Pico pin 28 (GND)|USB Breakout GND|
|Pico pin 18 (GND)|Display GND|
|Pico pin 13 (GND)|Bottom half GND (ribbon wire 2)|
|Magnet|Powerboost 500c EN (enable)|

