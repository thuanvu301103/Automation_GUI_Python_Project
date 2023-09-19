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

        # open new pirate tab
        pyautogui.hotkey('ctrl', 'shift', 'n')
        time.sleep(5)
        function.showwd ('New InPrivate tab - [InPrivate] - Microsoft\u200b Edge',0,0, 1914, 1011)
        pyautogui.hotkey('ctrl', 't')
        #function.showwd ("Lnk.parts - [InPrivate] - Microsoft\u200b Edge",0,0, 1914, 1011)

        # search link
        pyautogui.hotkey('alt', 'd') 
        pyautogui.typewrite(link, interval = 0.05)
        pyautogui.press('enter')
        time.sleep(15)

        # Click button 1: "1/2 GetLink"
        pyautogui.moveTo (970, 577, 2.2)
        pyautogui.leftClick()

        button = input("Type c if continue, typ n for next loop: ")
        while not button in ["c", "n"]:
            button = input("Type c if continue, typ n for next loop: ")
        if button == "n":
            return "continue"
        

        function.showwd ('Dünyanın Gelmiş Geçmiş En Güzel 7 Kadını - Sosyal Eğlence Platformu and 1 more page - [InPrivate] - Microsoft\u200b Edge',0,0, 1914, 1011)
        time.sleep(15)
        # Click button 2: "SIRADAKi"
        for i in range (1,4):
            pyautogui.moveTo (724, 339, 1)
            pyautogui.tripleClick ()
            pyautogui.hotkey('ctrl', 'c')
            flag = pyperclip.paste()
            if flag != "Linke Git":
                print ("True" if str(flag) == "Linke Git" else "False")
                # find button
                pyautogui.hotkey('ctrl', 'f')
                pyautogui.write("RADAKI")
                pyautogui.press('enter')
                pyautogui.moveTo (945, 587)
                pyautogui.leftClick()
                time.sleep(15)
            else: break

        # Click button 3: "Linke Git"
        pyautogui.moveTo (954, 341)
        pyautogui.leftClick()
        time.sleep(15)
        
        # Click button 4: "Get Link"
        pyautogui.moveTo (968, 507)
        pyautogui.leftClick()
        time.sleep(15)
        
        # close curent none used tab
        #pyautogui.hotkey('ctrl', 'shift', 'w')
        pyautogui.moveTo (1895, 31)
        pyautogui.leftClick()
        function.showwd ("New tab - Personal - Microsoft\u200b Edge",0,0, 1914, 1011)
        pyautogui.moveTo (1895, 31)
        pyautogui.leftClick()

        return "nill"