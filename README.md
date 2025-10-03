# Proyecto CRUD con Django y MySQL

Este es un proyecto CRUD utilizando **Django**, **Django REST Framework** y **MySQL** como base de datos. 
El propósito es gestionar tareas mediante una API RESTful.

---

### 1. Instalación de dependencias

Para comenzar, es necesario tener un entorno virtual y las dependencias requeridas para el proyecto.

**Comandos:**

1. Crear un entorno virtual:

    ```bash
    python -m venv venv
    ```

2. Activar el entorno virtual:

    - En **Windows**:

      ```bash
      .\venv\Scripts\activate
      ```

    - En **Mac/Linux**:

      ```bash
      source venv/bin/activate
      ```

3. Instalar las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

Las dependencias necesarias están listadas en `requirements.txt`. Algunas de ellas son:

- `asgiref==3.9.2`
- `Django==5.2.7`
- `djangorestframework==3.16.1`
- `mysqlclient==2.2.7`
- `python-dotenv==1.1.1`
- `sqlparse==0.5.3`
- `tzdata==2025.2`

---

### 2. Configuración de la base de datos MySQL

Este proyecto usa **MySQL** como base de datos. A continuación, se detalla cómo configurar MySQL:

1. Crear una base de datos en MySQL:

    ```sql
    CREATE DATABASE crud_db;
    ```

2. Asegurarse de tener un usuario con los permisos necesarios (puedes usar el usuario `root`
   para fines de desarrollo):

    ```sql
    CREATE USER 'root'@'localhost' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON crud_db.* TO 'root'@'localhost';
    ```

---

### 3. Configuración de Django

En el archivo `settings.py`, configurar la base de datos y las variables de entorno:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```
Configurar el archivo .env para gestionar las credenciales de forma segura:
```
DB_NAME=crud_db
DB_USER=root
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=3306
```
---

### 4. Migraciones y configuración de la base de datos

Una vez configurada la base de datos, debemos aplicar las migraciones de Django:

python manage.py makemigrations

---

### 5. Creación de la API RESTful
```
Se ha implementado un CRUD básico para las tareas. Las vistas son las siguientes:

Listar tareas: GET /tasks/

Crear tarea: POST /tasks/

Detalle de tarea (obtener, actualizar, eliminar): GET, PUT, DELETE /tasks/{id}/

Las vistas están implementadas en crud/views.py:

from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
```

---

### 6. Probar la API con Postman

Puedes probar los endpoints de la API utilizando Postman o cURL.
```
Listar tareas:

Método: GET

URL: http://127.0.0.1:8000/tasks/

Crear tarea:

Método: POST

URL: http://127.0.0.1:8000/tasks/

Cuerpo:

Obtener detalle de tarea:

Método: GET

URL: http://127.0.0.1:8000/tasks/{id}/

Actualizar tarea:

Método: PUT

URL: http://127.0.0.1:8000/tasks/{id}/

Cuerpo:

{
    "title": "Tarea actualizada",
    "completed": true
}


Eliminar tarea:

Método: DELETE

URL: http://127.0.0.1:8000/tasks/{id}/

```

---

### 7. Pruebas unitarias

El proyecto incluye pruebas unitarias para el modelo Task y la API. Las pruebas están 
implementadas en crud/tests.py.

Para ejecutar las pruebas:

1. Ejecuta el siguiente comando:

python manage.py test crud

Resultado esperado:
```
Found 4 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....
----------------------------------------------------------------------
Ran 4 tests in 0.119s

OK
Destroying test database for alias 'default'...
```

---

### 8. Configuración de GitHub Actions para CI

Se ha configurado GitHub Actions para realizar las pruebas automáticamente al realizar 
un push a la rama main o al abrir un pull request.

El archivo de configuración de GitHub Actions es el siguiente: .github/workflows/django.yml
```
name: Django CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    services:
      mysql:
        image: mysql:5.7
        env:
          MYSQL_ROOT_PASSWORD: password
          MYSQL_DATABASE: crud_db
        ports:
          - 3306:3306
        options: --health-cmd="mysqladmin ping --silent" --health-timeout=5s --health-start-period=10s

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Wait for MySQL to be ready
        run: |
          until mysqladmin ping -h127.0.0.1 --password=password --silent; do
            echo "Waiting for database..."
            sleep 5
          done

      - name: Run tests
        run: |
          python manage.py migrate
          python manage.py test
```

   Acciones:
      
     # Checkout: Obtiene el código del repositorio.
      
     # Set up Python: Configura la versión de Python.
      
     # Install dependencies: Instala las dependencias de requirements.txt.
      
     # Wait for MySQL: Espera a que MySQL esté disponible.
      
     # Run tests: Ejecuta las migraciones y las pruebas unitarias.

---

### 9. Despliegue y uso

El proyecto está listo para ser desplegado en un servidor con MySQL 
y servicios web como Heroku, AWS, o DigitalOcean.

1. Despliegue: Puedes usar Heroku o cualquier otro servicio de tu elección. Si usas Heroku, asegúrate
   de configurar las variables de entorno (como DB_NAME, DB_USER, etc.) en su panel de configuración.
2. Uso de la API: Puedes realizar peticiones a los endpoints de la API
   utilizando herramientas como Postman o cURL.





































