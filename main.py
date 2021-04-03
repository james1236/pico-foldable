# Initializes display and controls, shows menus
# Put .py files you want to run in /creations/ and they will show up in the menu
# Look at demo.py for an example of how to make a compatible creation

from machine import Pin, I2C, ADC

from time import sleep
import os

import framebuf

#Set to True to disable error handling and throw errors instead
#Highly reccomended to set to True while programming
debug = True

#Stop any previous music PWM
#from buzzer_music import music
#music().stop()


#Display wrapper class - better than display specific draw instructions...
class display:
    def __init__(self, display_type):
        self.display_type = display_type
        
        if (self.display_type == "SSD1306 Monochrome"):
            width = 128
            height = 64

            #Put the GP pins you use for SDA and SCL here
            i2c = I2C(0,sda=Pin(4),scl=Pin(5),freq=600000) #40000
            from ssd1306 import SSD1306_I2C
            self.oled = SSD1306_I2C(width,height,i2c)

            self.width = self.oled.width
            self.height = self.oled.height
        
        elif (self.display_type == "Pimoroni Pico Display"):
            
            import picodisplay
            
            self.oled = picodisplay
            self.width = self.oled.get_width()
            self.height = self.oled.get_height()
            picodisplay_buffer = bytearray(self.width * self.height * 2)  # 2-bytes per pixel (RGB565)
            self.oled.init(picodisplay_buffer)
            picodisplay_buffer = None
            self.oled.set_backlight(1.0)
            self.fill(0)
            
        elif (self.display_type == "Waveshare SSD1327 16 Bit Grey"):
            
            from ssd1327 import WS_OLED_128X128
            
            oled_i2c = I2C(0, sda=Pin(16), scl=Pin(17),freq=2300000)
            self.oled = WS_OLED_128X128(oled_i2c, addr=int(hex(oled_i2c.scan()[0])))
            
            self.width = self.oled.width
            self.height = self.oled.height
        
    def fill_rect(self, x, y, width, height, color):
        if (self.display_type == "SSD1306 Monochrome"):
            if (color > 0):
                color = 1
            self.oled.fill_rect(x,y,width,height,color)
            
        elif (self.display_type == "Pimoroni Pico Display"):
            c = round(255*color)
            self.oled.set_pen(c, c, c)
                
            self.oled.rectangle(x,y,width,height)
            
        elif (self.display_type == "Waveshare SSD1327 16 Bit Grey"):
            
            self.oled.fill_rect(x,y,width,height,round(15*color))
            
        else:
            #...since you can add support for other screens
            pass
        
    def show(self):
        if (self.display_type == "SSD1306 Monochrome" or self.display_type == "Waveshare SSD1327 16 Bit Grey"):
            self.oled.show()
            
        elif (self.display_type == "Pimoroni Pico Display"):
            self.oled.update()
        
    def fill(self, color):
        if (self.display_type == "SSD1306 Monochrome"):
            if (color > 0):
                color = 1
            self.oled.fill(color)
        
        elif (self.display_type == "Pimoroni Pico Display"):
            c = round(255*color)
            self.oled.set_pen(c, c, c)
            
            self.oled.clear()
            
        elif (self.display_type == "Waveshare SSD1327 16 Bit Grey"):
            self.oled.fill(round(15*color))
            
    def text(self, text, x, y, color=1):
        if (self.display_type == "SSD1306 Monochrome"):
            self.oled.text(text, x, y)
            
        elif (self.display_type == "Pimoroni Pico Display"):
            c = round(255*color)
            self.oled.set_pen(c, c, c)
            
            self.oled.text(text, x, y, 0, 1)
            
        elif (self.display_type == "Waveshare SSD1327 16 Bit Grey"):
            self.oled.text(text, x, y, round(15*color))
    
    def pixel(self, x, y, color):
        if (self.display_type == "SSD1306 Monochrome"):
            if (color > 0):
                color = 1
                
            self.oled.pixel(x, y, color)
        
        elif (self.display_type == "Pimoroni Pico Display"):
            c = round(255*color)
            self.oled.set_pen(c, c, c)
            
            self.oled.pixel(x, y)
            
        elif (self.display_type == "Waveshare SSD1327 16 Bit Grey"):
            self.oled.pixel(x, y, round(15*color))
            
    def blit(self, buffer, x, y, color):
        if (self.display_type == "SSD1306 Monochrome"):
            if (color > 0):
                color = 1
            self.oled.blit(buffer, x, y, color)
            
        elif (self.display_type == "Waveshare SSD1327 16 Bit Grey"):
            self.oled.blit(buffer, x, y, round(15*color))
            
    def line(self, x1, y1, x2, y2, color):
        if (self.display_type == "SSD1306 Monochrome"):
            if (color > 0):
                color = 1
            self.oled.line(x1, y1, x2, y2, color)
            
    def scroll(self, x, y):
        if (self.display_type == "SSD1306 Monochrome" or self.display_type == "Waveshare SSD1327 16 Bit Grey"):
            self.oled.scroll(x, y)
            
    def stroke_rect(self, x, y, width, height, color):
        self.fill_rect(0+x,0+y,width,1,color)
        self.fill_rect(width-1+x,0+y,1,height,color)
        self.fill_rect(0+x,height-1+y,width,1,color)
        self.fill_rect(0+x,0+y,1,height,color)


