# Trabajo_Final
## Trabajo final Python comisión 44065
Grupo:
- Mariano Ezequiel Schvartzman
- Mariano Moure Jorge

# Requisitos de instalación:
Este proyecto se realizó con Python 3.8. Se recomienda utilizar esta versión o más actual para evitar problemas de compatibilidad.

Como chequear mi versión de python:

in *nix systems:

```bash
> python --version
> python 3.8.0
```

in whindows

```bash
c:\> py --version
c:\> python 3.8.0
```

## instalar dependencias

para instalar las dependencias del proyecto, primero debes correr el comando `pip install` en la terminal. Asegurate de estar en la carpeta del proyecto y poder ver el archivo `requirements.txt` cuando haces un `ls` o `dir`

```bash
> pip install -r requirements.txt
```
## Instalación de dependencias adicionales

```bash
pip install django-bootstar4 
pip install django-bootstrap-datepcker-plus
```

una vez que terminas la instalación de dependencias, debes correr los siguientes comandos de Django:

### Migraciones

*nix:
```bash
> python manage.py migrate
```

windows:
```bash
c:\> py manage.py migrate
```

### Correr el servidor de pruebas

*nix:
```bash
> python manage.py runserver
```

windows:
```bash
c:\> py manage.py runserver
```

ir a localhost:8000/blog-opiniones

para acceder a la app.

Si todo sale bien, deberías ser capaz de abrir el navegador y ver la aplicación funcionando.

## link al video

https://youtu.be/n2KMc-3PZwE
