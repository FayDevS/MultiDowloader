# MultiDowloader
MultiDownloader is a fast, multi-platform tool for downloading videos and audio from various websites. Supports formats like MP4, MP3, and WEBM. Easy to use, lightweight, and available on Windows,  Linux. Open source and free to use. Simple interface for quick downloads.

Spanish
________________________________________
Dependencias:
1.	yt-dlp
o	Descripción: Un fork de youtube-dl que permite descargar videos y audios desde diversas plataformas. Se utiliza en este script para extraer la información del video y descargar el contenido multimedia.
o	Instalación: pip install yt-dlp
2.	tkinter
o	Descripción: Una biblioteca estándar de Python para crear interfaces gráficas de usuario (GUI). En este script, se usa para construir la interfaz donde los usuarios ingresan URLs y seleccionan opciones de descarga como formato y resolución.
o	Instalación: Viene preinstalada con Python, no es necesario instalarla.
3.	Pillow (PIL)
o	Descripción: Una biblioteca para trabajar con imágenes en Python. En este script, se utiliza para cargar y mostrar el logo de la aplicación en la interfaz de usuario.
o	Instalación: pip install Pillow
4.	os
o	Descripción: Un módulo estándar de Python que permite interactuar con el sistema operativo, como manipular rutas de archivos y directorios. En este script, se usa para gestionar la ruta de destino para las descargas.
o	Instalación: Viene preinstalado con Python.
5.	threading
o	Descripción: Un módulo estándar de Python utilizado para crear y gestionar hilos (threads). En este script, se usa para permitir que la descarga se realice de forma asíncrona, sin bloquear la interfaz gráfica.
o	Instalación: Viene preinstalado con Python.
6.	browser-cookie3
o	Descripción: Esta biblioteca permite acceder a las cookies almacenadas en navegadores como Chrome, Firefox, etc., facilitando la autenticación en servicios que requieren sesión. En este script, se usa para habilitar las descargas que requieren autenticación de navegador.
o	Instalación: pip install browser-cookie3
7.	subprocess
o	Descripción: Un módulo estándar de Python que permite ejecutar comandos del sistema operativo. En este script, se usa para llamar a ffmpeg y convertir archivos de audio a otros formatos como WAV.
o	Instalación: Viene preinstalado con Python.
8.	sys
o	Descripción: Un módulo estándar de Python que proporciona acceso a algunas variables y funciones que interactúan con el intérprete de Python. En este script, se usa para manejar argumentos del sistema y rutas de ejecución.
o	Instalación: Viene preinstalado con Python.
________________________________________
English:
________________________________________
Dependencies:
1.	yt-dlp
o	Description: A fork of youtube-dl that allows downloading videos and audios from various platforms. It is used in this script to extract video information and download the multimedia content.
o	Installation: pip install yt-dlp
2.	tkinter
o	Description: A standard Python library used for creating graphical user interfaces (GUIs). In this script, it is used to build the interface where users input URLs and select download options such as format and resolution.
o	Installation: Comes pre-installed with Python, no need to install separately.
3.	Pillow (PIL)
o	Description: A library for handling images in Python. In this script, it is used to load and display the app's logo on the user interface.
o	Installation: pip install Pillow
4.	os
o	Description: A standard Python module that allows interaction with the operating system, such as handling file paths and directories. In this script, it is used to manage the output path for downloaded files.
o	Installation: Comes pre-installed with Python.
5.	threading
o	Description: A standard Python module used for creating and managing threads. In this script, it is used to enable asynchronous downloading without blocking the graphical user interface.
o	Installation: Comes pre-installed with Python.
6.	browser-cookie3
o	Description: A library that allows access to cookies stored in web browsers like Chrome, Firefox, etc., making it easier to authenticate on services that require a browser session. In this script, it is used to enable downloads that require browser-based authentication.
o	Installation: pip install browser-cookie3
7.	subprocess
o	Description: A standard Python module that allows executing system commands. In this script, it is used to call ffmpeg for converting audio files to other formats like WAV.
o	Installation: Comes pre-installed with Python.
8.	sys
o	Description: A standard Python module that provides access to some variables and functions that interact with the Python interpreter. In this script, it is used to handle system arguments and execution paths.
o	Installation: Comes pre-installed with Python.

