import pyautogui as pag
import time
import random

time.sleep(3)
#Click on Safari
pos_safari = pag.position(477,1068)
pag.click(pos_safari)

#Survey 2:
pos_survey2=pag.position(487, 352)
pag.click(pos_survey2)
time.sleep(2)

pos_accept=pag.position(1656, 205)
pag.click(pos_accept)
time.sleep(4)

# #New Call
n_mach = random.randint(13,20) #Random 13-20 cuộc gọi bị mach
for i in range (n_mach):
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
