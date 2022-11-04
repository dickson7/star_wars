# Star Wars
API Rest para un sitio web para los fanáticos de star wars.

Los usuarios se puedes registrar y consumir la api. 

Los endpoint permiten listar los personajes de Star Wars, con detalles de peliculas y planetas. 

Adiconal se puede agregar y consultar los modelos Planetas, Personajes y Peliculas.

No se puede hacer uso de la api sin Bearer Token, una ves registrado, puede iniciar sesión y se le asignara el token. 

### Instalación 🔧

Para realizar la instalación se deben seguir los siguientes pasos,

_Clonación del repositorio_

```shell
git clone git@github.com:dickson7/star_wars.git
```

_Ingresamos en el directorio del repositorio clonado, y ejecutamos el siguiente comando para habilitar el entorno virtual_

```shell
python3 -m venv env
```

_Activamos el entorno virtual_

```shell
source env/bin/activate
```

_Instalamos las dependencias con pip_

```shell
(env)$ pip3 install -r requirements.txt
```

_Lanzamos migraciones_

```shell
(env)$ python3 manage.py makemigrations
(env)$ python3 manage.py migrate
```

_Como último paso realizamos la ejecución del servidor_

```shell
(env)$ python3 manage.py runserver
```

### Coleccion de Potsman 
En este repo se encuentra la collección de postman para probar y hacer uso de la api. 



#
## Tests
_Para ejecutar los tests usamos este comando_
```shell
(env)$ python3 manage.py test 
```
  
### Informe de cobetura
```shell
(env)$ coverage run manage.py test -v 2 && coverage report 
```

```python
Name                            Stmts   Miss  Cover
---------------------------------------------------
api/admin.py                        1      0   100%
api/apps.py                         4      0   100%
api/models.py                      28      0   100%
api/serializers.py                 14      0   100%
api/tests.py                       15      0   100%
api/urls.py                        13      0   100%
api/views/films.py                  7      0   100%
api/views/people.py                 7      0   100%
api/views/planets.py                7      0   100%
api/views/search_people.py         37     17    54%
authentication/admin.py             1      0   100%
authentication/apps.py              4      0   100%
authentication/backends.py         19      5    74%
authentication/models.py           13      0   100%
authentication/serializers.py      15      0   100%
authentication/urls.py              3      0   100%
authentication/views.py            30      2    93%
manage.py                          12      2    83%
starwars/settings.py               21      0   100%
starwars/urls.py                    3      0   100%
---------------------------------------------------
TOTAL                             254     26    90%
```



#
#
# Authentication

## Register

Este endpoint le permite registrarse en la app

```python
import requests
import json

url = "http://127.0.0.1:8000/api/auth/register"

payload = json.dumps({
  "username": "test",
  "email": "test@q2.com",
  "password": "q1w2e3r4"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


```



## Login

El inicio de sesión le dara el token para el consumo de los endpoint

```python
import requests
import json

url = "http://127.0.0.1:8000/api/auth/login"

payload = json.dumps({
  "username": "test",
  "password": "q1w2e3r4"
})
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InExIiwiZW1haWwiOiJxMUBxMS5jb20iLCJleHAiOjE2Njc2MDM4OTl9.zcCjyxR_r8Dp8dNJLj8JrzBKhMV_ehZx9BUcbQgsd_0',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```
#
# Search Endpoint

Este endpoint le permite consultar todos los personajes de Star Wars

```python
import requests

url = "http://127.0.0.1:8000/api/search_people/"

payload={}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InExIiwiZW1haWwiOiJxMUBxMS5jb20iLCJleHAiOjE2Njc2MDM4OTl9.zcCjyxR_r8Dp8dNJLj8JrzBKhMV_ehZx9BUcbQgsd_0'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```

Con el parametro ```name``` puede consultar por el nombre del personaje.

```python
import requests

url = "http://127.0.0.1:8000/api/search_people/?name=Luke Skywalker"

payload={}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InExIiwiZW1haWwiOiJxMUBxMS5jb20iLCJleHAiOjE2Njc2MDM4OTl9.zcCjyxR_r8Dp8dNJLj8JrzBKhMV_ehZx9BUcbQgsd_0'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
```
### People (personajes)
#### Method  ```POST```
```Python
import requests
import json

url = "http://127.0.0.1:8000/api/people/"

payload = json.dumps({
  "name": "Lama Su",
  "height": "229",
  "mass": "88",
  "gender": "male",
  "homeworld": "10",
  "films": "[2, 1]",
  "species": "32"
})
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InExIiwiZW1haWwiOiJxMUBxMS5jb20iLCJleHAiOjE2Njc2MDM4OTl9.zcCjyxR_r8Dp8dNJLj8JrzBKhMV_ehZx9BUcbQgsd_0',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```

### Films
#### Method  ```GET```
```Python
import requests

url = "http://127.0.0.1:8000/api/films/"

payload={}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InExIiwiZW1haWwiOiJxMUBxMS5jb20iLCJleHAiOjE2Njc2MDM4OTl9.zcCjyxR_r8Dp8dNJLj8JrzBKhMV_ehZx9BUcbQgsd_0'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

```
#### Method  ```POST```
```Python
import requests
import json

url = "http://127.0.0.1:8000/api/films/"

payload = json.dumps({
  "name": "Return of the Jedi",
  "episode_id": 6,
  "opening_crawl": "Luke Skywalker has returned to\r\nhis home planet of Tatooine in\r\nan attempt to rescue his\r\nfriend Han Solo from the\r\nclutches of the vile ...",
  "director": "Richard Marquand",
  "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
  "planets": "[1, 2 , 7 , 8, 9]"
})
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InExIiwiZW1haWwiOiJxMUBxMS5jb20iLCJleHAiOjE2Njc2MDM4OTl9.zcCjyxR_r8Dp8dNJLj8JrzBKhMV_ehZx9BUcbQgsd_0',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

### Planets
#### Method  ```POST```
```Python
import requests
import json

url = "http://127.0.0.1:8000/api/planets/"

payload = json.dumps({
  "name": "Hoth test",
  "rotation_period": "23",
  "orbital_period": "549",
  "diameter": "7200",
  "climate": "frozen",
  "gravity": "1.1 standard",
  "terrain": "tundra, ice caves, mountain ranges",
  "surface_water": "100",
  "population": "unknown",
  "residents": "[]",
  "films": "[2]"
})
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InExIiwiZW1haWwiOiJxMUBxMS5jb20iLCJleHAiOjE2Njc2MDM4OTl9.zcCjyxR_r8Dp8dNJLj8JrzBKhMV_ehZx9BUcbQgsd_0',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```
#### Method  ```GET```
```Python
import requests

url = "http://127.0.0.1:8000/api/planets/1"

payload={}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InExIiwiZW1haWwiOiJxMUBxMS5jb20iLCJleHAiOjE2Njc2MDM4OTl9.zcCjyxR_r8Dp8dNJLj8JrzBKhMV_ehZx9BUcbQgsd_0'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

```