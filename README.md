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
