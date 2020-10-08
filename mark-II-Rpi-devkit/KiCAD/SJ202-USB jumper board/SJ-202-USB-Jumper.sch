EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A 11000 8500
encoding utf-8
Sheet 1 1
Title "SJ-202-USB-Jumper"
Date "2020-10-03"
Rev "03"
Comp "Mycroft AI"
Comment1 "SJ-202-01"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:USB_A J1
U 1 1 5F528EEA
P 4150 4075
F 0 "J1" H 4207 4542 50  0000 C CNN
F 1 "USB_A" H 4207 4451 50  0000 C CNN
F 2 "libraries:USB_A_Female_UE27AC54100" H 4300 4025 50  0001 C CNN
F 3 "https://www.digikey.com/product-detail/en/0480372200/WM3983CT-ND/2421836" H 4300 4025 50  0001 C CNN
F 4 "WM3983CT-ND" H 4150 4075 50  0001 C CNN "Digikey"
F 5 "U-G-04WS-W-03" H 4150 4075 50  0001 C CNN "MPN"
F 6 "https://lcsc.com/product-detail/Others_Korean-Hroparts-Elec-U-G-04WS-W-03_C283548.html" H 4150 4075 50  0001 C CNN "Link"
F 7 "0480372200" H 4150 4075 50  0001 C CNN "Tempo"
	1    4150 4075
	1    0    0    -1  
$EndComp
Wire Wire Line
	4825 4175 4450 4175
Wire Wire Line
	5200 4275 4900 4275
Wire Wire Line
	4475 4275 4475 4475
Wire Wire Line
	4050 4475 4050 4550
$Comp
L power:GND #PWR0101
U 1 1 5F52A6FF
P 4900 4550
F 0 "#PWR0101" H 4900 4300 50  0001 C CNN
F 1 "GND" H 4905 4377 50  0000 C CNN
F 2 "" H 4900 4550 50  0001 C CNN
F 3 "" H 4900 4550 50  0001 C CNN
	1    4900 4550
	1    0    0    -1  
$EndComp
Connection ~ 4900 4550
Wire Wire Line
	4900 4550 5200 4550
$Comp
L power:+5V #PWR0102
U 1 1 5F52ABD7
P 4825 3875
F 0 "#PWR0102" H 4825 3725 50  0001 C CNN
F 1 "+5V" H 4840 4048 50  0000 C CNN
F 2 "" H 4825 3875 50  0001 C CNN
F 3 "" H 4825 3875 50  0001 C CNN
	1    4825 3875
	1    0    0    -1  
$EndComp
Wire Wire Line
	4825 3875 4450 3875
Text Notes 3200 900  0    197  ~ 39
SJ-202 - USB Jumper 
Text Notes 4000 5200 0    59   ~ 0
Connects USB-A on Rasbperry Pi\nto USB Micro on Mycroft backpack SJ-201
Wire Wire Line
	4475 4475 4150 4475
Wire Wire Line
	4050 4550 4900 4550
$Comp
L power:GND #PWR0103
U 1 1 5F530329
P 4900 4275
F 0 "#PWR0103" H 4900 4025 50  0001 C CNN
F 1 "GND" H 4905 4102 50  0000 C CNN
F 2 "" H 4900 4275 50  0001 C CNN
F 3 "" H 4900 4275 50  0001 C CNN
	1    4900 4275
	1    0    0    -1  
$EndComp
Connection ~ 4900 4275
Wire Wire Line
	4900 4275 4475 4275
Text Label 4525 4175 0    59   ~ 0
D-
Text Label 4525 4075 0    59   ~ 0
D+
$Comp
L Connector_Generic:Conn_01x04 J4
U 1 1 5F58F2C6
P 5625 3975
F 0 "J4" H 5705 4017 50  0000 L CNN
F 1 "Conn_01x04" H 5705 3926 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 5625 3975 50  0001 C CNN
F 3 "~" H 5625 3975 50  0001 C CNN
F 4 "210-91-04GB01" H 5625 3975 50  0001 C CNN "MPN"
F 5 "C390680" H 5625 3975 50  0001 C CNN "LCSC"
F 6 "https://lcsc.com/product-detail/Pin-Header-Female-Header_PINREX-210-91-04GB01_C390680.html" H 5625 3975 50  0001 C CNN "Link"
	1    5625 3975
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x02 J2
U 1 1 5F596E74
P 5025 3475
F 0 "J2" V 4989 3287 50  0000 R CNN
F 1 "5vJumper" V 5125 3575 50  0000 R CNN
F 2 "Jumper:SolderJumper-2_P1.3mm_Open_TrianglePad1.0x1.5mm" H 5025 3475 50  0001 C CNN
F 3 "~" H 5025 3475 50  0001 C CNN
F 4 "DNP" H 5025 3475 50  0001 C CNN "MPN"
	1    5025 3475
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5025 3675 5025 3875
Wire Wire Line
	5025 3875 4825 3875
Connection ~ 4825 3875
Wire Wire Line
	5125 3675 5125 3875
Connection ~ 5200 4275
Wire Wire Line
	5200 4275 5200 4550
Wire Wire Line
	5200 4175 5200 4275
Wire Wire Line
	4825 4075 4825 4175
Wire Wire Line
	4725 3975 4725 4075
Wire Wire Line
	4725 4075 4450 4075
Text Label 5150 3875 0    51   ~ 0
5vJump
Wire Wire Line
	5125 3875 5425 3875
Wire Wire Line
	4725 3975 5425 3975
Wire Wire Line
	4825 4075 5425 4075
Wire Wire Line
	5200 4175 5425 4175
$EndSCHEMATC
