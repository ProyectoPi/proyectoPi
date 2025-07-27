# Proyecto Fullstack con Django

## Configuración del Entorno de Desarrollo

Sigue estos pasos para levantar el proyecto en tu máquina local.

1.  **Clona el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd proyectoPi
    ```

2.  **Crea y activa un entorno virtual (Recomendado):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplica las migraciones para crear tu base de datos:**
    ```bash
    cd backend
    python manage.py migrate
    ```

5.  **Crea tu propio superusuario:**
    ```bash
    python manage.py createsuperuser
    ```
    *(Sigue las instrucciones en la consola para elegir tu nombre de usuario y contraseña)*

6.  **Inicia el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```

7.  **Accede al panel de administración** en [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) y usa las credenciales que acabas de crear.
