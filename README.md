# Laboratorio 1 | TET | Cristian Giraldo | Daniel Cifuentes | Universidad Eafit

## Conceptos fundamentales


Dos o más procesos / aplicaciones en Internet se pueden comunicar de diferentes maneras para implementar un servicio distribuido. Uno de los mecanismos de comunicación más básico es a través de *Sockets*, lo cual plantea una tubería o enlace de comunicación de intercambio de mensajes entre los procesos.

En este caso: el protocolo de la aplicación, middleware, API, etc es responsabilidad del diseñador y desarrollar la aplicación distribuida.

## Especificaciones del reto
1. Defina cualquier tipo de *aplicación sencilla distribuida* que desee diseñar e implementar. (ej: calculadora distribuida, chat, CRUD, etc)
1. Utilizar Sockets *TCP* o *UDP* en cualquier lenguaje de programación de su preferencia
1. Defina, diseñe e implemente el protocolo de aplicación que requiera para implementar dicha aplicación.
1. Realice inicialmente todos los supuestos que requiera respecto a tipo de sistema: C/S o P2P, tipo de arquitectura, y aplique algunos de los conceptos fundamentales de los sistemas distribuidos que se verán en esta Lectura: Introducción a Sistemas Distribuidos.
1. Impleméntela en *AWS Educate. Con el fin de probar la funcionalidad del sistema, se requiere que al menos instancie 3 máquinas **EC2*.


---

# Solución

Para la realización de este laboratorio se realizo una Calculadora usando Sockets en Python a través de protocolos TCP, donde es primordial la confiabilidad de los datos, evitando perdida o mezcla de información.

---

## Arquitectura
Para el desarrollo de este reto hicimos uso de una arquitectura *Cliente-Servidor*

![Cliente-Servidor](https://upload.wikimedia.org/wikipedia/commons/1/1c/Cliente-Servidor.png)

Este es un modelo de diseño de software para *sistemas distribuidos* en el cual las tareas se reparten entre los proveedores de reursos o servicios (servidores) y los demandantes (clientes). Un cliente realiza peticiones a otro programa ubicado en el *servidor*, quien le da la respuesta.

Este concepto es aplicable a programas que se ejecutan en una sola computadora, pero es más provechoso en un sistema operativo *multiusuario* distribuido a través de una red de computadoras.

En la arquitectura *cliente-servidor, por cada **cliente* que llega al *servidor, se crea un **hilo*.

---

## Instancias EC2
Para las máquinas virtuales, usamos instancias *EC2* de *AWS* con sistema operativo *Ubuntu*:


![EC2](https://i.imgur.com/rgIXnGA.jpeg)


### AWS
![Maquinas](https://i.imgur.com/7AvWSuK.jpeg)

### IPs Elasticas

![Elasticas](https://i.imgur.com/2aAHLIN.jpeg)

### Security Groups

![Permisos](https://i.imgur.com/YSaL9sE.jpg)

A través de los permisos otorgodos se garantiza la comunicación por medio de protocolos TCP con el Servidor.