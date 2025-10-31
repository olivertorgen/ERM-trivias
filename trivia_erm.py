import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk # Importante para cargar PNG/JPG

# --- 1. DATOS DE LA TRIVIA (Mismos datos de estructura) ---

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
        "pregunta": "Ubicación de Ecopuntos: Si estás en el centro de Posadas, ¿dónde podrías encontrar un Ecopunto para llevar tus residuos reciclables (plástico, papel, vidrio)?",
        "opciones": ["Costa Sur: Ubicado en el balneario.", "Itaembé Guazú: En la calle Aguará Guazú y los Cactus.", "Parque La Cascada", "Todas son correctas"],
        "respuesta_correcta": "Todas son correctas."
    },
]
# Preguntas de la Sección
PREGUNTAS_SOBRE_INCLUSIÓN = [
    {
        "pregunta": "🤝 ¿Cuál es la importancia de la inclusión en la educación tecnológica?",
        "opciones": ["Fomenta la diversidad y la igualdad de oportunidades para todos los estudiantes.", "Solo beneficia a estudiantes con discapacidades.", "No tiene impacto en el aprendizaje.", "Es un requisito legal sin beneficios prácticos."],
        "respuesta_correcta": "Fomenta la diversidad y la igualdad de oportunidades para todos los estudiantes."
    },
    {
        "pregunta": "🌍 ¿Cómo puede la tecnología contribuir a la inclusión social?",
        "opciones": ["Desarrollando herramientas accesibles para personas con discapacidades.", "Excluyendo a grupos minoritarios.", "Fomentando la competencia entre estudiantes.", "Limitando el acceso a la tecnología."],
        "respuesta_correcta": "Desarrollando herramientas accesibles para personas con discapacidades."
    },

    {
        "pregunta": "La ERM cuenta con profesionales en Educación Especial en su equipo. ¿Cuál es el rol principal de estos especialistas en el contexto de la escuela?",
        "opciones": ["Garantizar que las adaptaciones curriculares y los apoyos necesarios estén disponibles para la participación plena de todos los estudiantes, independientemente de sus habilidades o discapacidades.", "Dar las clases de robótica más difíciles", "Solo apoyar a los profesores más jóvenes", "Evaluar las habilidades técnicas de los estudiantes"],
        "respuesta_correcta": "Garantizar que las adaptaciones curriculares y los apoyos necesarios estén disponibles para la participación plena de todos los estudiantes"
    },
]

# Unir las preguntas (Intercalando una ética/ambiental cada dos de ERM)
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

# --- 2. CLASE PRINCIPAL DE LA APLICACIÓN ---

