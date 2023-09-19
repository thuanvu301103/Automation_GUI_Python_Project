from importmodule import *
import function
from webdriver import *

# ----- move 1:
def move_1 (i: int):
    # i: int - variaty in each move 
    p = subprocess.Popen(["C:\\Program Files\\UrbanVPN\\bin\\urbanvpn-gui.exe"])
    p.wait()

    function.showwd ("UrbanVPN", 548, 155, 100, 100)
    time.sleep(5)
    # Move mouse to choose country
    pyautogui.moveTo (1213, 293 + i*33)
    pyautogui.leftClick()
    # Run VPN (click Run)
    pyautogui.moveTo (797, 533)
    pyautogui.leftClick()
    time.sleep(15)

    # Close Urrban VPN window:
    pyautogui.moveTo (1358, 181)
    pyautogui.leftClick()

# ----- no else move for move 1

# ----- move 2: 
def move_2 ():
    # Open browser (Edge)
    p1 = subprocess.Popen(["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"])
    p1.wait()
    time.sleep(5)
    function.showwd ("New tab - Personal - Microsoft\u200b Edge",0,0, 1914, 1011)
    
    # Surf web
    web_A = web_driverA(1)
    for i in range (1, web_A.numacc + 1):
        cnt = web_A.surf(i)
        if cnt == "continue":
            continue
    
    # Disable VPN
    p = subprocess.Popen(["C:\\Program Files\\UrbanVPN\\bin\\urbanvpn-gui.exe"])
    p.wait()

    function.showwd ("UrbanVPN", 548, 155, 100, 100)
    pyautogui.moveTo (797, 533)
    pyautogui.leftClick()

# ----- no else move for move 2

# ----- move 3:
def move_3 ():
    p = subprocess.Popen(["C:\\Program Files\\UrbanVPN\\bin\\urbanvpn-gui.exe"])
    p.wait()

    function.showwd ("UrbanVPN",548,155, 100, 100)
    time.sleep(5)
    pyautogui.moveTo (1213, 293 + 15*33)
    pyautogui.scroll (-33)
    pyautogui.leftClick()
    # Run VPN (click Run)
    pyautogui.moveTo (797, 533)
    pyautogui.leftClick()
    pyautogui.moveTo (1358, 181)
    pyautogui.leftClick()
    time.sleep(15)

# ----- No else move for move 3