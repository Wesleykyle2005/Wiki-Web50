# Proyecto Wiki con Django

Este proyecto corresponde a una enciclopedia basada en Markdown, desarrollada con el framework Django.

## Descripción General

La aplicación permite:
- Crear nuevas entradas y guardarlas en formato Markdown.  
- Editar entradas existentes.  
- Buscar entradas por coincidencia de texto.  
- Visualizar entradas en HTML a partir de contenido Markdown.  
- Mostrar una página de error personalizada (error.html) o un error 404 si la URL no existe.

## Requisitos

- Python 3.x  
- Django 3.x o superior  

## Estructura de Archivos

- **wiki/**  
  - Contiene la configuración principal del proyecto (settings.py, urls.py, etc.).  

- **encyclopedia/**  
  - **templates/encyclopedia/**  
    - layout.html (plantilla base)  
    - index.html (lista de entradas)  
    - entry.html (vista de entrada en particular)  
    - new_entry.html (formulario para crear/editar entradas)  
    - error.html (manejo de errores personalizados)  
    - 404.html (error 404 personalizado)  
  - **views.py** (todas las vistas de la aplicación)  
  - **urls.py** (rutas específicas de la aplicación)  
  - **util.py** (funciones de lectura y escritura de archivos Markdown)  

- **manage.py**  
  - Archivo para administrar comandos de Django (migraciones, servidor de desarrollo, etc.).

## Instalación

1. Clonar este repositorio.  
2. Crear y activar un entorno virtual (opcional pero recomendado).  
3. Instalar las dependencias:

```
pip install django markdown2
python manage.py migrate
```