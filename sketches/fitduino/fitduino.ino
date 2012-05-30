int incomingByte = 0;   // for incoming serial data
int eyePin1 = 2;
int eyePin2 = 3;
int mouthPin1 = 4;
int mouthPin2 = 5;
int mouthPin3 = 6;
int mouthPin4 = 7;
int smilePin1 = 8;
int smilePin2 = 9;
int frownPin1 = 10;
int frownPin2 = 11;

void setup() {
  Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
  pinMode(eyePin1, OUTPUT);
  pinMode(eyePin2, OUTPUT);
  pinMode(mouthPin1, OUTPUT);
  pinMode(mouthPin2, OUTPUT);
  pinMode(mouthPin3, OUTPUT); 
  pinMode(mouthPin4, OUTPUT);
  pinMode(smilePin1, OUTPUT);
  pinMode(smilePin2, OUTPUT);
  pinMode(frownPin1, OUTPUT);
  pinMode(frownPin2, OUTPUT);  
  
  oneOnAtATime();
  turnAllOff();
}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    oneOnAtATime();
  
    // say what you got:
    Serial.print("I received: ");
    Serial.println(incomingByte, DEC);
    
    // adjust the lights, shit by 48 for DEC
    setLights(incomingByte - 48);    
  }
}

void setLights(int level) {
  // Always set these on
  digitalWrite(eyePin1, HIGH);
  digitalWrite(eyePin2, HIGH);
  digitalWrite(mouthPin1, HIGH);
  digitalWrite(mouthPin2, HIGH);
  digitalWrite(mouthPin3, HIGH);
  digitalWrite(mouthPin4, HIGH);
  if (level == 0) {
    digitalWrite(frownPin1, HIGH);
    digitalWrite(frownPin2, HIGH);
    digitalWrite(smilePin1, LOW);
    digitalWrite(smilePin2, LOW);
  } else if (level == 1) {
    digitalWrite(frownPin1, LOW);
    digitalWrite(frownPin2, LOW);
    digitalWrite(smilePin1, LOW);
    digitalWrite(smilePin2, LOW);
  } else if (level == 2) {
    digitalWrite(frownPin1, LOW);
    digitalWrite(frownPin2, LOW);
    digitalWrite(smilePin1, HIGH);
    digitalWrite(smilePin2, HIGH);   
  }
}

void oneOnAtATime(){
  int delayTime = 100; //the time (in milliseconds) to pause between LEDs
                       //make smaller for quicker switching and larger for slower
  
  for(int i = 2; i < 12; i++){
    int offLED = i - 1;  
    if(i == 2) {         
      offLED = 11;
    }      
    digitalWrite(i, HIGH);     
    digitalWrite(offLED, LOW); 
    delay(delayTime);
  }
}

void turnAllOff() {
    digitalWrite(frownPin1, LOW);
    digitalWrite(frownPin2, LOW);
    digitalWrite(smilePin1, LOW);
    digitalWrite(smilePin2, LOW);
    digitalWrite(eyePin1, LOW);
    digitalWrite(eyePin2, LOW);
    digitalWrite(mouthPin1, LOW);
    digitalWrite(mouthPin2, LOW);
    digitalWrite(mouthPin3, LOW);
    digitalWrite(mouthPin4, LOW);    
}