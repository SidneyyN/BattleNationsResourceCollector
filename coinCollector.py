import pyautogui 
import os
import time
import pyscreeze
pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True

# Get the absolute path to the coin image
scriptDir = os.path.dirname(os.path.abspath(__file__))
coinImagePath = os.path.join(scriptDir, "resourceImages", "image.png")

print(f"Looking for image at: {coinImagePath}")
print(f"Image exists: {os.path.exists(coinImagePath)}")

positions = []

try:
    start = time.time()
    for pos in pyautogui.locateAllOnScreen(coinImagePath, confidence=0.8):
        positions.append(pos)
    end = time.time()
    print("It took", end - start, "seconds!")
except pyscreeze.ImageNotFoundException:
    print("Coin image not found on screen")

print("We have successfully stored all the coordinates")

for pos in positions:
    coord = (pos[0], pos[1])
    print(coord)
    pyautogui.click(pos[0], pos[1])
print("Coins are all collected")