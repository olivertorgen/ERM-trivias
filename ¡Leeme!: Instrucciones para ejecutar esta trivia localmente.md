Pasos para Clonar y Ejecutar la Trivia 🤖
Hola! Soy Oliver Torgen, estudiante de la Escuela de Innovación Misiones, un gusto. Me alegra que quieras ejecutar esta trivia en tu propia máquina también. A continuación te dejo las instrucciones detalladas paso a paso para hacerlo!
Estos pasos son universales para cualquier usuario que tenga Python 3 instalado.
1. Requisitos Previos, El usuario debe tener instalado en su sistema:
Python 3: (Se recomienda la versión 3.8 o superior).
Git: Para poder clonar el repositorio de GitHub.
2. Clonar el Repositorio de GitHub
El usuario debe abrir su terminal o símbolo del sistema y ejecutar el siguiente comando, reemplazando  https://github.com/olivertorgen/ERM-trivias.git con la URL real de tu proyecto en GitHub:
Bash
# Navega al directorio donde quieres guardar el proyecto
cd /ruta/a/mis/proyectos
# Clona el repositorio
git clone https://github.com/olivertorgen/ERM-trivias.git
# Accede a la carpeta del proyecto clonado
cd nombre-del-repositorio 
3. Crear un Entorno Virtual (Recomendado)
Para evitar conflictos entre las dependencias de diferentes proyectos, es una buena práctica crear un entorno virtual.
Bash
# 1. Crea el entorno virtual (llamado 'venv' por convención)
python -m venv venv

# 2. Activa el entorno virtual:

# En Windows:
.\venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
4. Instalar las Dependencias
La trivia requiere la biblioteca Pillow para manejar las imágenes (.png). Es fundamental que esta biblioteca esté instalada en el entorno activo.
Si proporcionas un archivo requirements.txt en tu repositorio: (Contenido: Pillow)
Bash
pip install -r requirements.txt
Si no proporcionas el archivo:
Bash
pip install Pillow
5. Ejecutar la Aplicación
Una vez que las dependencias están instaladas, el usuario puede ejecutar el script principal. Suponiendo que el archivo que contiene el código de la trivia se llama trivia_erm.py:
Bash
python trivia_erm.py
La aplicación se iniciará en modo pantalla completa y la usted podrá comenzar a jugar la trivia.
📝 Resumen del Archivo requirements.txt
Para facilitar el paso 4, le sugiero crear un archivo llamado requirements.txt en la raíz de tu repositorio con el siguiente contenido:
Pillow
