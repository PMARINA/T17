//sine wave freq detection with 38.5kHz sampling rate and interrupts
//by Amanda Ghassaei
//http://www.instructables.com/id/Arduino-Frequency-Detection/
//July 2012

/*
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
*/

#include <Wire.h>
//#include <Adafruit_MLX90614.h>

//Adafruit_MLX90614 mlx = Adafruit_MLX90614();


//clipping indicator variables
boolean clipping = 0;
boolean doneWithSound = false;

const int CLIPLED = 13;
const int CORRLED = 2;

//data storage variables
byte newData = 0;
byte prevData = 0;

//freq variables
unsigned int timer = 0;//counts period of wave
unsigned int period;
int frequency;

byte correct = 0;
byte wrong = 0;

void setup(){
  
  Serial.begin(9600);

  //pinMode(CLIPLED, OUTPUT);//clipping indicator pin
  //pinMode(CORRLED, OUTPUT);//led indicator pin
  
  cli();//diable interrupts
  
  //set up continuous sampling of analog pin 0
  
  //clear ADCSRA and ADCSRB registers
  ADCSRA = 0;
  
  ADMUX |= (1 << REFS0); //set reference voltage
  ADMUX |= (1 << ADLAR); //left align the ADC value- so we can read highest 8 bits from ADCH register only
  
  ADCSRA |= (1 << ADPS2) | (1 << ADPS0); //set ADC clock with 32 prescaler- 16mHz/32=500kHz
  ADCSRA |= (1 << ADATE); //enabble auto trigger
  ADCSRA |= (1 << ADIE); //enable interrupts when measurement complete
  ADCSRA |= (1 << ADEN); //enable ADC
  ADCSRA |= (1 << ADSC); //start ADC measurements
  
  sei();//enable interrupts
  
  do {
    if (clipping){//if currently clipping
      PORTB &= B11011111;//turn off clippng indicator led
      clipping = 0;
    }
  
    frequency = 38462/period;//timer rate/period
    //print results
    //Serial.print(frequency);
    //Serial.println(" hz");
  
    if (3306 < frequency && 4294 > frequency) {
      correct++;
    } else {
      wrong++;
    }
    if (wrong + correct > 20) {
      //Serial.print(wrong);
      //Serial.print("");
      //Serial.println(correct);
      if (correct > (wrong * 3)) {
        Serial.println("sound");
        pinMode(5,OUTPUT);
        digitalWrite(5,HIGH);
        doneWithSound = true;
      } else {
        //digitalWrite(CORRLED, 0);
      }
      correct = 0;
      wrong = 0;
    }
    
    delay(50);
  } while(!doneWithSound);
  
  cli();//diable interrupts
  
  //set up continuous sampling of analog pin 0
  
  //clear ADCSRA and ADCSRB registers
  ADCSRA = 0b10000111;
  ADMUX = 0;
  
  sei();//enable interrupts
  
  analogReference(DEFAULT);
  
  while(true) {
    Serial.println(analogRead(A2));
    delay(80);
  }
}

ISR(ADC_vect) {//when new ADC value ready
  if (!doneWithSound) {
    prevData = newData;//store previous value
    newData = ADCH;//get value from A0
    if (prevData < 129 && newData >=129){//if increasing and crossing midpoint
      period = timer;//get period
      timer = 0;//reset timer
    }
    
    
    if (newData == 0 || newData == 1023){//if clipping
      PORTB |= B00100000;//set pin 13 high- turn on clipping indicator led
      clipping = 1;//currently clipping
    }
    
    timer++;//increment timer at rate of 38.5kHz
  }
  pinMode(6,INPUT)
}
  boolean a = false;
void loop(){
  a = a ||　Ｓｅｒｉａｌ．read（）＝＝　＂ｆｉｒｅ＂；
  ｉｆ（ａ）ｄｉｇｉｔａｌＷｒｉｔｅ（６，ＨＩＧＨ）
  while(Serial.read()!="fire"){
    digitalWrite(d6,i)
  }
  
}

