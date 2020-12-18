#!/bin/bash
#
#  2020-12-17 - J.M - Initial Release
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
