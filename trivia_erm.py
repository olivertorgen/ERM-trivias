import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 
from pygame import mixer # Necesario para la funcionalidad de sonido

# --- 1. DATOS DE LA TRIVIA (COMPLETOS) ---

# Preguntas de la Sección 1: ¿Cuánto Conoces a la ERM?
PREGUNTAS_ERM = [
    {
        "pregunta": "¿Cuál es la característica principal que hace única a la Escuela de Robótica de Misiones (ERM) en Argentina?",
        "opciones": ["Es el único espacio que enseña robótica.", "Es un espacio educativo de gestión estatal no arancelado pionero con equipamiento único en Latinoamérica.", "Está pensada solo para jóvenes y adolescentes.", "Solo se enfoca en programación."],
        "respuesta_correcta": "Es un espacio educativo de gestión estatal no arancelado pionero con equipamiento único en Latinoamérica."
    },
    {
        "pregunta": "¿A partir de qué edad pueden comenzar a asistir a los trayectos de la ERM?",
        "opciones": ["A partir de los 7 años", "A partir de los 5 años", "A partir de los 3 años", "A partir de los 9 años"],
        "respuesta_correcta": "A partir de los 3 años"
    },
    {
        "pregunta": "¿En qué año se fundó la Escuela de Robótica de Misiones (ERM)?",
        "opciones": ["2010", "2015", "2018", "2020"],
        "respuesta_correcta": "2015"
    },
    {
        "pregunta": "¿Cuál es uno de los principales objetivos de la ERM?",
        "opciones": ["Formar profesionales en robótica para empresas privadas.", "Brindar educación tecnológica gratuita y accesible a niños, jóvenes y adultos.", "Vender kits de robótica a estudiantes.", "Organizar competencias internacionales de robótica."],
        "respuesta_correcta": "Brindar educación tecnológica gratuita y accesible a niños, jóvenes y adultos."
    },
    {
        "pregunta": "¿Qué tipo de actividades se realizan en la ERM?",
        "opciones": ["Solo clases teóricas sobre robótica.", "Talleres prácticos, proyectos de robótica y programación.", "Competencias deportivas.", "Cursos de idiomas."],
        "respuesta_correcta": "Talleres prácticos, proyectos de robótica y programación."
    },
    {
        "pregunta": "¿Quiénes pueden asistir a la Escuela de Robótica de Misiones?",
        "opciones": ["Solo estudiantes universitarios.", "Niños, jóvenes y adultos de todas las edades.", "Solo profesionales del área tecnológica.", "Exclusivamente docentes."],
        "respuesta_correcta": "Niños, jóvenes y adultos de todas las edades."
    },
    {
        "pregunta": "¿Cuál es el enfoque pedagógico principal de la ERM?",
        "opciones": ["Aprendizaje memorístico.", "Aprendizaje basado en proyectos y resolución de problemas.", "Enseñanza tradicional con exámenes frecuentes.", "Clases magistrales sin interacción."],
        "respuesta_correcta": "Aprendizaje basado en proyectos y resolución de problemas."
    },

    {
        "pregunta": "¿Quién es la actual Coordinadora General de la Escuela de Robótica de Misiones?",
        "opciones": [" Ing. Solange Schelske", "c.P. Natalia Meira", "Lic. Araceli Vera", " No hay una coordinadora general, solo coordinadores de trayecto"],
        "respuesta_correcta": "Lic. Araceli Vera"
    },
    {
        "pregunta": "El objetivo principal de la ERM es que los estudiantes logren autonomía y sean protagonistas de su aprendizaje. ¿Qué tipo de Ley apoya este enfoque educativo en Misiones?",
        "opciones": ["Ley de Educación Superior", "Ley de Educación Disruptiva", "Ley Federal de Educación", "Ley de Financiamiento Educativo"],
        "respuesta_correcta": "Ley de Educación Disruptiva"
    },
    {
        "pregunta": "¿Qué tipo de profesionales conforman el equipo de trabajo multidisciplinario de la ERM?",
        "opciones": [" Solo Ingenieros y Técnicos", "Solo profesores de nivel inicial y educación especial", "Profesionales de distintas disciplinas como ingenieros, técnicos, profesores, y especialistas en diversas áreas", "Únicamente facilitadores de robótica" ],
        "respuesta_correcta": "Profesionales de distintas disciplinas como ingenieros, técnicos, profesores, y especialistas en diversas áreas"
    },
    {
        "pregunta": "¿Dónde está ubicada la Escuela de Robótica de Misiones (ERM)?",
        "opciones": ["Av. Mitre, 1000.", "Av. Gdor. Roca 480.", "Av. Maipú, 1500", "Av. Roque Perez 490"],
        "respuesta_correcta": "Av. Gdor. Roca 480."
    }
]

