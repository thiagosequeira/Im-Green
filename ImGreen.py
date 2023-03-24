import time
import random
import keyboard
import pyautogui

# Función para cerrar el programa
def exit_program():
    global running
    running = False

# Configurar la combinación de teclas y clic del mouse para salir del programa
pyautogui.alert('Presiona la tecla "Esc" para cerrar el programa.')
keyboard.add_hotkey('esc', lambda: exit_program())

# Define la función para enviar una letra aleatoria
def send_random_key():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    random_letter = random.choice(letters)
    keyboard.press(random_letter)
    keyboard.release(random_letter)

# Obtiene el tamaño de la pantalla
screen_width, screen_height = pyautogui.size()

# Define los límites del área de movimiento
x_min = screen_width // 3
x_max = (screen_width // 3) * 2
y_min = screen_height // 3
y_max = (screen_height // 3) * 2

# Repite la función cada 10 segundos
running = True
while running:
    try:
        send_random_key()
        # Obtiene la posición actual del cursor
        current_x, current_y = pyautogui.position()
        # Mueve el cursor a una posición aleatoria dentro de los límites del área de movimiento
        new_x = random.randint(x_min, x_max)
        new_y = random.randint(y_min, y_max)
        pyautogui.moveTo(new_x, new_y, duration=0.25)
        time.sleep(10)
    except Exception as e:
        print(f"Error: {e}")