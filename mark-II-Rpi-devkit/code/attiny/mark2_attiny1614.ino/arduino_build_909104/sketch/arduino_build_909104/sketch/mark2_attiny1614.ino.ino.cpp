#include <Arduino.h>
#line 1 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"

#include <Wire.h>

#include <tinyNeoPixel_Static.h>
#include <EEPROM.h>

#define NEOXPIXELPIN 1
#define MAXSTATES    10
#define BRIGHTNESS   100

// Parameter 1 = number of pixels in strip
// Parameter 2 = Arduino pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
// Parameter 4 = array to store pixel data in

#define NUMPIXELS   12
#define NUMPATTERNS 1 

// Since this is for the static version of the library, we need to supply the pixel array
// This saves space by eliminating use of malloc() and free(), and makes the RAM used for
// the frame buffer show up when the sketch is compiled.

byte pixels[NUMPIXELS * 3];
//byte bufferI2C[NUMPIXELS * 3 + 100];
byte bufferI2C[256];
byte pattern[NUMPATTERNS][NUMPIXELS];

// When we setup the NeoPixel library, we tell it how many pixels, and which pin to use to send signals.
// Note that for older NeoPixel strips you might need to change the third parameter--see the strandtest
// example for more information on possible values. Finally, for the 4th argument we pass the array we
// defined above.

tinyNeoPixel strip = tinyNeoPixel(NUMPIXELS, NEOXPIXELPIN, NEO_GRB, pixels);

// IMPORTANT: To reduce NeoPixel burnout risk, add 1000 uF capacitor across
// pixel power leads, add 300 - 500 Ohm resistor on first pixel's data input
// and minimize distance between Arduino and first pixel.  Avoid connecting
// on a live circuit...if you must, connect GND first.
//volatile byte state = 1;


#define TPU_RST_L   8   //PA1
#define TPU_PGOOD   9   //PA2
#define FAN_TACH    10  //PA3
#define FAN_PWM     0   //PA4

#define TPU_PMIC_EN 2   //PA6
#define GPIO_PA7    3   //PA7

/**
 * EEPROM addresses
 */
#define NUM_BOOTS   0
#define SERIAL_NUM  10
#define LED_COLOR_R 20
#define LED_COLOR_G 21 
#define LED_COLOR_B 22 

volatile byte state   = 0;
long lastButtonPress = 0;
volatile bool nextState       = false;
volatile bool readBuffer      = false;
#line 65 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void setup();
#line 93 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void loop();
#line 174 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void readNumBoots();
#line 201 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void setI2CreadOnly();
#line 228 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void setFan(byte fanSpeed);
#line 235 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void setState(byte s1);
#line 243 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
int getState();
#line 249 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
bool isBootSequenceRunning();
#line 256 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void cycleStates();
#line 268 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void colorWipe(uint32_t c, uint8_t wait);
#line 276 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void showi2cPixels();
#line 285 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void show_pattern();
#line 336 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void rainbow(uint8_t wait);
#line 362 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void theaterChase(uint32_t c, uint8_t wait);
#line 400 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
uint32_t Wheel(byte WheelPos);
#line 414 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void set_pattern();
#line 422 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void fill_pattern();
#line 450 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void receiveEvent(int howMany);
#line 504 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void requestEvent();
#line 65 "C:\\Dropbox\\Crashspace\\Mycroft\\programming\\mark2_attiny1614.ino\\mark2_attiny1614.ino.ino"
void setup() {

  Wire.begin(4);                // join i2c bus with address #4
  Wire.onReceive(receiveEvent); // register event
  Wire.onRequest(requestEvent);
  pinMode(NEOXPIXELPIN,OUTPUT);
  pinMode(FAN_PWM  ,   OUTPUT);
  pinMode(FAN_TACH ,   INPUT); 
  pinMode(TPU_PGOOD,   INPUT);
  pinMode(TPU_PMIC_EN, OUTPUT);
  digitalWrite(TPU_PMIC_EN, HIGH);
  //pinMode(TPU_INTR,    INPUT);

  //delay(5);
  pinMode(TPU_RST_L,   INPUT);
  //pinMode(TPU_RST_L,   OUTPUT);
  //if(digitalRead(TPU_PGOOD)){
    //digitalWrite(TPU_RST_L, HIGH);  
  //}
  strip.setBrightness(BRIGHTNESS);
  strip.show(); // Initialize all pixels to 'off'
  
  setFan(0); // Start Fan as off
  Serial.begin(57600); 
  
  readNumBoots();
}

