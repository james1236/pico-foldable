import utime

#Optional metadata for main menu
class description:
    name = "Python"
    #32x32 Horizonal - 1 bit per pixel (https://javl.github.io/image2cpp/)
    thumbnail = bytearray(b"\x00\x00\x00\x00\x00\x1f\xe0\x00\x00\x7f\xf8\x00\x00\xef\xfc\x00\x00\xc7\xfe\x00\x00\xc7\xfe\x00\x00\xff\xfe\x00\x00\x00\xfe\x00\x07\xff\xfe\xe0\x1f\xff\xfe\xf0\x3f\xff\xfe\xf8\x3f\xff\xfe\xf8\x7f\xff\xfe\xfc\x7f\xff\xfd\xfc\x7f\xff\xf9\xfc\x7f\xc0\x03\xfc\x7f\x3f\xff\xfc\x7e\x7f\xff\xfc\x7e\xff\xff\xfc\x3e\xff\xff\xf8\x3e\xff\xff\xf8\x1e\xff\xff\xf0\x0e\xff\xff\xc0\x00\xff\x00\x00\x00\xff\xfe\x00\x00\xff\xc6\x00\x00\xff\xc6\x00\x00\x7f\xec\x00\x00\x3f\xfc\x00\x00\x0f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00")

#Required class named 'creation'
class creation:
    def __init__(self, display, controller, *args): #Required init method in creation class
        self.frame = 0
        self.display = display
        self.controller = controller
        self.text = [
"def fizzbuzz(count):",
"    s = ''",
"    for i in range(count):",
"        if (i % 3 == 0 and i % 5 == 0):",
"            s = s + 'fizzbuzz\\n'",
"        elif (i % 3 == 0):",
"            s = s + 'fizz\\n'",
"        elif (i % 5 == 0):",
"            s = s + 'buzz\\n'",
"        else:",
"            s = s + str(i) + '\\n'",
"    return s",
"",
'output = fizzbuzz(51)'
        ]
        self.pos = [0, 0]
        self.linesPerScreen = 11
        self.colsPerScreen = 17
        self.charWidth = 8
        self.charHeight = 11
        self.mode = "Move"
        self.buttonCooldown = 5
        
    def close(self): #Optional, called by main.py when it must exit back to main menu
        pass
    
    def showText(self):
        for y in range(self.linesPerScreen):
            #textLineIndex = max(0, min((y - int(self.linesPerScreen/2)) + self.pos[1], len(self.text) - 1))
            textLineIndex = (y - int(self.linesPerScreen/2)) + self.pos[1]
            if (textLineIndex < 0 or textLineIndex > len(self.text) - 1):
                continue
            
            textLine = self.text[textLineIndex]
            
            startCol = min(max(0, self.pos[0] - int(self.colsPerScreen/2)), len(textLine) - 1)
            textLine = textLine[startCol: startCol + self.colsPerScreen]
            self.display.text(textLine, 0, y * self.charHeight)
            
            #Highlight current char
            highlightX = self.pos[0] - startCol
            if (textLineIndex == self.pos[1] and (highlightX < self.colsPerScreen)):
                self.display.stroke_rect(highlightX * self.charWidth, y * self.charHeight, self.charWidth, self.charHeight, 1)
                
    def showInfo(self):
        self.display.fill_rect(0,self.display.height - self.charHeight, self.display.width, self.charHeight, 1)
        self.display.text(self.mode, self.display.width - (self.charWidth * len(self.mode)), self.display.height - self.charHeight, 0)
    
    def tick(self): #Required, called by main.py in a loop
        start_time = utime.ticks_us()
        self.frame = self.frame + 1
        
        if (self.buttonCooldown > 0):
            self.buttonCooldown = self.buttonCooldown - 1
        
        #Read joystick input and use it to scroll graphics
        joy = self.controller.readJoystick()
        if (joy[2]):
            if (abs(joy[0]) > abs(joy[1])):
                #l/r
                if (joy[0] > 0):
                    #right
                    self.pos[0] = self.pos[0] + 1
                    if (self.mode == "Write"):
                        if (self.pos[0] > len(self.text[self.pos[1]]) - 1):
                            self.text[self.pos[1]] = self.text[self.pos[1]] + "a"
                else:
                    #left
                    self.pos[0] = self.pos[0] - 1
            else:
                if (joy[1] > 0):
                    #down
                    if (self.mode != "Write"):
                        self.pos[1] = self.pos[1] + 1
                    else:
                        line = self.text[self.pos[1]]
                        c = line[self.pos[0]]
                        
                        c = chr(ord(c) + 1)
                        line = line[:self.pos[0]] + c + line[self.pos[0] + 1:]
                        
                        self.text[self.pos[1]] = line
                else:
                    #up
                    if (self.mode != "Write"):
                        self.pos[1] = self.pos[1] - 1
                    else:
                        line = self.text[self.pos[1]]
                        c = line[self.pos[0]]
                        
                        c = chr(ord(c) - 1)
                        line = line[:self.pos[0]] + c + line[self.pos[0] + 1:]
                        
                        self.text[self.pos[1]] = line
                        
        #Bound col, line cursor pos to ranges of text
        self.pos[1] = max(0, min(self.pos[1], len(self.text) - 1))
        self.pos[0] = max(0, min(self.pos[0], len(self.text[self.pos[1]]) - 1))
                    
        but = [self.controller.readButton(0), self.controller.readButton(1)]
        if (self.buttonCooldown <= 0):
            if (but[0] and not but[1]):
                self.buttonCooldown = 5
                if (self.mode == "Move"):
                    self.mode = "Write"
                else:
                    self.mode = "Move"
            if (but[1] and self.mode == "Write" and not but[0]):
                #save
                self.buttonCooldown = 5
                f = open('program', 'w')
                f.write("\n".join(self.text))
                f.close()
                output = {}
                self.mode = "Output"
                print(exec(compile("\n".join(self.text), "<string>", "exec"), globals(), output))
                print(output['output'])
                self.text = (str(output['output']).split())
                self.pos = [0, 0]
        
        self.display.fill(0)
        self.showText()
        self.showInfo()
            
        #Render display
        self.display.show()
        
        #Wait a fixed amount of time between ticks (independent of time taken to calculate stuff in tick())
        while (utime.ticks_us() - start_time < 40000):
            pass

