import pygame, sys
import time
import math
import importlib
import uuid

from random import randint
from os import listdir
from os.path import isfile

from pygame.locals import *

DISPLAY_WIDTH=800
DISPLAY_HEIGHT=800
TILESIZE=50
LINEWIDTH = 5
PROJECTILE_VELOCITY=20
PROJECTILE_DAMAGE=randint(2,4)
ENERGY_CHARGE_PER_TURN=5

BLACK=(0,0,0)
DARK_GRAY = (50,50,50)
WHITE=(255,255,255)
GREEN=(0,200,0)
BRIGHT_GREEN=(150,255,150)
RED=(200,0,0)
BRIGHT_RED=(255,150,150)
BLUE=(0,0,255)

pygame.init()
screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
instructionFont = pygame.font.Font("freesansbold.ttf",24)
font = pygame.font.Font("freesansbold.ttf",14)
smallfont = pygame.font.Font("freesansbold.ttf",10)
#projectile_sound = pygame.mixer.Sound("projectile.wav")
#tank_sound = pygame.mixer.Sound("tank.wav")
#bomb_sound = pygame.mixer.Sound("bomb.wav")
clock = pygame.time.Clock()
intro=True


class object():
    def __init__(self, name, coordx, coordy, direction, sImg, ai, objType, subType=0):
        self.name = name
        self.initx = coordx
        self.inity = coordy
        self.initdir = direction
        self._x = coordx
        self._y = coordy
        self.direction=direction
        self.OrigSurfImg=sImg
        # direction: 0=north, 1=west, 2=south, 3=east
        self.surfImg = pygame.transform.rotate(self.OrigSurfImg, self.direction)
        self.health = 100
        self.energy=5
        self.ai = ai
        ai.robot = self
        #self.turnpoints = 0
        self.type=objType #1=tank, #2=projectile, #3=shield, #4=bomb, #5= powerup
        self.subtype=subType
        self.uid=uuid.uuid1() 
        self.parentuid=""
        self.shield=False
        self.velocity=0
        self.destinationx=0
        self.destinationy=0

    def getRect(self):
        return pygame.Rect(self._x, self._y, self.surfImg.get_width(), self.surfImg.get_height())
    
    def x(self):
        return self._x

    def y(self):
        return self._y
    
    def ram(self):
        global objects
        if self.energy >= 10:
            self._x += (-1)*10 * math.sin(math.radians(self.direction))
            self._y += (-1)*10 * math.cos(math.radians(self.direction)) 

            for o in objects:
                if o.type==1 and o.uid!=self.uid and self.getRect().colliderect(o.getRect()):
                    o.health -= randint(5, 15)
                    self.health -=randint(0,5)

        self.energy -=10


    def moveForward(self, speed=5):
        
        if self.energy > math.ceil(abs(speed)/2):
            if speed > 10:
                speed = 10
            elif speed < -10:
                speed = -10

            self._x += (-1)*speed * math.sin(math.radians(self.direction))
            self._y += (-1)*speed * math.cos(math.radians(self.direction)) 

            self.bordercheck(self)
            
            #pygame.mixer.Sound.play(tank_sound)
            self.energy-= math.ceil(abs(speed)/2)
        else:
            print("Not enough energy to moveForward")

    def bordercheck(self, obj):
            if obj.x() < 0:
                obj._x=0
            if obj.y() < 0:
                obj._y=0
            if obj.x() > 550:
                obj._x = 550
            if obj.y() > 550:
                obj._y = 550



    def turnLeft(self, speed=5):
        if self.energy > math.ceil(speed/2):
            if speed > 10:
                speed = 10
            if speed <=0:
                speed = 1
            self.direction+= speed
            self.surfImg = pygame.transform.rotate(self.OrigSurfImg, self.direction)
            self.energy-= math.ceil(speed/2)
        else:
            print("Not enough energy to turnLeft")


    def turnRight(self, speed=5):
        if self.energy > math.ceil(speed/2):
            if speed > 10:
                speed = 10
            if speed <=0:
                speed = 1
            self.direction-= speed
            self.surfImg = pygame.transform.rotate(self.OrigSurfImg, self.direction)
            self.energy-= math.ceil(speed/2)
        else:
            print("Not enough energy to turnRight")

    def fireProjectile(self, direction):
        if self.energy >= 10:
            ai1 = importlib.import_module("projectile")
            o = object("projectile", self._x,self._y, self.direction+direction, getSurfImg("projectile.png", 10, 10), ai1.AI(), 2)
            o.parentuid=self.uid
            objects.append(o) 
            #pygame.mixer.Sound.play(projectile_sound)
            self.energy -= 10
        else:
            print("Not enough energy to fire Projectile")

    def dropBomb(self, obj):
        if self.energy >=30:
            ai1 = importlib.import_module("bomb")
            o = object("bomb", self._x, self._y, self.getDirection(obj)+self.direction, getSurfImg("bomb.png", 30, 30), ai1.AI(), 4)
            o.parentuid=self.uid
            o.destinationx=obj.x()
            o.destinationy=obj.y()

            dis = self.getDistance(obj)
            o.velocity = dis/60

            objects.append(o)
            #pygame.mixer.Sound.play(bomb_sound)
            self.energy -= 40

    def repair(self, amount=3):
        if self.energy >= amount*4:
            self.health+= amount
            self.energy -= amount*4
        else:
            print("Not enough energy to repair ", amount, " points.")
    
    def shieldOn(self):
        if self.energy >=50 and self.shield==False:
            ai1 = importlib.import_module("shield")
            o = object("shield", self._x-10,self._y-10, self.direction, getSurfImg("shield.png", 70, 70), ai1.AI(), 3)
            o.parentuid=self.uid
            objects.append(o) 
            self.shield=True
            
        else:
            print("Not enough energy to activate shields.")


    def findEnemies(self):
        global objects
        enemies=[]
        for o in objects:
            if self.uid!=o.uid and o.type==1:
                enemies.append(o)
        return enemies

    def findAllObjects(self):
        global objects
        objs=[]
        for o in objects:
            if self.uid!=o.uid:
                objs.append(o)
        return objs

    def findClosestEnemy(self):
        global objects
        closestDistance = 5000
        closestEnemy=None
        for o in objects:
            if (self.uid!=o.uid and o.type==1):
                dis = math.sqrt((self._x-o.x())**2 + (self._y-o.y())**2)
                if  dis < closestDistance:
                    closestEnemy=o
                    closestDistance = dis
        return closestEnemy

    def getDirection(self, o):
        objdir = (-1)*(math.degrees(math.atan2((o.y()-self._y), (o.x()-self._x)))+90)
        #self.direction = self.direction % 360
        self.direction = self.normalizeDir(self.direction)
        #objdir = self.normalizeDir(objdir)
        newdir =objdir - self.direction
        newdir = self.normalizeDir(newdir)
        #print("selfdirection:", self.direction, " objdir:", objdir, " newdir:", newdir)

        return newdir

    def normalizeDir(self, dir):
        if dir > 360:
            dir = dir % 360
        elif dir < -360:
            dir = dir % 360
        if dir > 180:
            dir = dir-360
        elif dir < -180:
            dir = 360+ (dir)

        return dir

    def getDistance(self, o):
        dis = math.sqrt((self._x-o.x())**2 + (self._y-o.y())**2)
        return dis


    def projMoveForward(self):
        global objects
        self._x += (-1)*PROJECTILE_VELOCITY * math.sin(math.radians(self.direction))
        self._y += (-1)*PROJECTILE_VELOCITY * math.cos(math.radians(self.direction)) 

        enemy = None

        for o in objects:
            if o.type==1 and self.parentuid!=o.uid and self.getRect().colliderect(o.getRect()):
                enemy = o
            elif o.type==1 and self.parentuid==o.uid:

                if self.getDistance(o) > 250:
                    objects.remove(self)
                    enemy=None
                    break
            elif o.type==3 and self.getRect().colliderect(o.getRect()):
                enemy=None
                objects.remove(self)
                break
            
        if enemy!=None:
            enemy.health -= PROJECTILE_DAMAGE
            objects.remove(self)

        if self._x < 0 or self._x > 600:
            objects.remove(self)
        elif self._y < 0 or self._y > 600:
            objects.remove(self)

    def bombMoveForward(self):
        global objects

        self._x += (-1)*self.velocity * math.sin(math.radians(self.direction))
        self._y += (-1)*self.velocity * math.cos(math.radians(self.direction)) 

        if abs(self._x-self.destinationx) < 5 and abs(self._y-self.destinationy) < 5:
            for o in objects:
                if o.type==1 and self.parentuid!=o.uid and self.getRect().colliderect(o.getRect()):
                    o.health -= randint(5,20)
            
            objects.remove(self)


        
        #print(len(objects))

    def shieldMove(self):
        global objects

        for o in objects:
            #find parent
            if o.type==1 and self.parentuid==o.uid:
                if o.energy < 50:
                    objects.remove(self)
                    o.shield=False
                else:                     
                    self._x = o.x()-10
                    self._y = o.y()-10
                    o.energy -= 3
            elif o.type==2 and self.getRect().colliderect(o.getRect()):
                objects.remove(o)
                

        

    

