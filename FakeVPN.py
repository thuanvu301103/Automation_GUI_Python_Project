import pyautogui
import subprocess
from pywinauto.application import Application
import time
import win32gui, win32process, win32con
import os
import signal
import random

# ----- Surfweb classes

# abtract class
class browser:
    # numacc: int - number of account
    # fdir: string - dir file to get link
    def __init__(self, numacc):
        self.numacc = numacc
        # self.fdir = fdir
    def search (self, content):
        # move to search bar
        pyautogui.hotkey('alt', 'd') 
        # write content in search bar
        pyautogui.write(content)
        # press enter to searh
        pyautogui.press('enter')

# Class A: pubiza.com
class webA (browser):
    def surf (self):
        for i in range (1, self.numacc + 1):
            # Each account choose one link
            with open(f"E:\\Business\\FakeVPN\\src\\pubiza{i}.txt", "r") as file:
                lines = file.read().splitlines()
                link = random.choice(lines)
            self.search (link)
            # create new tab
            pyautogui.hotkey('ctrl', 't')
            # wait for browser to load
            time.sleep(15)
        # Click button 1: "1/2 Get link"
        for i in range (1, self.numacc + 1):
            # switch tab
            pyautogui.hotkey('ctrl', f"{i}")
            pyautogui.moveTo (970, 577)
            pyautogui.leftClick()
            time.sleep(15)
        # Click button 2-3-4: "SIRADAKI" (3 times)
        for j in range (3):
            for i in range (1, self.numacc + 1):
                # switch tab
                pyautogui.hotkey('ctrl', f"{i}")
                # find button
                pyautogui.hotkey('ctrl', 'f')
                pyautogui.write("RADAKI")
                pyautogui.press('enter')
                pyautogui.moveTo (952, 610)
                pyautogui.leftClick()
                pyautogui.leftClick()
                time.sleep(15)
        # Click button 5: "Link Git" to slit windown
        for i in range (1, self.numacc + 1):
            pyautogui.moveTo (954, 341)
            pyautogui.rightClick()
            for j in range (4):
                pyautogui.press('down')
            pyautogui.press('enter')
            time.sleep(15)
        # Click button 6: "Get Link"
        for i in range (1, self.numacc + 1):
            pyautogui.moveTo (1455, 455)
            pyautogui.leftClick()
            time.sleep(15)
        # close curent none used tab
        pyautogui.hotkey('ctrl', 'shift', 'w')

# ----- for make sure window show up on the top
def showwd(name, x, y, cx, cy):
    # name: string - name of the windown
    # x,y: int - position of windown
    # cx, cy: int - sizze of windown 
    windowList = []
    win32gui.EnumWindows(lambda hwnd, windowList: windowList.append((win32gui.GetWindowText(hwnd),hwnd)), windowList)
    # print (windowList)
    cmdWindow = [i for i in windowList if name in i[0]]
    win32gui.SetWindowPos(cmdWindow[0][1],win32con.HWND_TOPMOST,x,y,cx,cy,0)

### ----- Start automation moves

# ----- Move 1: 
def move_1 (i: int):
    # i: int - variaty in each move 
    # make sure UrbanVPN windown is always on top
    showwd ("UrbanVPN", 548, 155, 100, 100)
    # Move mouse to choose country
    pyautogui.moveTo (1213, 293 + i*33)
    pyautogui.leftClick()
    # Run VPN (click Run)
    pyautogui.moveTo (797, 533)
    pyautogui.leftClick()
    time.sleep(15)
# ----- No else move for move 1

# ----- Move 2:
def move_2 ():
    # OpenBrower
    p1 = subprocess.Popen(["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"])
    p1.wait()
    time.sleep(2)
    showwd ("New tab - Personal - Microsoft\u200b Edge",0,0, 1914, 1011)
    A.surf()
    # Then need to disable VPN
    pyautogui.moveTo (797, 533)
    pyautogui.leftClick()
# ----- No else move for move 2

# ----- Move 3:
def move_3 ():
    showwd ("UrbanVPN",548,155, 100, 100)
    pyautogui.moveTo (1213, 293 + 15*33)
    pyautogui.scroll (-33)
    pyautogui.leftClick()
    # Run VPN (click Run)
    pyautogui.moveTo (797, 533)
    pyautogui.leftClick()
    time.sleep(15)
# ----- No else move for move 3

### -----   Start automation

# ----- Open Windown: UrbanVPN
p = subprocess.Popen(["C:\\Program Files\\UrbanVPN\\bin\\urbanvpn-gui.exe"])
# Must wait for ủbanVPN to open
p.wait()
A = webA(1)

# ----- Start working with forst 15 countries
for i in range(15):
    # Move 1: Open and choose Country from  UrrbanVPN
    move_1 (i)
    # Move 2: Surfing web
    move_2 ()

# For the rest countries
pyautogui.moveTo (1213, 293 + 15*33)
for i in range (48):
    move_3 ()
    # Move 2: Surf web
    move_2 ()

# Scroll Urban to the start of list
pyautogui.scroll (33*(48+16))

# Close UrrbanVPN
pyautogui.moveTo (1355, 174)
pyautogui.leftClick()




