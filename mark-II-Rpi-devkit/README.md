# Mycroft Mark II - DevKit Prototype

## Kit Major Components
* Raspberry Pi 4
* SJ201 Daugherboard
* Audio Chamber
* Dual 5W Speaker drivers
* 4.2" Full Color touchscreen LCD
* Acrylic Enclosure
* Universal 12V power supply (USA, EU,UK, AUS, CCC)

## SJ201 Daughterboard
This prototype includes a custom daughterboard (SJ201) that integrates the components from the OTS prototype into a single PCB.

The SJ201 interfaces directly to the Raspberry Pi 4 via the 40-pin GPIO adding a high-quality speaker and microphone array, as well as LEDs and hardware inputs for non-voice interaction and feedback.

The part number SJ201 is derived from Mike’s “Simon Jester” alias in “The Moon is a Harsh Mistress”.

<img src="images/pcb-render-SJ-201-R6-back.png" width="500">
<img src="images/pcb-render-SJ-201-R6-front.png" width="500">

### SJ201 Major Components
* Audio Front End (XMOS XVF-3510) - for Microphone input processing
* I2S to Line Out (UDA1334ATS)
* 23W Amplifier (Texas Instruments TAS5806)
* 2 Digital MEMS Microphones (ST Micro MP34DT05)
* 12 RGB LEDs (WorldSemi WS2812B-MINI)
* 3 momentary buttons (volume up, volume down, action)
* 1 toggle switch (mic mute)
* ATtiny1614 - control LEDs, other I/O

### Technical Documentation
For technical details of these board see the 
* [SJ201-Datasheet](./KiCAD/SJ201-Raspberry%20Pi%204%20Daughterboard/README.md).

## New Form Factor
The SJ201 connects to the Raspberry Pi GPIO header at a 90 degree angle. This allows the microphone array and hardware inputs to be well positioned in the enclosure, whilst maintaining the simplicity of a direct connection to the main board. 

This interface makes a landscape form factor the most viable for this prototype. The blocking of the major components can be found within the [Mechanical CAD > MkII Blocking r2.zip](./Mechanical%20CAD/MkII%20Blocking%20r2.zip). 

<img src="./images/Mark II Mechanical Blocking.png" width="500">

## 3D Printable Case
STL files for 3D printing are available in this directory to print your own enclosure. For final construction you will also need threaded inserts and screws. For the inserts we recommend - Thread Diameter: M2.5; Pitch: 0.45; Outer Dia: 3.5mm; Length: 4mm. [Available here](https://www.amazon.com/uxcell-Threaded-Insert-Embedment-Knurled/dp/B01N8QX6RX?pd_rd_w=dPC71&content-id=amzn1.sym.deffa092-2e99-4e9f-b814-0d71c40b24af&pf_rd_p=deffa092-2e99-4e9f-b814-0d71c40b24af&pf_rd_r=6CG7999KDE4S7JZ48PGQ&pd_rd_wg=tgvPC&pd_rd_r=2c2f179c-25d6-434a-a10d-e7da619cf53c&pd_rd_i=B01N8QX6RX&psc=1&ref_=pd_bap_d_rp_1_t).

Complete assembly instructions can be found [here on Instructables](https://www.instructables.com/Mycroft-Mark-II-3D-Printed-Developer-Kit-Assembly/).

## Our open hardware principles
* **Copy our designs** – build your own Mycroft Mark 2 - Raspberry Pi Edition or its individual parts
* **Modify our designs** – remixing is encouraged
* **Sell products based on our designs** – commercial use is permitted
* **Always keep the open license** – contribute your output back to the community
* **Credit the original author(s)** – like they do in science

## Feedback or ideas

We are always keen to hear from the community about ways to improve these designs. Whether you're a hacker, maker, engineer, or something else - join us in the:
- [Community Forums](https://community.mycroft.ai)
- [Community Chat](https://chat.mycroft.ai)
- or email us at [dev@mycroft.ai](mailto:dev@mycroft.ai)