def drawIntro(AIPlayers, ChosenPlayers):
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    screen.fill((0,0,0))
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf = largeText.render("HyCap AI Tank Game", 1, (100,255,100))
    TextRect = pygame.Rect(0,0,DISPLAY_WIDTH/2, DISPLAY_HEIGHT/4)
    TextRect.center = ((DISPLAY_WIDTH/2),(100))
    screen.blit(TextSurf, TextRect)

    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 30
    BUTTON_VERT_SPACING=10
    BUTTON_HORZ_SPACING=20
    FIRST_BUTTON_X = 50
    FIRST_BUTTON_Y=100
    btnNum=0
    col = 0
    row = 0
    for player in AIPlayers:
        
        button(player[0],FIRST_BUTTON_X+col*(BUTTON_WIDTH+BUTTON_HORZ_SPACING),FIRST_BUTTON_Y+row*(BUTTON_VERT_SPACING+BUTTON_HEIGHT),BUTTON_WIDTH,BUTTON_HEIGHT,GREEN,BRIGHT_GREEN,action=choosePlayer, param1=player[1], param2=player[0])

        btnNum+=1
        col = math.floor(btnNum/10)
        row = btnNum % 10

    btnNum = 0
    col = 3
    row=0
    for player in ChosenPlayers:
        button(player[0],FIRST_BUTTON_X+col*(BUTTON_WIDTH+BUTTON_HORZ_SPACING),FIRST_BUTTON_Y+row*(BUTTON_VERT_SPACING+BUTTON_HEIGHT),BUTTON_WIDTH,BUTTON_HEIGHT,GREEN,BRIGHT_GREEN,action=removePlayer, param1=btnNum)
        btnNum +=1
        row = btnNum

    row = 0
    col = 4
    button("Start >>",FIRST_BUTTON_X+col*(BUTTON_WIDTH+BUTTON_HORZ_SPACING),FIRST_BUTTON_Y+row*(BUTTON_VERT_SPACING+BUTTON_HEIGHT),BUTTON_WIDTH,BUTTON_HEIGHT,GREEN,BRIGHT_GREEN,action=startGame)

    pygame.display.update()
    clock.tick(15)

