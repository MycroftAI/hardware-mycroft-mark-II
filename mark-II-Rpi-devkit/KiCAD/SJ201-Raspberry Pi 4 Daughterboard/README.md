# SJ201 Datasheet - Rev 6

This board interfaces directly to the Raspberry Pi 4 via the 40-pin GPIO adding a high-quality speaker and microphone array, as well as LEDs and hardware inputs for non-voice interaction and feedback.

The part number SJ201 is derived from Mike’s “Simon Jester” alias in “The Moon is a Harsh Mistress”.

<img src="../../images/pcb-render-SJ-201-R6-back.png" width="500">
<img src="../../images/pcb-render-SJ-201-R6-front.png" width="500">

## About this Document

This Datasheet will contain all the relevant information for the manufacturing of the SJ201 including information about PCB design, PCB manufacturing process.

## Major Components
* Audio Front End (XMOS XVF3510) - for Microphone input processing
* 23W I2S Digital Amplifier (Texas Instruments TAS5806MD)
* 2 Digital MEMS Microphones ([Knowles SPK0641HT4H-1](https://www.digikey.com/en/products/detail/knowles/SPK0641HT4H-1/8573345))
* 12 RGB LEDs (WorldSemi WS2812B-MINI)
* 3 momentary buttons (volume up, volume down, action)
* 1 toggle switch (mic mute)
* ATtiny1614 - control LEDs, other I/O
* I2S to Line Out (UDA1334ATS)

## Hardware Notes

- The SJ201 is plugged into the GPIO header of the Raspberry Pi 4 board.
- The pins required for the operation of the Raspberry Pi 4 MIPI and CSI are not used on the SJ201 GPIO header. The display and camera do not connect to the SJ201.
- The barrel jack on the SJ201 requires a 12V, 3A regulated DC input.

## Software Notes
- SHTDN (GPIO pin GPIO5) must be set high to enable the audio amplifier.
- The TAS5806 outputs I2S to the XMOS chip. 

## Configuration options

### Default Use Case

The SJ201 is connected to a Raspberry Pi4 via the header. 

12V is supplied to the SJ201 via the barrel jack.

The SJ201 creates 5V using a 3A buck converter, which powers the Raspberry Pi.

The SJ201 creates 3.3V using a linear regulator, which powers the on-board devices.

4.4ohm, 5W speakers are connected to the JST connectors. [Note, in the current implementation the amplifier is capable of supplying 13W to each speaker, so volume must be limited in software to avoid damage.]

### Test Configuration Options

The J5 header serves as a test point for the 3.3V, 5V and 12V supplies. 

The J5 header can also be used to bypass the on-board buck converter and/or linear regulator.

The buck converter does not need to be turned off - it can tolerate an external supply. To completely disable it, lift the appropriate pin.

The 1.0V supply can be tested using Test Point TP1_0V1 near the XMOS IC.

## Design Notes

### Power Domains

The SJ201 is powered by an external 12V 3A DC supply (wall wart) via a barrel connector. The SJ201 has 4 voltage domains:

- VDD 12V externally supplied power

- PVDD 12V Analog Audio Power

- 5V  5V derived from VDD (or USB Powered if Jumper USB_Power1 soldered)

- 3V  3.3V derived from 5V

- 1V  1.0V derived from 5V for the XMOS core

All power domains share a common ground.

- GND  Ground

### Microphone DSP

### Audio Amplifier

**Filterless modulation**  
We are using the TAS5806, in a "filterless amplifier" design. This is lower cost than using a true LC filter for each output, but can be susceptible to large EMI output if not done properly. This can lead to failure to meet FCC and other standards required for consumer electronics. The following design rules are intended to minimize EMI in the system.

**Speaker power**  
With a 4ohm speaker and a 12V supply, each channel can achieve ~13W. The speaker we're using is 4.4ohm, 5W max. The volume must be limited in software to avoid damaging the speaker.



## PCB Layout Checklist

Boxes marked 🗹 are for version 6.02 (also labeled R6 v2) of the KiCAD files.

### Layers - PCB checklist

Layer 1:  Main ICs, connectors and signal routing - Power (1.0v, PVDD 12v)

Layer 2:  GND

Layer 3:  Power (12V, 5V)

Layer 4:  Buttons, LEDs, signal routing (this layer faces upwards on device) 

### Power - PCB checklist

#### External Power Supply (VDD)

1. Barrel jack is centered on LED ring

2. Ferrite bead close to barrel jack to reduce EMI transmission along power cord to wall
   - Spec'd to handle 12V 3A

3. AOD4184A MOSFET to protect against reverse voltage (i.e. user plugs in a non-standard external power supply with GND on the center pin instead of on the outside of the barrel connector.)

4. Low resistance traces for VDD and GND connecting to power planes.

#### Analog Audio Power (PVDD)

1. PVDD does not contain loops (areas of PVDD that enclose non-PVDD areas)

2. PVDD does not contain narrow antenna-like features.

3. PVDD is primarily located on layer 3

4. PVDD connects to layer 1 traces through multiple vias for lower resistance

5. See Audio Amplifier for additional considerations

#### 5V power

XL Semiconductor's XL4015 buck converter is used to generate 5V at up to 5A from the barrel jack power. This part supports a minimum input voltage of 8V and a max of 36V. 

🗹  <http://www.xlsemi.com/datasheet/XL4015%20datasheet.pdf>

🗹  R1 and R8 are 1% tolerance (these set the output voltage. 10% resistors could result in an output range of 4.4V - 5.9V.)

#### 3.3V power

A linear regulator is used to derive 3.3V from 5V.

-   AZ1117CH-3.3

-   <https://www.diodes.com/assets/Datasheets/AZ1117C.pdf> 

### Microphones (MP34DT05-A)- PCB checklist

🗹  <https://www.st.com/content/ccc/resource/technical/document/datasheet/group3/c7/90/d3/f6/b7/e7/40/c8/DM00415595/files/DM00415595.pdf/jcr:content/translations/en.DM00415595.pdf> 

🗹  Power supply decoupling capacitors (100 nF ceramic, 1 μF ceramic) should be placed as near as possible to pin 1 of the device (common design practice). 

🗹  The L/R pin must be connected to Vdd or GND (refer to Table 6. L/R channel selection).

### LED (WS2812B-Mini)- PCB checklist

🗹  <https://datasheet.lcsc.com/szlcsc/2005251033_Worldsemi-WS2812B-Mini_C527089.pdf>

### Power on Reset - PCB checklist

-   <https://www.onsemi.com/pub/Collateral/NCP302-D.PDF> 

-   This circuit monitors multiple power supply rails for undervoltage conditions. If any of the three power supplies are in an undervoltage condition, the NCP302 reset output will be immediately set to an active low level. All three power supplies must be above their minimum voltage levels for the NCP302 reset output to generate a "Power Good" level (Reset Output = Power Supply 1 or VP).

### SG-210STF 24MHz clock - PCB checklist

🗹 Use recommended pad layout per datasheet.

-   <https://support.epson.biz/td/api/doc_check.php?mode=dl&lang=en&Parts=SG-210STF> 

### XMOS XVF3510 - PCB checklist 

Datasheets:

-   <https://www.xmos.com/documents/vocalfusionavs>

From page 26-27 of the XMOS VocalFusion XVF3510 datasheet (dated 2019-10-22).

10.1 SCHEMATICS DESIGN CHECK LIST

10.1.1. POWER SUPPLIES

🗹 The VDD (core) supply ramps monotonically (rises constantly) from 0V to its final value (0.95V - 1.05V) within 10ms (Section 6.1).

🗹 The VDD (core) supply is capable of supplying 1400mA (Section 6.1).

🗹 PLL_AVDD is filtered with a low pass filter, for example an RC filter, (Section 6.1)

10.1.2. POWER SUPPLY DECOUPLING

🗹 The design has multiple decoupling capacitors per supply, for example less than 12 402 or 0603 size surface mount capacitors of 100nF in value, per supply (Section 6.1).

🗹 A bulk decoupling capacitor of at least 10uF is placed on each supply (Section 6.1).

10.1.3. POWER ON RESET

🗹 The RST_N pins are asserted (low) until all supplies are good. There is enough time between VDDIO power good and RST_N to allow any boot flash to settle (Section 6.1).

10.1.4. CLOCKS

🗹 The CLK input pin is supplied with a clock with monotonic rising edges and low jitter.

🗹 A 24MHz reference clock must be connected to the CLK pin for all implementations.

🗹 MCLK_INOUT is connected to MCLK_IN via a PCB trace outside the device

🗹 All clock signals (CLK, MIC_CLK, QSPI_CLK, SPI_CLK, MCLK_IN, MCLK_INOUT, BCLK, LRCLK) and other audio signals must be routed well following high speed digital design guidelines, and may need buffering.

10.1.5. BOOT

🗹 To boot from QSPI flash, QSPI_CS_N, QSPI_D0 .. QSPI_D3, QSPI_D1_BOOTSEL, QSPI_CLK are connected and QSPI_D1_BOOTSEL is connected to QSPI D1 pin on flash device or pulled low/left floating (Section 6.4).

🗹 To boot from the local host processor through SPI, QSPI_D1_BOOTSEL must be pulled high and SPI_CS_N, SPI_MOSI and SPI_MISO must be connected.

10.1.6. MICROPHONES

🗹 Both MIC_DATA pins are connected to the PCB (Section 4.4).

10.1.7. JTAG AND DEBUGGING

🗹 You have decided as to whether you need an XSYS header or not (Section 7)

🗹 If you have not included an XSYS header, you have devised a method to program the SPI-flash (Section 7).

10.2 PCB LAYOUT DESIGN CHECK LIST

10.2.1. GROUND PLANE

🗹 Multiple vias (eg, 16) have been used to connect the ground paddle to the PCB ground plane. These minimize impedance and conduct heat away from the device. (Section 6.1)

🗹 Other than ground vias, there are no (or only a few) vias underneath or closely around the device. This creates a good, solid, ground plane.

10.2.2. POWER SUPPLY DECOUPLING

🗹 The decoupling capacitors are all placed close to a supply pin (Section 6.1).

🗹 The decoupling capacitors are spaced around the device (Section 6.1).

🗹 The ground side of each decoupling capacitor has a direct path back to the center ground of the device.

10.2.3. PLL_AVDD

🗹 The PLL_AVDD filter (especially the capacitor) is placed close to the PLL_AVDD pin (Section 6.1).

### Audio Amplifier - PCB checklist

The following notes are related to the PCB layout wrt the TAS5806. We also used the MAX9744 design notes, as that was the amplifier for the first iteration and the notes are generally applicable.

1. 🗹 Ferrite bead close to 12V barrel connector
   - "It is sometimes helpful to insert RF chokes in series with the power supplies for the amplifier. Properly placed, they can confine high-frequency transient currents to local loops near the amplifier, instead of being conducted for long distances down the power supply wires." [Ref 1]

2. 🗹 Compact LC circuit from output of amplifier to JST speaker connectors
   - "the entire LC filter (including the speaker wiring) should be laid out as compactly as possible, and kept close to the amplifier." [Ref 1]

3. 🗹 Make speaker connections parallel and close to minimize area and therefore the "antenna" created
   - "Traces for current drive and return paths should be kept together to minimize loop areas." [Ref 1]

4. 🗹 Speaker wires from JST to speaker element are twisted pair and less than 10cm long.
   - "to minimize loop areas ... using twisted pairs for the speaker wires is helpful)" [Ref 1]

5.  🗹 Connect PGND to GND at a single point on the PCB. [Ref 3, p23]

6. 🗹 Connect all VDD power supplies together and bypass with a 1uF cap to GND. [Ref 3, p23]

7. 🗹 Place a bulk capacitor between PVDD and PGND. [Ref 3, p23]

8. 🗹 Use large, low-resistance output traces to speaker filters and JST connectors. [Ref 3, p23]

9. 🗹 Use large traces for the power-supply to PVDD and PGND. [Ref 3, p23]

10. 🗹 Thermal pad (area fill exposed copper) under amplifier on layer 1. [Ref 3, p23]
   - There should be no solder-mask in this area. [TODO: verify]

11. 🗹 Connect thermal pad on layer 1 to PGND on layer 2 using multiple vias. PGND area as large as practical for better heat dissipation. [Ref 3, p23]


## Production Checklist

WS2812 Mini

- [] This has to be baked for 48 hours at the baking temperature of 70-75℃ before being used. 

- [] Use up with 2 hours after taking out from oven.

- [] Please replace the unused LEDs into oven.


## References

1\. Analog Class D Amps

- <https://www.analog.com/en/analog-dialogue/articles/class-d-audio-amplifiers.html>
  - Class-D audio amplifiers. 
  - Good information about the why's of component placement and trace layout.

2\. MAXIM Class D Thermal Considerations

- <https://www.maximintegrated.com/en/design/technical-documents/app-notes/3/3879.html>
  - Board layout
  - Speaker impedance choice

3\. MAX9744 data sheet
