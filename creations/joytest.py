class description:
    name = "JoyTest"
    thumbnail = bytearray(b"\xff\xff\xff\xff\x80\x00\x00\x01\x80\x1f\xfc\x01\x80\x60\x03\x01\x80\x80\x00\x81\x81\x00\x00\x41\x82\x00\x00\x21\x84\x00\x00\x11\x88\x00\x0f\x11\x90\x00\x0b\x09\x90\x00\x0d\x09\xa0\x00\x0f\x05\xa0\x00\x10\x05\xa0\x00\x20\x05\xa0\x00\x40\x05\xa0\x01\x80\x05\xa0\x01\x80\x05\xa0\x00\x00\x05\xa0\x00\x00\x05\xa0\x00\x00\x05\xa0\x00\x00\x05\xa0\x00\x00\x09\x90\x00\x00\x09\x90\x00\x00\x11\x88\x00\x00\x11\x84\x00\x00\x21\x82\x00\x00\x41\x81\x80\x01\x81\x80\x60\x06\x01\x80\x1f\xf8\x01\x80\x00\x00\x01\xff\xff\xff\xff")

class creation:    
    def __init__(self, display, controller, *args):
        self.frame = 0
        self.display = display
        self.controller = controller
        
        self.display.fill(0)
        
        self.display.stroke_rect(0,0,self.display.width,self.display.height,1)
        
        self.center = (round(self.display.width/2),round((self.display.height + 10)/2))
        self.display.pixel(self.center[0],self.center[1],1)
        
        self.display.show()
    
    def tick(self):
        #Display joystick read info
        joy = self.controller.readJoystick()
        
        self.display.fill_rect(0,0,self.display.width,10,0)
        
        if (joy[2]): #Outside deadzone
            self.display.text(str(joy),0,0)
            
            x = self.center[0] + round(joy[0])
            y = self.center[1] + round(joy[1])
            
            self.display.pixel(x,y,1)
            
        self.display.show()

