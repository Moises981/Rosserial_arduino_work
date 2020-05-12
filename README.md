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
Usar el arduino como topic publisher, para publicar el estado de sus pines y usar ROS como subscriber a esos pines.
Usar el ROS como publisher para poder controlar los puertos PWM del arduino


