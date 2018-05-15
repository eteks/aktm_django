/*
Final demo program to the client
Flow proceed as follows:-
 * Opening the box, waits for 5 seconds and closes the box
 * SMS will be sent to the user
 * Key status will be logged as IN
 * Giving an input as 1 in the serial monitor, will open and close the box
 * Key status will be logged as OUT

Pending:
 * Key detection using PIR sensor
 * SMS reply back to the URL automatically
*/

#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <ESP8266HTTPClient.h>
#include  <Servo.h> 

//Parameters to be configured 
const char* ssid = "Smartnet";
const char* password = "ets_2017";
const int led = LED_BUILTIN;
String smsUrl = "";
String mobile_no = "8072812034";
String msg_to_send = "Your%20car%20is%20ready.%20Please%20visit%20us%20and%20reply%20back%20'BYE6REPLY'%20to%209220592205%20to%20get%20your%20key";
//String msg_to_send = "HI";
String loggingUrl = "http://10.0.0.14:8000/save_key_status/";
String company = "A";
String branch = "Kathirkamam";
String product_id = "AHKR001";
String box_id = "1";
String createdby = "AHKR001";
String key_status_IN = "IN";
String key_status_OUT = "OUT";
bool ONETIME = true;
int angle = 0; 
int incomingByte = 0;

// Initializing servo motors and HTTP port
Servo left_servo;        //initialize a servo object for the connected servo  
Servo right_servo;
ESP8266WebServer server(80);

// Function to open the box
void openBox(){
 for(angle = 0; angle < 180; angle += 1)    // command to move from 0 degrees to 180 degrees 
  {                                  
    left_servo.write(angle);                 //command to rotate the servo to the specified angle
    right_servo.write(angle);
    delay(15); 
  } 
  Serial.println("Box is opened");
}

//Function to close the box
void closeBox(){
  for(angle = 180; angle >= 1; angle -= 1)     // command to move from 180 degrees to 0 degrees 
  {                                
    left_servo.write(angle);              //command to rotate the servo to the specified angle
    right_servo.write(angle);
    delay(15);                       
  }  
  Serial.println("Box is closed");
}
                
//Function to log the key status as IN in the Web application
void loggingKeyIn(){
  box_id = "1";
  loggingUrl = loggingUrl+"?company="+company+"&branch="+branch+"&product_id="+product_id+"&box_id="+box_id+"&key_status="+key_status_IN+"&createdby="+createdby;
  //Serial.print("Inside Logging in");
  HTTPClient http; 
  http.begin(loggingUrl);
  int httpResponseCode = http.GET();
  //Serial.print(httpResponseCode);
   if(httpResponseCode == 200){
     String payload = http.getString();
     Serial.println("Logged the Key Status as IN");
   }
  http.end();
}


//Function to log the key status as OUT in the Web application
void loggingKeyOut(){
  box_id = "1";
  loggingUrl = loggingUrl+"?company="+company+"&branch="+branch+"&product_id="+product_id+"&box_id="+box_id+"&key_status="+key_status_OUT+"&createdby="+createdby;
  //Serial.print("Inside Logging in");
  HTTPClient http; 
  http.begin(loggingUrl);
  int httpResponseCode = http.GET();
  //Serial.print(httpResponseCode);
   if(httpResponseCode == 200){
     String payload = http.getString();
     Serial.println("Logged the Key Status as OUT");
   }
  http.end();
}


// Function to send SMS to the user
void sendSMS(){
  mobile_no = "8072812034";
  smsUrl = "http://dnd.blackholesolution.com/api/sendmsg.php?user=VALLIK&pass=abcd1234&sender=VALLIK&phone="+mobile_no+"&text="+msg_to_send+"&priority=ndnd&stype=normal";
  
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http; 
    http.begin(smsUrl);
    int httpResponseCode = http.GET();
    
    if(httpResponseCode == 200){
      String payload = http.getString();
      Serial.println("SMS sent to the user");
     }
    http.end();
  }
}

// Default function to set up the parameters
void setup(void){
  Serial.begin(115200);
  left_servo.attach(4);      // attach the signal pin of servo to pin4 of arduino
  right_servo.attach(4);
  WiFi.begin(ssid, password);
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print("Connecting...");
  }
  
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
}

//Function to release the key
void releaseKey(){
   openBox();
   delay(5000);
   closeBox();
   loggingKeyOut();
}

//Function to drop the key
void dropKey(){
   openBox(); // Opening the box
   delay(5000); 
   closeBox(); // Closing the box
   sendSMS(); //Sending SMS to the user
   loggingKeyIn(); // Logging the key status as IN in the Web application
}

//Default function to loop 
void loop() {
    if(ONETIME){
      closeBox();
      ONETIME = 0;
      delay(10000);
      dropKey();
      }
    if (Serial.available() > 0) {
      incomingByte = Serial.read(); // read the incoming byte:
      if(incomingByte == 49){
        releaseKey();
      }
    }
   
}


