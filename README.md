# Mi Proyecto Django

Este es un proyecto desarrollado con **Django** que implementa una aplicación CRUD. A continuación, se documentan los pasos para contribuir al proyecto y cómo trabajar con Git y GitHub.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

- Python 3.x
- Django
- MySQL (o el motor de base de datos que prefieras)

## Instalación

Sigue estos pasos para configurar tu entorno de desarrollo local:

## 1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/mi-proyecto-django.git

## 2. Accede al directorio del proyecto:

cd mi-proyecto-django

## 3. Instala las dependencias:

Asegúrate de tener un entorno virtual configurado y activa el entorno:

python -m venv venv
source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En WindowsL

luego, instala las dependencias del proyecto:

pip install -r requirements.txt

## 4. Configura la base de datos:

Asegúrate de tener MySQL o el motor de base de datos que uses configurado en tu máquina. Si usas MySQL, asegúrate de crear una base de datos llamada crud_db.

## 5. Realiza las migraciones:

python manage.py migrate

## 6. Inicia el servidor:

python manage.py runserver