# Pregunta que incluye imágenes (Ecopuntos)
PREGUNTA_ECOPUNTOS = "Ubicación de Ecopuntos: Si estás en Posadas, ¿dónde podrías encontrar un Ecopunto para llevar tus residuos reciclables (plástico, papel, vidrio)?"

# Preguntas de la Sección 3: Compromiso Social y Ambiental (Intercaladas)
PREGUNTAS_ETICAS_AMBIENTALES = [
    {
        "pregunta": "♻️ ¿Cuál es el primer paso más efectivo para reducir tu huella de carbono diaria, basado en la regla de las 3R?",
        "opciones": ["Reemplazar todos tus electrodomésticos.", "Implementar la regla de las 3R (Reducir, Reutilizar, Reciclar).", "Usar solo bolsas de tela en el supermercado.", "Cambiar el auto por una moto."],
        "respuesta_correcta": "Implementar la regla de las 3R (Reducir, Reutilizar, Reciclar)."
    },
    {
        "pregunta": "🌱 ¿Cuál de las siguientes acciones contribuye más a la sostenibilidad ambiental?",
        "opciones": ["Plantar árboles y conservar áreas verdes.", "Usar más plástico para embalajes.", "Aumentar el uso de vehículos privados.", "Comprar productos desechables."],
        "respuesta_correcta": "Plantar árboles y conservar áreas verdes."
    },
    {
        "pregunta": PREGUNTA_ECOPUNTOS,
        "opciones": ["Costa Sur: Ubicado en el balneario.", "Itaembé Guazú: En la calle Aguará Guazú y los Cactus.", "Parque La Cascada", "Todas son correctas."],
        "respuesta_correcta": "Todas son correctas."
    },
]

# Funciones de Mapeo
def obtener_preguntas_combinadas():
    """Combina las preguntas de ERM y Éticas/Ambientales para el flujo."""
    preguntas_combinadas = []
    total_erm = len(PREGUNTAS_ERM)
    total_eticas = len(PREGUNTAS_ETICAS_AMBIENTALES)

    for i in range(total_erm):
        preguntas_combinadas.append(PREGUNTAS_ERM[i])
        if i < total_eticas:
            preguntas_combinadas.append(PREGUNTAS_ETICAS_AMBIENTALES[i])
    return preguntas_combinadas

def determinar_trayecto(edad):
    """Devuelve el nombre del trayecto basado en la edad."""
    if 3 <= edad <= 4:
        return "PequeBot"
    elif 5 <= edad <= 6:
        return "TrendKids"
    elif 7 <= edad <= 8:
        return "TecnoKids"
    elif 9 <= edad <= 12:
        return "MakerJuniors"
    elif 13 <= edad <= 15:
        return "TeensMaker"
    elif 16 <= edad <= 18:
        return "TeamInn"
    else: # edad >= 19
        return "HighMaker"

