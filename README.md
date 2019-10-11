# MACProgramming
**Actores / Elementos en Accion**
* Estaciones
* Canal
* Tramas
* Agentes de Red que consumen servicios
* Tramas de Control

## Canal:
Tiene ciertos parametros como el ruido que determina la probabilidad de que hayan errores
*-Tasa de Errores*
*Retraso minimo relativo a la distancia entre estaciones*
* Esto es un factor que multiplicada a la distancia da el retraso para que llegue a la otra estacion

## Estaciones
Tienen una cola donde se simula un buffer de cierto tamaño
Poseen funcionalidad para controlar errores y analizar tramas
* Errores
    * Checksum, CRC
* Tramas
    * Checkeo de banderas de tramas
* Simulan ejecutar funciones para enviar tramas a capa de red
* Tienen la capacidad de crear tramas y enviarlas
* Tiene un parametro que especifica su capacidad, si se recibe mas que esa pierde tramas.

## Tramas
* Su contenido esta en formato de bytes ('b)
* Al crearse se setean mediante probabilidades, la chance de que tengan errores o no lleguen.
* Se aplica lo mismo para la trama de control

### Ciclo de Acciones de una Estacion