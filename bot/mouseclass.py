import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

class Mouse:

    def log_in_vpn(self):
        pyautogui.moveTo(1143, 89, duration=0.25)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(821, 307, duration=0.25)
        pyautogui.click()
        pyautogui.typewrite('theweekencl')
        pyautogui.moveTo(817, 385, duration=0.25)
        pyautogui.click()
        pyautogui.typewrite('Cn57hksWy8xMTAe')
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.moveTo(907, 42, duration=0.25)
        pyautogui.click()
        pyautogui.moveTo(311, 42, duration=0.25)
        pyautogui.click()
        