# Rosserial_arduino_work
Rosserial es una libreria de arduino que sirve para crear un nodo de comunicacion serial de ROS con este nodo se puede crear un topico , ya puede ser un publisher , subscriber o incluso un service , esto dependera del uso que se le quiera dar al arduino o tros placas con referencia a ROS.

Especificaciones de la libreria Rosserial para el arduino:
ATMEGA328P(6/6 Publishers o subscribers 150/150 bytes).
ATMEGA328P(25/25 Publishers o subscribers 280/280 bytes).
Otros(25/25 Publishers o subscribers 512/512 bytes).

Ademas rosserial posee para librerias para diferentes hardwares:
Rosserial_arduino
Rosserial_xbee
Rosserial_teensy
Rosserial_stm32
Rosserial_windows
Rosserial_embededlinux
Rosserial_mbed
Rosserial_tivac

Para trabajar con rosserial_arduino debemos añadir los paquetes de rosserial mediante la clonacion del git:
https://github.com/ros-drivers/rosserial

Una vez copiado compilamos el catkin_ws o el espacio de trabajo de ROS.
![asus@asus-ROG-Strix-G531GT-G531GT: ~-Escritorio-Rosserial_arduino_work_015](https://user-images.githubusercontent.com/59718261/81739850-a6d5f600-9461-11ea-805f-5f5f9ad47580.png)

Creamos un paquete de ROS para poder crear nuestro topic y subscriber , en este ejemplo lo que quiero hacer es :
Usar el arduino como publisher para mandar un string o texto en un topic.
Usar el ROS como publisher para mandar tiempo de retardo entre apagado y encendido del led en segundos , y el arduino como subscriber para obtener esos datos del topic.

Primero se debe instalar la libreria rosserial en arduino IDE para ellos sigue las siguientes instrucciones.
http://wiki.ros.org/rosserial_arduino/Tutorials/Arduino%20IDE%20Setup
Despues de ello creamos un sketch de arduino para compilar , el cual se encuentra en la carpeta ARDUINO_ROS dentro del catkin_Ws.

![Arduino_ROS Arduino 1 8 12_016](https://user-images.githubusercontent.com/59718261/81755709-1c9c8a80-947f-11ea-85db-879d3131a04d.png)

Una vez subido el sketch al arduino se debe activar el roscore.

![roscore http:--asus-ROG-Strix-G531GT-G531GT:11311-_017](https://user-images.githubusercontent.com/59718261/81755775-4c4b9280-947f-11ea-8ca8-403b74b430a7.png)

Despues lanzar el rosserial_node con el comando "rosrun rosserial_python serial_node.py /dev/ttyACM0".

![asus@asus-ROG-Strix-G531GT-G531GT: ~_018](https://user-images.githubusercontent.com/59718261/81755849-8a48b680-947f-11ea-9b16-88193f997ff0.png)

Ahora si procemos a usar "rostopic list" tendremos lo siguiente:

![asus@asus-ROG-Strix-G531GT-G531GT: ~_019](https://user-images.githubusercontent.com/59718261/81755881-aba9a280-947f-11ea-8515-0fd7743ec936.png)

Si procedemos a ver el topic led_state que declaramos que tendria un publisher de tipo string que mandaria un mensaje "Proceso ok" , para ello introducir el siguiente comando "rostopic echo /led_state":

![asus@asus-ROG-Strix-G531GT-G531GT: ~_020](https://user-images.githubusercontent.com/59718261/81755977-06db9500-9480-11ea-8cea-d2f672a080d4.png)

Despues para mandar publicar un mensaje al topic /led_builtin , en el cual se puede mandar el tiempo del parpadeo del led , para ello podemos usar el siguiente comando "rostopic pub /led_builtin std_msgs/Int32 [TAB] + [TAB]", presionar dos veces TAB no escribirlas.

![asus@asus-ROG-Strix-G531GT-G531GT: ~_021](https://user-images.githubusercontent.com/59718261/81756208-b44ea880-9480-11ea-94bd-04f1c3dd380d.png)

Sin embargo , se observara que al lanzarlo o cada vez que lo ejecutemos este cambiara de estado ,esto se debe a que solo manda un mensaje publicador una sola vez , entonces si creamos un topic_publisher con ROS , podremos hacer que este parpadee en x tiempo.

![Selección_023](https://user-images.githubusercontent.com/59718261/81756617-dac11380-9481-11ea-8e45-715246966c34.png)

Ahora ejecutemos el launch topic_pub.launch para ello se usa el siguiente comando:

![-home-asus-Escritorio-Rosserial_arduino_work-catkin_ws-src-topic_arduino-launch-topic_pub launch http:--localhost:11311_024](https://user-images.githubusercontent.com/59718261/81756862-9bdf8d80-9482-11ea-9bde-f307e130f50b.png)

Despues de esto el led deberia estar parpadeando a razon de un segundo a no ser que se cambie el valor del retard.data en el publisher.








