import pyautogui 
import os
pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True

# Get the absolute path to the coin image
scriptDir = os.path.dirname(os.path.abspath(__file__))
coinImagePath = os.path.join(scriptDir, "resourceImages", "image.png")

print(f"Looking for image at: {coinImagePath}")
print(f"Image exists: {os.path.exists(coinImagePath)}")

try:
    result = pyautogui.locateCenterOnScreen(coinImagePath, confidence=0.5)
    print(f"First match found at: {result}")
    pyautogui.click(result[0], result[1])
except pyautogui.ImageNotFoundException:
    print("Coin image not found on screen")

# print("\nAll coin locations:")
# for pos in pyautogui.locateAllOnScreen(coinImagePath):
#     print(pos)

