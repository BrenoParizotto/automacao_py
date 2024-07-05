import pyautogui as py
import time

py.moveTo(20, 120) ## abrir chrome
py.leftClick()
py.leftClick()
time.sleep(5)
py.write("https://www.intecbi.com.br/ilumisol/paineis/cd01/faturamento/")
py.press('enter')
time.sleep(3)

py.keyDown('ctrl') #duplicar pagina
py.press('l')
py.keyUp('ctrl')
time.sleep(3)
py.keyDown('alt')
py.press('enter')
py.keyUp('alt')
time.sleep(3)


py.keyDown('ctrl') 
py.press('l')
py.keyUp('ctrl')
py.write("https://intecbi.com.br/indicadores/")
py.press('enter')
time.sleep(3)


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
