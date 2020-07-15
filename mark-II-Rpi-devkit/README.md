# Mycroft Mark II - DevKit Prototype

*⛵️ Note that this repository is a work-in-progress. It will be updated and improved on over time.*

The second iteration of the Mark II prototype. 

## SJ201 Daughterboard
This prototype includes a custom daughterboard (SJ201) that integrates the components from the OTS prototype into a single PCB (SJ201).

The SJ201 interfaces directly to the Raspberry Pi 4 via the 40-pin GPIO adding a high-quality speaker and microphone array, as well as LEDs and hardware inputs for non-voice interaction and feedback.

The SJ201 can also be used as a USB microphone array with barge-in support. In this configuration the amplifiers do not work as the USB port cannot supply the required power.

The part number SJ201 is derived from Mike’s “Simon Jester” alias in “The Moon is a Harsh Mistress”.

<img src="./images/pcb-render-v0.60-back.png" width="500">
<img src="./images/pcb-render-v0.60-front.png" width="500">

### Major Components
* USB Soundcard (PCM2706)
* Audio Front End (XMOS XVF-3510) - for Microphone input processing
* 20W Amplifier (Maxim Integrated MAX9744)
* 2 Digital MEMS Microphones (ST Micro MP34DT05)
* 12 RGB LEDs (WorldSemi WS2813-MINI)
* 3 momentary buttons (volume up, volume down, action)
* 1 toggle switch (mic mute)

### Technical Documentation
For technical details of this board see the [SJ201-Datasheet](./KiCAD/SJ201-Raspberry%20Pi%204%20Daughterboard/README.md).

## New Form Factor
The SJ201 connects to the Raspberry Pi GPIO header at a 90 degree angle. This allows the microphone array and hardware inputs to be well positioned in the enclosure, whilst maintaining the simplicity of a direct connection to the main board. 

This interface makes a landscape form factor the most viable for this prototype. The blocking of the major components can be found within the [Mechanical CAD > MkII Blocking r2.zip](./Mechanical%20Cad/MkII%20Blocking%20r2.zip). 

<img src="./images/Mark II Mechanical Blocking.png" width="500">

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
