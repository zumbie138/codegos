import pyautogui
import time as tempo
coord_x=908
coord_y=575

def right_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click(button='right')
    tempo.time(1/4)

def left_click(x, y, clicks=1):
    pyautogui.moveTo(x, y)
    pyautogui.click(clicks=clicks)
    tempo.time(1/4)
    
for in range(4):
    for in range(15):
        right_click
        left_click