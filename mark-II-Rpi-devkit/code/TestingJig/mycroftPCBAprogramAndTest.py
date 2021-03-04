#!/usr/bin/env python
'''

install:


    sudo apt-get -y install libfreetype6-dev
    sudo apt-get -y install -y libsdl2-dev
    sudo apt-get -y install apt-file
    sudo apt-file update
    sudo apt-get -y install libsdl1.2-dev
    
    
    sudo apt-get -y install python3-pygame
    
    
    sudo pip3 install pygame_gui
    sudo apt-get -y install python3-smbus

    sudo pip3 install tailer    
    
install Arduino-CLI
    curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh 
add megaTinyCore to list
    /home/mycroft/bin/arduino-cli config init 
    sudo /home/mycroft/bin/arduino-cli config init 
    nano -w /home/mycroft/.arduino15/arduino-cli.yaml
    board_manager:
        additional_urls: [http://drazzy.com/package_drazzy.com_index.json]
    /home/mycroft/bin/arduino-cli core update-index
    /home/mycroft/bin/arduino-cli core install megaTinyCore:megaavr
    
    
    sudo nano -w /root/.arduino15/arduino-cli.yaml
    board_manager:
        additional_urls: [http://drazzy.com/package_drazzy.com_index.json] 
    sudo /home/mycroft/bin/arduino-cli core update-index
    sudo /home/mycroft/bin/arduino-cli core install megaTinyCore:megaavr
 
cat /opt/mycroft/startup.sh
    #!/bin/bash
    source /opt/mycroft/.venv/bin/activate
    sudo chown -R mycroft:mycroft /var/log/mycroft
    #/opt/mycroft/pairing.sh &
    #/opt/mycroft/./start-mycroft.sh all 
    sudo -u mycroft screen -A -m -d -S precise_test sudo python3 /home/mycroft/PCBtests/precise_test.py
    sudo -u mycroft screen -A -m -d -S pygame sudo python3 /home/mycroft/PCBtests/mycroftPCBAprogramAndTest.py
run:
(.venv) mycroft@localhost:~$ sudo python3 /home/mycroft/PCBtests/mycroftPCBAprogramAndTest.py

'''
import pygame
import pygame_gui
from  pygame.locals import *
import smbus
import subprocess
#from precise_runner import PreciseEngine, PreciseRunner
from time import sleep
import os
import tailer
import datetime
import RPi.GPIO as gpio

result = subprocess.getoutput('sudo /opt/mycroft/stop-mycroft.sh')
print(result)


# Start precise externally before running script

#subprocess.getoutput('sudo python3 /home/mycroft/PCBtests/precise_test.py &')
#print("precise_test: %s" % result)
#pygame.mixer.pre_init(frequency=44100)

pygame.quit() 

pygame.init()
#pygame.mixer.init(frequency=44100)
pygame.font.init()
print("pygame started")



