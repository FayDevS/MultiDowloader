from yt_dlp import YoutubeDL
from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import threading
import browser_cookie3
import subprocess  # Agregado este import
import sys

class MultiDownloaderGUI:
    def __init__(self, master):
        self.master = master
        master.title("Multi Downloader Pro")
        
        # Configurar ventana principal
        master.geometry("900x750")
        master.configure(bg='#1a1a1a')
        master.resizable(False, False)  # Prevenir redimensionamiento
        
        # Variables para menús desplegables
        self.video_resolution = StringVar(value="none")
        self.video_format = StringVar(value="none")
        self.audio_format = StringVar(value="none")
        self.output_path = StringVar(value=os.path.expanduser("~/Downloads"))

        try:
            # Cargar logo
            logo_path = os.path.join(os.path.dirname(__file__), "assets/youtubemp3.png")
            logo_image = Image.open(logo_path)
            logo_image = logo_image.resize((150, 150), Image.Resampling.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            
            logo_label = Label(master, image=self.logo_photo, bg='#1a1a1a')
            logo_label.pack(pady=10)
        except Exception as e:
            print(f"Error al cargar el logo: {e}")

        # Marco principal
        main_frame = Frame(master, bg='#2d2d2d')
        main_frame.pack(padx=20, pady=10, fill=BOTH, expand=True)

        # URL Entry
        Label(main_frame, text="URL del Video:", bg='#2d2d2d', fg='white', 
              font=('Segoe UI', 12)).pack(pady=5)
        self.url_entry = Entry(main_frame, width=50, font=('Segoe UI', 10))
        self.url_entry.pack(pady=5)

        # Directorio de salida
        dir_frame = Frame(main_frame, bg='#2d2d2d')
        dir_frame.pack(pady=10)
        Label(dir_frame, text="Carpeta de Destino:", bg='#2d2d2d', fg='white', 
              font=('Segoe UI', 10)).pack(side=LEFT)
        Entry(dir_frame, textvariable=self.output_path, width=40).pack(side=LEFT, padx=5)
        Button(dir_frame, text="Examinar", command=self.browse_directory).pack(side=LEFT)

        # Menús desplegables
        options_frame = Frame(main_frame, bg='#2d2d2d')
        options_frame.pack(pady=10)

        # Resolución
        resolution_frame = Frame(options_frame, bg='#2d2d2d')
        resolution_frame.pack(side=LEFT, padx=10)
        Label(resolution_frame, text="Resolución", bg='#2d2d2d', fg='white').pack()
        resolutions = ["none", "mejor", "2160p", "1440p", "1080p", "720p", "480p", "360p"]
        OptionMenu(resolution_frame, self.video_resolution, *resolutions).pack()

        # Formato de video
        video_format_frame = Frame(options_frame, bg='#2d2d2d')
        video_format_frame.pack(side=LEFT, padx=10)
        Label(video_format_frame, text="Formato Video", bg='#2d2d2d', fg='white').pack()
        video_formats = ["none", "mp4", "webm", "mkv"]
        OptionMenu(video_format_frame, self.video_format, *video_formats).pack()

        # Formato de audio
        audio_format_frame = Frame(options_frame, bg='#2d2d2d')
        audio_format_frame.pack(side=LEFT, padx=10)
        Label(audio_format_frame, text="Formato Audio", bg='#2d2d2d', fg='white').pack()
        audio_formats = ["none", "mp3", "wav", "m4a"]
        OptionMenu(audio_format_frame, self.audio_format, *audio_formats).pack()

        # Botones
        buttons_frame = Frame(main_frame, bg='#2d2d2d')
        buttons_frame.pack(pady=20)

        self.download_button = Button(buttons_frame, text="Descargar", command=self.start_download)
        self.download_button.pack(side=LEFT, padx=5)
        Button(buttons_frame, text="Solo Audio", command=self.download_audio_only).pack(side=LEFT, padx=5)
        Button(buttons_frame, text="Solo Video", command=self.download_video_only).pack(side=LEFT, padx=5)

        # Barra de progreso
        self.progress_bar = ttk.Progressbar(main_frame, length=400, mode='determinate')
        self.progress_bar.pack(pady=10)

        # Etiqueta de estado
        self.status_label = Label(main_frame, text="Listo para descargar", bg='#2d2d2d', fg='white')
        self.status_label.pack()

        # Crear menú
        self.create_menu()

    def browse_directory(self):
        """Abre el diálogo para seleccionar carpeta de destino"""
        directory = filedialog.askdirectory()
        if directory:
            self.output_path.set(directory)

    def progress_hook(self, d):
        """Actualiza la barra de progreso durante la descarga"""
        if d['status'] == 'downloading':
            try:
                percent = d['_percent_str']
                percent = float(percent.replace('%', ''))
                self.progress_bar["value"] = percent
                self.status_label.config(text=f"Descargando: {percent:.1f}%")
            except:
                pass
        elif d['status'] == 'finished':
            self.status_label.config(text="Descarga completada. Procesando...")

    def start_download(self):
        """Inicia el proceso de descarga"""
        input_file = self.url_entry.get()
        output_dir = self.output_path.get()
        selected_resolution = self.video_resolution.get()
        selected_video_format = self.video_format.get()
        selected_audio_format = self.audio_format.get()

        if not input_file:
            MessageBox.showerror("Error", "Por favor ingresa una URL")
            return

        # Desactivar botón durante la descarga
        self.download_button.config(state='disabled')
        
        # Reiniciar barra de progreso
        self.progress_bar["value"] = 0
        self.status_label.config(text="Iniciando descarga...")
        
        # Iniciar descarga en un hilo separado
        thread = threading.Thread(
            target=self.download_video,
            args=(
                input_file,
                output_dir,
                selected_resolution,
                selected_video_format,
                selected_audio_format,
                True,  # use_browser_cookies
                False,  # audio_only
                False   # video_only
            )
        )
        thread.daemon = True
        thread.start()

    def download_audio_only(self):
        """Descarga solo el audio"""
        self.download_button.config(state='disabled')
        url = self.url_entry.get()
        if not url:
            MessageBox.showerror("Error", "Por favor ingresa una URL")
            return
        
        thread = threading.Thread(
            target=self.download_video,
            args=(
                url,
                self.output_path.get(),
                "none",
                "none",
                self.audio_format.get(),
                True,  # use_browser_cookies
                True,  # audio_only
                False  # video_only
            )
        )
        thread.daemon = True
        thread.start()

    def download_video_only(self):
        """Descarga solo el video"""
        self.download_button.config(state='disabled')
        url = self.url_entry.get()
        if not url:
            MessageBox.showerror("Error", "Por favor ingresa una URL")
            return
        
        thread = threading.Thread(
            target=self.download_video,
            args=(
                url,
                self.output_path.get(),
                self.video_resolution.get(),
                self.video_format.get(),
                "none",
                True,  # use_browser_cookies
                False, # audio_only
                True  # video_only
            )
        )
        thread.daemon = True
        thread.start()

    def get_ffmpeg_path(self):
        """Busca la ruta de ffmpeg en el sistema"""
        try:
            # Intenta encontrar ffmpeg en PATH
            result = subprocess.run(['where', 'ffmpeg'], 
                                  capture_output=True, 
                                  text=True, 
                                  check=True)
            return result.stdout.strip().split('\n')[0]
        except:
            # Rutas comunes donde podría estar ffmpeg
            common_paths = [
                r"C:\ffmpeg\bin\ffmpeg.exe",
                r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
                r"C:\Program Files (x86)\ffmpeg\bin\ffmpeg.exe",
                r"C:\Users\{username}\AppData\Local\Programs\ffmpeg\bin\ffmpeg.exe",
                r"c:\Users\{username}\Documents\ffmpeg\ffmpeg\bin\ffmpeg.exe",
                os.path.join(os.getenv('LOCALAPPDATA'), 'Programs', 'ffmpeg', 'bin', 'ffmpeg.exe')
            ]
            
            for path in common_paths:
                if os.path.exists(path):
                    return path
                    
            raise FileNotFoundError("ffmpeg no encontrado. Por favor, instálalo y asegúrate de que esté en el PATH del sistema.")

    def download_video(self, url, output_path, video_resolution, video_format, audio_format, use_browser_cookies, audio_only, video_only):
        
        try:
            # Sanitize output path
            output_path = os.path.abspath(output_path)
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            # Obtener ruta de ffmpeg
            ffmpeg_path = self.get_ffmpeg_path()
            
            # Configuración base
            ydl_opts = {
                'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
                'no_warnings': True,
                'quiet': True,
                'progress_hooks': [self.progress_hook],
                'format': 'best',
                'noplaylist': True,
                'prefer_ffmpeg': True,
                'ffmpeg_location': ffmpeg_path
            }

            with YoutubeDL({'quiet': True}) as ydl:
                # Get video info first
                info = ydl.extract_info(url, download=False)
                video_title = info['title']
                safe_title = "".join([c for c in video_title if c.isalnum() or c in (' ', '-', '_')]).rstrip()

                # Configure format options
                if audio_only:
                    if audio_format in ['mp3', 'wav', 'm4a']:
                        ydl_opts.update({
                            'format': 'bestaudio/best',
                            'postprocessors': [{
                                'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'mp3' if audio_format == 'wav' else audio_format,
                                'preferredquality': '192',
                            }],
                            'keepvideo': False,
                        })
                elif video_only:
                    if video_format != 'none':
                        ydl_opts['format'] = f'bestvideo[ext={video_format}]/bestvideo'
                        ydl_opts['postprocessors'] = []
                else:
                    if video_resolution != "none" and video_format != "none":
                        if video_resolution == "mejor":
                            ydl_opts['format'] = f'bestvideo[ext={video_format}]+bestaudio/best'
                        else:
                            height = video_resolution[:-1]
                            ydl_opts['format'] = f'bestvideo[height<={height}][ext={video_format}]+bestaudio/best'
                    else:
                        ydl_opts['format'] = 'bestvideo+bestaudio/best'

                # Download the file
                with YoutubeDL(ydl_opts) as ydl_download:
                    ydl_download.download([url])

                # Modificar la parte de conversión WAV para usar la ruta correcta de ffmpeg
                if audio_only and audio_format == 'wav':
                    mp3_file = os.path.join(output_path, f"{safe_title}.mp3")
                    wav_file = os.path.join(output_path, f"{safe_title}.wav")
                    
                    if os.path.exists(mp3_file):
                        try:
                            subprocess.run([
                                ffmpeg_path,
                                '-i', mp3_file,
                                '-acodec', 'pcm_s16le',
                                '-ar', '44100',
                                wav_file
                            ], check=True, capture_output=True, text=True)
                            
                            if os.path.exists(wav_file):
                                os.remove(mp3_file)
                                self.status_label.config(text=f"Archivo guardado en: {wav_file}")
                            else:
                                raise Exception("Error en la conversión a WAV")
                        except subprocess.CalledProcessError as e:
                            raise Exception(f"Error en la conversión: {e.stderr}")

                self.status_label.config(text=f"Descarga completada en: {output_path}")
                self.progress_bar["value"] = 100

        except FileNotFoundError as fnf:
            MessageBox.showerror("Error", str(fnf))
            self.status_label.config(text="Error: ffmpeg no encontrado")
        except Exception as error:
            error_msg = str(error)
            self.status_label.config(text=f"Error: {error_msg}")
            MessageBox.showerror("Error", error_msg)
        finally:
            self.master.after(0, lambda: self.download_button.config(state='normal'))

    def create_menu(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        help_menu.add_command(label="Acerca de", command=self.popup_author)
        help_menu.add_command(label="Donar", command=self.popup_donate)

    def popup_author(self):
        MessageBox.showinfo("Acerca de", "Multi Downloader Pro\nCreado por FayDev\nVersión 2.0")

    def popup_donate(self):
        """Muestra el diálogo de donación con el enlace de PayPal"""
        donate_text = """¡Gracias por usar YouTube Multi Downloader Pro!

      Si te gusta esta aplicación, considera hacer una donación:

      PayPal: https://www.paypal.me/faycraxE

      Tu apoyo ayuda a mantener y mejorar el proyecto."""
        
        MessageBox.showinfo("Donar", donate_text)

    
 


if __name__ == '__main__':
    root = Tk()
    app = MultiDownloaderGUI(root)
    root.mainloop()  # Esta línea es crucial para mantener la ventana abierta