void loop() {
  switch(state){
    case 0:
      colorWipe(strip.Color(34, 167, 240), 70 ); // Blue
      colorWipe(strip.Color(0, 0, 0), 50); // 
      //setState( 1 );
      break;
    case 1:
      //strip.show();
      showi2cPixels();
      //colorWipe(strip.Color(200, 0, 0), 70 ); // Blue
      //colorWipe(strip.Color(0, 0, 0), 50); // 
   
      break;
    case 2:
      // Some example procedures showing how to display to the pixels:
      colorWipe(strip.Color(255, 0, 0), 50); // Red
      colorWipe(strip.Color(0, 0, 0), 50); // Red
      break;
    case 3:
      colorWipe(strip.Color(0, 255, 0), 50); // Green
      colorWipe(strip.Color(0, 0, 0), 50); // Red
      break;
    case 4:
      colorWipe(strip.Color(0, 0, 0), 0); // black
      //setState( 1 );
      break;

    case 5:
       theaterChase(strip.Color(127, 127, 127), 200); // White
       break;
    case 6:
      rainbow(5);
      break;
    case 7:
//      rainbowCycle(20);
      break;
    case 8:
 //     theaterChaseRainbow(50);
      break;
/*  
    case 9:
      crossfade();
      break;
 */
    case 10:
      show_pattern();
      state = 255;
      break;
    // 100 - 199 are commands that read stuff from the buffer
    case 100: // set pallete N
      set_pattern();
      break;
    case 101: // fill pallete N with single RGB
      fill_pattern();
      break;
/*    
    case 103: // cross fade between pallete N and M
      setup_crossfade();
      state = 9;
      break;
*/
    case 104:
      show_pattern();
      state = 255;
      break;
    case 202: 
    case 255:
      break;
    default:
      //colorWipe(strip.Color(0, 0, 0), 0); // black
      strip.show();
      break;
  } // end switch stmt

  nextState = false;
  
  setI2CreadOnly();
  
}

void readNumBoots(){
  bufferI2C[0xF5] = EEPROM.read(NUM_BOOTS);
  bufferI2C[0xF6] = EEPROM.read(NUM_BOOTS + 1);
  bufferI2C[0xF7] = EEPROM.read(NUM_BOOTS + 2);
  bufferI2C[0xF8] = EEPROM.read(NUM_BOOTS + 3);  
  long numBootsVal = 0;
  numBootsVal += bufferI2C[0xF5] << 24;
  numBootsVal += bufferI2C[0xF6] << 16;
  numBootsVal += bufferI2C[0xF7] << 8;
  numBootsVal += bufferI2C[0xF8];
  numBootsVal += 1;
  
  EEPROM.write(NUM_BOOTS    , numBootsVal & 0xFF);
  EEPROM.write(NUM_BOOTS + 1,(numBootsVal >> 8) & 0xFF);
  EEPROM.write(NUM_BOOTS + 2,(numBootsVal >> 16) & 0xFF);
  EEPROM.write(NUM_BOOTS + 3,(numBootsVal >> 32) & 0xFF);  
  
  bufferI2C[0xF5] = EEPROM.read(NUM_BOOTS);
  bufferI2C[0xF6] = EEPROM.read(NUM_BOOTS + 1);
  bufferI2C[0xF7] = EEPROM.read(NUM_BOOTS + 2);
  bufferI2C[0xF8] = EEPROM.read(NUM_BOOTS + 3); 
}
long lastReadTime   = 0;
#define READ_INTERVAL 100
/**
 * Read in statuses from inputs and load them into I2CBuffer
 */
void setI2CreadOnly(){
   if (millis() - lastReadTime > READ_INTERVAL ){
     // bufferI2C[80] = pulseIn(FAN_TACH, HIGH, 100) ;
      bufferI2C[0x51] = digitalRead(TPU_PGOOD);
      bufferI2C[0x52] = digitalRead(TPU_PMIC_EN);
      //bufferI2C[0x53] = digitalRead(TPU_INTR);
      bufferI2C[0x54] = digitalRead(TPU_RST_L);
      bufferI2C[0x60] = 0xFF;    
      
      long timestampNow = millis();  
      bufferI2C[0xF0] = timestampNow & 0xFF;
      bufferI2C[0xF1] = (timestampNow >> 8) & 0xFF;
      bufferI2C[0xF2] = (timestampNow >> 16) & 0xFF;
      bufferI2C[0xF3] = (timestampNow >> 24) & 0xFF;
      bufferI2C[0xF4] = 0xF4; 

      
      
      lastReadTime = millis();
   }
   
}


