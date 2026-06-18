# CHATBOT DE GESTIÓN DE VACACIONES

## Descripción

Este proyecto fue desarrollado como Trabajo Práctico Integrador para la materia Organización Empresarial de la Tecnicatura Universitaria en Programación (UTN).

El sistema consiste en un chatbot que simula el proceso de solicitud y gestión de vacaciones de empleados dentro de una institución educativa.

El objetivo es automatizar un proceso administrativo que normalmente se realiza de forma manual, aplicando conceptos de modelado de procesos BPMN, gestión de estados y persistencia de datos.

---

## Funcionalidades

* Validación de identidad mediante ID de empleado.
* Consulta de antigüedad del empleado.
* Cálculo automático de días de vacaciones.
* Solicitud de fechas de vacaciones.
* Registro de solicitudes en una base de datos simulada.
* Manejo de errores y control de intentos.
* Derivación automática a Recursos Humanos ante errores reiterados.

---

## Archivos del Proyecto

### empleados.csv

Contiene la información básica de los empleados:

* ID de empleado
* Nombre
* Antigüedad

### vacaciones.csv

Contiene la información de las solicitudes de vacaciones:

* ID de empleado
* Fecha de inicio
* Fecha de fin
* Estado de la solicitud

### code.py

Contiene toda la lógica del chatbot.

---

## Flujo General del Sistema

1. El empleado ingresa su ID.
2. El sistema valida la existencia del empleado.
3. Se calcula la cantidad de días de vacaciones disponibles.
4. El usuario ingresa una fecha de inicio.
5. El sistema valida la solicitud.
6. La información se registra en la base de datos.
7. Se notifica el resultado de la operación.

---

## Tecnologías Utilizadas

* Python
* CSV como base de datos simulada
* GitHub
* GitHub Desktop

---

## Integrantes

* Leila Gómez
* Micaela Ibarra

---

## Materia

Organización Empresarial

Tecnicatura Universitaria en Programación (UTN)
