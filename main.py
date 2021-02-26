# Initializes display and shows menus
# Put creations you want to run in /creations/ and they will automatically show up in the menu
# Look at demo.py for an example of how to make a creation

from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C

from time import sleep
import os

import framebuf

#Set to True to disable error handling and throw errors instead
#Highly reccomended to set to True while programming
debug = False

#Stop any previous music PWM
from buzzer_music import music
music().stop()

width = 128
height = 64

#Put the GP pins you use for SDA and SCL here
i2c = I2C(0,sda=Pin(4),scl=Pin(5),freq=600000) #40000
oled = SSD1306_I2C(width,height,i2c)

#Display wrapper class - better than display specific draw instructions...
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
            #...since you can add support for other screens
            pass
        
    def show(self):
        if (self.display_type == "SSD1306 Monochrome"):
            self.oled.show()
        
    def fill(self, color):
        if (self.display_type == "SSD1306 Monochrome"):
            self.oled.fill(color)
            
    def text(self, text, x, y):
        if (self.display_type == "SSD1306 Monochrome"):
            self.oled.text(text, x, y)
    
    def pixel(self, x, y, color):
        if (self.display_type == "SSD1306 Monochrome"):
            self.oled.pixel(x, y, color)
            
    def blit(self, buffer, x, y, color):
        if (self.display_type == "SSD1306 Monochrome"):
            self.oled.blit(buffer, x, y, color)
            
    def line(self, x1, y1, x2, y2, color):
        if (self.display_type == "SSD1306 Monochrome"):
            self.oled.line(x1, y1, x2, y2, color)
        
    def stroke_rect(self, x, y, width, height, color):
        self.fill_rect(0+x,0+y,width,1,color)
        self.fill_rect(width-1+x,0+y,1,height,color)
        self.fill_rect(0+x,height-1+y,width,1,color)
        self.fill_rect(0+x,0+y,1,height,color)


display = display(oled,"SSD1306 Monochrome")

#Class for creations to use input
class controller:
    def __init__(self, analogs, buttons, joyscale=1000, deadzone=10):
        self.joystick = False
        self.joyscale = joyscale
        self.deadzone = deadzone
        
        if (len(analogs) >= 2):
            #Use analogs as joystick
            self.joyX = analogs[0]
            self.joyY = analogs[1]
            
            self.joystick = True
            self.joyCenter = (self.joyX.read_u16(),self.joyY.read_u16())
            
        self.buttons = buttons
            
    def readJoystick(self):
        x = self.joyX.read_u16() - self.joyCenter[0]
        y = self.joyY.read_u16() - self.joyCenter[1]
        
        x = x / self.joyscale
        y = y / self.joyscale
        
        outsideDeadzone = False
        if (abs(x) > self.deadzone or abs(y) > self.deadzone):
            outsideDeadzone = True
            
        return (x, y, outsideDeadzone)
    
    
    def readButton(self, buttonNumber):
        return self.buttons[buttonNumber].value()
        



controller = controller(analogs=[
    ADC(Pin(27)),
    ADC(Pin(26))
], buttons=[
    Pin(2, machine.Pin.IN, machine.Pin.PULL_UP),
    Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)
])


creations = os.listdir('/creations/')

#Remove non .py files from creations array
i = 0
while (i < len(creations)):
    if (not (".py" in creations[i])):
        creations.pop(i)
    else:
        i = i + 1
    
creation = None

mainMenu = True
cursor = 0

frame = 0

names = []
thumbnails = []

#Get name+thumbnail for each creation
i = 0
for filename in creations:
    #Attempt Import
    exec("try:\n    from creations."+creations[i].replace('.py','')+" import description\nexcept ImportError:\n    pass")
    
    try:
        description
    except NameError:
        #Unsuccessful
        names.append(creations[i].replace('.py',''))
        thumbnails.append(None)
    else:
        #Successful
        if (hasattr(description, 'name')):
            names.append(description.name)
        else:
            names.append(creations[i].replace('.py',''))
            
        if (hasattr(description, 'thumbnail')):
            thumbnails.append(framebuf.FrameBuffer(description.thumbnail, 32, 32, framebuf.MONO_HLSB))
        else:
            thumbnails.append(None)
        
        del description
    i = i + 1


