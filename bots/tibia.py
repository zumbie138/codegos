import pyautogui
import time as tempo
import keyboard

def right_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click(button='right')

def left_click(x, y, clicks=1):
    pyautogui.moveTo(x, y)
    pyautogui.click(clicks=clicks)
    

while True:
    if keyboard.is_pressed('ENTER'):
        while True:
            if keyboard.is_pressed('space'):
                break
            right_click(675,296)
            tempo.sleep(0.5)
            # left_click(755, 296)
            left_click(705, 296)
            tempo.sleep(0.5)
    elif keyboard.is_pressed('ESC'):
        break