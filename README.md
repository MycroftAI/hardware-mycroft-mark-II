# Mycroft Mark II - Rpi Prototype Hardware
*Mycroft's Mark II Raspberry Pi 3 based prototype designs*  
*⛵️ Note that this repository is a work-in-progress. It will be updated and improved on over time.*

![Exploded view of prototype](https://raw.githubusercontent.com/MycroftAI/hardware-mycroft-mark-II-rpi/master/Mark%20II%20Rpi3%20r2%20Assembly%20diagram_sm.png?token=AF3P7DRJZP6BDCAP2DEV3C26HSL2W)

## Our open hardware principles
* **Copy our designs** – build your own Mycroft Mark 2 - Raspberry Pi Edition or its individual parts
* **Modify our designs** – remixing is encouraged
* **Sell products based on our designs** – commercial use is permitted
* **Always keep the open license** – contribute your output back to the community
* **Credit the original author(s)** – like they do in science

## License
We're open-sourcing all our designs under the CERN Open Hardware License, which is one of the open hardware licenses recommended by OSHWA, the Open Source Hardware Association. The release involves every single piece of our design except components we have no control over, like the Raspberry Pi. We've also joined the Open Source Hardware Certification Program.

[![Open Source Hardware Logo](https://github.com/MycroftAI/hardware-mycroft-mark-1/blob/master/oshw.png "OSHW")](https://certification.oshwa.org/)

## Instructions
### Getting Started
To begin you need to purchase the parts listed in the [Bill of Materials (BOM)](BOM.md). The Mark II Raspberry Pi 3 prototype consists of 7 major components and many smaller components needed to connect them together. The 7 major components are:

* **Raspberry Pi 3B (not 3B+ or 4 yet)**
* **Seeed Studios Respeaker Mic Array v2.0**
* **Waveshare 4.3" IPS 800x480 LCD**
* **Drok 12v to 5v 5A buck converter part # 200217**
* **Adafruit 20W Stereo class D Amplifer - MAX9744**
* **A pair of Tymphany Peerless TC5FC07-04 speaker drivers**
* **A set of 3D printed Mark II Raspbery Pi 3 prototype parts**

![System diagram](https://raw.githubusercontent.com/MycroftAI/hardware-mycroft-mark-II-rpi/master/Mark%20II%20Rpi3%20r2%20System%20diagram_sm.png?token=AF3P7DWIXOV57HQI6RJZSZ26HSLWO)

### Creating the Custom Cable Assemblies
To connect the Raspberry Pi, Respeaker Mic Array V2.0, and Adafruit Amplifer two custom cable assemblies are required. The first cable assembly allows the Respeaker Mic Array to communicate to the Raspberry Pi via USB and to the Amplifer via analog stereo audio. To create the Microphone cable assembly follow this video guide:  
[![Microphone cable assembly video guide](https://img.youtube.com/vi/UepmmYCgYgI/0.jpg)](https://youtu.be/UepmmYCgYgI)

The second cable assembly connects the i2c interface from the GPIO on the Raspberry Pi to the Adafruit amplifier. This allows the Raspberry Pi to digitally control the gain on the amplifier. To create the GPIO to i2c cable assembly follow this video guide:  
[![GPIO to i2c cable assembly video guide](https://img.youtube.com/vi/yoYU8CrY8kU/0.jpg)](https://youtu.be/yoYU8CrY8kU).

The connectors and ribbon cables required to build both of these cable assemblies are listed in the BOM.

### 3D Printing the Housing
The parts for the housing are shared as both STL and STP files in the CAD directory. Our internal prototypes are printed on a Formlabs SLA 3D printer but these can be adapted for printing on an FFF machine as well. You will need to orient the parts and slice them based on the requirements of your printer.

## Contact
If you are doing, or planning to do, something interesting with our designs, or if you just have a question regarding the files, get in touch with our Chief of Design Derick! (He was the one who designed Mycroft Mark II’s enclosure.)

![alt text](https://github.com/MycroftAI/hardware-mycroft-mark-1/blob/master/Derick.png "Derick")

**Derick Schweppe**  
Mycroft AI’s Chief of Design  
derick.schweppe@mycroft.ai
