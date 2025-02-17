# Creemos un Taximetro digital

<details>
  <summary>¿Que voy a encontrarme?</summary>
  <ol>
    <li>
      <a href="#Acerca-del-proyecto">Acerca del proyecto</a>
      <ul>
        <li><a href="#estado-del-proyecto">Estado del proyecto</a></li>
        <li><a href="#Mis-herramientas">Mis herramientas</a></li>
      </ul>
    </li>
    <li>
      <a href="#Empecemos">Empecemos</a>
      <ul>
        <li><a href="#¿Cómo-me-organizo?">¿Cómo me organizo?</a></li>
        <li><a href="#Vamos-paso-a-paso">Vamos paso a paso</a></li>
      </ul>
    </li>
    <li><a href="#Pongamoslo-a-prueba">Pongamoslo a prueba</a></li>
    <li><a href="#Pruebalo-en-tu-local">Pruebalo en tu local</a></li>
  </ol>
</details>

## Acerca del proyecto
Vamos a modernizar el sistema de taxis a la vez que practicamos el uso de python, en este reto nos enfrentaremos con el uso de clases y funciones que nos permitan calcular el precio de un trayecto ya sea mientras esta el taxi en pausa o en movimiento (los taximetros no paran hasta terminar el trayecto). Acompañame a esta aventura.

### Estado del proyecto

:construction: Proyecto en construcción :construction:

### Mis herramientas
* Aprende a usar jira en 15 minutos: [jira](https://www.youtube.com/watch?v=fIHFcMy-Azo)
* Crea commits convencionales: [conventional commits](https://dev.to/achamorro_dev/conventional-commits-que-es-y-por-que-deberias-empezar-a-utilizarlo-23an)
* Crea diagramas UML: [draw.io](https://app.diagrams.net/)
* Sobre clases en python: [clases](https://blog.hubspot.es/website/clases-python)
* : []()
* : []()

## Empecemos

### ¿Cómo me organizo?

- Accede a mi kanban de jira: [Kanban](https://abigailmasapanta.atlassian.net/jira/software/projects/TAX/boards/3?atlOrigin=eyJpIjoiMWFmMjJjMDg0ZWQwNDZhMWE4M2MyMzAxYjVkMzI2YzQiLCJwIjoiaiJ9)
- [ ]

### Vamos paso a paso

> [!WARNING]
> 
> Todo lo escrito es en base a mi experiencia, cada quien tiene su propio camino y tiempo. Espero que lo tomes como un complemento a tu formación y no como las sagradas escrituras.

#### Planificación y Diseño
Antes de empezar a picar código me gusta implementar un diagrama UML de lo que será mi programa. Hago esto no solo por tener buenas prácticas, también para que me sirva de guía en el estimado del tiempo que le dedicaré. Esto es totalmente flexible y se puede modelar según lo que vaya aprendiendo a lo largo del desarrollo del programa.

![UML](https://github.com/abbyenredes/taximetro_digital/blob/main/img/tax%C3%ADmetro(b%C3%A1sico).drawio.png)

A raiz de este diagrama voy a crear la estructura basica de mi código para así poder hacerme una idea de que conocimientos necesito y que debo reforzar:

📂 taximetro.py  
├── **Clase Taximetro** (Lógica del cálculo de tarifas)  
├── **Métodos:**  
│   ├── `iniciar_viaje()` (Resetea y empieza el conteo)  
│   ├── `cambiar_estado(nuevo_estado)` (Alterna entre parado y en movimiento)  
│   ├── `finalizar_viaje()` (Calcula el total y finaliza el viaje)  
├── **Función `main()`** (Menú interactivo en la terminal)  

#### Implementación de la Base
Vamos armando ya en código nuestro plan: 

Primero importo la libreria [time](https://docs.python.org/es/3.10/library/time.html) ya que voy a estar usandola para el conteo del tiempo en el ejecute mi programa, depues voy a crear una clase llamada `taximeter` acompañada de 2 variables globales que son mi precio en movimiento y mi precio parado.

A continuación agregó el método `start_trip()`
en el Empezare el viaje en el que volvaremos informacion como: inicio, estado, registro del tiempo.

Ahora creamos un método para cambiar el estado del taxi (en movimiento o parado) `change_state()` aqui llamamos a las variables globales y registramos su tiempo ya sea si elegimos que esta en marcha o esta parado. 

#### La lógica en el calculo de tarifas

##### Costo cuando está en reposo (idle):

```plaintext
Costo acumulado += (Tiempo transcurrido × 0.02)
```

##### Costo cuando está en movimiento (moving):

```plaintext
Costo acumulado += (Tiempo transcurrido × 0.05)
```
##### Cálculo de tarifas

| Estado       | Duración (segundos) | Tarifa aplicada (€ por segundo) | Costo acumulado (€) |
|-------------|--------------------|---------------------------------|--------------------|
| **Idle**    | 10 sec             | 0.02 €/s                        | 10 × 0.02 = 0.20   |
| **Moving**  | 20 sec             | 0.05 €/s                        | 20 × 0.05 = 1.00   |
| **Idle**    | 5 sec              | 0.02 €/s                        | 5 × 0.02 = 0.10    |
| **Moving**  | 15 sec             | 0.05 €/s                        | 15 × 0.05 = 0.75   |
| **Fin de viaje** | -          | -                                | **Total: 2.05€**  |

Con esta lógica vamos a realizar nuestro último método `end_trip()` para finalizar mi recorrido y devuelver el total del precio del recorrido.
#### Menú interactivo
Creamos un menú sencillo a base de concicionales del 1-4; Para finalizar creo el método main en el que se ejecutara mi código que a su vez tiene un submenú que pregunta al usuario si quiere iniciar un nuevo trayecto, en el cual uso el método lower para poner en minúscula tanto "Y" como "N".
## Pongamoslo a prueba

![](link)

## Pruebalo en tu local
Descargate mi repositorio:

`git clone https://github.com/abbyenredes/taximetro_digital.git`

Accede a la carpeta:

`cd taximetro_digital`

Ejecuta el programa:

`python3 tax_basic.py`


> [!IMPORTANT]
> Verifica tu versión de python antes de ejecutar este programa `python3 --version` ya que depende de ello puedes ejecutar con python o python3

# Good Luck
![cat](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR7zX8eUGUkdq6m5H0_B85HegxkRSbZvI2Epw&s)
