import pyautogui
import os

os.system("pip install pyautogui")

print("Press CTRL+C in the window to stop spamming.")

spam = input("What would you like to spam? ")

pyautogui.alert("Press OK to start spamming.")

while True:
    list_ = list(spam)
    for char in list_:
        pyautogui.press(char)
    pyautogui.press('return')
    print('output')
