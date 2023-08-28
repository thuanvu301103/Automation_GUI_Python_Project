import automove
from importmodule import *

# ----- Start working with first 15 countries
for i in range(15):
    automove.move_1(i)
    automove.move_2()

# ----- For the rest countries
pyautogui.moveTo (1213, 293 + 15*33)
for i in range (48):
    automove.move_3 ()
    automove.move_2 ()

# Scroll Urban to the start of list
pyautogui.scroll (33*(48+16))

# Close UrrbanVPN
pyautogui.moveTo (1355, 174)
pyautogui.leftClick()




