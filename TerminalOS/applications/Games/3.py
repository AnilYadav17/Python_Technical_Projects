import pyautogui
import time

print("Starting in 5 seconds...")
time.sleep(5)

print("Screen Size:", pyautogui.size())

print("Current Mouse Position:", pyautogui.position())

pyautogui.moveTo(500, 300, duration=2)

pyautogui.click()

pyautogui.doubleClick()

pyautogui.rightClick()

pyautogui.scroll(-500)

pyautogui.moveRel(200, 100, duration=1)

print("Demo Finished")
