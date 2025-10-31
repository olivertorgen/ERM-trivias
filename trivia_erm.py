import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 
import pygame.mixer as mixer 

# ----------------------------------------------------------------------
# --- 1. DATOS DE LA TRIVIA Y FUNCIONES AUXILIARES ---
# ----------------------------------------------------------------------

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
        "opciones": ["c.P. Natalia Meira", "Lic. Araceli Vera", " No hay una coordinadora general, solo coordinadores de trayecto"],
        "respuesta_correcta": "Lic. Araceli Vera"
    },
    {
        "pregunta": "El objetivo principal de la ERM es que los estudiantes logren autonomía y sean protagonistas de su aprendizaje. ¿Qué tipo de Ley apoya este enfoque educativo en Misiones?",
        "opciones": ["Ley de Educación Superior", "Ley de Educación Disruptiva", "Ley Federal de Educación", "Ley de Financiamiento Educativo"],
        "respuesta_correcta": "Ley de Educación Disruptiva"
    },
    {
        "pregunta": "¿Qué tipo de profesionales conforman el equipo de trabajo multidisciplinario de la ERM?",
        "opciones": [" Solo Ingenieros y Técnicos", "Solo profesores de nivel inicial y educación especial", "Profesionales de distintas disciplinas como ingenieros, técnicos, profesores, especialistas en diversas áreas", "Únicamente facilitadores de robótica" ],
        "respuesta_correcta": "Profesionales de distintas disciplinas como ingenieros, técnicos, profesores, especialistas en diversas áreas"
    },
    {
        "pregunta": "¿Dónde está ubicada la Escuela de Robótica de Misiones (ERM)?",
        "opciones": ["Av. Mitre, 1000.", "Av. Gdor. Roca 480.", "Av. Maipú, 1500", "Av. Roque Perez 490"],
        "respuesta_correcta": "Av. Gdor. Roca 480."
    }
]

# Preguntas de la Sección 3: Compromiso Social y Ambiental (Intercaladas)
PREGUNTAS_ETICAS_AMBIENTALES = [
    {
        "pregunta": "¿Cuál de las siguientes acciones contribuye más a la sostenibilidad ambiental?",
        "opciones": ["Plantar árboles y conservar áreas verdes.", "Usar más plástico para embalajes.", "Aumentar el uso de vehículos privados.", "Comprar productos desechables."],
        "respuesta_correcta": "Plantar árboles y conservar áreas verdes."
    },
    {
        "pregunta": "Ubicación de Ecopuntos: Si estás en Posadas, ¿dónde podrías encontrar un Ecopunto para llevar tus residuos reciclables (plástico, papel, vidrio)?",
        "opciones": ["Costa Sur: Ubicado en el balneario.", "Itaembé Guazú: En la calle Aguará Guazú y los Cactus.", "Parque La Cascada", "Todas son correctas."],
        "respuesta_correcta": "Todas son correctas."
    },
]

# Preguntas sobre Inclusión
PREGUNTAS_SOBRE_INCLUSIÓN = [
    {
        "pregunta": "¿Cuál es la importancia de la inclusión en la educación tecnológica?",
        "opciones": ["Fomenta la diversidad y la igualdad de oportunidades para todos los estudiantes.", "Solo beneficia a estudiantes con discapacidades.", "No tiene impacto en el aprendizaje.", "Es un requisito legal sin beneficios prácticos."],
        "respuesta_correcta": "Fomenta la diversidad y la igualdad de oportunidades para todos los estudiantes."
    },
    {
        "pregunta": "¿Cómo puede la tecnología contribuir a la inclusión social?",
        "opciones": ["Desarrollando herramientas accesibles para personas con discapacidades.", "Excluyendo a grupos minoritarios.", "Fomentando la competencia entre estudiantes.", "Limitando el acceso a la tecnología."],
        "respuesta_correcta": "Desarrollando herramientas accesibles para personas con discapacidades."
    },
    {
        "pregunta": "La ERM cuenta con profesionales en Educación Especial en su equipo. ¿Cuál es el rol principal de estos especialistas en el contexto de la escuela?",
        "opciones": ["Garantizar que las adaptaciones curriculares y los apoyos necesarios estén disponibles para la participación plena de todos los estudiantes, independientemente de sus habilidades o discapacidades.", "Dar las clases de robótica más difíciles", "Solo apoyar a los profesores más jóvenes", "Evaluar las habilidades técnicas de los estudiantes"],
        "respuesta_correcta": "Garantizar que las adaptaciones curriculares y los apoyos necesarios estén disponibles para la participación plena de todos los estudiantes, independientemente de sus habilidades o discapacidades."
    },
]

