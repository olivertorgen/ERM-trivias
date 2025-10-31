import pygame.mixer
import time
import os

# --- CONFIGURACIÓN DE RUTAS DE ARCHIVOS DE SONIDO ---
# ¡IMPORTANTE! Reemplace estas rutas con la ubicación absoluta o relativa de sus archivos de audio locales.
# Asegúrese de que sus archivos de sonido estén en formato .WAV, .MP3 o .OGG.
# Si los archivos no se encuentran en la ruta especificada, el programa mostrará una ADVERTENCIA.

# Ruta de ejemplo para el sonido de victoria. ¡CÁMBIALA!
VICTORY_SOUND_PATH = 'ruta/a/su/sonido_victoria.wav' 
# Ruta de ejemplo para el sonido de error. ¡CÁMBIALA!
ERROR_SOUND_PATH = 'ruta/a/su/sonido_error.wav'

# --- INICIALIZACIÓN Y CARGA DE SONIDOS ---
def initialize_mixer():
    """
    Inicializa el mezclador de Pygame y carga los archivos de sonido.
    Retorna los objetos Sound para victoria y error.
    """
    try:
        # Inicializa Pygame Mixer (frecuencia estándar de 44100 Hz)
        pygame.mixer.init(frequency=44100, size=-16, channels=2)
        print("Mezclador de Pygame inicializado.")
    except pygame.error as e:
        print(f"Error al inicializar Pygame Mixer: {e}")
        return None, None

    victory_sound = None
    error_sound = None

    # Carga el sonido de victoria
    if os.path.exists(VICTORY_SOUND_PATH):
        try:
            victory_sound = pygame.mixer.Sound(VICTORY_SOUND_PATH)
            print(f"Sonido de victoria cargado desde: {VICTORY_SOUND_PATH}")
        except pygame.error as e:
            # Captura errores específicos al cargar formatos no soportados, etc.
            print(f"Error al cargar el sonido de victoria (Verifique el formato): {e}")
    else:
        print(f"ADVERTENCIA: Archivo de sonido de victoria no encontrado en: {VICTORY_SOUND_PATH}")

    # Carga el sonido de error
    if os.path.exists(ERROR_SOUND_PATH):
        try:
            error_sound = pygame.mixer.Sound(ERROR_SOUND_PATH)
            print(f"Sonido de error cargado desde: {ERROR_SOUND_PATH}")
        except pygame.error as e:
            # Captura errores específicos al cargar formatos no soportados, etc.
            print(f"Error al cargar el sonido de error (Verifique el formato): {e}")
    else:
        print(f"ADVERTENCIA: Archivo de sonido de error no encontrado en: {ERROR_SOUND_PATH}")
        
    return victory_sound, error_sound

# Carga los sonidos al inicio del script para que estén listos
VICTORY_SOUND, ERROR_SOUND = initialize_mixer()

def play_victory_sound():
    """Reproduce el sonido de victoria si está cargado."""
    if VICTORY_SOUND:
        # Reproduce el sonido una sola vez (loop=0)
        VICTORY_SOUND.play()
        print("Reproduciendo sonido de victoria...")
    else:
        print("No se puede reproducir el sonido de victoria: objeto Sound no cargado.")

def play_error_sound():
    """Reproduce el sonido de error si está cargado."""
    if ERROR_SOUND:
        # Reproduce el sonido una sola vez (loop=0)
        ERROR_SOUND.play()
        print("Reproduciendo sonido de error...")
    else:
        print("No se puede reproducir el sonido de error: objeto Sound no cargado.")

# --- DEMOSTRACIÓN DEL USO ---
if __name__ == "__main__":
    # La demo solo se ejecuta si al menos un sonido se cargó con éxito
    if VICTORY_SOUND or ERROR_SOUND:
        print("\n--- INICIO DE DEMOSTRACIÓN ---")
        
        # 1. Prueba el sonido de victoria
        play_victory_sound()
        # Espera 2 segundos para permitir que el sonido se reproduzca antes de continuar
        time.sleep(2) 
        
        # 2. Prueba el sonido de error
        play_error_sound()
        time.sleep(2)
        
        print("--- DEMOSTRACIÓN FINALIZADA ---")
    else:
        print("\nEl programa no pudo cargar ningún archivo de sonido. Por favor:")
        print("1. Instale 'pygame': pip install pygame")
        print("2. Verifique que las rutas de archivo en las variables VICTORY_SOUND_PATH y ERROR_SOUND_PATH sean correctas.")

    # Cierra el mezclador de Pygame al finalizar el programa principal
    pygame.mixer.quit()
