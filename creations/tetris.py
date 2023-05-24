from buzzer_music import music
import framebuf
import random

import utime
import _thread

background = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xe0\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf8\x00\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xbf\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xbf\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xbf\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x3f\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xbf\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xbf\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xbf\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xbf\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xb8\x19\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xb8\x19\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xb8\x19\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xb8\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xb8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xb8\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xa0\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x3f\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xbf\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x3f\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xbf\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x3f\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x3f\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x3f\xff\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x3f\x60\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\xfb\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x03\xf9\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x0f\xf0\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x3f\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x3f\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x3c\x7d\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xb3\xfd\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x8f\xfd\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xbf\xfd\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xb8\x01\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xb8\x07\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xb8\x1f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x38\x7f\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xb9\xfe\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xbf\xf8\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\xbf\xe0\xe0\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf8\xbf\x80\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbe\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
background = framebuf.FrameBuffer(background, 128, 64, framebuf.MONO_HLSB)

musicPlaying = False
mySong = None
musicThreadInstance = None

def musicThread():
    global mySong
    global musicPlaying
    
    while True:
        utime.sleep(0.02)
        if (not musicPlaying):
            mySong.stop()
            del mySong
            break
        
        try:
            mySong.tick()
        except Exception:
            pass

def startMusic():
    global mySong
    global musicPlaying
    global musicThread
    
    song = '0 E3 1 0;2 E4 1 0;4 E3 1 0;6 E4 1 0;8 E3 1 0;10 E4 1 0;12 E3 1 0;14 E4 1 0;16 A3 1 0;18 A4 1 0;20 A3 1 0;22 A4 1 0;24 A3 1 0;26 A4 1 0;28 A3 1 0;30 A4 1 0;32 G#3 1 0;34 G#4 1 0;36 G#3 1 0;38 G#4 1 0;40 E3 1 0;42 E4 1 0;44 E3 1 0;46 E4 1 0;48 A3 1 0;50 A4 1 0;52 A3 1 0;54 A4 1 0;56 A3 1 0;58 B3 1 0;60 C4 1 0;62 D4 1 0;64 D3 1 0;66 D4 1 0;68 D3 1 0;70 D4 1 0;72 D3 1 0;74 D4 1 0;76 D3 1 0;78 D4 1 0;80 C3 1 0;82 C4 1 0;84 C3 1 0;86 C4 1 0;88 C3 1 0;90 C4 1 0;92 C3 1 0;94 C4 1 0;96 G2 1 0;98 G3 1 0;100 G2 1 0;102 G3 1 0;104 E3 1 0;106 E4 1 0;108 E3 1 0;110 E4 1 0;114 A4 1 0;112 A3 1 0;116 A3 1 0;118 A4 1 0;120 A3 1 0;122 A4 1 0;124 A3 1 0;0 E6 1 1;4 B5 1 1;6 C6 1 1;8 D6 1 1;10 E6 1 1;11 D6 1 1;12 C6 1 1;14 B5 1 1;0 E5 1 6;4 B4 1 6;6 C5 1 6;8 D5 1 6;10 E5 1 6;11 D5 1 6;12 C5 1 6;14 B4 1 6;16 A5 1 1;20 A5 1 1;22 C6 1 1;24 E6 1 1;28 D6 1 1;30 C6 1 1;32 B5 1 1;36 B5 1 1;36 B5 1 1;37 B5 1 1;38 C6 1 1;40 D6 1 1;44 E6 1 1;48 C6 1 1;52 A5 1 1;56 A5 1 1;20 A4 1 6;16 A4 1 6;22 C5 1 6;24 E5 1 6;28 D5 1 6;30 C5 1 6;32 B4 1 6;36 B4 1 6;37 B4 1 6;38 C5 1 6;40 D5 1 6;44 E5 1 6;48 C5 1 6;52 A4 1 6;56 A4 1 6;64 D5 1 6;64 D6 1 1;68 D6 1 1;70 F6 1 1;72 A6 1 1;76 G6 1 1;78 F6 1 1;80 E6 1 1;84 E6 1 1;86 C6 1 1;88 E6 1 1;92 D6 1 1;94 C6 1 1;96 B5 1 1;100 B5 1 1;101 B5 1 1;102 C6 1 1;104 D6 1 1;108 E6 1 1;112 C6 1 1;116 A5 1 1;120 A5 1 1;72 A5 1 6;80 E5 1 6;68 D5 1 7;70 F5 1 7;76 G5 1 7;84 E5 1 7;78 F5 1 7;86 C5 1 7;88 E5 1 6;96 B4 1 6;104 D5 1 6;112 C5 1 6;120 A4 1 6;92 D5 1 7;94 C5 1 7;100 B4 1 7;101 B4 1 7;102 C5 1 7;108 E5 1 7;116 A4 1 7'
    mySong = music(song, True, 6)
    musicPlaying = True
    
    #Run music on second thread
    musicThreadInstance = _thread.start_new_thread(musicThread, ())
    

