#! /usr/bin/env python
import rospy           #libreria de ROS para python
from std_msgs.msg import Int32  #libreria del msg INT32

class Pub_msgs(object):  
    def __init__(self):        
        self._pub=rospy.Publisher("/led_builtin",Int32,queue_size=1)  #definir publisher 
        self.retard=Int32()       #guardar msg en retard
        self.retard.data=1        #dar como dato 1 a msg

    def launch(self):
        self._pub.publish(self.retard) #publicar msg
        
if __name__=="__main__":          
    rospy.init_node("led_time")  #Crear nodo led_time
    launch_Data=Pub_msgs()       
    rate=rospy.Rate(10)
    ctrlc_c=False

    def shutdownhook():          #Si se cancela el topic, entonces llamar esta funcion
        global ctrlc_c
        ctrlc_c=True
        rospy.loginfo("Nodo apagado")

    rospy.on_shutdown(shutdownhook)

    while not ctrlc_c:         #Mientras el topic no este cancelado
        launch_Data.launch()   #publicar data
        rate.sleep()           #frecuencia de repeticion

        

