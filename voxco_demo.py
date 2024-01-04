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
pag.typewrite('add_your_username') #add your correct username
time.sleep(2)

pos_bypass = pag.position(918, 651)
pag.click(pos_bypass)

pos_pass=pag.position(840, 409)
pag.click(pos_pass)
pag.typewrite('add_your_password') #add your correct password
time.sleep(1)

pos_code=pag.position(842, 445)
pag.click(pos_code)
pag.typewrite('add_your_code') #add your correct code
time.sleep(2)

pos_login=pag.position(851, 499)
pag.click(pos_login)
time.sleep(5)

#Survey 1:

#Survey 2:
# pos_survey2=pag.position(487, 352)
# pag.click(pos_survey2)
# time.sleep(2)

# pos_accept=pag.position(1656, 205)
# pag.click(pos_accept)
# time.sleep(4)

# Test Survey
pos_survey2_test=pag.position(486, 376)
pag.click(pos_survey2_test)
time.sleep(2)
pos_accept=pag.position(1656, 205)
pag.click(pos_accept)
time.sleep(4)

# #New Call
pos_newcall=pag.position(202, 258)
pag.click(pos_newcall)
time.sleep(2)

#Mach
sleep_mach = random.randint(170,230)
time.sleep(sleep_mach)
pos_mach=pag.position(980, 312)
pag.click(pos_mach)
time.sleep(3)

#Next
pos_next1=pag.position(813,900)
pag.click(pos_next1)
time.sleep(3)

#Unclick Other
pos_other=pag.position(234,402)
pag.click(pos_other)
time.sleep(5)

#Next 2
pos_next2=pag.position(817, 774)
pag.click(pos_next2)
time.sleep(3)

#Mess
#Start Survey
#Relink: Type: SP wants to do it online (wait time: 5s)
#Check: type: SP has it in their email and will do it later on their own (wait time 7s)