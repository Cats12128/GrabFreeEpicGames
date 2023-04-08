import win32gui, win32con
from time import sleep
import webbrowser as web
import pygetwindow as window
import pyautogui as p
import subprocess
import cv2 as cv
import numpy as np
from GrabFreeEpicGame import DrawRectangle
from GrabFreeEpicGame import *

tab_presses = 45
sleep(1)
for press in range(tab_presses):
    sleep(.05)
    pyautogui.press('tab')
pyautogui.press("enter")