class MycroftPCBATest:
    font_path = "/opt/mycroft/.venv/lib/python3.8/site-packages/sphinx_rtd_theme/static/fonts/RobotoSlab-Regular.ttf"
    is_running = True
    screen          = ''
    attiny_I2C_Pass = False
    XMOS_I2C_Pass   = False
    TAS_I2C_Pass    = False
    Speakers_Pass   = False
    Mics_Pass       = False
    BtnVolUp_Pass   = False
    BtnVolDown_Pass = False
    BtnAction_Pass  = False
    SwitchMic_Pass  = False
    micStatusTest  = False
    SerialNum       = ""
    SerialNumLast   = ""
    SerialNum_Pass  = False
    
    arduinoCompiled = False
    VolUpPin        = 22
    VolDownPin      = 23
    ActionPin       = 24
    MicSwPin        = 25
    boxLeft         = 0
    boxTop          = 0
    boxLeftStart    = 10
    boxTopStart     = 30
    bus = ''
    rotation        = 0
    renderingScreen = True
    
    startTesting    = False

    def __init__(self):  
        # hide the mouse cursor
        #print("init")
        pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0)) 
        #print("pygame.mouse.set_cursor")
        #pygame.display.set_caption('Mycroft PCBA Test')
        #print("pygame.display.set_caption")
        gpio.setmode(gpio.BCM)
        gpio.setup(self.VolUpPin  , gpio.IN)
        gpio.setup(self.VolDownPin, gpio.IN)
        gpio.setup(self.ActionPin , gpio.IN)
        gpio.setup(self.MicSwPin  , gpio.IN)
        #gpio.add_event_detect(self.VolUpPin  , gpio.FALLING,  self.event_callback)
        #gpio.add_event_detect(self.VolDownPin, gpio.FALLING,  self.event_callback)
        #gpio.add_event_detect(self.ActionPin , gpio.FALLING,  self.event_callback)
        #gpio.add_event_detect(self.MicSwPin  , gpio.FALLING,  self.event_callback)
        
        self.compileArduino()
        #print ("Touch screen to start")
        self.drawScreen()
        #print ("Draw Screen")
        #pygame.display.flip() 
         
    def startupProcedure(self):
        self.startTesting    = True
        self.printPassFail()
        result = subprocess.getoutput('sudo /home/mycroft/PCBtests/start-xmos-kevin.sh &')
        #print("startXmos %s" % result)

        self.programATtiny()
        
        self.bus = smbus.SMBus(1) # 1 indicates /dev/i2c-1

        self.checkI2C()
        self.testSpeakers()
        if(self.Mics_Pass == False):
            self.testSpeakers()

        self.printPassFail()
        self.drawScreen()
        
    def reset(self):
        
        self.attiny_I2C_Pass = False
        self.XMOS_I2C_Pass   = False
        self.TAS_I2C_Pass    = False
        self.Speakers_Pass   = False
        self.Mics_Pass       = False
        self.BtnVolUp_Pass   = False
        self.BtnVolDown_Pass = False
        self.BtnAction_Pass  = False
        self.SwitchMic_Pass  = False
        self.micStatusTest   = False
        self.SerialNum_Pass  = False
        self.SerialNumLast   = ""
        
    def startProgramming(self): 
        self.reset()
        self.resetSerialNum()
        self.startupProcedure()
        
    def checkI2C(self):
        self.attiny_I2C_Pass = False
        self.TAS_I2C_Pass    = False
        for device in range(128):
            try:
                #device = 0x04
                self.bus.read_byte(device)
                print(hex(device))
                if(device == 0x04 ):
                    self.attiny_I2C_Pass = True
                if(device == 0x2f ):
                    self.TAS_I2C_Pass    = True
            except: # exception if read_byte fails
                pass
                #print("Fail %s" % hex(device))
            
        result = subprocess.getoutput('/usr/sbin/vfctrl_i2c GET_VERSION')
        print(result)
        if("GET_VERSION:v4.1.0" in result ):
            self.XMOS_I2C_Pass = True
        if(self.attiny_I2C_Pass == False and self.TAS_I2C_Pass == False):
            self.reset()
    '''
        Burn bootloader and program ATtiny1614
    '''
    def programATtiny(self):
        
        result = subprocess.getoutput('sudo /home/mycroft/bin/arduino-cli burn-bootloader -b megaTinyCore:megaavr:atxy4 --programmer atmelice_updi')
        print(result)  
        
        self.compileArduino()
        
        result = subprocess.getoutput('sudo /home/mycroft/bin/arduino-cli upload --fqbn megaTinyCore:megaavr:atxy4 --programmer atmelice_updi /home/mycroft/PCBtests/mark2_attiny1614.ino/mark2_attiny1614.ino')
        print(result)
        
        self.sendSerialNum()
        
        return True
    def compileArduino(self):       
        if(self.arduinoCompiled == False):
            result = subprocess.getoutput('sudo -u mycroft /home/mycroft/bin/arduino-cli compile --fqbn megaTinyCore:megaavr:atxy4 /home/mycroft/PCBtests/mark2_attiny1614.ino/mark2_attiny1614.ino')
            print(result)        
            self.arduinoCompiled = True
    '''
        Play an audio WAV and test the microphone
        Look into the heymycroft.log file to see if a recent activation has been recorded
    '''    
    def testSpeakers(self):
        micStatus = gpio.input(self.MicSwPin)

        print("mic status %d" % micStatus)
        if(micStatus == 1):  # mic must be switched to Zero to record
            print("Mic switch is in Off position")
            return False        
        
        listCommands = ["GET_VERSION",
                "SET_CH1_BEAMFORM_ENABLE 0",
                "SET_ALT_ARCH_ENABLED 0",
                #"SET_ADAPTATION_CONFIG_AEC 2"
                ]  #temporarily turn off AEC and ADEC

        for i in listCommands :
            try:
                result = subprocess.getoutput('/usr/sbin/vfctrl_i2c %s' % i)
                print(result.split("\n")[1])
            except:
                pass
        
        #play audio        
        result = subprocess.getoutput('aplay /home/mycroft/PCBtests/heymycroft-kevin1.wav')
        print(result)
        sleep(1.5)
        tail = tailer.tail(open('/home/mycroft/PCBtests/heymycroft.log'),1)
        dateString = tail[0][0:19]
        print(dateString)      #2021-02-02 00:28:39
        date_time_obj = datetime.datetime.strptime(dateString, '%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.now()
        secondsSinceLastActivation = (now - date_time_obj).total_seconds()
        print(secondsSinceLastActivation)
        
        if(secondsSinceLastActivation < 2.0):
            self.Speakers_Pass   = True
            self.Mics_Pass       = True
            return True
        return False
        
    '''
        Draw stuff on the screen
    '''    
    def drawScreen(self):
        #print("pygame drawscreen start")
        self.renderingScreen = True
        self.screen = pygame.display.set_mode((800, 480))
        #print("pygame drawscreen start2")
        
        #print("pygame.display.set_mode((800, 480))")
        background = pygame.Surface((800, 480))
        #print("pygame drawscreen start3")
        #print("pygame.Surface")
        background.fill(pygame.Color('#FFFFFF'))
        manager = pygame_gui.UIManager((800, 600))
        self.screen.blit(background, (0, 0))
        #print("pygame background")
        font_size = 32
        fontObj = pygame.font.Font(self.font_path, font_size)

        RED   = (204,0,  0)
        GREEN = (0,  153,51)
        BLUE  = (0,  0,  128)
        BLACK = (0,  0,  0)
        WHITE = (255,255,255)

        # draw title
        w, h = pygame.display.get_surface().get_size()
        text = fontObj.render("Mycroft PCBA Test", True, (0,0,0))
        text_rect = text.get_rect(center=(w//2, 12))
        self.screen.blit(text, text_rect)      
        #print("pygame screen.blit")
        attiny_I2C_Color = RED
        XMOS_I2C_Color   = RED
        TAS_I2C_Color    = RED
        Speakers_Color   = RED
        Mics_Color       = RED
        BtnVolUp_Color   = RED
        BtnVolDown_Color = RED
        BtnAction_Color  = RED
        SwitchMic_Color  = RED
        
        Serialnum_Color  = RED
         
        if(self.attiny_I2C_Pass):
            attiny_I2C_Color = GREEN
        if(self.XMOS_I2C_Pass):
            XMOS_I2C_Color   = GREEN
        if(self.TAS_I2C_Pass):
            TAS_I2C_Color    = GREEN
        if(self.Speakers_Pass):
            Speakers_Color   = GREEN
        if(self.Mics_Pass):
            Mics_Color       = GREEN
        if(self.BtnVolUp_Pass):
            BtnVolUp_Color   = GREEN
        if(self.BtnVolDown_Pass):
            BtnVolDown_Color = GREEN
        if(self.BtnAction_Pass):
            BtnAction_Color  = GREEN
        if(self.SwitchMic_Pass):
            SwitchMic_Color  = GREEN
            
        serialText = "Serial Num"
        if(self.SerialNum_Pass):
            Serialnum_Color  = GREEN
            serialText = "#: %s " % self.SerialNumLast


        self.boxLeft = self.boxLeftStart
        self.boxTop  = self.boxTopStart
        #print("pygame rect")
        pygame.draw.rect(self.screen,attiny_I2C_Color,(self.getTL())) 
        pygame.draw.rect(self.screen,XMOS_I2C_Color  ,(self.getTL())) 
        pygame.draw.rect(self.screen,TAS_I2C_Color   ,(self.getTL())) 
        pygame.draw.rect(self.screen,Speakers_Color  ,(self.getTL()))
        pygame.draw.rect(self.screen,Mics_Color      ,(self.getTL())) 
        pygame.draw.rect(self.screen,BtnVolUp_Color  ,(self.getTL()))
        pygame.draw.rect(self.screen,BtnVolDown_Color,(self.getTL()))
        pygame.draw.rect(self.screen,BtnAction_Color ,(self.getTL()))
        pygame.draw.rect(self.screen,SwitchMic_Color ,(self.getTL()))
        pygame.draw.rect(self.screen,Serialnum_Color ,(self.getTL()))
        
        
        self.boxLeft = self.boxLeftStart
        self.boxTop  = self.boxTopStart
        
        # render text
        font_size = 20
        fontObj = pygame.font.Font(self.font_path, font_size)
        self.screen.blit(fontObj.render("ATtiny I2C", 1, WHITE), (self.getTL(True)))
        self.screen.blit(fontObj.render("XMOS I2C", 1, WHITE), (self.getTL(True)))  
        self.screen.blit(fontObj.render("TAS_I2C", 1, WHITE), (self.getTL(True)))  
        self.screen.blit(fontObj.render("Speakers", 1, WHITE), (self.getTL(True)))  
        self.screen.blit(fontObj.render("Mics", 1, WHITE), (self.getTL(True)))  
        self.screen.blit(fontObj.render("BtnVolUp", 1, WHITE), (self.getTL(True)))  
        self.screen.blit(fontObj.render("BtnVolDown", 1, WHITE), (self.getTL(True)))  
        self.screen.blit(fontObj.render("Btn Action", 1, WHITE), (self.getTL(True)))  
        self.screen.blit(fontObj.render("Switch Mic", 1, WHITE), (self.getTL(True)))  
        self.screen.blit(fontObj.render(serialText, 1, WHITE), (self.getTL(True)))  
             
        #print("pygame screen.blit - finished")
        self.screen.blit(pygame.transform.rotate(self.screen, 180), (0, 0)) 
        #print("pygame transform.rotate")        
        #self.rotation = 180 + self.rotation
        #if(self.rotation >= 360):
        #    self.rotation = 0
        #    self.screen.blit(pygame.transform.rotate(self.screen, 180), (0, 0)) 
        
        self.renderingScreen = False
        
        
    def isRenderingScreen(self):
        return self.renderingScreen
    '''
        Get top left for each of the boxes
    '''
    def getTL(self, centered = False):
        width   = 170
        height  = 100
        boxTop  = self.boxTop
        boxLeft = self.boxLeft
        
        self.boxTop  = self.boxTop + height + 10
        if(self.boxTop + height >= 480):
            self.boxTop  = self.boxTopStart
            self.boxLeft = self.boxLeft + width + 10
        if(centered):
            return (int(boxLeft + 5),int(boxTop + height/ 2 - 10))
        return (int(boxLeft),int(boxTop),int(width),int(height))
        
    '''
        Print out pass/fail instead of True/False
    '''
    def pf(self,someBool): 
        if someBool:
            return "Pass"
        
        return "Fail"
    def checkGPIO(self):
        
        if(gpio.input(self.VolUpPin) == False):
            if(self.BtnVolUp_Pass == False):
                self.BtnVolUp_Pass    = True
                self.printPassFail()
            self.BtnVolUp_Pass    = True
            
        if(gpio.input(self.VolDownPin) == False):
            if(self.BtnVolDown_Pass == False):
                self.BtnVolDown_Pass  = True
                self.printPassFail()
            self.BtnVolDown_Pass  = True
            
        if(gpio.input( self.ActionPin) == False):
            if(self.BtnAction_Pass == False):
                self.BtnAction_Pass   = True
                self.printPassFail()
            self.BtnAction_Pass   = True
        
        micStatus = gpio.input(self.MicSwPin)        
        if(micStatus == False and self.micStatusTest == True):
            if(self.SwitchMic_Pass == False):
                self.SwitchMic_Pass   = True 
                self.printPassFail()
            self.SwitchMic_Pass   = True  
        # make sure the mic switch is returned to Mic Record
        if(micStatus == True):
            self.micStatusTest = True
            if(self.SwitchMic_Pass == True):
                self.SwitchMic_Pass = False
                self.checkI2C()                
                self.printPassFail()
            self.SwitchMic_Pass   = False   
            
        return False
        
    '''
        Event callback caused runtime errors and bugs
    '''
    def event_callback(self, channel):
        #if(self.startTesting):
        print("Callback channel: %s" % channel)
        
        if(channel == self.VolUpPin):
            self.BtnVolUp_Pass    = True
            
        if(channel == self.VolDownPin):
            self.BtnVolDown_Pass  = True
            
        if(channel == self.ActionPin):
            self.BtnAction_Pass   = True
            
        if(channel == self.MicSwPin):
            self.SwitchMic_Pass   = True  
        micStatus = gpio.input(self.MicSwPin)
        
        if(micStatus == 1):
            self.SwitchMic_Pass   = False   
            
        self.printPassFail()
        return False
    
    def checkAllPassFail(self):
        if( self.attiny_I2C_Pass and
            self.XMOS_I2C_Pass   and
            self.TAS_I2C_Pass    and 
            self.Speakers_Pass   and
            self.Mics_Pass       and 
            self.BtnVolUp_Pass   and
            self.BtnVolDown_Pass and
            self.BtnAction_Pass  and
            self.SwitchMic_Pass  and
            self.SerialNum_Pass ):  
            return True
        return False
        
    def printPassFail(self):
        print("---------------------------------------------")
        print("ATtiny I2C   : %s" %(self.pf(self.attiny_I2C_Pass)))
        print("XMOS I2C     : %s" %(self.pf(self.XMOS_I2C_Pass)))
        print("TAS amp I2C  : %s" %(self.pf(self.TAS_I2C_Pass)))
        print("Speakers     : %s" %(self.pf(self.Speakers_Pass)))   
        print("Mics         : %s" %(self.pf(self.Mics_Pass)))   
        print("Btn Vol Up   : %s" %(self.pf(self.BtnVolUp_Pass)))   
        print("Btn Vol Down : %s" %(self.pf(self.BtnVolDown_Pass)))   
        print("Btn Action   : %s" %(self.pf(self.BtnAction_Pass)))   
        print("Switch Mic   : %s" %(self.pf(self.SwitchMic_Pass)))   
        print("Serial Num   : %s %s" %(self.pf(self.SerialNum_Pass) , self.SerialNumLast)   )
        
        print("---------------------------------------------")
        if(self.checkAllPassFail()):
            print("********  All Systems Pass! ************")
        self.drawScreen()
    def sendSerialNum(self):
        if(len(self.SerialNum) >= 8):
            result = subprocess.getoutput('i2cset -y 1 0x04 0xE1  0x%s' % self.SerialNum[0:2])
            result = subprocess.getoutput('i2cset -y 1 0x04 0xE2  0x%s' % self.SerialNum[2:4])
            result = subprocess.getoutput('i2cset -y 1 0x04 0xE3  0x%s' % self.SerialNum[4:6])
            result = subprocess.getoutput('i2cset -y 1 0x04 0xE4  0x%s' % self.SerialNum[6:8])
            print("Wrote serial to ATtiny")
            self.SerialNum_Pass = True
            self.SerialNumLast = self.SerialNum
            self.printPassFail()
        self.printSerilNumAttiny()
        self.resetSerialNum()
        
    def printSerilNumAttiny(self):
        sleep(0.25)
        result = subprocess.getoutput('i2cget -y 1 0x04 0xE1  ' )
        print(result)
        result = subprocess.getoutput('i2cget -y 1 0x04 0xE2  ' )
        print(result)
        result = subprocess.getoutput('i2cget -y 1 0x04 0xE3  ' )
        print(result)
        result = subprocess.getoutput('i2cget -y 1 0x04 0xE4  ' )
        print(result)
    def resetSerialNum(self):
        self.SerialNum = ""
        
    def setSerialNum(self, num):
        if(len(self.SerialNum) >= 8):
            self.resetSerialNum()
        self.SerialNum = self.SerialNum + num
        
    def printSerialNum(self):
        print(self.SerialNum)
        
            
    def is_running(self):
        return is_running

mpcb = MycroftPCBATest()

lastPos = (9999,9999)

while mpcb.is_running:

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            mpcb.is_running = False
        if event.type == MOUSEBUTTONDOWN or event.type == MOUSEMOTION:
            pos = event.pos
            print(pos)
            if(lastPos[0] != pos[0] and lastPos[1] != pos[1]):
                mpcb.startProgramming() #restart test
            lastPos = pos
            
        if event.type == KEYDOWN :      
            key = event.key
            mod = event.mod
            unicode = event.unicode
            scancode = event.scancode
            if(key != 13 and key != 304):
                #print("Keypress: %s %s %s %s " %(key, mod, unicode, scancode))
                mpcb.setSerialNum(unicode)
                #mpcb.printSerialNum()
            if(key == 13):
                mpcb.printSerialNum()
                mpcb.sendSerialNum()
                
                
    if(mpcb.isRenderingScreen() == False):
        pygame.display.update()
    mpcb.checkGPIO()
    sleep(0.1)
