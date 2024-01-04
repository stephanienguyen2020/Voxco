import pyautogui as pag
import time

for i in range(3):
    time.sleep(3)
    #pos = pag.position()
    #print(pos)

    #New Call
    pos_newcall=pag.position(202, 258)
    pag.click(pos_newcall)
    time.sleep(2)

    #Mach
    #time.sleep(180) #random giua 170-230s
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