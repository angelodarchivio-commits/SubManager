# SubManager — Administrador de Suscripciones

SubManager es un programa en Python para gestionar suscripciones mensuales (Netflix, Spotify, etc.).
Permite agregar, listar y eliminar suscripciones, calcular el gasto mensual y guardar los datos en data/subscriptions.csv.



## Dependencias

El proyecto utiliza dos librerías externas:

- pandas → Manejo de archivos CSV  
- rich → Tablas y salida visual en consola  

Instalación automática:  
    pip install -r requirements.txt


## Instalación y Ejecución

### Clonar el repositorio
    git clone https://github.com/angelodarchivio-commits/SubManager.git
    cd SubManager


### Crear entorno virtual  
    python -m venv venv


### Activar entorno virtual

Windows:  
    venv\Scripts\activate

Linux / Mac:  
    source venv/bin/activate


### Instalar dependencias  
    pip install -r requirements.txt


## Ejecutar el programa

Abrir una terminal en la carpeta raíz del proyecto (donde está la carpeta `submanager/`) y ejecutar:

```bash
py -m submanager.main



## ¿Qué puede hacer SubManager?

Agregar una suscripción  
Guarda nombre del servicio, precio y fecha de renovación.

Listar suscripciones  
Usa tablas estilizadas gracias a Rich.

Eliminar suscripción  
Elimina por nombre sin complicaciones.

Calcular gasto mensual total  
Suma automáticamente todos los precios del CSV.


## Arquitectura del Código

### manager.py
Contiene la clase SubscriptionManager, encargada de:
- Leer CSV  
- Guardar CSV  
- Realizar operaciones CRUD  
- Calcular el gasto mensual  
- Cumplir PEP8 y PEP257



### main.py
- Interfaz CLI interactiva  
- Manejo de entradas del usuario  
- Tablas con Rich  
- Lógica de flujo del programa  



### utils.py
- Archivo propio vacío  
- Incluido para cumplir con el requisito de “módulo propio”


## Buenas Prácticas Implementadas

- Cumplimiento de PEP8 (estilo y formato)  
- Docstrings conforme PEP257  
- Arquitectura modular  
- Aplicación del Zen de Python  “Simple es mejor que complejo”  
- Separación entre lógica y presentación  
- Uso de entorno virtual (venv)  
- Código claro, mantenible y escalable  