1. Installing FFmpeg on Linux
Ubuntu/Debian:
Update your system:

Open a terminal and run:

bash
Copiar
Editar
sudo apt update
sudo apt upgrade
Install FFmpeg:

Run the following command to install FFmpeg:

bash
Copiar
Editar
sudo apt install ffmpeg
Verify the installation:

To check if FFmpeg is installed correctly, run:

bash
Copiar
Editar
ffmpeg -version
You should see something like this:

pgsql
Copiar
Editar
ffmpeg version 4.x.x-xxxx
built with gcc 9.x.x (Ubuntu 9.x.x-x)
configuration: --enable-gpl --enable-libx264 --enable-libx265 ...
CentOS/RHEL/Fedora:
Install the EPEL repository:

bash
Copiar
Editar
sudo yum install epel-release
Install FFmpeg:

For CentOS 7 or earlier:

bash
Copiar
Editar
sudo yum install ffmpeg ffmpeg-devel
For Fedora (newer versions):

bash
Copiar
Editar
sudo dnf install ffmpeg
Verify the installation:

bash
Copiar
Editar
ffmpeg -version
2. Installing FFmpeg on Windows
Method 1: Using the ZIP file (Recommended)
Download FFmpeg:

Go to the official FFmpeg website and select Windows.

You can also download FFmpeg directly from gyan.dev, where you can find the latest builds.

Extract the ZIP file:

After downloading the ZIP file, extract it to a folder on your PC, for example: C:\ffmpeg.

Add FFmpeg to your PATH environment variable:

To run FFmpeg from any location in the terminal (CMD), you need to add it to your PATH environment variable.

Right-click on This PC or My Computer, and select Properties.

Then, click Advanced system settings and then Environment Variables.

In the System Variables section, find the Path variable and click Edit.

Add the path to the bin directory inside the FFmpeg folder (e.g., C:\ffmpeg\bin) to the list. Make sure to separate multiple entries with a semicolon ;.

Click OK.

Verify the installation:

Open Command Prompt (CMD) and type:

bash
Copiar
Editar
ffmpeg -version
If everything is set up correctly, you should see the FFmpeg version information.

3. Installing Python dependencies
Now, to install the dependencies for your Python project, as mentioned before, create a file called requirements.txt with the following lines:

r
Copiar
Editar
yt-dlp
Pillow
browser-cookie3
Install dependencies:

If you already have Python installed, open a terminal (or CMD on Windows) and navigate to the folder where requirements.txt is located. Then run:

bash
Copiar
Editar
pip install -r requirements.txt
This will install all the dependencies listed in the file.

Verify the installations:

To ensure the dependencies have been installed correctly, you can run:

bash
Copiar
Editar
pip list
This will show a list of all installed libraries. You should see yt-dlp, Pillow, and browser-cookie3 among them.

4. Additional Recommendations
If you run into issues while installing dependencies, it's recommended to use a virtual environment to avoid conflicts with system-wide libraries. Here's how you can create a virtual environment in Python:

Create a virtual environment:

bash
Copiar
Editar
python -m venv myenv
Activate the virtual environment:

On Windows:

bash
Copiar
Editar
myenv\Scripts\activate
On Linux/macOS:

bash
Copiar
Editar
source myenv/bin/activate
Now, install the dependencies in the virtual environment:

bash
Copiar
Editar
pip install -r requirements.txt
Make sure you have Python 3.x installed, as some libraries might not be compatible with older Python versions.

# MultiDownloader Pro

MultiDownloader Pro is a multi-platform tool for downloading videos and audio from various online platforms. It allows users to download media files in different formats and resolutions.

## Features:
- Download videos and audio from various platforms.
- Select video resolution and audio format.
- Simple graphical user interface built with Tkinter.
- Option to download video or audio separately.

---

## Installation Guide

### Prerequisites:
- Python 3.x
- FFmpeg (for media conversion and processing)

  

#### **On Linux (Ubuntu/Debian)**

1. Update your system:

   ```bash
   sudo apt update
   sudo apt upgrade

## Dependencies
2 install dependencies:

   ```bash
   pip install requirements.txt





