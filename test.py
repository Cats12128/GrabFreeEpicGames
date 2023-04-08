import win32gui, win32con
from time import sleep
import webbrowser as web
import pygetwindow as window
import pyautogui as p
import subprocess
import cv2 as cv
import numpy as np
from GrabFreeEpicGame import DrawRectangle


fni = "images\FreeNowImage.png"
c=.95
sleep(.5)
while True:
    print(f"c is {c}")
    locations = p.locateAllOnScreen(fni, confidence=c)
    locations = list(locations)
    c -= .05
    if locations:
        print(f"locations found: {locations}")
        print(f'c is {c}')
        DrawRectangle(locations)
        quit()
    elif c==0:
        print("c is 0, no matches")
        quit()