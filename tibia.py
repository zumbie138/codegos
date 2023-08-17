import pyautogui

coord_x = 198
coord_y = 243
coord_z = 180
coord_w = 280
coord_s = 1128
coord_p = 690
coord_q = 107

def right_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click(button='right')

def left_click(x, y, clicks=1):
    pyautogui.moveTo(x, y)
    pyautogui.click(clicks=clicks)

right_click(coord_x, coord_y)

left_click(coord_z, coord_w)

right_click(coord_x, coord_y)

left_click(coord_z, coord_s)

right_click(coord_x, coord_y)

left_click(coord_p, coord_q)

right_click(coord_x, coord_y)

right_click(665, 350)
right_click(665, 350)
right_click(665, 350)
