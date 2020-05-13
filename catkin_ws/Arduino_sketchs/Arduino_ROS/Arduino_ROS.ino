/* 
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */

#include <ros.h>
#include <std_msgs/Int32.h>
#include <std_msgs/String.h>

ros::NodeHandle  nh;

std_msgs::String state_msgs;
ros::Publisher led_state("led_state",&state_msgs);
char estado[10] = "Proceso ok";

void messageCb( const std_msgs::Int32& retard){
    digitalWrite(LED_BUILTIN,HIGH-digitalRead(LED_BUILTIN));
    delay(retard.data*1000);
}

ros::Subscriber<std_msgs::Int32> sub("led_builtin", &messageCb );

void setup()
{ 
  pinMode(LED_BUILTIN, OUTPUT);
  nh.initNode();
  nh.advertise(led_state);
  nh.subscribe(sub);
}

void loop()
{  
  state_msgs.data = estado;
  led_state.publish( &state_msgs );
  nh.spinOnce();
  delay(100);
}
