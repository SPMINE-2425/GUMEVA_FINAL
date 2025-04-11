# GUMEVA_FINAL
# Juan Felipe Ramirez 
# Sergio Medina
# Juan Pablo Gutierrez 

# GUMEVA_FINAL

GUMEVA_FINAL es una aplicación desarrollada en Python que integra una API conectada a una base de datos y un frontend construido con Streamlit. Utiliza `Poetry` para el manejo de dependencias y entorno virtual.

---

## 📦 Requisitos previos

- Python 3.11 o superior
- Git (opcional)
- Conexión a la base de datos configurada
- `curl` o `Invoke-WebRequest` (para instalar Poetry)

---

## 🔧 1. Instalar Poetry

### En MacOS/Linux:

```bash
curl -sSL https://install.python-poetry.org | python3 -
En Windows (PowerShell):
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
Luego, asegúrate de cerrar y volver a abrir tu terminal o agregar Poetry al PATH.

Verifica que se haya instalado correctamente:

poetry --version
📁 2. Clonar el repositorio e instalar dependencias

git clone https://github.com/tu_usuario/GUMEVA_FINAL.git
cd GUMEVA_FINAL
poetry install
Este comando instalará automáticamente todas las dependencias del proyecto definidas en el archivo pyproject.toml.
⚙️ 3. Ejecutar la API

La API se encuentra en la carpeta my_api y es responsable de conectarse a la base de datos y correr el modelo.

Desde la raíz del proyecto, ejecuta:

cd my_api
poetry run python main.py
Esto levantará la API localmente, normalmente en http://localhost:8000 o según esté definido en tu archivo main.py.

🌐 4. Ejecutar la aplicación Streamlit

La interfaz de usuario está en la carpeta app, en el archivo app2.py. Para correrla:

Desde la raíz del proyecto:

cd app
poetry run streamlit run app2.py
Esto abrirá la aplicación en tu navegador por defecto, en la dirección: http://localhost:8501

💡 Tips útiles

Puedes activar el entorno virtual directamente con:
poetry shell
Y luego ejecutar comandos sin anteponer poetry run.

Para agregar nuevas dependencias:
poetry add nombre_paquete
Si estás trabajando con variables de entorno sensibles, puedes crear un archivo .env en la raíz del proyecto y cargarlas desde tu código usando python-dotenv o similar.
📂 Estructura del Proyecto

GUMEVA_FINAL/
│
├── app/                  # Aplicación Streamlit (frontend)
│   └── app2.py
│
├── my_api/               # API que conecta con la base de datos y ejecuta el modelo
│   └── main.py
│
├── pyproject.toml        # Archivo de configuración de Poetry
└── README.md             # Instrucciones del proyecto