def choosePlayer(playerFile, playerName):
    global ChosenPlayers

    ChosenPlayers.append([playerName, playerFile])
    time.sleep(.5)
    #print(ChosenPlayers)
    #intro=False



def removePlayer(idxPlayer):
    global ChosenPlayers
    ChosenPlayers.pop(idxPlayer)
    time.sleep(.5)
    #print(ChosenPlayers)

def button(msg,x,y,w,h,ic,ac,action=None, param1=None, param2=None):
    btnText = pygame.font.Font("freesansbold.ttf",14)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x, y, w, h))
        if click[0] == 1 and action != None:
            if param1==None and param2==None:
                action()         
            elif param2==None:
                action(param1)
            else:
                action(param1, param2)
    else:
        pygame.draw.rect(screen, ic,(x,y, w, h))
    
    TextSurf = btnText.render(msg, 1, (200,0,0))
    TextRect = pygame.Rect(0,0,w, h)
    TextRect.center = ((x+w/2,y+h/2))
    screen.blit(TextSurf, TextRect)

def GoToIntro():
    global intro

    intro=True

def startGame():
    global intro, ChosenPlayers, objects
    intro=False

    numPlayer = 0
    for player in ChosenPlayers:
        ai1 = importlib.import_module(player[1])
        if numPlayer==0:
            x = 50
            y = 50
            direction = 270
        elif numPlayer==1:
            x = 550
            y = 550
            direction=90
        elif numPlayer==2:
            x = 50
            y = 550
            direction=270
        elif numPlayer==3:
            x = 550
            y = 50
            direction = 90
        elif numPlayer==4:
            x = 300
            y = 50
            direction = 0
        elif numPlayer==5:
            x = 300
            y = 550
            direction = 180
        elif numPlayer==6:
            x = 50
            y = 300
            direction = 270
        elif numPlayer==7:
            x = 550
            y = 300
            direction = 90
        
        objects.append( object(player[0], x,y, direction, getSurfImg(ai1.AI().image, TILESIZE, TILESIZE), ai1.AI(), 1)) 
        #print(player[0] + " loaded.")
        numPlayer +=1

def getSurfImg(imgFile, sizex, sizey):

    sImg = pygame.transform.scale(pygame.image.load("DozerBlue.png").convert_alpha(), (sizex, sizey))
    if imgFile != "":
        sImg = pygame.transform.scale(pygame.image.load(imgFile).convert_alpha(), (sizex, sizey))   
    #sImg = pygame.transform.rotate(self.sImg, direction*90)
    return sImg

