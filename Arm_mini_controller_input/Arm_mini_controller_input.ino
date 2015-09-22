/*
* Arm mini-controller input code
* Reads potentiometer voltages and hand button to serial
*/

const int shPivot = A0;  //Shoulder yaw pivot //Higher is right, 900-200, mid 520
const int shBase = A1; //Shoulder up/down joint //Higher is up, 700-300, mid 500
const int elPivot = A2; //Elbow yaw pivot //Higher is right, 900-200, mid 520
const int elBase = A3; //Elbow up/down pivot //Higher is down, 750-350, mid 500
const int wrist = A4; //Wrist rotation //Higher is CCW, 0-1023, mid 510

const int handButt = 2; //Gripper button //1 is close, 0 is open

void setup() {
  // initialize serial communications at 115200 bps:
  Serial.begin(9600); 
  pinMode(handButt, INPUT);
}

void loop() {
  int sensArr[6];
  
  sensArr[0] = analogRead(shPivot);
  sensArr[1] = analogRead(shBase);
  sensArr[2] = analogRead(elPivot);
  sensArr[3] = analogRead(elBase);
  sensArr[4] = analogRead(wrist);
  sensArr[5] = digitalRead(handButt);

//  //When request is made for data
//  if (Serial.available()) {
//    //Clear input buffer chars
//    while ( Serial.available() ) { 
//      Serial.read();
//    }
//	
//    //Write out arm data
//    for (int i = 0; i < 6; i++) {
//      Serial.println(sensArr[i]);
//    }
//    //Serial.flush();
//  }
  
  //Write out arm data
  for (int i = 0; i < 6; i++) {
    Serial.println(sensArr[i]);
  }
  Serial.println(';');
  //Serial.flush();
  
}
