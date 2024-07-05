import pyautogui as py
import time

time.sleep(1800)

py.press('f11')
py.keyDown('ctrl')
py.press ('tab')
py.keyUp('ctrl')

time.sleep(3)

py.press('f5')

py.moveTo(800,500) #botao de login
py.leftClick()

time.sleep(3)

py.moveTo(50,540) #botao do relatório login
py.leftClick()

time.sleep(3)

py.press('f11')
py.moveTo(45,200) 
time.sleep(5)
py.leftClick()
#py.press('esc') # reltório em tela cheia


time.sleep(1740)

py.press('f11')
py.keyDown('ctrl')
py.press ('tab')
py.keyUp('ctrl')
time.sleep(3)
py.press('f11')

