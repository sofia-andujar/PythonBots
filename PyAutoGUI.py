import time
import pyautogui as bot

# Getting familiar with PyAutoGUI
# https://pyautogui.readthedocs.io/en/latest/

print('Bot using PyAutoGUI'.center(50,'-'))
time.sleep(1)

print(bot.size())
print(bot.position())
bot.moveTo(1,1079)
bot.click()
bot.press('esc')

bot.alert('This is an alert','ALERT','okay chill')