#display = display("SSD1306 Monochrome")
#display = display("Pimoroni Pico Display") #WIP
display = display("Waveshare SSD1327 16 Bit Grey")

#Class for creations to use input
class controller:
    def __init__(self, analogs=[], buttons=[], joyscale=1000, deadzone=10, picodisplay=None):
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
        
        self.usePicodisplay = False
        if (not (picodisplay is None)):
            self.usePicodisplay = True
            self.picodisplay = picodisplay
            
            
    def readJoystick(self):
        if (self.joystick):
            x = self.joyX.read_u16() - self.joyCenter[0]
            y = self.joyY.read_u16() - self.joyCenter[1]
            
            x = x / self.joyscale
            y = y / self.joyscale
            
            outsideDeadzone = False
            if (abs(x) > self.deadzone or abs(y) > self.deadzone):
                outsideDeadzone = True
                
            return (x, y, outsideDeadzone)
        
        else:
            #Emulate non existant joystick with buttons
            if (not self.readButton(0)):
                return (0, -20, True)
            elif (not self.readButton(1)):
                return (0, 20, True)
            elif (not self.readButton(2)):
                return (-20, 0, True)
            elif (not self.readButton(3)):
                return (20, 0, True)
            
            return (0,0,False)
    
    
    def readButton(self, buttonNumber):
        if (self.usePicodisplay):
            if (buttonNumber == 0):
                if (display.oled.is_pressed(display.oled.BUTTON_A)):
                    return True
                else:
                    return False
            
            elif (buttonNumber == 1):
                if (display.oled.is_pressed(display.oled.BUTTON_B)):
                    return True
                else:
                    return False
                
            elif (buttonNumber == 2):
                if (display.oled.is_pressed(display.oled.BUTTON_X)):
                    return True
                else:
                    return False
                
            elif (buttonNumber == 3):
                if (display.oled.is_pressed(display.oled.BUTTON_Y)):
                    return True
                else:
                    return False
        else:
            if (buttonNumber >= len(self.buttons)):
                return False
            return not self.buttons[buttonNumber].value()

controller = controller(analogs=[
    ADC(Pin(27)),
    ADC(Pin(26))
], buttons=[
    Pin(2, machine.Pin.IN, machine.Pin.PULL_UP),
    Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)
])

#controller = controller(picodisplay=display)


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
def errorHan(e, customMessage=None):
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
        display.text(o[i],0,i*8)
        
    if (not (customMessage is None)):
        o = []
        while customMessage:
            o.append(customMessage[:n])
            customMessage = customMessage[n:]
        
        for j in range(len(o)):
            display.text(o[j],0,((i+1)*8)+(j*8))
        
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
    
    print("onSelect")
    
    display.fill(0)
    display.text("Loading %s..." % creations[cursor].replace('.py',''), 0, 0)
    display.show()
    
    autorunFile = open('autorun', 'w')
    autorunFile.write(str(cursor))
    autorunFile.close()
    
    exec("try:\n    from creations.%s import creation\nexcept Exception:\n    pass" % creations[cursor].replace('.py',''))
    
    mainMenu = False
    try:
        creation = creation(display, controller)
    except Exception as e:
        errorHan(e, "Error while trying to create object from expected 'creation' class in the file")
    
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
buttonCooldown = 30

heldDown = 0

while True:
    frame = frame + 1
    
    buttonCooldowns[0] = max(0, (buttonCooldowns[0] - 1))
    buttonCooldowns[1] = max(0, (buttonCooldowns[1] - 1))
    
    #Hold down both buttons for 60 frames to exit to main menu
    if (controller.readButton(0) and controller.readButton(1)):
        heldDown = heldDown + 1
        if (heldDown > 60):
            heldDown = 0
            buttonCooldowns[0] = 50
            buttonCooldowns[1] = 50
            
            if (not(creation is None)):
                try:
                    creation.close()
                except Exception:
                    pass
                creation = None
            mainMenu = True
                
    else:
        heldDown = 0
    
    if (mainMenu):
        #Move cursor
        if (moveCooldown > 0):
            moveCooldown = moveCooldown - 1
        
        joy = controller.readJoystick()
        if (joy[2] and (moveCooldown <= 0) and (abs(joy[1]) > abs(joy[0]))):
            moveCooldown = 20
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
            if (controller.readButton(0)):
                buttonCooldowns[0] = buttonCooldown
                select = True
        
        display.fill(0)
        if (not (thumbnails[cursor] is None)):
            display.blit(thumbnails[cursor],display.width-40,16,0)
        
        #List files in creations folder
        ySpacing = 11
        i = 0
        
        #Calculate scroll position of text
        scroll = 0
        if (len(creations) > 5):
            if (cursor > 2):
                scroll = (cursor-2)*ySpacing
                
                #Stop scroll at the bottom
                if ((len(creations)-1) - cursor < 3):
                    scroll = (len(creations)-5)*ySpacing
        
        scroll = 0 - scroll

            
        for filename in creations:
            display.text(names[i],9,3+(ySpacing*i)+scroll)
            
            #Selection Border
            if (cursor == i):
                display.stroke_rect(8,3+(ySpacing*i)-1+scroll,len(filename.replace('.py',''))*8+2,ySpacing,1)
            
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