EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A 11000 8500
encoding utf-8
Sheet 1 6
Title ""
Date "2020-08-16"
Rev "0.66"
Comp "Mycroft"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text Notes 4475 3775 0    197  ~ 0
Raspberry Pi\n& USB Hub
Text Notes 7575 3900 0    197  ~ 0
Audio Amplifier\n& \nUSB Sound Card
Text Notes 4375 1975 0    197  ~ 0
XMOS\nMicrophone \nArray
$Sheet
S 860  2860 2270 1420
U 5EAAC9A5
F0 "Power" 47
F1 "Power.sch" 47
$EndSheet
Text Notes 1400 3625 0    197  ~ 0
Power
Text Notes 4825 5750 0    197  ~ 0
Monitor\n& Touch
Wire Notes Line
	3380 3540 4060 3540
Wire Notes Line
	5490 4810 5490 4310
Wire Notes Line
	5390 4310 5400 4310
Text Notes 860  900  0    197  ~ 39
Mycroft Mark 2
Text Notes 5400 4775 1    63   ~ 0
MIPI DSI\nConnector
Text Notes 5650 2650 1    63   ~ 0
USB
$Sheet
S 7500 2850 2560 1310
U 5EA9C67D
F0 "AudioAmp" 50
F1 "AudioAmp.sch" 50
$EndSheet
$Sheet
S 4275 4875 2275 1175
U 5EAB86B0
F0 "Monitor" 50
F1 "monitor.sch" 50
$EndSheet
$Sheet
S 4275 2850 2275 1325
U 5EA9C461
F0 "RaspberryPi" 50
F1 "RaspberryPi.sch" 50
$EndSheet
$Sheet
S 4275 950  2270 1330
U 5EA9C76D
F0 "xmos" 47
F1 "xmos.sch" 47
$EndSheet
Wire Notes Line
	5690 2835 5690 2335
Text Notes 7075 3525 2    63   ~ 0
USB
Wire Notes Line
	6625 3600 7450 3600
$Comp
L Mechanical:MountingHole H1
U 1 1 5F08AB51
P 8000 6100
F 0 "H1" H 8100 6146 50  0000 L CNN
F 1 "MountingHole" H 8100 6055 50  0000 L CNN
F 2 "MountingHole:MountingHole_3mm_Pad_Via" H 8000 6100 50  0001 C CNN
F 3 "~" H 8000 6100 50  0001 C CNN
	1    8000 6100
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H2
U 1 1 5F08B35B
P 8000 6275
F 0 "H2" H 8100 6321 50  0000 L CNN
F 1 "MountingHole" H 8100 6230 50  0000 L CNN
F 2 "MountingHole:MountingHole_3mm_Pad_Via" H 8000 6275 50  0001 C CNN
F 3 "~" H 8000 6275 50  0001 C CNN
	1    8000 6275
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H3
U 1 1 5F08B63A
P 8000 6475
F 0 "H3" H 8100 6521 50  0000 L CNN
F 1 "MountingHole" H 8100 6430 50  0000 L CNN
F 2 "MountingHole:MountingHole_3mm_Pad_Via" H 8000 6475 50  0001 C CNN
F 3 "~" H 8000 6475 50  0001 C CNN
	1    8000 6475
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H4
U 1 1 5F08B83C
P 8000 6675
F 0 "H4" H 8100 6721 50  0000 L CNN
F 1 "MountingHole" H 8100 6630 50  0000 L CNN
F 2 "MountingHole:MountingHole_3mm_Pad_Via" H 8000 6675 50  0001 C CNN
F 3 "~" H 8000 6675 50  0001 C CNN
	1    8000 6675
	1    0    0    -1  
$EndComp
$Comp
L Graphic:Logo_Open_Hardware_Small #LOGO2
U 1 1 5F5E3BA9
P 9875 6525
F 0 "#LOGO2" H 9875 6800 50  0001 C CNN
F 1 "Logo_Open_Hardware_Small" H 9875 6300 50  0001 C CNN
F 2 "mycroft:mycroft_logo" H 9875 6525 50  0001 C CNN
F 3 "~" H 9875 6525 50  0001 C CNN
	1    9875 6525
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H5
U 1 1 5F5E5223
P 8800 6650
F 0 "H5" H 8900 6696 50  0001 L CNN
F 1 "MountingHole" H 8900 6605 50  0001 L CNN
F 2 "mycroft:mycroft_logo_graphic" H 8800 6650 50  0001 C CNN
F 3 "~" H 8800 6650 50  0001 C CNN
	1    8800 6650
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H6
U 1 1 5F5E5F93
P 8800 6475
F 0 "H6" H 8900 6521 50  0001 L CNN
F 1 "MountingHole" H 8900 6430 50  0001 L CNN
F 2 "Symbol:OSHW-Symbol_6.7x6mm_SilkScreen" H 8800 6475 50  0001 C CNN
F 3 "~" H 8800 6475 50  0001 C CNN
	1    8800 6475
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H7
U 1 1 5F18D39F
P 8975 6650
F 0 "H7" H 9075 6696 50  0001 L CNN
F 1 "MountingHole" H 9075 6605 50  0001 L CNN
F 2 "mycroft:mycroft_logo_words" H 8975 6650 50  0001 C CNN
F 3 "~" H 8975 6650 50  0001 C CNN
	1    8975 6650
	1    0    0    -1  
$EndComp
Text Notes 900  1125 0    79   ~ 16
SJ201-Raspberry Pi 4 Daughterboard
$EndSCHEMATC
