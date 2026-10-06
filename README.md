# Tienda - Sistema CRUD de Productos

Sistema web sencillo para gestionar los productos de una tienda, desarrollado con Flask y una base de datos MySQL alojada en la nube (Railway). Permite registrar, consultar, modificar y retirar productos, cada uno asociado a una categoria.

Proyecto de practica de Bases de Datos y Programacion.

## Tecnologias

- Python 3.11.9
- Flask
- MySQL (alojado en Railway)
- mysql-connector-python
- HTML, CSS y JavaScript (sin frameworks)

## Funcionalidades

El sistema esta organizado en cuatro pestañas:

| Pestaña | Operacion | Descripcion |
|---|---|---|
| REGISTRAR | Create | Agrega un producto nuevo y le asigna una categoria desde una lista desplegable. |
| CATALOGO | Read | Muestra todos los productos con su categoria y un filtro de busqueda en vivo. |
| MODIFICAR | Update | Busca un producto por ID y permite editar sus datos. |
| RETIRAR | Delete | Busca un producto por ID, muestra su informacion y lo elimina previa confirmacion. |

## Estructura del proyecto

```
crud_tienda/
├── .venv/
├── app.py
├── db.py
├── requirements.txt
├── static/
│   ├── css/
│   │   ├── base.css
│   │   ├── create.css
│   │   ├── read.css
│   │   ├── update.css
│   │   └── delete.css
│   └── js/
│       ├── base.js
│       ├── read.js
│       └── delete.js
└── templates/
    ├── base.html
    ├── create.html
    ├── read.html
    ├── update.html
    └── delete.html
```

- `app.py`: rutas de Flask y logica del CRUD.
- `db.py`: funcion de conexion a la base de datos.
- `templates/`: plantillas HTML (Jinja2). `base.html` contiene la barra de pestañas y las demas heredan de ella.
- `static/`: hojas de estilo y scripts, separados por pestaña.

## Modelo de datos

Relacion uno a muchos: una categoria puede tener varios productos.

```
categorias (1) ────< (N) productos
```

```sql
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    id_categoria INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

INSERT INTO categorias (nombre) VALUES
('Bebidas'),
('Snacks'),
('Lacteos'),
('Limpieza'),
('Panaderia');
```

## Requisitos

- Python 3.11 o superior
- Una base de datos MySQL accesible desde internet (en este proyecto, Railway)

## Instalacion

1. Clonar el repositorio y entrar a la carpeta del proyecto.

2. Crear y activar el entorno virtual (PowerShell):

```
python -m venv .venv
.venv\Scripts\activate
```

En Linux o macOS: `source .venv/bin/activate`

3. Instalar las dependencias:

```
python -m pip install --upgrade pip
pip install Flask mysql-connector-python
pip freeze > requirements.txt
```

Si el archivo `requirements.txt` ya existe, basta con:

```
pip install -r requirements.txt
```

## Configuracion de la base de datos

1. Ejecutar en MySQL el script SQL de la seccion "Modelo de datos".

2. Editar `db.py` con las credenciales de la base de datos:

```python
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="HOST_PUBLICO",
        port=PUERTO_PUBLICO,
        user="USUARIO",
        password="PASSWORD",
        database="BASE_DE_DATOS"
    )
```

Datos de conexion en Railway:

- Los valores de host y puerto publicos se obtienen de la variable `MYSQL_PUBLIC_URL`, con el formato `mysql://USUARIO:PASSWORD@HOST:PUERTO/BASE`.
- No se debe usar `mysql.railway.internal` ni el puerto 3306, porque solo funcionan dentro de la red interna de Railway.

## Ejecucion

Con el entorno virtual activado:

```
python app.py
```

Abrir en el navegador: `http://127.0.0.1:5000`

## Rutas

| Ruta | Metodos | Descripcion |
|---|---|---|
| `/` | GET | Redirige al catalogo. |
| `/create` | GET, POST | Formulario de registro de productos. |
| `/read` | GET | Listado de productos con su categoria. |
| `/update?id=N` | GET, POST | Busca un producto por ID y guarda los cambios. |
| `/delete?id=N` | GET, POST | Muestra un producto por ID y lo elimina. |

## Notas de seguridad

- Las consultas SQL usan parametros (`%s`), lo que evita inyeccion SQL.
- No subir al repositorio las credenciales reales de `db.py`. Si se llegaron a publicar, regenerar la contraseña desde Railway.
- Agregar `.venv/` a un archivo `.gitignore`.

## Autor

sxmuelvm