def drawBattlefieldPygame():
    """draws the battlefield with Pygame"""
    global state, redsquares, bluesquares, bot1img, bot2img, namefont, textfont, ai1name, ai2name, uwimg, walls, rbulimg, bbulimg, textBlob

    #Get the display surface
    screen = pygame.display.get_surface()

    #Clear the screen
    screen.fill((0,0,0))
    
    #draw grid lines
    for i in range(1,10):
        pygame.draw.line(screen,(50,50,50),(0,i*(TILESIZE+LINEWIDTH*2)),(600,i*(TILESIZE+LINEWIDTH*2)),LINEWIDTH)
        pygame.draw.line(screen,(50,50,50),(i*(TILESIZE+LINEWIDTH*2),0),(i*(TILESIZE+LINEWIDTH*2),600),LINEWIDTH)

    #Objects
    numOfPlayers=0
    numOfAlivePlayers = 0
    for o in objects:
        if o.type==1:
            #Draw the robot's health bars
            text = font.render(o.name, True, WHITE) 
            if o.energy > 0:
                screen.blit(smallfont.render("Health", True, BLACK), pygame.Rect(600,22+ 45*numOfPlayers, 195, 10))
                pygame.draw.rect(screen,(255,255,0),((600,34+ 45*numOfPlayers),(int(o.energy*195/100.0),10)))

            if o.health >0:
                screen.blit(text, pygame.Rect(600,4+ 45*numOfPlayers, 195, 10))
                pygame.draw.rect(screen,(0,255,0),((600,22+ 45*numOfPlayers),(int(o.health*195/100.0),10)))
                screen.blit(o.surfImg, o.getRect())
                numOfAlivePlayers+=1
            else:
                objects.remove(o)
                
            

            screen.blit(smallfont.render("Energy", True, BLACK), pygame.Rect(600,34+ 45*numOfPlayers, 195, 10))
            numOfPlayers+=1
        elif o.type==2 or o.type==3 or o.type==4:
            screen.blit(o.surfImg, o.getRect())

    if numOfAlivePlayers==1:
        state="win"


    rectw = 600
    recth = 200
    NOTE_X = 0
    NOTE_Y = 600
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 30
    BUTTON1_X = 20
    BUTTON1_Y = DISPLAY_HEIGHT - 20 - BUTTON_HEIGHT
    BUTTON2_X = BUTTON1_X + BUTTON_WIDTH + 20
    BUTTON2_Y = BUTTON1_Y

    if state=="win":
        sInstructions = pygame.Surface((rectw, recth))
        sInstructions.fill(DARK_GRAY)
        rectInstructions=pygame.Rect(NOTE_X, NOTE_Y, rectw, recth)
        screen.blit(sInstructions, rectInstructions)
        drawText(screen, "Game Over!", (255,255,255), rectInstructions, instructionFont, aa=True, bkg=(255,255,255))
        button("Play Again",BUTTON1_X, BUTTON1_Y,BUTTON_WIDTH,BUTTON_HEIGHT,GREEN,BRIGHT_GREEN,action=GoToIntro)
    
    pygame.display.update()

    #add a delay between frames

    time.sleep(.2)


def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    """
    Takes the parameters of surface, which is where the text is going
    to be displayed,cf.surface for example and the text, which is
    whatever text we want to be displayed, the color, which is
    well, the color (0,0,0) input format, and the font is the location
    of the font you would like to use alternatively. This function
    then calculates the maximum we can fit in the size of our textbox
    and draws it to our surface with whichever parameters we give.
    """
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = 0
    # get the height of the font
    fontHeight = font.size('Tg')[1]
    # Split by newline.
    sp_text = text.split('\n')
    # Loop through text.
    for text in sp_text:
        # Old code to print to screen.
        while text:
            i = 1
            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break
            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1
            temp = text[:i].strip()
            # if we've wrapped the text, then adjust the wrap to the
            # last word
            if i < len(text):
                i = text.rfind(' ', 0, i) + 1
            # render the line and blit it to the surface
            if bkg:
                image = font.render(temp[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(temp[:i], aa, color)
            surface.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing
            # Remove leading and trailing newline and spaces.
            text = text[i:].strip() 

#----------------------   Game starts -------------------------------            

AIPlayers = []
ChosenPlayers = []
objects=[]
state=""
for f in  listdir():
    if isfile(f):
        if "AI" in f:
            name =f.replace("AI", "").replace(".py", "")
            file1 = f.replace(".py", "")
            AIPlayers.append([name, file1])

while True:

    if intro:
        drawIntro(AIPlayers, ChosenPlayers)

    else:
        drawBattlefieldPygame()
        
            
        for o in objects:
            
            try: # Prevent PythonBattle from crashing when AI code fails
                if state == "win":
                    break
                else:
                    if o.type==1:
                        o.energy+=ENERGY_CHARGE_PER_TURN
                        if o.energy > 100:
                            o.energy = 100
                        o.ai.turn()
                    else:
                        o.ai.turn()
            except Exception as e:
                print("failed with error:")
                print(e)

            
        # Capture all events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # key codes: https://www.pygame.org/docs/ref/key.html
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
