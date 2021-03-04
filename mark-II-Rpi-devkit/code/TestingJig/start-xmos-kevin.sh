#!/bin/bash
source /opt/mycroft/.venv/bin/activate

#/usr/bin/setup_mclk
#/usr/bin/setup_bclk
#sleep 1
#arecord -d 1 > /dev/null 2>&1 || true
#aplay dummy > /dev/null 2>&1 || true
#sleep 1
sudo -u '#1050' gpio -g mode 16 out || true
sudo -u '#1050' gpio -g mode 27 out || true
sudo -u '#1050' gpio -g write 16 1 || true
sudo -u '#1050' gpio -g write 27 1 || true
sleep 1

echo "GPIO Set"
/opt/mycroft/.venv/bin/python /opt/mycroft/send_image_from_rpi.py --direct /opt/mycroft/app_xvf3510_int_spi_boot_v4_1_0.bin || true
echo "XMOS Sent"
sleep 1

python /home/mycroft/PCBtests/tas5806Test-kevin.py || true
#python /opt/mycroft/led_test.py || true