# ----------------------------------------------------------------------
# --- 2. CLASE PRINCIPAL DE LA APLICACIÓN (AJUSTES DE DISTRIBUCIÓN) ---
# ----------------------------------------------------------------------
class TriviaApp:
    # --- CONFIGURACIÓN DE ESTILOS ---
    COLOR_FONDO = "#2E0058"       # Violeta Oscuro (usado para frames/widgets, el fondo principal es la imagen)
    COLOR_TEXTO = "#F0DEFF"       # Violeta claro
    COLOR_RESALTE = "#FFD700"     # Amarillo/Oro
    FUENTE_TITULO = ("Arial", 36, "bold")
    FUENTE_PREGUNTA = ("Arial", 24, "bold")
    FUENTE_OPCION = ("Arial", 20)
    FUENTE_BOTON = ("Arial", 22, "bold")

    # Rutas de assets
    PATH_FONDO = "assets/Fondo (1).png"  
    PATH_LOGO = "assets/Isotipo (1).png" 
    PATH_CORRECT_SOUND = "assets/sonido_correcto.mp3"
    PATH_ERROR_SOUND = "assets/sonido_incorrecto.mp3"
    # --- NUEVA RUTA DE MÚSICA DE FONDO ---
    PATH_MUSIC_BG = "assets/musica_fondo.mp3" 

    # --- NUEVAS RUTAS DE ECOPUNTOS ---
    PATH_ECOPUNTO_LEFT = "assets/ecopunto1.png"
    PATH_ECOPUNTO_RIGHT = "assets/ecopunto2.png"

    # Rutas de los logos de trayecto
    PATH_LOGOS = {
        "PequeBot": "assets/pequebot.jpg",
        "TrendKids": "assets/trendkids.jpg",
        "TecnoKids": "assets/tecnokids.jpg",
        "MakerJuniors": "assets/makerjuniors.jpg",
        "TeensMaker": "assets/tm.jpg",
        "TeamInn": "assets/ti.jpg",
        "HighMaker": "assets/hm.jpg"
    }

    def __init__(self, master):
        self.master = master
        master.title("🤖 TRIVIA ERM - TecnoTravesía")
        master.attributes('-fullscreen', True)
        # El color de fondo de la ventana principal solo se verá si la imagen de fondo falla
        master.config(bg=self.COLOR_FONDO) 

        self.puntuacion_erm = 0
        self.trayecto_asignado = ""
        self.preguntas = obtener_preguntas_combinadas()
        self.indice_pregunta = 0
        self.total_preguntas_erm = len(PREGUNTAS_ERM)
        self.respuesta_seleccionada = tk.StringVar(master)
        
        # Variables para imágenes (persistentes)
        self.bg_image_tk = None
        self.logo_image_tk = None # Logo de bienvenida (Isotipo (1).png)
        self.fondo_label = None # Referencia al Label del fondo persistente
        
        # Variables de animación y logo del trayecto
        self.pulse_animation_id = None # Para el botón de inicio
        self.logo_animation_id = None  # Para el logo del trayecto final
        self.trayecto_logo_label = None # Referencia al Label del logo del trayecto
        self.logo_image_tk_animated = None # Versión animada del logo del trayecto
        self.logo_base_size = (200, 200) # Tamaño base para el logo del trayecto
        self.logo_current_scale = 1.0
        self.logo_path = None # Ruta del logo del trayecto actual
        
        # --- Variables para las imágenes de Ecopuntos ---
        self.ecopunto_img_left = None
        self.ecopunto_img_right = None
        self.ecopunto_label_left = None
        self.ecopunto_label_right = None
        
        # --- CONFIGURACIÓN DE SONIDO (Pygame Mixer) ---
        self.sound_enabled = False
        self.music_enabled = False # Nuevo: Flag para la música de fondo
        self.sound_correct = None
        self.sound_error = None
        try:
            # Re-inicializar por si el init de afuera fue demasiado básico
            mixer.init(frequency=44100)
            self.sound_correct = mixer.Sound(self.PATH_CORRECT_SOUND)
            self.sound_error = mixer.Sound(self.PATH_ERROR_SOUND)
            self.sound_enabled = True
            
            # --- LÓGICA DE MÚSICA DE FONDO ---
            # Cargar y reproducir la música de fondo en loop (-1)
            mixer.music.load(self.PATH_MUSIC_BG)
            mixer.music.set_volume(0.3) # Establecer un volumen bajo (0.0 a 1.0)
            mixer.music.play(-1) # -1 significa loop infinito
            self.music_enabled = True
            print(f"Música de fondo y efectos de sonido habilitados.")
            
        except FileNotFoundError:
            print(f"Advertencia: Archivos de sonido/música MP3 no encontrados en assets/. El audio estará deshabilitado.")
            self.sound_enabled = False
            self.music_enabled = False
        except Exception as e:
            print(f"Advertencia: Pygame o sus dependencias fallaron. El audio estará deshabilitado. Error: {e}")
            self.sound_enabled = False
            self.music_enabled = False
        
        self.current_screen = "welcome"
        self.master.bind('<space>', self.on_space_press)
        
        # Primero configurar el fondo una vez al inicio de la aplicación
        self.configurar_fondo()
        self.mostrar_bienvenida()

    # --- LÓGICA DE TECLAS Y ESTADO ---
    def on_space_press(self, event):
        """Maneja la pulsación de la tecla ESPACIO para avanzar en la trivia o iniciarla."""
        # Evitar que la barra espaciadora interactúe si se está editando la edad
        if self.master.focus_get() is not None and isinstance(self.master.focus_get(), tk.Entry):
            return 
        
        if self.current_screen == "welcome":
            if self.pulse_animation_id:
                self.master.after_cancel(self.pulse_animation_id)
            self.mostrar_pregunta_erm()
        elif self.current_screen == "trivia":
            if 0 <= self.indice_pregunta < len(self.preguntas):
                self.verificar_respuesta(force_skip=True)
            else:
                self.mostrar_diagnostico_edad()
        elif self.current_screen == "result":
            self.reiniciar_trivia()

    # --- UTILIDADES DE VISTA Y SONIDO ---
    def reproducir_sonido(self, tipo):
        """Reproduce un sonido de victoria o error usando pygame.mixer."""
        if not self.sound_enabled:
            return
        try:
            # Opcional: bajar el volumen de la música temporalmente (ducking)
            if self.music_enabled:
                mixer.music.set_volume(0.1) 
                self.master.after(500, lambda: mixer.music.set_volume(0.3)) # Volver al volumen original después de 500ms
                
            if tipo == "victoria" and self.sound_correct:
                self.sound_correct.play()
            elif tipo == "error" and self.sound_error:
                self.sound_error.play()
        except Exception as e:
            print(f"Error al reproducir el sonido {tipo} con Pygame: {e}")

    def limpiar_vista(self):
        """Elimina todos los widgets de la vista actual y detiene animaciones, EXCEPTO el fondo."""
        if self.pulse_animation_id is not None:
            self.master.after_cancel(self.pulse_animation_id)
            self.pulse_animation_id = None
        if self.logo_animation_id is not None:
            self.master.after_cancel(self.logo_animation_id)
            self.logo_animation_id = None
            self.logo_current_scale = 1.0 

        # Limpiar referencias de imágenes de ecopuntos (importante para GC)
        self.ecopunto_img_left = None
        self.ecopunto_img_right = None
        if self.ecopunto_label_left: self.ecopunto_label_left.destroy()
        if self.ecopunto_label_right: self.ecopunto_label_right.destroy()
        self.ecopunto_label_left = None
        self.ecopunto_label_right = None


        for widget in self.master.winfo_children():
            # Excluir el Label de fondo si existe y tiene la referencia
            if widget is self.fondo_label:
                continue
            widget.destroy()

    def configurar_fondo(self):
        """Carga y configura una imagen de fondo si no ha sido creada ya."""
        # SOLO CREAR EL FONDO UNA VEZ
        if self.fondo_label:
            # Si ya existe, solo nos aseguramos de que esté en la capa más baja
            self.fondo_label.lower() 
            return 

        try:
            resample_method = Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.LANCZOS
            img = Image.open(self.PATH_FONDO)
            ancho, alto = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
            
            img = img.resize((ancho, alto), resample_method)
            
            self.bg_image_tk = ImageTk.PhotoImage(img)
            
            # Crear y almacenar la referencia del label de fondo
            self.fondo_label = tk.Label(self.master, image=self.bg_image_tk, name='fondo_label')
            self.fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
            
            # Asegurarse de que el fondo esté siempre detrás de todos los demás widgets
            self.fondo_label.lower() 

        except FileNotFoundError:
            print(f"Advertencia: Archivo de fondo no encontrado en {self.PATH_FONDO}. Usando color sólido.")
            # Si no hay imagen, el color de fondo configurado en master.config(bg=self.COLOR_FONDO) será visible
        except Exception as e:
            print(f"Error al cargar imagen de fondo: {e}. Usando color sólido.")
            # Si hay un error, el color de fondo configurado en master.config(bg=self.COLOR_FONDO) será visible


    def cargar_imagenes_ecopuntos(self):
        """Carga y redimensiona las imágenes laterales de ecopuntos a un tamaño más pequeño."""
        try:
            resample_method = Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.Resampling.LANCZOS
            ancho_deseado = 200 

            # Imagen Izquierda
            img_left = Image.open(self.PATH_ECOPUNTO_LEFT)
            img_left = img_left.resize((ancho_deseado, int(ancho_deseado * img_left.height / img_left.width)), resample_method)
            self.ecopunto_img_left = ImageTk.PhotoImage(img_left)

            # Imagen Derecha
            img_right = Image.open(self.PATH_ECOPUNTO_RIGHT)
            img_right = img_right.resize((ancho_deseado, int(ancho_deseado * img_right.height / img_right.width)), resample_method)
            self.ecopunto_img_right = ImageTk.PhotoImage(img_right)
            return True
        except FileNotFoundError:
            print("Advertencia: No se encontraron los archivos de imagen ecopunto1.png o ecopunto2.png.")
            return False
        except Exception as e:
            print(f"Error al cargar/redimensionar imágenes de ecopuntos: {e}")
            return False

    def animar_boton_pulso(self, boton, color_base, color_resalte, duration=150):
        """Crea un efecto de pulsación de color para el botón de inicio."""
        current_bg = boton.cget("bg")
        if color_base in current_bg:
            new_bg = color_resalte
        else:
            new_bg = color_base
        boton.config(bg=new_bg)
        self.pulse_animation_id = self.master.after(
            duration, self.animar_boton_pulso, boton, color_base, color_resalte, duration
        )
    
    # --- LÓGICA DE ANIMACIÓN DE LOGO DEL TRAYECTO ---
    def animate_logo_scale(self):
        """Crea un efecto de pulso animado escalando el logo del trayecto."""
        if not self.trayecto_logo_label or not self.logo_path:
            return

        # Alternar escala: 1.0 (base) <-> 1.1 (pulso)
        if self.logo_current_scale == 1.0:
            self.logo_current_scale = 1.1
        else:
            self.logo_current_scale = 1.0

        new_width = int(self.logo_base_size[0] * self.logo_current_scale)
        new_height = int(self.logo_base_size[1] * self.logo_current_scale)

        try:
            resample_method = Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.Resampling.LANCZOS
            img = Image.open(self.logo_path)
            img = img.resize((new_width, new_height), resample_method)
            self.logo_image_tk_animated = ImageTk.PhotoImage(img) # Actualizar la imagen animada
            self.trayecto_logo_label.config(image=self.logo_image_tk_animated)
        except Exception:
             # Detener animación si hay un error de imagen/ruta
            if self.logo_animation_id:
                self.master.after_cancel(self.logo_animation_id)
            return

        self.logo_animation_id = self.master.after(400, self.animate_logo_scale) # Pulso cada 400ms

    # --- FLUJO DE VISTAS ---

    def mostrar_bienvenida(self):
        """Muestra la pantalla inicial (Sección de bienvenida)."""
        self.current_screen = "welcome"
        self.limpiar_vista() # Limpia todo EXCEPTO el fondo que ya está puesto
        
        main_frame = tk.Frame(self.master, bg=self.COLOR_FONDO) 
        main_frame.pack(expand=True)

        # --- Logo (Isotipo (1).png) ---
        try:
            resample_method = Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.Resampling.LANCZOS
            logo_img = Image.open(self.PATH_LOGO)
            logo_img = logo_img.resize((640, 360), resample_method)
            self.logo_image_tk = ImageTk.PhotoImage(logo_img)
            logo_label = tk.Label(main_frame, image=self.logo_image_tk, bg=self.COLOR_FONDO)
            logo_label.pack(pady=20)
        except FileNotFoundError:
            tk.Label(main_frame, text="Escuela de Robótica de Misiones (ERM)", font=("Arial", 30, "bold"), fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=20)
        except Exception as e:
            print(f"Error al cargar el logo de bienvenida: {e}")
            tk.Label(main_frame, text="Logo ERM", font=("Arial", 30, "bold"), fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=20)

        # Título e Instrucciones
        titulo = tk.Label(main_frame, text="🎉 BIENVENIDO/A a la Trivia ERM: TecnoTravesía 🎉",
                           font=self.FUENTE_TITULO, fg=self.COLOR_RESALTE, bg=self.COLOR_FONDO)
        titulo.pack(pady=10)
        instrucciones = tk.Label(main_frame, text="Responde unas preguntas para obtener tu guía de recorrido en la feria de ciencias.", 
                                     font=self.FUENTE_PREGUNTA, wraplength=800, fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO)
        instrucciones.pack(pady=10)

        COLOR_BASE_INICIO = "#4CAF50"
        COLOR_RESALTE_INICIO = "#00FF7F"

        boton_iniciar = tk.Button(main_frame, text="🚀 INICIAR TRIVIA 🤖\n(O pulsa ESPACIO)", 
                                     command=lambda: (self.master.after_cancel(self.pulse_animation_id) if self.pulse_animation_id else None, self.mostrar_pregunta_erm()), 
                                     bg=COLOR_BASE_INICIO, fg="black", font=self.FUENTE_BOTON, relief=tk.RAISED, bd=5, activebackground=COLOR_RESALTE_INICIO)
        boton_iniciar.pack(pady=40, ipadx=20, ipady=10)
        self.animar_boton_pulso(boton_iniciar, COLOR_BASE_INICIO, COLOR_RESALTE_INICIO)

    def mostrar_pregunta_erm(self):
        """Muestra la pregunta actual de la Sección 1/3, incluyendo imágenes de Ecopuntos si aplica."""
        self.current_screen = "trivia"
        if self.indice_pregunta >= len(self.preguntas):
            self.mostrar_diagnostico_edad()
            return
            
        self.limpiar_vista() # Limpia todo EXCEPTO el fondo persistente

        pregunta_data = self.preguntas[self.indice_pregunta]
        pregunta_texto = pregunta_data["pregunta"]
        self.respuesta_seleccionada.set(None)

        # Verificar si es la pregunta de Ecopuntos
        is_ecopuntos_question = PREGUNTA_ECOPUNTOS in pregunta_texto

        # Frame principal para organizar los elementos horizontalmente
        # Este frame tendrá el COLOR_FONDO definido para sus elementos, no para cubrir el fondo de la ventana
        outer_frame = tk.Frame(self.master, bg=self.COLOR_FONDO) 
        outer_frame.pack(expand=True, fill=tk.BOTH)

        # --- Lógica de Imágenes Laterales (Solo para la pregunta de Ecopuntos) ---
        if is_ecopuntos_question and self.cargar_imagenes_ecopuntos():
            # Etiqueta izquierda
            self.ecopunto_label_left = tk.Label(outer_frame, image=self.ecopunto_img_left, bg=self.COLOR_FONDO)
            self.ecopunto_label_left.pack(side=tk.LEFT, padx=10, fill=tk.Y)
            # Etiqueta derecha
            self.ecopunto_label_right = tk.Label(outer_frame, image=self.ecopunto_img_right, bg=self.COLOR_FONDO)
            self.ecopunto_label_right.pack(side=tk.RIGHT, padx=10, fill=tk.Y)

        # Frame para el contenido central (pregunta y opciones)
        central_column_frame = tk.Frame(outer_frame, bg=self.COLOR_FONDO)
        central_column_frame.pack(expand=True)

        tk.Label(central_column_frame, text=f"📍 PREGUNTA {self.indice_pregunta + 1}/{len(self.preguntas)}", 
                     font=self.FUENTE_PREGUNTA, fg=self.COLOR_RESALTE, bg=self.COLOR_FONDO).pack(pady=10)
        tk.Label(central_column_frame, text=pregunta_texto, 
                     font=self.FUENTE_PREGUNTA, wraplength=800, justify=tk.CENTER, fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=20)

        opciones_frame = tk.Frame(central_column_frame, bg=self.COLOR_FONDO)
        opciones_frame.pack(pady=20)

        for i, opcion in enumerate(pregunta_data["opciones"]):
            rb = tk.Radiobutton(opciones_frame, text=opcion, variable=self.respuesta_seleccionada, value=opcion, 
                                 font=self.FUENTE_OPCION, bg=self.COLOR_FONDO, fg=self.COLOR_TEXTO, selectcolor=self.COLOR_FONDO, 
                                 anchor="w", justify=tk.LEFT, activebackground=self.COLOR_FONDO, activeforeground=self.COLOR_RESALTE, bd=0, highlightthickness=0) 
            rb.pack(pady=5, padx=20, fill='x')

        tk.Button(central_column_frame, text="SIGUIENTE ➡️\n(O pulsa ESPACIO para saltar)", command=self.verificar_respuesta, 
                     bg="#004D99", fg="white", font=self.FUENTE_BOTON, relief=tk.RAISED, bd=5, activebackground="#006BB9").pack(pady=40, ipadx=20, ipady=10)

    def verificar_respuesta(self, event=None, force_skip=False):
        """Verifica la respuesta actual, actualiza la puntuación y avanza. Permite saltar."""
        if self.indice_pregunta >= len(self.preguntas):
            self.mostrar_diagnostico_edad()
            return

        respuesta_usuario = self.respuesta_seleccionada.get()
        if not respuesta_usuario:
            if not force_skip:
                self.reproducir_sonido("error")
                messagebox.showwarning("Advertencia", "Por favor, selecciona una opción antes de continuar.")
                return
            else:
                respuesta_usuario = "SKIPPED_BY_SPACE"

        pregunta_data = self.preguntas[self.indice_pregunta]
        es_pregunta_erm = any(d["pregunta"] == pregunta_data["pregunta"] for d in PREGUNTAS_ERM)

        if respuesta_usuario == pregunta_data["respuesta_correcta"]:
            if es_pregunta_erm:
                self.puntuacion_erm += 1
            self.reproducir_sonido("victoria")
            messagebox.showinfo("Resultado", "✅ ¡CORRECTO! +1 Conocimiento")
        elif respuesta_usuario == "SKIPPED_BY_SPACE":
            # No notificar nada al saltar
            pass 
        else:
            self.reproducir_sonido("error")
            messagebox.showinfo("Resultado", f"❌ INCORRECTO. La respuesta era: {pregunta_data['respuesta_correcta']}")

        self.indice_pregunta += 1
        self.mostrar_pregunta_erm()

    def mostrar_diagnostico_edad(self):
        """Muestra el formulario para la edad (Sección 2)."""
        self.current_screen = "age_form"
        self.limpiar_vista() # Limpia todo EXCEPTO el fondo persistente
        
        central_column_frame = tk.Frame(self.master, bg=self.COLOR_FONDO)
        central_column_frame.pack(expand=True)
        
        tk.Label(central_column_frame, text="🧭 SECCIÓN 2: ¿A QUÉ TRAYECTO PERTENECES?", 
                     font=self.FUENTE_TITULO, fg=self.COLOR_RESALTE, bg=self.COLOR_FONDO).pack(pady=30)
        
        tk.Label(central_column_frame, text="¡Estás a punto de obtener tu guía! Ingresa tu edad actual (solo el número):", 
                     font=self.FUENTE_PREGUNTA, fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=20)

        # Campo de entrada de edad
        self.entrada_edad = tk.Entry(central_column_frame, font=self.FUENTE_TITULO, width=5, justify=tk.CENTER, 
                                         bg="#FFFFFF", fg="#000000", bd=5)
        self.entrada_edad.pack(pady=20)
        self.entrada_edad.focus_set()

        tk.Button(central_column_frame, text="✅ CONFIRMAR EDAD", command=self.procesar_edad, 
                     bg="#4CAF50", fg="black", font=self.FUENTE_BOTON, relief=tk.RAISED, bd=5, activebackground="#6BC96E").pack(pady=30, ipadx=20, ipady=10)

    def procesar_edad(self):
        """Maneja la validación de la edad y asigna el trayecto."""
        try:
            edad = int(self.entrada_edad.get())
            if edad < 3 or edad > 100:
                self.reproducir_sonido("error")
                messagebox.showerror("Error", "Por favor, ingresa una edad válida (entre 3 y 100).")
                return
            
            self.trayecto_asignado = determinar_trayecto(edad)
            # Definir la ruta del logo para la vista final
            if self.trayecto_asignado in self.PATH_LOGOS:
                self.logo_path = self.PATH_LOGOS[self.trayecto_asignado]
            else:
                self.logo_path = None
            
            self.mostrar_resultado_final()
            
        except ValueError:
            self.reproducir_sonido("error")
            messagebox.showerror("Error", "Entrada no válida. Por favor, ingresa un número entero para tu edad.")

    def reiniciar_trivia(self):
        """Reinicia el estado de la aplicación para comenzar de nuevo."""
        # Restablecer variables de estado y puntuación
        self.puntuacion_erm = 0
        self.indice_pregunta = 0
        self.trayecto_asignado = ""
        self.respuesta_seleccionada.set(None)

        # Detener cualquier animación de logo que esté activa
        if self.logo_animation_id:
            self.master.after_cancel(self.logo_animation_id)
            self.logo_animation_id = None
        self.logo_current_scale = 1.0 
        self.logo_path = None
        if self.trayecto_logo_label: # Destruir el label del logo del trayecto si existe
            self.trayecto_logo_label.destroy()
            self.trayecto_logo_label = None

        # Volver a la pantalla de bienvenida
        self.mostrar_bienvenida()

    def mostrar_resultado_final(self):
        """Muestra el resultado, el logo animado del trayecto y la recomendación (Sección 4)."""
        self.current_screen = "result"
        self.limpiar_vista() # Limpia todo EXCEPTO el fondo persistente

        # Usamos un Frame central que expande para centrar todo
        central_column_frame = tk.Frame(self.master, bg=self.COLOR_FONDO)
        central_column_frame.pack(expand=True, padx=20, pady=20)
        
        tk.Label(central_column_frame, text="✨ ¡TU RECORRIDO PERSONALIZADO! ✨", 
                     font=self.FUENTE_TITULO, fg=self.COLOR_RESALTE, bg=self.COLOR_FONDO).pack(pady=5)
        
        # --- Logo del Trayecto Asignado (Animado) ---
        if self.logo_path:
            try:
                # Cargar el logo en tamaño base
                resample_method = Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.Resampling.LANCZOS
                img = Image.open(self.logo_path)
                img = img.resize(self.logo_base_size, resample_method)
                self.logo_image_tk_animated = ImageTk.PhotoImage(img) # Usar la variable animada para el inicio
                
                self.trayecto_logo_label = tk.Label(central_column_frame, image=self.logo_image_tk_animated, bg=self.COLOR_FONDO)
                self.trayecto_logo_label.pack(pady=10)
                
                # Iniciar la animación de pulso
                self.animate_logo_scale() 
            except Exception as e:
                print(f"Error al cargar/mostrar el logo del trayecto: {e}")
                tk.Label(central_column_frame, text=f"LOGO {self.trayecto_asignado}", font=self.FUENTE_PREGUNTA, fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=10)
        else:
            tk.Label(central_column_frame, text=f"Trayecto: {self.trayecto_asignado}", font=self.FUENTE_PREGUNTA, fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=10)
        
        # --- Lógica de Recomendación (Nivel de Conocimiento) ---
        recomendacion = ""
        if self.puntuacion_erm >= 8:
            nivel_conocimiento = "FAN DE LA ERM, Alto"
            recomendacion = f"¡Felicidades, un verdadero fan de la ERM! Has demostrado un conocimiento estelar.\n\nTe sugerimos comenzar tu recorrido en el área de **Innovación y Proyecto Final** (TeamInn/HighMaker) y en el stand de **Tecnología Sostenible y Ética** (Visión de Futuro)."
            mensaje_final = "¡Felicidades, un verdadero fan de la ERM! Has demostrado un conocimiento estelar."
        elif self.puntuacion_erm >= 5:
            nivel_conocimiento = "VISITANTE AVANZADO, Medio-Alto"
            recomendacion = f"¡Muy bien! Tienes una base sólida, pero siempre hay algo más que aprender. 🤔\n\nComienza visitando el stand de tu Trayecto asignado: **{self.trayecto_asignado}**, y luego pasa por los stands de **Historia y Valores de la ERM** (Pilares Fundamentales)."
            mensaje_final = "¡Muy bien! Tienes una base sólida, pero siempre hay algo más que aprender. 🤔"
        else:
            nivel_conocimiento = "APRENDIZ DE ROBÓTICA, Bajo"
            recomendacion = f"¡Genial! No te preocupes, la feria es el lugar perfecto para sumergirte en el mundo ERM. 👍\n\nDirígete primero al stand de **{self.trayecto_asignado}** y luego a la zona de **PequeBot/TrendKids** (Fundamentos Visuales y Divertidos) para conocer lo básico de forma lúdica."
            mensaje_final = "¡Genial! No te preocupes, la feria es el lugar perfecto para sumergirte en el mundo ERM. 👍"

        tk.Label(central_column_frame, text=mensaje_final, font=self.FUENTE_PREGUNTA, fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO, wraplength=800).pack(pady=10)
        
        # Resumen
        resumen_frame = tk.Frame(central_column_frame, bg=self.COLOR_FONDO)
        resumen_frame.pack(pady=20)
        
        tk.Label(resumen_frame, text=f"Puntuación ERM: {self.puntuacion_erm}/{self.total_preguntas_erm} ({nivel_conocimiento})", 
                     font=self.FUENTE_OPCION, fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=5)
                      
        tk.Label(resumen_frame, text=f"Trayecto Asignado: {self.trayecto_asignado}",
                     font=self.FUENTE_TITULO, fg=self.COLOR_RESALTE, bg=self.COLOR_FONDO).pack(pady=5)
        tk.Label(resumen_frame, text=f"Empezá tu recorrido en la TecnoTravesía visitando a tu trayecto asignado", 
                     font=self.FUENTE_OPCION, fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=5)
        tk.Label(resumen_frame, text=f"Por favor pulsá ESPACIO para reiniciar la trivia",
                     font=self.FUENTE_TITULO, fg=self.COLOR_RESALTE, bg=self.COLOR_FONDO).pack(pady=10)
        
        
        # Recuadro de recomendación con texto justificado y centrado
        tk.Label(central_column_frame, text=recomendacion, font=self.FUENTE_OPCION, wraplength=900, justify=tk.CENTER, 
                     fg="#000000", bg="#E0E0E0", bd=5, relief=tk.GROOVE).pack(pady=10, padx=20, ipady=15)
        
        # Botones finales
        botones_frame = tk.Frame(central_column_frame, bg=self.COLOR_FONDO)
        botones_frame.pack(pady=40)
        
        tk.Button(botones_frame, text="REINICIAR 🔄", command=self.reiniciar_trivia, 
                     bg="#004D99", fg="white", font=self.FUENTE_BOTON, relief=tk.RAISED, bd=5).pack(side=tk.LEFT, padx=10, ipadx=20, ipady=10)

        tk.Button(botones_frame, text="SALIR ❌", command=self.master.destroy, 
                     bg="#CC0000", fg="white", font=self.FUENTE_BOTON, relief=tk.RAISED, bd=5).pack(side=tk.LEFT, padx=10, ipadx=20, ipady=10)


# --- 3. INICIAR LA APLICACIÓN ---

if __name__ == "__main__":
    # La inicialización de Pygame Mixer debe ser antes de crear la ventana principal.
    try:
        # Se inicializa de forma básica aquí, pero la configuración real (incluyendo la carga de música)
        # se hace dentro de TriviaApp.__init__ para usar las rutas de assets.
        mixer.init() 
    except Exception:
        pass # Si falla, la aplicación continuará sin sonido

    root = tk.Tk()
    app = TriviaApp(root)
    root.mainloop()