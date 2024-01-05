import pyautogui as pag
import time
import random

def new_call_button():
    pos_newcall = pag.position(202, 258)
    pag.click(pos_newcall)
    time.sleep(2)

#Click on Safari
def click_safari():
    time.sleep(3)
    pos_safari = pag.position(477,1068)
    pag.click(pos_safari)
    time.sleep(2)

#Pick Survey 2:
def pick_survey2():
    pos_survey2=pag.position(487, 352)
    pag.click(pos_survey2)
    time.sleep(2)

    pos_accept=pag.position(1656, 205)
    pag.click(pos_accept)
    time.sleep(4)

#Pick Test Survey:
def pick_TS():
    pos_survey2_test=pag.position(486, 376)
    pag.click(pos_survey2_test)
    time.sleep(2)
    pos_accept=pag.position(1656, 205)
    pag.click(pos_accept)
    time.sleep(4)
    
#Mach option:
def select_mach():
    sleep_mach = random.randint(160,230)
    time.sleep(sleep_mach)

    x, y = pag.locateCenterOnScreen("Images/Mach.png", confidence =0.8)
    pag.moveTo(x,y, 1)
    pag.click()
    # pos_mach=pag.position(980, 312)
    # pag.click(pos_mach)
    time.sleep(3)

def next1():
    pos_next1=pag.position(813,900)
    pag.click(pos_next1)
    time.sleep(3)

def unclick_other():
    pos_other=pag.position(234,402)
    pag.click(pos_other)
    time.sleep(5)

def next2():
    pos_next2=pag.position(817, 774)
    pag.click(pos_next2)
    time.sleep(3)

def select_full(): #Voicemail full (cannot leave message)
    sleep_full = random.randint(160,230)
    time.sleep(sleep_full)
    
    pos_full=pag.position(976, 292)
    pag.click(pos_full)
    time.sleep(3)

def select_ring(): #phone just rings, no machine, mostly landlind
    sleep_ring = random.randint(160,230)
    time.sleep(sleep_ring)
    
    pos_ring=pag.position(893, 355)
    pag.click(pos_ring)
    time.sleep(3)

def select_out(): #Out of service
    sleep_out = random.randint(160,230)
    time.sleep(sleep_out)
    
    pos_out=pag.position(1125, 291)
    pag.click(pos_out)
    time.sleep(3)

def select_ok(): #OK connection
    sleep_ok = random.randint(160,230)
    time.sleep(sleep_ok)
    
    pos_ok=pag.position(1021, 273)
    pag.click(pos_ok)
    time.sleep(3)

#Hang option:
def select_hang():
    sleep_hang = random.randint(160,230)
    time.sleep(sleep_hang)
    
    pos_hang=pag.position(1163, 250)
    pag.click(pos_hang)
    time.sleep(3)

def select_check(): #SP wants to do it online and already have the link
    sleep_check = random.randint(160,230)
    time.sleep(sleep_check)
    
    pos_check=pag.position(980, 338)
    pag.click(pos_check)
    time.sleep(3)


def full_mach(): #from new call to full machine
    new_call_button()
    select_mach()
    next1()
    unclick_other()
    next2()

def full_ring(): #from new call to full ring
    new_call_button()
    select_ring()
    next1()
    unclick_other()
    next2()

def full_out(): #from new call to full out
    new_call_button()
    select_out()
    next1()
    unclick_other()
    next2() 

def log_in():
    #Open Voxco
    pag.typewrite('https://us1intweb.voxco.com/Voxco.Agent/Login.aspx?ReturnUrl=%2fVoxco.Agent%2fFrameLayout.aspx')
    pag.press('enter')
    time.sleep(5)

    #Login id
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

    #Press login
    pos_login=pag.position(851, 499)
    pag.click(pos_login)
    time.sleep(5)