pieces = (
    ( #Rotation 0 (normal)
        ((0,0),(-1,0),(1,0),(0,1)), #T
        ((0,0),(-1,0),(0,1),(1,1)), #_|-
        ((0,0),(-1,0),(1,0),(-1,1)), #|__
        ((0,0),(-1,0),(1,0),(2,0)), #line
        ((0,0),(-1,0),(1,0),(1,1)), #__|
        ((0,0),(1,0),(0,1),(1,1)), #square
        ((0,0),(1,0),(0,1),(-1,1)), #-|_
    ),
    ( #Rotation 1 (right)
        ((0,0),(0,-1),(1,0),(0,1)), #T
        ((0,0),(0,1),(1,0),(1,-1)), #_|-
        ((0,0),(0,-1),(0,1),(1,1)), #|__
        ((1,0),(1,1),(1,-1),(1,-2)), #line
        ((0,0),(0,1),(0,-1),(1,-1)), #__|
        ((0,0),(1,0),(0,1),(1,1)), #square
        ((0,0),(1,0),(1,1),(0,-1)), #-|_
    ),
    ( #Rotation 2 (upside down)
        ((0,0),(-1,0),(1,0),(0,-1)), #T
        ((0,0),(1,0),(0,-1),(-1,-1)), #_|-
        ((0,0),(-1,0),(1,0),(1,-1)), #|__
        ((0,-1),(-1,-1),(1,-1),(2,-1)), #line
        ((0,0),(1,0),(-1,0),(-1,-1)), #__|
        ((0,0),(1,0),(0,1),(1,1)), #square
        ((0,0),(-1,0),(0,-1),(1,-1)), #-|_
    ),
    ( #Rotation 3 (left)
        ((0,0),(-1,0),(0,1),(0,-1)), #T
        ((0,0),(0,-1),(-1,0),(-1,1)), #_|-
        ((0,0),(0,1),(0,-1),(-1,-1)), #|__
        ((0,0),(0,1),(0,-1),(0,-2)), #line
        ((0,0),(0,-1),(0,1),(-1,1)), #__|
        ((0,0),(1,0),(0,1),(1,1)), #square
        ((0,0),(0,1),(-1,0),(-1,-1)), #-|_
    ),
)


class description:
    name = "Tetris"
    thumbnail = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x2a\xd5\x50\x00\x1f\xef\xf8\x00\x3f\xf7\xf0\x00\x1f\xef\xf8\x00\x3f\xf7\xf0\x00\x1f\xef\xf8\x00\x3f\xf7\xf0\x00\x1f\xef\xf8\x00\x3f\xf7\xf0\x00\x15\x2a\xa8\x00\x00\x15\x56\xa8\x00\x0f\xfb\xfc\x00\x1f\xf7\xf8\x00\x0f\xfb\xfc\x00\x1f\xf7\xf8\x00\x0f\xfb\xfc\x00\x1f\xf7\xf8\x00\x0f\xfb\xfc\x00\x1f\xf7\xf8\x00\x0a\xab\x54\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

