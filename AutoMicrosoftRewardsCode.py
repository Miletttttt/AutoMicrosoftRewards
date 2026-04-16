import pyautogui
import time 
import pyperclip
import random

# =====================
# Entrar no REWARDS
# =====================

pyautogui.press("win")
time.sleep(1)
#muda para o teu navegador!
pyautogui.write("brave")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("https://rewards.bing.com")
pyautogui.press("enter")

# =====================
# Resgatar CONJUNTO DIÁRIO
# =====================

time.sleep(2)

pyautogui.click(x=450, y=450)
time.sleep(.75)
pyautogui.scroll(-300)
time.sleep(1)
pyautogui.click(x=550, y=600)
time.sleep(1)
pyautogui.click(x=100, y=18)
time.sleep(1)
pyautogui.click(x=1150,y=650)
time.sleep(1)
pyautogui.click(x=100, y=18)
time.sleep(1)
pyautogui.click(x=1550,y=650)