# La pregunta específica donde se mostrarán las imágenes
PREGUNTA_ECOPUNTOS = "¿dónde podrías encontrar un Ecopunto para llevar tus residuos reciclables (plástico, papel, vidrio)?"

# Función para combinar las preguntas
def obtener_preguntas_combinadas():
    """Combina las preguntas de ERM, Éticas/Ambientales e Inclusión para el flujo."""
    preguntas_combinadas = []
    total_erm = len(PREGUNTAS_ERM)
    total_eticas = len(PREGUNTAS_ETICAS_AMBIENTALES)
    total_inclusion = len(PREGUNTAS_SOBRE_INCLUSIÓN)
    
    max_len = max(total_erm, total_eticas, total_inclusion)

    # Intercalar preguntas para asegurar variedad
    for i in range(max_len):
        if i < total_erm:
            preguntas_combinadas.append(PREGUNTAS_ERM[i])
        
        if i < total_eticas:
            preguntas_combinadas.append(PREGUNTAS_ETICAS_AMBIENTALES[i])

        if i < total_inclusion:
            preguntas_combinadas.append(PREGUNTAS_SOBRE_INCLUSIÓN[i])
            
    return preguntas_combinadas

# Mapeo de Trayectos (Sección 2)
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
    COLOR_FONDO = "#2E0058"       # Violeta Oscuro
    COLOR_TEXTO = "#F0DEFF"       # Violeta claro
    COLOR_RESALTE = "#FFD700"     # Amarillo/Oro
    
    FUENTE_TITULO = ("Arial", 36, "bold") 
    FUENTE_PREGUNTA = ("Arial", 24, "bold")
    FUENTE_OPCION = ("Arial", 20)
    FUENTE_BOTON = ("Arial", 22, "bold")
    
    # Rutas de assets
    PATH_FONDO = "assets/fondo_espacial.png"    
    PATH_LOGO = "assets/Escuela de robotica misiones.png"     
    PATH_CORRECT_SOUND = "assets/sonido_correcto.mp3"  
    PATH_ERROR_SOUND = "assets/sonido_incorrecto.mp3"
    
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
        master.config(bg=self.COLOR_FONDO) 
        
        self.puntuacion_erm = 0
        self.trayecto_asignado = ""
        self.preguntas = obtener_preguntas_combinadas()
        self.indice_pregunta = 0
        self.total_preguntas_erm = len(PREGUNTAS_ERM)    
        
        self.respuesta_seleccionada = tk.StringVar(master)
        self.bg_image_tk = None
        self.logo_image_tk = None
        
        # Variables de animación
        self.pulse_animation_id = None  
        self.logo_animation_id = None
        self.logo_label = None  
        self.logo_image_tk_animated = None
        
        self.logo_base_size = (200, 200)    
        self.logo_current_scale = 1.0

        # --- Variables para las imágenes de Ecopuntos ---
        self.ecopunto_img_left = None
        self.ecopunto_img_right = None
        self.ecopunto_label_left = None
        self.ecopunto_label_right = None
        
        # --- CONFIGURACIÓN DE SONIDO (Pygame Mixer) ---
        self.sound_enabled = False
        self.sound_correct = None
        self.sound_error = None
        try:
            mixer.init(frequency=44100)
            self.sound_correct = mixer.Sound(self.PATH_CORRECT_SOUND)
            self.sound_error = mixer.Sound(self.PATH_ERROR_SOUND)
            self.sound_enabled = True
        except FileNotFoundError:
            print(f"Advertencia: Archivos de sonido MP3 no encontrados en assets/. El audio estará deshabilitado.")
            self.sound_enabled = False
        except Exception as e:
            print(f"Advertencia: Pygame o sus dependencias fallaron. El audio estará deshabilitado. Error: {e}")
            self.sound_enabled = False
        # ---------------------------------------------

        self.current_screen = "welcome"
        self.master.bind('<space>', self.on_space_press) 

        self.mostrar_bienvenida()

    # --- LÓGICA DE TECLAS Y ESTADO ---

    def on_space_press(self, event):
        """Maneja la pulsación de la tecla ESPACIO para avanzar en la trivia o iniciarla."""
        
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

    # --- UTILIDADES DE VISTA Y SONIDO ---
    
    def reproducir_sonido(self, tipo):
        """Reproduce un sonido de victoria o error usando pygame.mixer."""
        if not self.sound_enabled:
            return
            
        try:
            if tipo == "victoria" and self.sound_correct:
                self.sound_correct.play()
            elif tipo == "error" and self.sound_error:
                self.sound_error.play()
        except Exception as e:
            print(f"Error al reproducir el sonido {tipo} con Pygame: {e}")

    def limpiar_vista(self):
        """Elimina todos los widgets de la vista actual y detiene animaciones."""
        if self.pulse_animation_id is not None:
            self.master.after_cancel(self.pulse_animation_id)
            self.pulse_animation_id = None
            
        if self.logo_animation_id is not None:
            self.master.after_cancel(self.logo_animation_id)
            self.logo_animation_id = None
            
        # Limpiar referencias de imágenes de ecopuntos (es importante para que el garbage collector las libere)
        self.ecopunto_img_left = None
        self.ecopunto_img_right = None
        self.ecopunto_label_left = None
        self.ecopunto_label_right = None
            
        for widget in self.master.winfo_children():
            widget.destroy()

    def configurar_fondo(self):
        """Carga y configura una imagen de fondo, o usa un color sólido como fallback."""
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Label) and widget.winfo_name() == 'fondo_label':
                widget.destroy()
                break
                
        fondo_label = None
        try:
            resample_method = Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.LANCZOS
            
            img = Image.open(self.PATH_FONDO)
            ancho, alto = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
            img = img.resize((ancho, alto), resample_method)
            self.bg_image_tk = ImageTk.PhotoImage(img)
            
            fondo_label = tk.Label(self.master, image=self.bg_image_tk, name='fondo_label')
            fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
            fondo_label.lower() 
        except FileNotFoundError:
            print(f"Advertencia: Archivo de fondo no encontrado en {self.PATH_FONDO}. Usando color sólido.")
        except Exception as e:
            print(f"Error al cargar imagen de fondo: {e}. Usando color sólido.")
            
        return fondo_label

    def cargar_imagenes_ecopuntos(self):
        """Carga y redimensiona las imágenes laterales de ecopuntos a un tamaño más pequeño."""
        try:
            resample_method = Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.LANCZOS
            
            # --- Ajuste CLAVE: Reducir el tamaño deseado para las imágenes de Ecopuntos ---
            # Por ejemplo, un ancho fijo de 150px, dejando que el alto se ajuste proporcionalmente
            ancho_deseado = 200 # Antes era basado en la mitad de la pantalla, ahora un valor fijo más pequeño
            
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
            duration,    
            self.animar_boton_pulso,    
            boton, color_base, color_resalte, duration
        )
            
    # --- LÓGICA DE ANIMACIÓN DE LOGO ---

    def animate_logo_scale(self):
        """Crea un efecto de pulso animado escalando el logo del trayecto."""
        if not self.logo_label or not hasattr(self, 'logo_path') or not self.logo_path:
            return

        # Alternar escala: 1.0 (base) <-> 1.05 (pulso)
        if self.logo_current_scale == 1.0:
            self.logo_current_scale = 1.05
        else:
            self.logo_current_scale = 1.0

        new_width = int(self.logo_base_size[0] * self.logo_current_scale)
        new_height = int(self.logo_base_size[1] * self.logo_current_scale)

        try:
            resample_method = Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.LANCZOS
            img = Image.open(self.logo_path)    
            img = img.resize((new_width, new_height), resample_method)
            
            self.logo_image_tk_animated = ImageTk.PhotoImage(img)    
            self.logo_label.config(image=self.logo_image_tk_animated)
            
        except FileNotFoundError:
            if self.logo_animation_id:
                self.master.after_cancel(self.logo_animation_id)
                self.logo_animation_id = None
            self.logo_label.config(text=f"ERROR: LOGO '{self.trayecto_asignado}' NO ENCONTRADO", image='')
            return
        except Exception as e:
            print(f"Error al cargar o animar el logo: {e}")
            if self.logo_animation_id:
                self.master.after_cancel(self.logo_animation_id)
                self.logo_animation_id = None
            self.logo_label.config(text=f"Error de formato de imagen para {self.trayecto_asignado}", image='')
            pass

        self.logo_animation_id = self.master.after(500, self.animate_logo_scale)

    # --- FLUJO DE VISTAS ---

    def mostrar_bienvenida(self):
        """Muestra la pantalla inicial (Sección de bienvenida)."""
        self.current_screen = "welcome" 
        self.limpiar_vista()
        self.configurar_fondo()
        
        main_frame = tk.Frame(self.master, bg=self.COLOR_FONDO)
        main_frame.pack(expand=True)    

        # --- Logo ERM ---
        try:
            resample_method = Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.LANCZOS
            logo_img = Image.open(self.PATH_LOGO)
            logo_img = logo_img.resize((428, 118), resample_method)
            self.logo_image_tk = ImageTk.PhotoImage(logo_img)
            logo_label = tk.Label(main_frame, image=self.logo_image_tk, bg=self.COLOR_FONDO)
            logo_label.pack(pady=20)
        except FileNotFoundError:
            tk.Label(main_frame, text="Escuela de Robótica de Misiones (ERM)", font=("Arial", 30, "bold"), fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=20)
        except Exception:
            tk.Label(main_frame, text="Logo ERM", font=("Arial", 30, "bold"), fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=20)

        # Título e Instrucciones
        titulo = tk.Label(main_frame, text="🎉 BIENVENIDO/A A LA TRIVIA ERM TecnoTravesía 🎉", 
                             font=self.FUENTE_TITULO, fg=self.COLOR_RESALTE, bg=self.COLOR_FONDO)
        titulo.pack(pady=20)

        instrucciones = tk.Label(main_frame, text="Responde unas preguntas para obtener tu guía de recorrido en la feria de ciencias.",
                                     font=self.FUENTE_PREGUNTA, wraplength=800, fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO)
        instrucciones.pack(pady=10)

        COLOR_BASE_INICIO = "#4CAF50"    
        COLOR_RESALTE_INICIO = "#00FF7F"     

        # El comando del botón llama a la misma lógica de iniciar
        boton_iniciar = tk.Button(main_frame, text="🚀 INICIAR TRIVIA 🤖\n(O pulsa ESPACIO)",    
                                     command=lambda: (self.master.after_cancel(self.pulse_animation_id) if self.pulse_animation_id else None, self.mostrar_pregunta_erm()),  
                                     bg=COLOR_BASE_INICIO, fg="black", font=self.FUENTE_BOTON, relief=tk.RAISED, bd=5,    
                                     activebackground=COLOR_RESALTE_INICIO)
        boton_iniciar.pack(pady=40, ipadx=20, ipady=10)
        
        self.animar_boton_pulso(boton_iniciar, COLOR_BASE_INICIO, COLOR_RESALTE_INICIO)


    def mostrar_pregunta_erm(self):
        """Muestra la pregunta actual de la Sección 1/3, incluyendo imágenes de Ecopuntos si aplica."""
        self.current_screen = "trivia" 
            
        if self.indice_pregunta >= len(self.preguntas):
            self.mostrar_diagnostico_edad()
            return

        self.limpiar_vista()
        self.configurar_fondo()
        
        pregunta_data = self.preguntas[self.indice_pregunta]
        pregunta_texto = pregunta_data["pregunta"]
        self.respuesta_seleccionada.set(None)

        # Verificar si es la pregunta de Ecopuntos
        is_ecopuntos_question = PREGUNTA_ECOPUNTOS in pregunta_texto

        # Usamos un Frame principal para organizar los elementos horizontalmente
        # Este frame contendrá las imágenes laterales y un frame central para la pregunta
        outer_frame = tk.Frame(self.master, bg=self.COLOR_FONDO)
        outer_frame.pack(expand=True, fill=tk.BOTH)

        # --- Lógica de Imágenes Laterales (Solo para la pregunta de Ecopuntos) ---
        if is_ecopuntos_question and self.cargar_imagenes_ecopuntos():
            # Etiqueta izquierda
            self.ecopunto_label_left = tk.Label(outer_frame, image=self.ecopunto_img_left, bg=self.COLOR_FONDO)
            self.ecopunto_label_left.pack(side=tk.LEFT, padx=10, fill=tk.Y) # padx ajustado a 10
            
            # Etiqueta derecha
            self.ecopunto_label_right = tk.Label(outer_frame, image=self.ecopunto_img_right, bg=self.COLOR_FONDO)
            self.ecopunto_label_right.pack(side=tk.RIGHT, padx=10, fill=tk.Y) # padx ajustado a 10

        # Frame para el contenido central (pregunta y opciones)
        central_column_frame = tk.Frame(outer_frame, bg=self.COLOR_FONDO)
        central_column_frame.pack(expand=True) # expandirá para ocupar el espacio restante
        
        tk.Label(central_column_frame, text=f"📍 PREGUNTA {self.indice_pregunta + 1}/{len(self.preguntas)}",    
                     font=self.FUENTE_PREGUNTA, fg=self.COLOR_RESALTE, bg=self.COLOR_FONDO).pack(pady=10)
        
        tk.Label(central_column_frame, text=pregunta_texto,  
                     font=self.FUENTE_PREGUNTA, wraplength=800, justify=tk.CENTER, fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=20)

        opciones_frame = tk.Frame(central_column_frame, bg=self.COLOR_FONDO)
        opciones_frame.pack(pady=20)    
        
        for i, opcion in enumerate(pregunta_data["opciones"]):
            rb = tk.Radiobutton(opciones_frame, text=opcion, variable=self.respuesta_seleccionada, value=opcion,    
                                 font=self.FUENTE_OPCION,    
                                 bg=self.COLOR_FONDO,    
                                 fg=self.COLOR_TEXTO,    
                                 selectcolor=self.COLOR_FONDO,    
                                 anchor="w",  
                                 justify=tk.LEFT,     
                                 activebackground=self.COLOR_FONDO,  
                                 activeforeground=self.COLOR_RESALTE,
                                 bd=0, highlightthickness=0)  
            rb.pack(pady=5, padx=20, fill='x')  

        tk.Button(central_column_frame, text="SIGUIENTE ➡️\n(O pulsa ESPACIO para saltar)", command=self.verificar_respuesta,    
                     bg="#004D99", fg="white", font=self.FUENTE_BOTON, relief=tk.RAISED, bd=5,    
                     activebackground="#006BB9").pack(pady=40, ipadx=20, ipady=10)

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
            pass
        else:
            self.reproducir_sonido("error")
            messagebox.showinfo("Resultado", f"❌ INCORRECTO. La respuesta era: {pregunta_data['respuesta_correcta']}")

        self.indice_pregunta += 1
        self.mostrar_pregunta_erm()

    def mostrar_diagnostico_edad(self):
        """Muestra el formulario para la edad (Sección 2)."""
        self.current_screen = "age_form" 
        self.limpiar_vista()
        self.configurar_fondo()
        
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
                     bg="#4CAF50", fg="black", font=self.FUENTE_BOTON, relief=tk.RAISED, bd=5,
                     activebackground="#6BC96E").pack(pady=30, ipadx=20, ipady=10)

    def procesar_edad(self):
        """Maneja la validación de la edad y asigna el trayecto."""
        try:
            edad = int(self.entrada_edad.get())
            if edad < 3 or edad > 100:
                self.reproducir_sonido("error")
                messagebox.showerror("Error", "Por favor, ingresa una edad válida (entre 3 y 100).")
                return
            
            self.trayecto_asignado = determinar_trayecto(edad)
            
            # Buscamos la ruta del logo aquí para usarla en animate_logo_scale
            if self.trayecto_asignado in self.PATH_LOGOS:
                self.logo_path = self.PATH_LOGOS[self.trayecto_asignado]
            else:
                self.logo_path = None
                
            self.mostrar_resultado_final()
            
        except ValueError:
            self.reproducir_sonido("error")
            messagebox.showerror("Error", "Entrada no válida. Por favor, ingresa un número entero para tu edad.")
            
    # --- FUNCIÓN DE REINICIO (RE-INTRODUCIDA) ---
    
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
            self.logo_current_scale = 1.0 # Resetear escala
        
        # Volver a la pantalla de bienvenida
        self.mostrar_bienvenida()

    # --- VISTA FINAL OPTIMIZADA (AJUSTES DE DISTRIBUCIÓN) ---

    def mostrar_resultado_final(self):
        """Muestra el resultado, el logo animado del trayecto y la recomendación (Sección 4)."""
        self.current_screen = "result"
        self.limpiar_vista()
        self.configurar_fondo()
        
        # Usamos un Frame central que expande para centrar todo
        central_column_frame = tk.Frame(self.master, bg=self.COLOR_FONDO)
        central_column_frame.pack(expand=True, padx=20, pady=20)
        
        tk.Label(central_column_frame, text="✨ ¡TU RECORRIDO PERSONALIZADO! ✨",
                             font=self.FUENTE_TITULO, fg=self.COLOR_RESALTE, bg=self.COLOR_FONDO).pack(pady=5)
        
        # --- Lógica de Recomendación (Nivel de Conocimiento) ---
        if self.puntuacion_erm >= 8: 
            nivel_conocimiento = "FAN DE LA ERM (Alto)"
            mensaje_final = "¡Felicidades, un verdadero fan de la ERM! Conocimiento estelar."
        elif self.puntuacion_erm >= 5: 
            nivel_conocimiento = "VISITANTE AVANZADO (Medio-Alto)"
            mensaje_final = "¡Muy bien! Base sólida, siempre hay algo más que aprender. 🤔"
        else:
            nivel_conocimiento = "APRENDIZ DE ROBÓTICA (Bajo)"
            mensaje_final = "¡Genial! La feria es el lugar perfecto para sumergirte en el mundo ERM. 👍"
            
        tk.Label(central_column_frame, text=mensaje_final, font=self.FUENTE_PREGUNTA, fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO, wraplength=800).pack(pady=5)
        
        # --- Contenedor para Logo y Puntuación (Flexibilidad en dos columnas) ---
        info_container_frame = tk.Frame(central_column_frame, bg=self.COLOR_FONDO)
        info_container_frame.pack(pady=10)

        # --- Sub-Frame 1: Animación de Logo del Trayecto (Izquierda) ---
        logo_container_frame = tk.Frame(info_container_frame, bg=self.COLOR_FONDO)
        logo_container_frame.pack(side=tk.LEFT, padx=50) 
        
        tk.Label(logo_container_frame, text="TU TRAYECTO ASIGNADO ES:",
                             font=("Arial", 18, "bold"), fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack()
                          
        tk.Label(logo_container_frame, text=self.trayecto_asignado.upper(),
                             font=("Arial", 40, "bold"), fg=self.COLOR_RESALTE, bg=self.COLOR_FONDO).pack(pady=5)

        self.logo_label = tk.Label(logo_container_frame, bg=self.COLOR_FONDO)
        self.logo_label.pack(pady=10)

        # Aquí usamos self.logo_path que se definió en procesar_edad()
        if self.logo_path:
            self.animate_logo_scale()
        else:
            self.logo_label.config(text="Logo no disponible", font=self.FUENTE_OPCION, fg="red")

        # --- Sub-Frame 2: Resumen y Recomendación Breve (Derecha) ---
        resumen_frame = tk.Frame(info_container_frame, bg=self.COLOR_FONDO)
        resumen_frame.pack(side=tk.RIGHT, padx=50)

        tk.Label(resumen_frame, text="--- RESUMEN DE CONOCIMIENTO ---",
                         font=("Arial", 22, "underline"), fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=10)
        
        tk.Label(resumen_frame, text=f"Puntuación ERM: {self.puntuacion_erm}/{self.total_preguntas_erm} ({nivel_conocimiento})", 
                         font=("Arial", 20, "bold"), fg=self.COLOR_RESALTE, bg=self.COLOR_FONDO).pack(pady=5)

        tk.Label(resumen_frame, text="PUNTO DE PARTIDA RECOMENDADO",
                         font=("Arial", 20, "bold"), fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=10)

        recomendacion = (
            f"¡Por favor reinicia la trivia para el siguiente visitante!"
        )

        tk.Label(resumen_frame, text=recomendacion, font=self.FUENTE_OPCION, wraplength=400, justify=tk.CENTER, 
                         fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=5)

        # --- BOTONES DE ACCIÓN (Debajo de los Contenedores) ---
        botones_frame = tk.Frame(central_column_frame, bg=self.COLOR_FONDO)
        botones_frame.pack(pady=30) # Aumentar pady para separar de la info
        
        # Botón para Reiniciar la trivia (VISIBLE Y CENTRADO ABAJO)
        tk.Button(botones_frame, text="🔁 REINICIAR TRIVIA", command=self.reiniciar_trivia, 
                     bg="#FFD700", fg="#2E0058", font=self.FUENTE_BOTON, relief=tk.RAISED, bd=5,
                     activebackground="#FFEB3B").pack(side=tk.LEFT, padx=30, ipadx=20, ipady=10)


# ----------------------------------------------------------------------
# --- 3. INICIALIZACIÓN DE TKINTER ---
# ----------------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = TriviaApp(root)
    root.mainloop() 
    
    # Liberar recursos de sonido al cerrar
    try:
        if mixer.get_init():
            mixer.quit()
    except Exception:
        pass