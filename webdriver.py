from importmodule import *
pyautogui.FAILSAFE = False

# ----- abtract class
class web_driver: 

    # numacc: int - numbers of account website
    def __init__(self, numacc):
        self.numacc = numacc

# ----- first website: pubiza.com
class web_driverA (web_driver):

    def surf (self, numacc):
        
        # Each account choose randomly one link
        with open(f"E:\\Business\\src\\pubiza{numacc}.txt", "r") as file:
            lines = file.read().splitlines()
            link = random.choice(lines)

        # search link
        pyautogui.hotkey('alt', 'd') 
        pyautogui.typewrite(link, interval = 0.05)
        pyautogui.press('enter')
        time.sleep(15)

        # Click button 1: "1/2 GetLink"
        pyautogui.moveTo (957, 482, 2.2)
        pyautogui.leftClick()
        time.sleep(15)
        
        # Click button 2: "SIRADAKi"
        for i in range (1,4):
            pyautogui.moveTo (560, 300, 1)
            pyautogui.tripleClick ()
            pyautogui.hotkey('ctrl', 'c')
            flag = pyperclip.paste()
            if flag != "Linke Git":
                print ("True" if str(flag) == "Linke Git" else "False")
                # find button
                pyautogui.hotkey('ctrl', 'f')
                pyautogui.write("RADAKI")
                pyautogui.press('enter')
                pyautogui.moveTo (957, 541)
                pyautogui.leftClick()
                time.sleep(15)
            else: break

        # Click button 3: "Linke Git"
        pyautogui.moveTo (966, 297)
        pyautogui.leftClick()
        time.sleep(15)
        
        # Click button 4: "Get Link"
        pyautogui.moveTo (963, 451)
        pyautogui.leftClick()
        time.sleep(15)
        
        # close curent none used tab
        #pyautogui.hotkey('ctrl', 'shift', 'w')
        pyautogui.moveTo (1887, 39)
        pyautogui.leftClick()