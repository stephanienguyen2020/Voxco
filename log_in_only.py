import pyautogui as pag
import time
import random

time.sleep(3)
#Click on Safari
pos_safari = pag.position(477,1068)
pag.click(pos_safari)
pag.typewrite('https://us1intweb.voxco.com/Voxco.Agent/Login.aspx?ReturnUrl=%2fVoxco.Agent%2fFrameLayout.aspx')
pag.press('enter')
time.sleep(5)

#Login
pos_id = pag.position(919,373)
pag.click(pos_id)
pag.typewrite('tn2510')
time.sleep(2)

pos_bypass = pag.position(918, 651)
pag.click(pos_bypass)

pos_pass=pag.position(840, 409)
pag.click(pos_pass)
pag.typewrite('Hoangtu259*..1234567')
time.sleep(1)

pos_code=pag.position(842, 445)
pag.click(pos_code)
pag.typewrite('CUSSW')
time.sleep(2)

pos_login=pag.position(851, 499)
pag.click(pos_login)
time.sleep(5)
