import pyautogui
import cv2 as cv
import numpy as np
import webbrowser as web
from time import sleep
import subprocess
import pygetwindow

#variables
url = "https://store.epicgames.com/en-US/"
filepath = "Z:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"
windowname = "epic"
currentGame = 0
maxNumOfGames = 2
pyautogui.FAILSAFE = True

#images to match
FREENOWIMAGE = "images\FreeNowImage.png"
GETIMAGE = "images\GetImage.png"
PLACEORDERIMAGE = "images\PlaceOrderImage.png"
INLIBRARYIMAGE = "images\InLibraryImage.png"

def FindClick(image):
    while True:
        sleep(2)
        getLoc = pyautogui.locateOnScreen(image, confidence=.95)
        alreadyInLibrary = pyautogui.locateOnScreen(INLIBRARYIMAGE, confidence=.95)
        if getLoc:
            #x_val = getLoc.left + (getLoc.width/2)
            #y_val = getLoc.top + (getLoc.height/2)
            pyautogui.click(getLoc.center())
            return print(f'Clicked on location matching {image}')
        elif alreadyInLibrary:
            return print('Game already redeemed')
        

def DrawRectangle(LocAllImg):
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    top_left = (LocAllImg[0].left, LocAllImg[0].top)
    bottom_right = (LocAllImg[0].left + LocAllImg[0].width, LocAllImg[0].top + LocAllImg[0].height)
    cv.rectangle(screenshot,top_left, bottom_right, color=(0,255,0), thickness=2, lineType=cv.LINE_4)
    cv.imshow("Screenshot", screenshot)
    cv.waitKey(0)

def openUrlInBrowserAndMax(url):
    web.open(url, new=0, autoraise=True)
    sleep(1)
    chromeWindow = pygetwindow.getWindowsWithTitle("chrome")[0]
    chromeWindow.maximize()

def openApplication(filepath, windowname):
    subprocess.call(filepath)
    sleep(1)
    window = pygetwindow.getWindowsWithTitle(windowname)[0]
    window.maximize()

def moveCursorToCenter():
    screenSizeX = pyautogui.size()[0]
    screenSizeY = pyautogui.size()[1]
    pyautogui.moveTo(screenSizeX/2, screenSizeY/2)

while True:
    openUrlInBrowserAndMax(url)
    while True:
        freeNowLoc = pyautogui.locateAllOnScreen(FREENOWIMAGE, grayscale=True, confidence=.92)
        freeNowLoc = list(freeNowLoc) #saves result as a list instead of a generator
        
        if not freeNowLoc:
            print("NOT FOUND")
            pyautogui.scroll(-400)
                
        elif freeNowLoc:
            print(f'Found image matching {FREENOWIMAGE}')
            if currentGame == 0:
                numFreeGames = maxNumOfGames
            print(f'Number of Free Games: {numFreeGames}')
            print(f'Free Now button found at" {freeNowLoc}')
            x_val = freeNowLoc[currentGame].left + (freeNowLoc[currentGame].width/2)
            y_val = freeNowLoc[currentGame].top + (freeNowLoc[currentGame].height/2)
            pyautogui.click(x=x_val, y=y_val)
            currentGame += 1
            break
    
    FindClick(GETIMAGE)    
    FindClick(PLACEORDERIMAGE)

    if currentGame >= numFreeGames:
        break