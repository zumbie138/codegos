import pyautogui
import keyboard
from time import sleep

while True:
    if keyboard.is_pressed('ENTER'):
        x, y = pyautogui.position()
        print(f"Coordenadas: ({x}, {y})")
        sleep(1)
    elif keyboard.is_pressed('ESC'):
        break