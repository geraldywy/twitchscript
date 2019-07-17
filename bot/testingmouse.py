import pyautogui
from mouseclass import Mouse

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

mouse = Mouse()
mouse.log_in_vpn()

print('all done')