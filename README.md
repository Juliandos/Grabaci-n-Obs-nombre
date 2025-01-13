#Proyecto 2 - Extracción de info de libros de tres librerias

## 1. Introducción

Este proyecto permite modificar los nombres de los videos generados por OBS Studio u otros similares, la idea es automatizar el proceso a personas que tengan que generar estos tipos de archivos y guardarlos con nombres apropiados

# 2. Instalación

## 2.1 Requisitos

    - Python 3.8 o superior
    - OBS Studio
    - Librería watchdog

## 2.2 Creation virtual environment
Use this to create a virtual environment

```bash
    python -m venv venv
```

## 2.2 Activación entorno virtual
Usa esto para activar tu entorno virtual

Linux/Mac OS:

```bash
    source venv/bin/activate
    ```

Windows:

```bash
    venv\Scripts\activate
```

## 2.3 Install dependencies

Para instalar las dependencias desde el entorno virtual usa este comando:

```bash
pip install -r requirements.txt
```

# 3 Execution
Para ejecutar el modelo usa el siguiente comando:

```bash
flask --app app run --debug
```
