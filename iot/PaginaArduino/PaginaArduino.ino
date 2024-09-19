#include <Wire.h>
#include <RTClib.h>
RTC_DS3231 rtc;
void setup() {
Serial.begin(9600);
if(! rtc.begin()){
  while(1);
}

pinMode(2, OUTPUT);
pinMode(3, OUTPUT);

}

String recibo;
String horaactual;
String minutoactual;
String horaencendido;
String minutoencendido;
String horaapagado;
String minutoapagado;

int horaactualint;
int minutoactualint;
int horaencendidoint=18;
int minutoencendidoint=10;
int horaapagadoint=18;
int minutoapagadoint=20;
int hora;
int minuto;




void loop() {


  if(Serial.available()){
  recibo = Serial.readString();
  horaactual = recibo.substring(0,2);
  horaactualint = horaactual.toInt();
  minutoactual = recibo.substring(3,5);
  minutoactualint = minutoactual.toInt();
  horaencendido = recibo.substring(6,8);
  horaencendidoint = horaencendido.toInt();
  minutoencendido = recibo.substring(9,11);
  minutoencendidoint = minutoencendido.toInt();
  horaapagado = recibo.substring(12,14);
  horaapagadoint = horaapagado.toInt();
  minutoapagado = recibo.substring(15,17);
  minutoapagadoint = minutoapagado.toInt();
  rtc.adjust(DateTime(2023, 1, 1, horaactualint, minutoactualint, 00)); 
  }
 
  DateTime fecha = rtc.now();
  
    if(fecha.hour() == horaencendidoint && fecha.minute() == minutoencendidoint){
    digitalWrite(2,HIGH);

  }
   
      if(fecha.hour() == horaapagadoint && fecha.minute() == minutoapagadoint){
    digitalWrite(2,LOW);

  }


}
