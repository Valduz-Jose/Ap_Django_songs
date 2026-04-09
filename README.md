# 🎵 Music Management System - Django CRUD

[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0-green.svg)](https://www.djangoproject.com/)
[![Render](https://img.shields.io/badge/Deploy-Render-black.svg)](https://ap-django-songs.onrender.com/)

Este es un sistema de gestión de canciones desarrollado con **Django**. Permite realizar las operaciones básicas de un CRUD (Crear, Leer, Actualizar y Eliminar) sobre una base de datos relacional, implementando una arquitectura de capas mediante el uso de **Servicios** para separar la lógica de negocio de las vistas.

🚀 **Demo en vivo:** [https://ap-django-songs.onrender.com/](https://ap-django-songs.onrender.com/)

---

## ✨ Características

- **Gestión Completa de Canciones:** Registro de título, artista y popularidad.
- **Interfaz Responsiva:** Diseño limpio utilizando plantillas de Django y CSS.
- **Arquitectura de Servicios:** Implementación de `SongService` para un código más limpio y mantenible.
- **Seguridad:** Uso de variables de entorno para proteger datos sensibles.
- **Producción:** Configurado para desplegarse en Render con PostgreSQL y WhiteNoise para archivos estáticos.

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python 3.14 + Django 6.0
- **Base de Datos:** MySQL (Desarrollo) / PostgreSQL (Producción)
- **Servidor Web:** Gunicorn
- **Estáticos:** WhiteNoise
- **Gestión de Entorno:** Django-environ

---

## ⚙️ Instalación Local

Si deseas ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Valduz-Jose/Ap_Django_songs.git](https://github.com/Valduz-Jose/Ap_Django_songs.git)
   cd Ap_Django_songs
   ```

2. **Crear y activar entorno virtual:**

```Bash
python -m venv .venv
# En Windows:
.venv\Scripts\activate
```

3. **Instalar dependencias:**

```Bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno:**
Crea un archivo .env en la raíz con los siguientes datos:

```Fragmento de código
DEBUG=True
SECRET_KEY=tu_clave_secreta
DB_NAME=tu_bd
DB_USER=tu_usuario
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=3306
```

5. **Ejecutar migraciones y servidor:**

```Bash
python manage.py migrate
python manage.py runserver
```

## 📂 Estructura del Proyecto
- **canciones/:** Aplicación principal.
- **canciones/services.py:** Capa de lógica de negocio (Servicios).
- **django_songs/:** Configuración global del proyecto.
- **templates/:** Archivos HTML.
- **staticfiles/:** Archivos estáticos preparados para producción.

👤 Autor
Jose Alejandro Valduz Contreras

GitHub: @Valduz-Jose

Proyecto: Music Management System

<img width="1641" height="709" alt="Captura de pantalla 2026-04-09 160045" src="https://github.com/user-attachments/assets/c4481b26-4209-43a9-9eeb-4c1946312cbb" />
<img width="1634" height="700" alt="Captura de pantalla 2026-04-09 160033" src="https://github.com/user-attachments/assets/f29ed931-1583-4717-be73-6539d20d3e0a" />
<img width="1661" height="671" alt="Captura de pantalla 2026-04-09 145212" src="https://github.com/user-attachments/assets/499f82f6-51a1-49a1-a21f-2453e4376a87" />
<img width="1652" height="612" alt="Captura de pantalla 2026-04-09 160053" src="https://github.com/user-attachments/assets/457b2f22-6800-435e-9d66-90af7b87696e" />