#Handle errors thrown by creations so that they can be dropped back to main menu
#Disable by setting debug = True
def errorHan(e):
    global debug
    global mainMenu
    global creation
    global display
    
    if (debug):
        raise e
        return

    e = repr(e)
    print(e)
    print("Set debug = True in main.py to throw exceptions...")
    
    #Split exception string into screen width strings
    n = int(display.width/8)
    o = []
    while e:
        o.append(e[:n])
        e = e[n:]
    
    display.fill(0)
    for i in range(len(o)):
        display.text(o[i],0,10+(i*8))
        
    display.show()
    sleep(5)
    creation = None
    mainMenu = True
    music().stop()

#Function to load into the selected creation
def onSelect():
    global creations
    global cursor
    global creation
    global mainMenu
    global display
    global config
    
    display.fill(0)
    display.text("Loading %s..." % creations[cursor].replace('.py',''), 0, 0)
    display.show()
    
    autorunFile = open('autorun', 'w')
    autorunFile.write(str(cursor))
    autorunFile.close()
    
    exec("from creations.%s import creation" % creations[cursor].replace('.py',''))
    
    mainMenu = False
    try:
        creation = creation(display, controller)
    except Exception as e:
        errorHan(e)
    
#Try to auto open previous creation
autorunFile = open('autorun', 'r')
c = autorunFile.read()
if (not (c == '')):
    cursor = int(c)
    if (cursor >= len(creations)):
        cursor = len(creations)-1
    onSelect()
autorunFile.close()

moveCooldown = 0

buttonCooldowns = [0,0]
buttonCooldown = 100

while True:
    frame = frame + 1
    
    buttonCooldowns[0] = max(0, (buttonCooldowns[0] - 1))
    buttonCooldowns[1] = max(0, (buttonCooldowns[1] - 1))
    
    if (mainMenu):
        #Move cursor
        if (moveCooldown > 0):
            moveCooldown = moveCooldown - 1
        
        joy = controller.readJoystick()
        if (joy[2] and (moveCooldown <= 0) and (abs(joy[1]) > abs(joy[0]))):
            moveCooldown = 8
            if (joy[1] > 0):
                #up
                cursor = cursor + 1
                if (cursor >= len(creations)):
                    cursor = 0
            else:
                #down
                cursor = cursor - 1
                if (0 > cursor):
                    cursor = len(creations)-1
            
        #Detect button press
        select = False
        if (buttonCooldowns[0] == 0):
            if (not controller.readButton(0)):
                buttonCooldowns[0] = buttonCooldown
                select = True
        
        display.fill(0)
        if (not (thumbnails[cursor] is None)):
            display.blit(thumbnails[cursor],display.width-40,16,0)
        
        #List files in creations folder
        ySpacing = 11
        i = 0
            
        for filename in creations:
            display.text(names[i],9,3+(ySpacing*i))
            
            #Selection Border
            if (cursor == i):
                display.stroke_rect(8,3+(ySpacing*i)-1,len(filename.replace('.py',''))*8+2,ySpacing,1)
            
            i = i + 1
        
            
        #Scroll bar
        display.stroke_rect(0,0,4,display.height,1)
        
        position = cursor/max((len(creations)-1),1)
        display.fill_rect(1,round(position*display.height)-round(display.height/8),2,round(display.height/4),1)
                
        display.show()
        
        if (select):
            onSelect()
        
    else:
        #Run loaded creation
        try:
            creation.tick()
        except Exception as e:
            errorHan(e)
        
        #Exit creation on button press
        if (buttonCooldowns[0] == 0):
            if (not controller.readButton(0)):
                buttonCooldowns[0] = buttonCooldown
                try:
                    creation.close()
                except Exception:
                    pass
                creation = None
                mainMenu = True
