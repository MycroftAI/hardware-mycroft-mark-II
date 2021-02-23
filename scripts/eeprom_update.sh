#!/bin/bash

# Copyright 2020 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#  2020-12-17 - J.M. - Initial Release
#  2021-02-19 - J.M. - Improved Docs
#
#  This script is intended to run headless and uses the LEDS for communication.
#  To use it you need to have the WiFi setup on the Linux device.
#
#  5x Red LED Blink = Not On Network
#  5x Green LED Blink = Updating
#  5x Both Red and Green LED Blink = EEPROM Updated
#
#  This script is updating the EEPROM and needs to be run as root.
#
#  To run it automagically at boot ( on Raspbian only ) 
#  Copy this script to /etc/eeprom_update.sh
#  Chmod the script to executable> chmod +x /etc/eeprom_update.sh
#  Edit /etc/rc.local
#  Add: /etc/eeprom_update.sh
#
#  Make sure your WiFi creds ( if using WiFi ) are up to date and the device connects to the network.
#  You can do this by editing /etc/wpa_supplicant/wpa_supplicant.conf
#
#  Reboot
#
#  After this is done you will have a card that  connects to the network, checks the eeprom version and does the update automatically.
#  Total time for the update should be around 90 seconds.
#

# Make sure we are running as root
echo "eeprom_update.sh: Checking to see if running as root."
if [ "$EUID" -ne 0 ]; then
  echo "eeprom_update.sh: Not running as root.  Exiting."
  exit
fi
echo "eeprom_update.sh: Running as root."

# Shut off LEDS
echo "eeprom_update.sh: Disabling LEDS."
echo none > /sys/class/leds/led0/trigger
echo none > /sys/class/leds/led1/trigger
echo 0 > /sys/class/leds/led0/brightness
echo 0 > /sys/class/leds/led1/brightness

# Check for a network connection, if we don't have one flash LEDS and write error log.
echo "eeprom_update.sh: Checking for active Internet connection."
if [ ` ping -c 1 -q google.com >&/dev/null; echo $?` != 0 ]; then
  echo "eeprom_update.sh: No Internet connection found.  Exiting."
  echo "ERROR: Device is not on the network." >> /var/log/syslog
  for i in 1 2 3 4 5; do
    echo 1 > /sys/class/leds/led1/brightness
    sleep 1
    echo 0 > /sys/class/leds/led1/brightness
	sleep 1
  done
  exit
fi
echo "eeprom_update.sh: Internet connection found."

# Install rpi-eeprom if necessary
echo "eeprom_update.sh: Checking for rpi-eeprom package."
if [ `dpkg -s rpi-eeprom | grep -c "install ok installed"` != 1 ]; then
  echo "eeprom_update.sh: No rpi-eeprom package found.  Installing."
  apt-get install rpi-eeprom -y
else
  echo "eeprom_update.sh: rpi-eeprom package found."
fi

# Set the device to the stable branch
echo "eeprom_update.sh: Setting EEPROM channel to stable"
echo 'FIRMWARE_RELEASE_STATUS="stable"' > /etc/default/rpi-eeprom-update

# Check for update
echo "eeprom_update.sh: Checking EEPROM version."
if [ `rpi-eeprom-update | grep -c "BOOTLOADER: update available"` == 1 ]; then
  echo "eeprom_update.sh: Update available.  Installing"
  rpi-eeprom-update -a
  for i in 1 2 3 4 5; do
    echo 1 > /sys/class/leds/led0/brightness
    sleep 1
    echo 0 > /sys/class/leds/led0/brightness
	sleep 1
  done
  reboot
elif [ `rpi-eeprom-update | grep -c "BOOTLOADER: up-to-date"` == 1 ]; then
    echo "eeprom_update.sh: No updates available.  Shutting down."
  # Blink the Lights Together for 5 seconds, then shutdown
  for i in 1 2 3 4 5
  do
    echo 0 > /sys/class/leds/led1/brightness
    echo 0 > /sys/class/leds/led0/brightness
    sleep 1
    echo 1 > /sys/class/leds/led1/brightness
    echo 1 > /sys/class/leds/led0/brightness
	sleep 1
  done
  shutdown -h now
fi
