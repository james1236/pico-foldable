# Initializes display and shows menus
# Put python files you want to run in /creations/ and they will automatically show up in the menu

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

from time import sleep
import os

width = 128
height = 64

#Put the GP pins you use for SDA and SCL here
i2c = I2C(0,sda=Pin(4),scl=Pin(5),freq=600000) #40000
oled = SSD1306_I2C(width,height,i2c)

#Display wrapper class
class display:
    def __init__(self, oled, display_type):
        self.oled = oled
        self.width = oled.width
        self.height = oled.height
        self.display_type = display_type
        
    def fill_rect(self, x, y, width, height, color):
        if (self.display_type == "SSD1306 Monochrome"):
            self.oled.fill_rect(x,y,width,height,color)
        else:
            #Can add support for other screens
            pass
        
    def show(self):
        if (self.display_type == "SSD1306 Monochrome"):
            oled.show()
        
    def fill(self, color):
        if (self.display_type == "SSD1306 Monochrome"):
            oled.fill(color)
            
    def text(self, text, x, y):
        if (self.display_type == "SSD1306 Monochrome"):
            oled.text(text, x, y)
    
    def pixel(self, x, y, color):
        if (self.display_type == "SSD1306 Monochrome"):
            oled.pixel(x, y, color)
        
    def stroke_rect(self, x, y, width, height, color):
        self.fill_rect(0+x,0+y,width,1,color)
        self.fill_rect(width-1+x,0+y,1,height,color)
        self.fill_rect(0+x,height-1+y,width,1,color)
        self.fill_rect(0+x,0+y,1,height,color)

display = display(oled,"SSD1306 Monochrome")

creations = os.listdir('/creations/')
creation = None

mainMenu = True
cursor = 0

frame = 0

def onSelect():
    exec("from creations.%s import creation" % creations[cursor].replace('.py',''))
    creation = creation(display)
    mainMenu = False

while True:
    display.fill(0)
    
    if (mainMenu):
        #List files in creations folder
        ySpacing = 11
        i = 0
            
        for filename in creations:
            display.text(filename.replace('.py',''),9,3+(ySpacing*i))
            
            #Selection Border
            if (cursor == i):
                display.stroke_rect(8,3+(ySpacing*i)-1,len(filename.replace('.py',''))*8+2,ySpacing,1)
            
            i = i + 1
        
            
        #Scroll bar
        display.stroke_rect(0,0,4,display.height,1)
        
        position = cursor/max((len(creations)-1),1)
        display.fill_rect(1,round(position*display.height)-round(display.height/8),2,round(display.height/4),1)
                
        display.show()
            
    else:
        #Run loaded creation
        creation.tick()
        sleep(0.0166)


#Draw Examples

#oled.fill_rect(20,20,50,10,1)

#oled.contrast(255)
#oled.pixel(20,20,1)

#oled.invert(1)
#oled.invert(0)
        
#File Example
        
#f = open('/creations/log.txt', 'w')
#f.write('some data')
#f.close()