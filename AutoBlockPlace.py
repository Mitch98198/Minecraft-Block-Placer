import pyautogui
import time

file_path = open("placeBlocks.txt")
print("You have 3 seconds to switch to Minecraft")
time.sleep(5)
for line in file_path:
    command = line.strip()
    print(command)
    pyautogui.press("t")
    pyautogui.write(command)
    pyautogui.press("enter")