/**
 * Speed is 0 to 255
 */
void setFan(byte fanSpeed){

  // FAN_PWM at zero turns on Fan
  // invert input so 255 is full on, zero is off
  analogWrite(FAN_PWM, constrain(255 - fanSpeed, 0, 255));

}
inline void setState(byte s1){
  state = s1;
  if(state > MAXSTATES){
      state = MAXSTATES;
   }
   //nextState = true;
   readBuffer = false;
}
int getState(){
  return state;  
}
/**
 * Is the boot sequence running
 */
bool isBootSequenceRunning(){
  if(getState() == 0){
    return true;  
  }  
  return false;
}

void cycleStates(){
  if(millis() - lastButtonPress > 100 ){
    state++;
    if(state > MAXSTATES){
      setState(0);
    }
    lastButtonPress = millis();
  }
  nextState = true;
}

// Fill the dots one after the other with a color
void colorWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i<strip.numPixels() && !nextState; i++) {
    strip.setPixelColor(i, c);
    strip.show();
    delay(wait);
  }
}

void showi2cPixels() {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
    strip.setPixelColor(i, strip.Color(bufferI2C[i * 3], bufferI2C[i * 3+1], bufferI2C[i * 3+2]) ); // set color from i2c
    delay(10);
    strip.show();
  }
  strip.show();
}

void show_pattern() {
  byte pattern_num = bufferI2C[1];
  for(byte i=0; i<strip.numPixels(); i++) {
    strip.setPixelColor(i, strip.Color(pattern[pattern_num][i*3], pattern[pattern_num][i*3+1], pattern[pattern_num][i*3+2] )); // set color from pattern
    delay(10);
  }
  strip.show();
}

/*
byte fade_pattern_0;
byte fade_pattern_1;
byte fade_step;
byte fade_speed;
byte fade_pause;

void setup_crossfade() {
   fade_pattern_0 = bufferI2C[1];
   fade_pattern_1 = bufferI2C[2];
   fade_step      = bufferI2C[3];
   fade_speed     = bufferI2C[4];
   fade_pause     = bufferI2C[5];
}

void crossfade() {
  byte temp;
  uint16_t r,g,b;
  while (!nextState) {
    for(byte fade = 0; fade < 255; fade += fade_step) {
      for(byte i = 0; i < strip.numPixels(); i++) {      
        r = (((pattern[fade_pattern_0][i*3 + 0] * fade)) / 256)
          + ((pattern[fade_pattern_1][i*3 + 0] * (255 - fade)) / 256);
        g = (((pattern[fade_pattern_0][i*3 + 1] * fade)) / 256)
          + ((pattern[fade_pattern_1][i*3 + 1] * (255 - fade)) / 256);
        b = (((pattern[fade_pattern_0][i*3 + 2] * fade)) >> 8)
          + ((pattern[fade_pattern_1][i*3 + 2] * (255 - fade)) / 256);
        strip.setPixelColor(i, strip.Color(r,g,b));   
      }
      strip.show();
      temp = fade_pattern_0;
      fade_pattern_0 = fade_pattern_1;
      fade_pattern_1 = temp; 
      delay(fade_speed);
    }
    delay(fade_pause);
  }
}
*/



void rainbow(uint8_t wait) {
  uint16_t i, j;

  for(j=0; j<256 && !nextState; j++) {
    for(i=0; i<strip.numPixels() && !nextState; i++) {
      strip.setPixelColor(i, Wheel((i+j) & 255));
    }
    strip.show();
    delay(wait);
  }
}
/*
// Slightly different, this makes the rainbow equally distributed throughout
void rainbowCycle(uint8_t wait) {
  uint16_t i, j;

  for(j=0; j<256*5 && !nextState; j++) { // 5 cycles of all colors on wheel
    for(i=0; i< strip.numPixels() && !nextState; i++) {
      strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}
*/
//Theatre-style crawling lights.
void theaterChase(uint32_t c, uint8_t wait) {
  for (int j=0; j<10 && !nextState; j++) {  //do 10 cycles of chasing
    for (int q=0; q < 3 && !nextState; q++) {
      for (int i=0; i < strip.numPixels(); i=i+3) {
        strip.setPixelColor(i+q, c);    //turn every third pixel on
      }
      strip.show();

      delay(wait);

      for (int i=0; i < strip.numPixels() && !nextState; i=i+3) {
        strip.setPixelColor(i+q, 0);        //turn every third pixel off
      }
    }
  }
}

