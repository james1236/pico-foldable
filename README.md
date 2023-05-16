# pico-foldable
A small foldable raspberry pi pico console with a peizo buzzer, a joystick, a display and some buttons

<br>

### Parts

Raspberry Pi Pico (RP2040)

Passive Piezo Electric Buzzer

Adafruit Powerboost 500C

Female MicroUSB Breakout Board

FFC (Flexible flat cable) from RPI camera module

3mm dia x 1mm tick Neodynium magnets with 0.13kg pull x4

<a href="https://www.waveshare.com/1.5inch-OLED-Module.htm">128x128, Waveshare 1.5inch OLED display Module I2C Mode SSD1327</a>

Joystick - Sparkfun COM-09426

2x Momentary Tactile PCB Push Buttons 6mm x 6mm

500mAh 3.7V LiPo Battery

1x 500 Ohm Resistor for buzzer

### Ribbon Cable Wires
1. bat 3.7
2. GND
3. buzzer - 500 ohm resistor
4. button 1
5. button 2
6. x
7. y
8. VCC

### Pico Wires
||
|---|
|Pico pin TP2 (Test pad 2) -> USB Breakout Data Minus (DM or D-)|
|Pico pin TP3 (Test pad 3) -> USB Breakout Data Plus (DP or D+)|
|Pico pin 1 (GP0) -> 500 ohm resistor -> buzzer (ribbon wire 3)|
|Pico pin 21 (GP16) -> SDA (DIN) Display|
Pico pin 22 (GP17)-> SCK (CLK) Display|
|Pico pin 40 (VBUS) -> Powerboost 500c USB positive pad|
|Pico pin 36 (3V3 OUT) -> VCC Display|
|Pico pin 33 (GND) -> Powerboost 500c USB negative pad|
|Pico pin 28 (GND) -> USB Breakout GND|
|Pico pin 18 (GND) -> GND Display|
|Pico pin 13 (GND) -> Bottom half ground (ribbon wire 2)|

