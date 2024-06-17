# Django Balance Project

Este es un proyecto base de Django diseñado específicamente para estructurar y organizar el proyecto. Proporciona una estructura escalable y está preparado para ser utilizado con una base de datos PostgreSQL.

## 🚀 Pasos de instalación

### 1. Crear un entorno virtual

Utilizamos `venv` para manejar entornos virtuales. Para crear un nuevo entorno virtual llamado `venv-inmobiliaria`, ejecuta:

python3.11 -m venv venv-inmoniliaria


Activar el entorno virtual:


- **Linux o Mac**:

source venv-inmobiliaria/bin/activate

- **Windows**:

cd venv-inmobiliaria

cd Scripts

```./activate```


### 2. Instalación de dependencias

Una vez dentro del entorno virtual, navega hasta la raíz del proyecto y ejecuta:

pip install -r requirements.txt



### 3. Configuración de credenciales

Dentro de la raíz del proyecto, crea un archivo llamado `secret.json` con la siguiente estructura:

```json
{
    "FILENAME": "secret.json",
    "SECRET_KEY": "clave_secreta_pedir_administrador_del_sistema",
    "DB_NAME": "DB_Inmobiliaria",
    "DB_USER": "postgres",
    "DB_PASSWORD": "tango12",
    "DB_HOST": "localhost",
    "DB_PORT": 5432
}
```
Nota: Asegúrate de cambiar los valores de SECRET_KEY, DB_NAME, DB_USER y DB_PASSWORD a los apropiados para tu configuración.

### 4. Configuración de la base de datos

Dado que utilizamos PostgreSQL como base de datos, asegúrate de tenerlo instalado y en ejecución.

### 5. Crear y aplicar migraciones

Para crear las migraciones y aplicarlas, ejecuta:

python manage.py makemigrations
python manage.py migrate

### 6. Variable de entorno
al ejecutar la aplicación o al configurar tu entorno virtual. Puedes hacerlo directamente en la terminal antes de ejecutar tu aplicación.

**En sistemas basados en Unix/Linux/Mac**

###########################################################

sudo su root

source venv-balance/bin/activate

export DEVELOPMENT_ENVIRONMENT="True"

python manage.py runserver

###########################################################

```export DEVELOPMENT_ENVIRONMENT=True```

**En Windows (CMD)**

```set DEVELOPMENT_ENVIRONMENT=True```


### 7. Ejecutar el proyecto

```python manage.py runserver```

¡Listo! Ahora puedes acceder a tu proyecto Django desde http://localhost:8000/.



## RESUMEN DE INSTALACION
###########################################################

python3.11 -m venv venv-inmobiliaria

source venv-inmobiliaria/bin/activate

pip install -r requirements.txt

**secret.json**
{
    "FILENAME": "secret.json",
    "SECRET_KEY": "clave_secreta_pedir_administrador_del_sistema",
    "DB_NAME": "DB_Inmobiliaria",
    "DB_USER": "postgres",
    "DB_PASSWORD": "password",
    "DB_HOST": "localhost",
    "DB_PORT": 5432,
}

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

###########################################################