/*
//Theatre-style crawling lights with rainbow effect
void theaterChaseRainbow(uint8_t wait) {
  for (int j=0; j < 256 && !nextState; j++) {     // cycle all 256 colors in the wheel
    for (int q=0; q < 3 && !nextState; q++) {
      for (int i=0; i < strip.numPixels() && !nextState; i=i+3) {
        strip.setPixelColor(i+q, Wheel( (i+j) % 255));    //turn every third pixel on
      }
      strip.show();

      delay(wait);

      for (int i=0; i < strip.numPixels() && !nextState; i=i+3) {
        strip.setPixelColor(i+q, 0);        //turn every third pixel off
      }
    }
  }
}
*/
// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos) {
  WheelPos = 255 - WheelPos;
  if(WheelPos < 85) {
    return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  }
  if(WheelPos < 170) {
    WheelPos -= 85;
    return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
  WheelPos -= 170;
  return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
}


void set_pattern() {
  byte pattern_num = bufferI2C[0];
  byte addrStart   = bufferI2C[1];
  pattern[pattern_num][addrStart * 3] = bufferI2C[2];
  pattern[pattern_num][addrStart * 3] = bufferI2C[3];
  pattern[pattern_num][addrStart * 3] = bufferI2C[4];
}

void fill_pattern() {
  byte pattern_num = bufferI2C[0];
  for (byte i=0; i < NUMPIXELS; i++) {
    pattern[pattern_num][1 + i * 3] = bufferI2C[1];
    pattern[pattern_num][2 + i * 3] = bufferI2C[2];
    pattern[pattern_num][3 + i * 3] = bufferI2C[3];
  }
}



byte lastNumItems = 0;
byte addrStart    = 0;
volatile byte reg          = 0;
// function that executes whenever data is received from master
// this function is registered as an event, see setup()
/**
 * 
 * sudo ./vfctrl_usb  SET_I2C_WITH_REG 74 5 13   5  100 101 102 103 104 105 106 107 108 109 110 116  112  113  0  0  0  0  0  0  0  0  0  0  0  0  0 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 0  0  0  0  0  0  0  0  0  0  
 * SET_I2C_WITH_REG 74 5 13   5 
 *               74 Address
 *                5 start byte
 *               13 length
 *                5 state to set 
 *          101...  12 bytes for colors
 *                  
 **/

void receiveEvent(int howMany) {
  readBuffer = true;
  byte i = 0;

  lastNumItems = howMany;

  /**
   * if how many, then requesting a read, else read pixel values
   */
  if(howMany == 1){
    reg = Wire.read();
    Serial.print(reg);
  }
  else{
    addrStart     = Wire.read() ; // first byte is pixel address or command
    
    if(addrStart < NUMPIXELS) {
      while (1 <= Wire.available()) { // loop through all but the last
        byte c = Wire.read(); // receive byte as a character
        bufferI2C[addrStart * 3 + i] = c;
        i++;
      }
      setState(1);
    }
    else  {
      while (1 <= Wire.available()) { // loop through all but the last
        byte c = Wire.read(); // receive byte as a character
        bufferI2C[addrStart ] = c; 
      }     
      //setState(addrStart - NUMPIXELS);
    }
    
    if (addrStart == 101){ //0x65
      byte fanSpeed = 0;
      fanSpeed = bufferI2C[101]; 
      setFan(fanSpeed);  
    }
    /**
     * Set the Enable TPU
     */
    if (addrStart == 0x52){
      if(bufferI2C[0x52] == 1){
        digitalWrite(TPU_PMIC_EN, HIGH);
      }
      else{
        digitalWrite(TPU_PMIC_EN, LOW);
      }
    }
    nextState = true;
  }
}


//byte startingNum = 0;
void requestEvent() {
   //byte count = 0;
   if(reg < 256 && reg >= 0 ){
     Wire.write(bufferI2C[reg]);
     //Wire.write(reg);
   }
   //Wire.write(0x44);
   //Serial.println(bufferI2C[reg]);
}

