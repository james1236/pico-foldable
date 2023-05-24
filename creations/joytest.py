class description:
    name = "JoyTest"
    thumbnail = bytearray(b"\xff\xff\xff\xff\xff\xfc\x3f\xff\xff\xf8\x1f\xff\xff\xf0\x0f\xff\xff\xf0\x0f\xff\xff\xf0\x0f\xff\xff\xf0\x0f\xff\xff\xf8\x1f\xff\xff\xfe\x7f\xff\xff\xfe\x7f\xff\xff\xfe\x7f\xff\xff\xfe\x7f\xff\xff\xfe\x7f\xff\xff\xce\x73\xff\xff\x0e\x70\xff\xfc\x3e\x7c\x3f\xf0\xfe\x7f\x0f\xc1\xfe\x7f\x83\x8f\xf8\x1f\xf1\x8f\xf0\x0f\xf1\x83\xf8\x1f\xc1\x80\xff\xff\x01\x80\x7f\xfe\x01\xc0\x1f\xf8\x03\xf0\x00\x00\x0f\xfc\x00\x00\x3f\xff\x00\x00\xff\xff\x80\x01\xff\xff\xe0\x07\xff\xff\xf8\x1f\xff\xff\xfe\x7f\xff\xff\xff\xff\xff")

class creation:    
    def __init__(self, display, controller, *args):
        self.frame = 0
        self.display = display
        self.controller = controller
        
        self.display.fill(0)
        
        self.center = (round(self.display.width/2),round((self.display.height + 10)/2))
        self.display.pixel(self.center[0],self.center[1],1)
        
        self.display.show()
        
        self.history = []
    
    def tick(self):
        #Display joystick read info
        joy = self.controller.readJoystick()
        but = [self.controller.readButton(0), self.controller.readButton(1)]
        
        self.display.fill(0)
        self.display.fill_rect(0,0,self.display.width,10,0)
        
        if (joy[2]): #Outside deadzone
            self.display.text(str(joy),0,0)
            
            x = self.center[0] + round(joy[0])
            y = self.center[1] + round(joy[1])
            
            self.history.append([x,y])
            if (len(self.history) > 16):
                self.history.pop(0)
            
        for index, pixel in enumerate(self.history):
            self.display.pixel(pixel[0],pixel[1],16-index)
            
        self.display.fill_rect(0,self.display.height-10,20,self.display.height-10, 0)
        
        if (but[0]):
            self.display.text("A",0,self.display.height-10)
        if (but[1]):
            self.display.text("B",10,self.display.height-10)
            
        self.display.show()

