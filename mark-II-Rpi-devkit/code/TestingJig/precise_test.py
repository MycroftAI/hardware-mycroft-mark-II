#!/usr/bin/env python3
'''

install directions:
    sudo apt-get -y remove libportaudio2
    sudo apt-get -y install libasound2-dev
    git clone -b alsapatch https://github.com/gglockner/portaudio
    
    cp /home/mycroft/PCBtests/pa_linux_alsa.c /home/mycroft/portaudio/src/hostapi/alsa/pa_linux_alsa.c
    cd portaudio
    ./configure && make
    sudo make install
    sudo ldconfig
    cd ..


   wget http://files.portaudio.com/archives/pa_stable_v190600_20161030.tgz
   tar xvzf pa_stable_v190600_20161030.tgz
   cd portaudio/
   cp /home/mycroft/PCBtests/pa_linux_alsa.c  /home/mycroft/portaudio/src/hostapi/alsa/pa_linux_alsa.c
   ./configure
   make
   sudo make install
   ldconfig
   
   sudo pip3 install precise-runner
   
   
   
run:
   sudo python3 /home/mycroft/PCBtests/precise_test.py
'''

from precise_runner import PreciseEngine, PreciseRunner
from time import sleep
import os
import logging
logging.basicConfig(filename='/home/mycroft/PCBtests/heymycroft.log', format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

logging.warning('File-started')

def on_activation():
    os.system("aplay /opt/mycroft/mycroft/res/snd/start_listening.wav")
    print("\n *** Hello! *** \n")
    logging.warning('activated')


def on_prediction(confidence):
    #print(confidence)
    #logging.warning(confidence)
    return True
trigger_lvl = 3

engine = PreciseEngine('/home/mycroft/.mycroft/precise/precise-engine/precise-engine', '/home/mycroft/.mycroft/precise/hey-mycroft.pb')

#runner = PreciseRunner(engine, on_activation=lambda: print('hello'))
runner = PreciseRunner(engine, trigger_lvl, sensitivity=0.5, on_activation=on_activation, on_prediction=on_prediction)

runner.start()

# Sleep forever
while True:
    #print("1")
    sleep(1000)


