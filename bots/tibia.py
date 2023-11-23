import pyautogui
import time as tempo
def right_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click(button='right')

def left_click(x, y, clicks=1):
    pyautogui.moveTo(x, y)
    pyautogui.click(clicks=clicks)
    
coord_x = 1275
coord_y = 285
coord_z = 520
coord_w = 503
coord_s = 898
coord_p = 535
coord_q = 292
coord_u = 472
coord_t = 918
coord_v = 335
aux=0
auxi=int(input("quantas vezes quer fazer?"))
tempo.sleep(5)
while True:
    aux+=1
    if aux==auxi:
        break
    else:
        right_click(coord_x, coord_y)
        tempo.sleep(1/4)
        left_click(coord_z, coord_w)
        tempo.sleep(1/4)
        right_click(coord_x, coord_y)
        tempo.sleep(1/4)
        left_click(coord_s, coord_p)
        tempo.sleep(1/4)
        right_click(coord_x, coord_y)
        tempo.sleep(1/4)
        left_click(coord_q, coord_u)
        tempo.sleep(1/4)
        right_click(coord_x, coord_y)
        tempo.sleep(1/4)
        left_click(coord_t, coord_v)
        tempo.sleep(1/4)
        right_click(1199, 576)
        tempo.sleep(1/4)
        pyautogui.press('f4') 
        tempo.sleep(1/4)
