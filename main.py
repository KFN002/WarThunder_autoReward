import subprocess
import os

import schedule as schedule

import time
import pyautogui
import datetime
from ctypes import Structure, windll, c_uint, sizeof, byref
import sys
import ctypes


def get_reward():
    warthunder()
    killProcess()
    '''
    shutdown()
    '''


def warthunder():
    os.startfile("D:\SteamLibrary\steamapps\common\War Thunder\launcher.exe")  # Path to launcher.exe here
    time.sleep(60)
    pyautogui.press('enter')
    time.sleep(60)
    pyautogui.press('enter')
    time.sleep(100)
    pyautogui.press('enter')


def killProcess():
    os.system("taskkill /f /im aces.exe")
    time.sleep(1)


def shutdown():
    subprocess.call(["shutdown", "/s"])


schedule.every(25).hours.do(get_reward)

while True:
    schedule.run_pending()
