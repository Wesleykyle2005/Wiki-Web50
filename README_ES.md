# 📚 Wiki - CS50 Web Programming

Una enciclopedia en línea inspirada en Wikipedia, desarrollada con Django. Las entradas se almacenan en formato Markdown y se convierten dinámicamente a HTML para su visualización.

---

## 📝 Descripción

Este proyecto implementa una enciclopedia web interactiva con las siguientes funcionalidades:
- 👁️ Visualización de entradas en `/wiki/TITULO`.
- 🗂️ Lista de entradas con enlaces en la página de inicio.
- 🔍 Búsqueda de entradas por coincidencia exacta o parcial.
- ✍️ Creación y edición de entradas en formato Markdown.
- 🎲 Acceso a una entrada aleatoria.
- 🔄 Conversión automática de Markdown a HTML usando la librería `markdown2`.
- ⚠️ Páginas de error personalizadas para entradas no encontradas o duplicadas.

## 📷 Capturas de Pantalla

### Página principal (Index)
![Index page](encyclopedia/static/encyclopedia/images/index.png)

### Visualización de una entrada de Python
![Python entry](encyclopedia/static/encyclopedia/images/entry_python.png)

### Formulario para crear una nueva entrada
![New entry form](encyclopedia/static/encyclopedia/images/new_entry.png)

### Formulario para editar una entrada
![Edit entry form](encyclopedia/static/encyclopedia/images/edit_entry.png)



## 🏛️ Antecedentes

Inspirado en [Wikipedia](https://www.wikipedia.org/), este proyecto utiliza [Markdown](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) en lugar de Wikitext para almacenar entradas. Cada entrada es un archivo `.md` en la carpeta `entries/`, lo que simplifica la creación y edición de contenido. El contenido se convierte a HTML para su renderización en el navegador.

---

## 🗂️ Estructura del Proyecto

- **`wiki/`**: Configuración del proyecto Django (`settings.py`, `urls.py`, etc.).
- **`encyclopedia/`**: Aplicación principal.
  - `views.py`: Lógica de las vistas y manejo de formularios.
  - `urls.py`: Rutas de la aplicación.
  - `util.py`: Funciones para gestionar entradas (listar, guardar, recuperar).
  - `templates/encyclopedia/`:
    - `layout.html`: Plantilla base con barra lateral y navegación.
    - `index.html`: Lista de entradas.
    - `entry.html`: Visualización de una entrada.
    - `new_entry.html`: Formulario para crear entradas.
    - `edit_entry.html`: Formulario para editar entradas.
    - `error.html`, `404.html`: Páginas de error personalizadas.
  - `static/encyclopedia/`: Archivos CSS y otros recursos estáticos.
- **`entries/`**: Archivos Markdown de las entradas.
- **`manage.py`**: Script de administración de Django.

---

## ✅ Requisitos y Funcionalidades

- **Página de entrada**: `/wiki/TITULO` muestra el contenido Markdown convertido a HTML o un error 404 si no existe.
- **Página de índice**: Muestra todas las entradas como enlaces a sus respectivas páginas.
- **Búsqueda**: 
  - Coincidencia exacta redirige a la entrada.
  - Coincidencia parcial muestra una lista de resultados con enlaces.
- **Nueva página**: Formulario para crear entradas, con validación para evitar duplicados.
- **Editar página**: Formulario para modificar el contenido Markdown de una entrada.
- **Página aleatoria**: Redirige a una entrada seleccionada al azar.
- **Conversión Markdown a HTML**: Usa `markdown2` para convertir el contenido. Opcionalmente, implementa conversión manual con expresiones regulares.

---

## ⚙️ Instalación

1. 🌀 Clona el repositorio:
   ```bash
   git clone https://github.com/Wesleykyle2005/Wiki-Web50
   cd Wiki-Web50
   ```
2. 🛡️ (Opcional) Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. 📦 Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. 🗄️ Aplica las migraciones de Django:
   ```bash
   python manage.py migrate
   ```
5. 🚀 Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

---

## 💡 Ejemplo de Uso

- 🌐 Accede a `http://127.0.0.1:8000/` en tu navegador.
- 🔍 Busca entradas por nombre o subcadena desde la barra lateral.
- 📝 Crea nuevas entradas con el enlace "Create New Page".
- ✏️ Edita entradas existentes desde su página.
- 🎲 Accede a una entrada aleatoria con "Random Page".
- 📁 Las entradas se almacenan como archivos `.md` en la carpeta `entries/`.

---

## 🏅 Buenas Prácticas y Consejos

- 🛡️ Usa el filtro `|safe` en las plantillas para renderizar HTML generado desde Markdown: `{{ variable|safe }}`.
- 🗂️ Mantén los nombres de los archivos Markdown iguales al título de la entrada para evitar confusiones.
- 📖 Revisa la [guía de Markdown de GitHub](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) para entender la sintaxis soportada.
- 🖋️ Ahora el proyecto utiliza la fuente Linux Libertine a través de [cdnfonts](https://www.cdnfonts.com/linux-libertine.font) para asemejarse a Wikipedia.
- 📱 El diseño es completamente responsivo gracias a media queries, adaptándose a computadoras, tablets y móviles.
- 🟢 El código ha sido validado con pylint (10.00/10) y formateado con black, garantizando calidad y estilo profesional.

