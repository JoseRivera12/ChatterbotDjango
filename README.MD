# ORWELL | Chatbot

Proyecto Escolar. Chatbot para brindar soporte técnico básico de computadoras.
El bot se configura a partir de un archivo yml para responder preguntas básicas acerca de problemas comunes de computadoras y en caso de no contar con una respuesta genera una cita de reparación a la que pueden acceder sólo los usuarios administradores o técnicos. Además se guardan todas las conversaciones generadas para determinar casos en los cuales el bot no responda como se espera

Stack

- Django
- Python
- MongoDB
- Chatterbot
- PostgreSQL

Se creó el archivo docker-compose ya que al realizar la instalación existía una incompatibilidad con algunas versiones de las dependencias. además de ser más fácil de instalar.


## Instalación

Es necesario instalar previamente docker y docker-compose

I. El primero paso es clonar el repositorio

```sh
$ git clone git@github.com:JoseRivera12/ChatterbotDjango.git
```

II. El siguiente paso es levantar los contenedores ejecutando los siguientes pasos

```sh
$ docker-compose build
$ docker-compose up
```

III. Lo siguiente es acceder al contenedor de Django para ejecutar las migraciones de la base de datos y el entrenamiento del bot que se encuentra en el archivo soporte.yml

```sh
$ docker ps #obtiene los identificadores de los contenedores
$ docker exec -it <id-container> sh
$ python manage.py migrate
$ cd /proyecto_is/
$ python train.py
```
### El proyecto se podría adecuar a otros casos creando otros archivos yml de entrenamiento para el bot o modificando el archivo soporte.yml

## Otra forma de entrenar el bot es crear una cuenta de administrador y escribir las preguntas y respuestas en "Entrenar al bot"
