'''
sudo apt-get update && sudo apt-get install python3-gpiozero python-gpiozero


run with:
sudo python3 gpiotest.py

'''

from gpiozero import Button
from time import sleep

button = []
button.append(Button(22))
button.append(Button(23))
button.append(Button(24))
button.append(Button(25))


while True:
    for b in button:
        print("%d: " % (b.pin.number), end = '')
        if b.is_pressed:
            print("ON  " , end = '')
        else:
            print("OFF ", end = '')
    print("")
    sleep(1)
