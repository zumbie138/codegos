import pyautogui
import time as tempo
import keyboard

def right_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click(button='right')
    
while True:
    if keyboard.is_pressed('ENTER'):
        print('loop iniciado')
        while True:
            if keyboard.is_pressed('space'):
                print('loop pausado')
                break
            right_click(675,296)
            print('botao direito precionado')
            tempo.sleep(5)
    elif keyboard.is_pressed('ESC'):
        print('loop interrompido')
        break