class TriviaApp:
    # --- CONFIGURACIÓN DE ESTILOS ---
    COLOR_FONDO = "#000022"  # Azul muy oscuro, casi negro (Espacio)
    COLOR_TEXTO = "#00FF00"  # Verde brillante (Neon/Arcade)
    COLOR_RESALTE = "#FFD700"  # Amarillo/Oro para títulos
    FUENTE_TITULO = ("Courier New", 30, "bold") # Fuente arcade/pixelada
    FUENTE_PREGUNTA = ("Courier New", 22, "bold")
    FUENTE_OPCION = ("Courier New", 18)
    FUENTE_BOTON = ("Courier New", 20, "bold")
    
    # Rutas de assets (Deben existir en la carpeta 'assets/')
    PATH_FONDO = "assets/fondo_espacial.png" 
    PATH_LOGO = "assets/logo_erm.png" 

    def __init__(self, master):
        self.master = master
        master.title("🤖 TRIVIA ERM - La Gala")
        
        # --- REQUERIMIENTO 1: Pantalla Completa ---
        master.attributes('-fullscreen', True) 
        # Configurar el fondo de la ventana principal
        master.config(bg=self.COLOR_FONDO) 
        
        # Variables de la aplicación
        self.puntuacion_erm = 0
        self.trayecto_asignado = ""
        self.preguntas = obtener_preguntas_combinadas()
        self.indice_pregunta = 0
        self.total_preguntas_erm = len(PREGUNTAS_ERM)
        self.respuesta_seleccionada = tk.StringVar(master)
        
        # Variables para imágenes (deben ser atributos de instancia para evitar que GC las elimine)
        self.bg_image_tk = None
        self.logo_image_tk = None
        
        # Inicializar con la vista de bienvenida
        self.mostrar_bienvenida()

    # --- UTILIDADES DE VISTA ---

    def limpiar_vista(self):
        """Elimina todos los widgets de la vista actual."""
        for widget in self.master.winfo_children():
            widget.destroy()

    def configurar_fondo(self):
        """Carga y configura una imagen de fondo si existe, sino usa un color sólido."""
        try:
            # Abrir y redimensionar la imagen para que cubra la pantalla
            img = Image.open(self.PATH_FONDO)
            # Obtener el tamaño actual de la ventana (para full-screen, es el tamaño de la pantalla)
            ancho, alto = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
            
            # Redimensionar la imagen para que coincida con el tamaño de la pantalla
            # Se usa Image.Resampling.LANCZOS para calidad, se requiere Pillow 9.0+
            # Si da error, usar Image.LANCZOS
            img = img.resize((ancho, alto), Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.LANCZOS)
            
            self.bg_image_tk = ImageTk.PhotoImage(img)
            
            # Usar un Label como contenedor del fondo
            fondo_label = tk.Label(self.master, image=self.bg_image_tk)
            fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
            
            return fondo_label # Devuelve el label de fondo

        except FileNotFoundError:
            print(f"Advertencia: No se encontró el archivo de fondo en {self.PATH_FONDO}. Usando color sólido.")
            # Si no hay imagen, el color de fondo de la ventana principal se mantiene.
            return None
        except Exception as e:
            print(f"Error al cargar la imagen de fondo: {e}. Usando color sólido.")
            return None


    # --- FLUJO DE VISTAS ---

    def mostrar_bienvenida(self):
        """Muestra la pantalla inicial (Sección de bienvenida)."""
        self.limpiar_vista()
        self.configurar_fondo()
        
        # Frame principal centrado
        main_frame = tk.Frame(self.master, bg=self.COLOR_FONDO, padx=50, pady=50)
        # Usar expand=True para que el frame se centre en la pantalla
        main_frame.pack(expand=True) 

        # --- Logo ERM ---
        try:
            logo_img = Image.open(self.PATH_LOGO)
            logo_img = logo_img.resize((200, 200), Image.Resampling.LANCZOS if hasattr(Image, 'Resampling') else Image.LANCZOS)
            self.logo_image_tk = ImageTk.PhotoImage(logo_img)
            logo_label = tk.Label(main_frame, image=self.logo_image_tk, bg=self.COLOR_FONDO)
            logo_label.pack(pady=20)
        except FileNotFoundError:
             print(f"Advertencia: No se encontró el logo en {self.PATH_LOGO}. Continuando sin logo.")
        except Exception as e:
             print(f"Error al cargar el logo: {e}. Continuando sin logo.")


        titulo = tk.Label(main_frame, text="🎉 BIENVENIDO/A A LA TRIVIA ERM - LA GALA 🎉", 
                          font=self.FUENTE_TITULO, fg=self.COLOR_RESALTE, bg=self.COLOR_FONDO)
        titulo.pack(pady=20)

        instrucciones = tk.Label(main_frame, text="Responde unas preguntas para obtener tu guía de recorrido en la feria de ciencias.", 
                                 font=self.FUENTE_PREGUNTA, wraplength=800, fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO)
        instrucciones.pack(pady=10)

        # Botón con estética contrastante
        boton_iniciar = tk.Button(main_frame, text="🚀 INICIAR TRIVIA 🤖", command=self.mostrar_pregunta_erm, 
                                  bg="#4CAF50", fg="black", font=self.FUENTE_BOTON, relief=tk.RAISED, bd=5)
        boton_iniciar.pack(pady=40, ipadx=20, ipady=10)

    def mostrar_pregunta_erm(self):
        """Muestra la pregunta actual de la Sección 1/3."""
        if self.indice_pregunta >= len(self.preguntas):
            self.mostrar_diagnostico_edad()
            return

        self.limpiar_vista()
        self.configurar_fondo()
        
        pregunta_data = self.preguntas[self.indice_pregunta]
        self.respuesta_seleccionada.set(None) # Limpiar selección

        # Frame contenedor para centrar todo el contenido
        content_frame = tk.Frame(self.master, bg=self.COLOR_FONDO, padx=50, pady=50)
        content_frame.pack(expand=True)
        
        # Título de la sección
        tk.Label(content_frame, text=f"📍 PREGUNTA {self.indice_pregunta + 1}/{len(self.preguntas)}", 
                 font=self.FUENTE_PREGUNTA, fg=self.COLOR_RESALTE, bg=self.COLOR_FONDO).pack(pady=10)
        
        # Pregunta
        tk.Label(content_frame, text=pregunta_data["pregunta"], 
                 font=self.FUENTE_PREGUNTA, wraplength=900, justify=tk.CENTER, fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=20)

        # Opciones con RadioButtons (Centradas)
        opciones_frame = tk.Frame(content_frame, bg=self.COLOR_FONDO)
        opciones_frame.pack(pady=30)
        
        # Para forzar el centrado visual, usamos un ancho fijo y anchor="w" dentro de un frame centrado
        for i, opcion in enumerate(pregunta_data["opciones"]):
            rb = tk.Radiobutton(opciones_frame, text=opcion, variable=self.respuesta_seleccionada, value=opcion, 
                                font=self.FUENTE_OPCION, bg=self.COLOR_FONDO, fg=self.COLOR_TEXTO, selectcolor=self.COLOR_FONDO, # selectcolor hace que el circulito sea del mismo color que el fondo
                                anchor="w", width=70, justify=tk.LEFT, activebackground=self.COLOR_FONDO, 
                                activeforeground=self.COLOR_RESALTE) 
            rb.pack(pady=10, padx=20, fill='x')

        # Botón para la siguiente pregunta
        tk.Button(content_frame, text="SIGUIENTE ➡️", command=self.verificar_respuesta, 
                  bg="#004D99", fg="white", font=self.FUENTE_BOTON, relief=tk.RAISED, bd=5).pack(pady=40, ipadx=20, ipady=10)

    def verificar_respuesta(self):
        """Verifica la respuesta actual, actualiza la puntuación y avanza."""
        respuesta_usuario = self.respuesta_seleccionada.get()
        if not respuesta_usuario:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una opción antes de continuar.")
            return

        pregunta_data = self.preguntas[self.indice_pregunta]
        
        # Solo puntuamos si la pregunta original es de la ERM (las intercaladas no suman puntos)
        # Esto es una simplificación, ya que el arreglo de preguntas combinadas no distingue
        # si la pregunta es de ERM o Ética, pero podemos asumir que las preguntas originales
        # de la ERM son las que tienen índice par (0, 2, 4, etc.) en la lista combinada,
        # O simplemente comparar con las listas originales (método más robusto):
        es_pregunta_erm = any(d["pregunta"] == pregunta_data["pregunta"] for d in PREGUNTAS_ERM)

        if respuesta_usuario == pregunta_data["respuesta_correcta"]:
            if es_pregunta_erm:
                self.puntuacion_erm += 1
            # Opcional: reemplazar messagebox por un pop-up más estilizado de tkinter (más complejo),
            # pero por simplicidad se mantiene messagebox.
            tk.messagebox.showinfo("Resultado", "✅ ¡CORRECTO! +1 Conocimiento")
        else:
            tk.messagebox.showinfo("Resultado", f"❌ INCORRECTO. La respuesta era: {pregunta_data['respuesta_correcta']}")

        self.indice_pregunta += 1
        self.mostrar_pregunta_erm()

    def mostrar_diagnostico_edad(self):
        """Muestra el formulario para la edad (Sección 2)."""
        self.limpiar_vista()
        self.configurar_fondo()
        
        # Frame contenedor
        content_frame = tk.Frame(self.master, bg=self.COLOR_FONDO, padx=50, pady=50)
        content_frame.pack(expand=True)
        
        tk.Label(content_frame, text="🧭 SECCIÓN 2: ¿A QUÉ TRAYECTO PERTENECES?", 
                 font=self.FUENTE_TITULO, fg=self.COLOR_RESALTE, bg=self.COLOR_FONDO).pack(pady=30)
        
        tk.Label(content_frame, text="¡Estás a punto de obtener tu guía! Ingresa tu edad actual (solo el número):", 
                 font=self.FUENTE_PREGUNTA, fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=20)

        self.entrada_edad = tk.Entry(content_frame, font=self.FUENTE_TITULO, width=5, justify=tk.CENTER, 
                                     bg="#FFFFFF", fg="#000000", bd=5)
        self.entrada_edad.pack(pady=20)

        tk.Button(content_frame, text="✅ CONFIRMAR EDAD", command=self.calcular_trayecto, 
                  bg="#4CAF50", fg="black", font=self.FUENTE_BOTON, relief=tk.RAISED, bd=5).pack(pady=30, ipadx=20, ipady=10)

    def calcular_trayecto(self):
        """Procesa la edad ingresada y llama al resultado final."""
        try:
            edad = int(self.entrada_edad.get())
            if edad < 3 or edad > 100:
                messagebox.showerror("Error", "Por favor, ingresa una edad válida (entre 3 y 100).")
                return
            
            self.trayecto_asignado = determinar_trayecto(edad)
            tk.messagebox.showinfo("Trayecto Asignado", f"¡Con {edad} años, tu trayecto es: {self.trayecto_asignado}!")
            self.mostrar_resultado_final()
            
        except ValueError:
            messagebox.showerror("Error", "Entrada no válida. Por favor, ingresa un número entero para tu edad.")

    def mostrar_resultado_final(self):
        """Muestra el resultado y la recomendación (Sección 4)."""
        self.limpiar_vista()
        self.configurar_fondo()
        
        # Frame contenedor
        content_frame = tk.Frame(self.master, bg=self.COLOR_FONDO, padx=50, pady=50)
        content_frame.pack(expand=True)
        
        tk.Label(content_frame, text="✨ ¡RECORRIDO RECOMENDADO! ✨", 
                 font=self.FUENTE_TITULO, fg=self.COLOR_RESALTE, bg=self.COLOR_FONDO).pack(pady=20)

        if self.puntuacion_erm >= 8: 
            nivel_conocimiento = "FAN DE LA ERM (Alto)"
            recomendacion_extra = "Tecnología Sostenible y Ética (Visión de Futuro)"
            mensaje_final = "¡Felicidades, un verdadero fan de la ERM! Has demostrado un conocimiento estelar."
        elif self.puntuacion_erm >= 5: 
            nivel_conocimiento = "VISITANTE AVANZADO (Medio-Alto)"
            recomendacion_extra = "Historia y Valores de la ERM (Pilares Fundamentales)"
            mensaje_final = "¡Muy bien! Tienes una base sólida, pero siempre hay algo más que aprender. 🤔"
        else:
            nivel_conocimiento = "APRENDIZ DE ROBÓTICA (Bajo)"
            recomendacion_extra = "PequeBot/TrendKids (Fundamentos Visuales y Divertidos)"
            mensaje_final = "¡Genial! No te preocupes, la feria es el lugar perfecto para sumergirte en el mundo ERM. 👍"
            
        tk.Label(content_frame, text=mensaje_final, font=self.FUENTE_PREGUNTA, fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO, wraplength=800).pack(pady=10)
        
        # Resumen
        resumen_frame = tk.Frame(content_frame, bg=self.COLOR_FONDO)
        resumen_frame.pack(pady=20)
        
        tk.Label(resumen_frame, text=f"Puntuación ERM: {self.puntuacion_erm}/{self.total_preguntas_erm} ({nivel_conocimiento})", 
                 font=self.FUENTE_OPCION, fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=5)
                 
        tk.Label(resumen_frame, text=f"Trayecto Asignado: **{self.trayecto_asignado}**", 
                 font=self.FUENTE_PREGUNTA, fg=self.COLOR_RESALTE, bg=self.COLOR_FONDO).pack(pady=10)
        
        # Recomendación
        recomendacion = (
            f"1. **Punto de Partida Recomendado:** Comienza en el stand de **{self.trayecto_asignado}** "
            "para interactuar con desafíos de tu nivel.\n\n"
            f"2. **Punto de Interés:** Luego, visita el stand de **{recomendacion_extra}** "
            "para profundizar en los temas éticos y de valores de la Escuela y complementar tu recorrido."
        )
        
        tk.Label(content_frame, text="--- TU GUÍA DE RECORRIDO ---", 
                 font=("Courier New", 20, "underline"), fg=self.COLOR_TEXTO, bg=self.COLOR_FONDO).pack(pady=15)
        
        # Recuadro de recomendación con texto justificado y centrado
        tk.Label(content_frame, text=recomendacion, font=self.FUENTE_OPCION, wraplength=900, justify=tk.CENTER, 
                 fg="#000000", bg="#E0E0E0", bd=5, relief=tk.GROOVE).pack(pady=10, padx=20, ipady=15)
        
        tk.Button(content_frame, text="SALIR ❌", command=self.master.destroy, 
                  bg="#CC0000", fg="white", font=self.FUENTE_BOTON, relief=tk.RAISED, bd=5).pack(pady=40, ipadx=20, ipady=10)


# --- 3. INICIAR LA APLICACIÓN ---

if __name__ == "__main__":
    root = tk.Tk()
    app = TriviaApp(root)
    root.mainloop()