class creation:
    def __init__(self, display, controller, *args):
        self.frame = 0
        self.display = display
        
        self.board = []
        for y in range(20):
            self.board.append([])
            for x in range(10):
                self.board[y].append(0)
        
        self.score = 0
        self.moveCooldownDefault = 7
        self.level = 0
        self.linesCleared = 0
        self.boardX = 95
        self.boardY = 7
        
        self.controller = controller
        
        self.takePiece()
        self.piecePos = (4,20)
        self.stepDelay = 40
        self.allowSoftDrop = True
        
        self.moveCooldown = 0
        
        startMusic()
        
        self.display.fill(0)
        self.display.blit(background,0,0,0)
        
        #Draw score
        self.display.fill_rect(50,0,len(str(self.score))*8,8,0)
        self.display.text("score:",0,-2)
        self.display.text("0",50,0)
        
        #Get highscore
        highscoreFile = open('creations/tetris_highscore', 'r')
        c = highscoreFile.read()
        if (c == ''):
            self.highscore = 0
        else:
            self.highscore = int(c)
            
        highscoreFile.close()
        
        #Draw highscore
        self.display.text("most:",0,self.display.height-7)
        self.display.pixel(26,self.display.height-7,0)
        self.display.pixel(28,self.display.height-7,0)
        self.display.fill_rect(42,self.display.height-7,len(str(self.highscore))*8,8,0)
        self.display.text(str(self.highscore),42,self.display.height-7)
        
        self.display.show()
        
    def close(self): #Called by main.py when it must exit back to main menu
        global musicPlaying
        #mySong.stop()
        musicPlaying = False
        musicThreadInstance.join()
        #utime.sleep(0.03) #Sleep to be sure other thread has ended
        
    def takePiece(self):
        #Clear lines
        y = 0
        linesCleared = 0
        while ((20 - linesCleared) > y):
            if (sum(self.board[y]) == 10):
                self.board.pop(y)
                y = y - 1
                linesCleared = linesCleared + 1
            y = y + 1
            
        #Add empty lines back
        for i in range(linesCleared):
            self.board.append([0,0,0,0,0,0,0,0,0,0])
            
        
        if (linesCleared > 0):
            #Calc score
            if (linesCleared == 1):
                try:
                    mySong.arpnote = 0
                    mySong.playingNotes = ["A4"]
                    mySong.playingDurations = [5]
                except Exception:
                    pass
                score = 40
            elif (linesCleared == 2):
                try:
                    mySong.arpnote = 0
                    mySong.playingNotes = ["A4", "E5"]
                    mySong.playingDurations = [5, 5]
                except Exception:
                    pass
                score = 100
            elif (linesCleared == 3):
                try:
                    mySong.arpnote = 0
                    mySong.playingNotes = ["A4", "E5", "A5"]
                    mySong.playingDurations = [5, 5, 5]
                except Exception:
                    pass
                score = 300
            else:
                try:
                    mySong.arpnote = 0
                    mySong.playingNotes = ["A4", "E5", "A5", "C#6"]
                    mySong.playingDurations = [5, 5, 5, 5]
                except Exception:
                    pass
                score = 1200
            
            self.score = self.score + (score*(self.level+1))
            self.linesCleared = self.linesCleared + linesCleared
            
            #Increase level only after score is calculated
            self.level = int(self.linesCleared / 10)
            #Reset delay between drops
            self.frame = 0
            
            #Change time between piece drops depending on level
            if (5 >= self.level):
                self.stepDelay = (40-(self.level*4))
            elif (10 >= self.level):
                self.stepDelay = (20-((self.level-5)*2))
            else:
                self.stepDelay = max(1,10-(self.level-10))
                
            #Speed up input on later levels
            self.moveCooldownDefault = max(-3,7-int(self.level/3))
            
            #Highscore calc
            if (self.score > self.highscore):
                self.highscore = self.score
                
                #Save highscore
                highscoreFile = open('creations/tetris_highscore', 'w')
                highscoreFile.write(str(self.highscore))
                highscoreFile.close()
                
                #Draw highscore
                self.display.fill_rect(42,self.display.height-7,len(str(self.highscore))*8,8,0)
                self.display.text(str(self.highscore),42,self.display.height-7)
            
            #Draw score
            self.display.fill_rect(50,0,len(str(self.score))*8,8,0)
            self.display.text(str(self.score),50,0)
            
            #Redraw board since lines were cleared
            self.drawBoard()
        else:
            try:
                mySong.arpnote = 0
                mySong.playingNotes = ["A2"]
                mySong.playingDurations = [2]
            except Exception:
                pass
            
        #Take new piece
        self.pieceRotation = 0
        self.piecePos = (4,19)
        self.pieceType = random.randrange(0, 7)
        
        #Stop soft drop from last piece
        joy = self.controller.readJoystick()
        if (joy[2] and (not (joy[0] > 0))): #X and Y swapped since the game is played horizontally
            self.allowSoftDrop = False
        
    def rotate(self, direction):
        self.pieceRotation = self.pieceRotation + direction
        if (self.pieceRotation > 3):
            self.pieceRotation = 0
        elif (self.pieceRotation < 0):
            self.pieceRotation = 3
        
        movement = 0
        while (movement < 4):
            flag = False
            for seg in range(4):
                segTransform = pieces[self.pieceRotation][self.pieceType][seg]
                x = segTransform[0] + self.piecePos[0] + movement
                y = segTransform[1] + self.piecePos[1]
                
                #Unsaveable rotation
                if (self.board[max(min(y,19),0)][max(min(x,9),0)] != 0 or 0 > y):
                    self.pieceRotation = self.pieceRotation - direction
                    if (self.pieceRotation > 3):
                        self.pieceRotation = 0
                    elif (self.pieceRotation < 0):
                        self.pieceRotation = 3
                    return False
                
                if (0 > x): #A seg is out of bounds after rotation
                    flag = True
                    movement = movement + 1 #Shift piece to the right
                    break
                if (x > 9):
                    flag = True
                    movement = movement - 1 #Shift piece to the left
                    break
                
            if (not flag):
                self.piecePos = (self.piecePos[0] + movement, self.piecePos[1])
                return True
        
        #More than 4 shifts needed, abort rotation
        self.pieceRotation = self.pieceRotation - direction
        if (self.pieceRotation > 3):
            self.pieceRotation = 0
        elif (self.pieceRotation < 0):
            self.pieceRotation = 3
        return False
    
    def step(self):
        global musicPlaying
        #Move down one
        self.piecePos = (self.piecePos[0], self.piecePos[1] - 1)
        
        #Test collision
        flag = False
        for seg in range(4):
            segTransform = pieces[self.pieceRotation][self.pieceType][seg]
            x = segTransform[0] + self.piecePos[0]
            y = segTransform[1] + self.piecePos[1]
            if (0 > y or ((0 <= x <= 9 and 0 <= y <= 19) and self.board[y][x] != 0)):
                flag = True
                break
        
        if (flag):
            #Piece collided - move back up
            self.piecePos = (self.piecePos[0], self.piecePos[1] + 1)
            for seg in range(4):
                segTransform = pieces[self.pieceRotation][self.pieceType][seg]
                x = segTransform[0] + self.piecePos[0]
                y = segTransform[1] + self.piecePos[1]
                if (0 <= x <= 9 and 0 <= y):
                    if (y <= 19):
                        #Place each seg in board
                        self.board[segTransform[1] + self.piecePos[1]][segTransform[0] + self.piecePos[0]] = 1
                    else:
                        #Game Over
                        #mySong.stop()
                        musicPlaying = False
                        utime.sleep(0.3) #Sleep to be sure other thread has ended
                        self.__init__(self.display, self.controller)
                    
            self.takePiece()
            return True #collided
        
        return False
    
    def drawSeg(self, x, y, color):
        self.display.fill_rect(self.boardX-((19-y)*5),self.boardY+(x*5),5,5,color)
        self.display.fill_rect(self.boardX+1-((19-y)*5),self.boardY+1+(x*5),3,3,0)
        self.display.pixel(self.boardX+2-((19-y)*5),self.boardY+2+(x*5),color)
        
    def drawPiece(self, pieceTransform, piecePos, color=1):
        self.show = True # Tell display to draw changes at end of frame
        for seg in range(4):
            segTransform = pieceTransform[seg]
            x = segTransform[0] + piecePos[0]
            y = segTransform[1] + piecePos[1]
            if (0 <= x <= 9 and 0 <= y <= 19):
                self.drawSeg(x,y,color)
                
    def drawBoard(self):
        self.show = True
        self.display.fill_rect(0,self.boardY,20*5,10*5,0)
        
        for y in range(20):
            for x in range(10):
                if (self.board[y][x] != 0):
                    self.drawSeg(x, y, 1)
        
    def tick(self):
        start_time = utime.ticks_us()
        
        self.show = False
        joy = self.controller.readJoystick()
        
        if (self.moveCooldown > -5):
            self.moveCooldown = self.moveCooldown - 1
        
        #Out of deadzone
        if (joy[2]):
            #X and Y swapped since the game is played horizontally
            x = joy[1]
            y = joy[0]
            if (abs(x) > abs(y)):
                self.allowSoftDrop = True
            if (y > 0):
                self.allowSoftDrop = True
            
            if (self.moveCooldown <= 0):
                #Find primary direction
                if (abs(x) > abs(y)):
                    self.moveCooldown = self.moveCooldownDefault
                    if (x > 0):
                        #right
                        movement = 1
                    else:
                        #left
                        movement = -1
                        
                    #Check if movement is permitted
                    flag = False
                    for seg in range(4):
                        segTransform = pieces[self.pieceRotation][self.pieceType][seg]
                        x = segTransform[0] + self.piecePos[0] + movement
                        y = segTransform[1] + self.piecePos[1]
                        if (not(0 <= x <= 9)):
                            flag = True
                            break
                        if (self.board[min(y,19)][x] != 0):
                            flag = True
                            break
                        
                    if (not flag):
                        #Move and redraw piece
                        self.drawPiece(pieces[self.pieceRotation][self.pieceType], self.piecePos, 0)
                        self.piecePos = (self.piecePos[0] + movement,self.piecePos[1])
                        self.drawPiece(pieces[self.pieceRotation][self.pieceType], self.piecePos, 1)

                else:
                    if (y > 0):
                        #up
                        #Rotate
                        if (self.moveCooldown <= -5):
                            self.moveCooldown = self.moveCooldownDefault
                            oldPieceTransform = pieces[self.pieceRotation][self.pieceType]
                            oldPiecePos = self.piecePos
                            
                            if (self.rotate(1)):
                                self.drawPiece(oldPieceTransform, oldPiecePos, 0)
                                self.drawPiece(pieces[self.pieceRotation][self.pieceType], self.piecePos, 1)
                    else:
                        #down
                        #Softdrop
                        if (self.allowSoftDrop):
                            self.frame = self.stepDelay
                            #self.score = self.score + 1
        else:
            self.allowSoftDrop = True
            #Disable cooldown when stick is moved back to neutral
            self.moveCooldown = -5
                
        
        if (self.frame % self.stepDelay == 0):
            oldPieceTransform = pieces[self.pieceRotation][self.pieceType]
            oldPiecePos = self.piecePos
            
            #If, after step(), a new piece wasn't drawn
            if (not self.step()):
                #Clear old piece
                self.drawPiece(oldPieceTransform, oldPiecePos, 0)
            
            #Draw new piece
            self.drawPiece(pieces[self.pieceRotation][self.pieceType], self.piecePos)
            
        
        if (self.show):
            self.display.show()
        self.frame = self.frame + 1
        
        try:
            pass #mySong.tick()
        except Exception:
            pass
        
        while (utime.ticks_us() - start_time < 20000):
            pass
