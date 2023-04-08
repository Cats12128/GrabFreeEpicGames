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
        buttonLocation = pyautogui.locateCenterOnScreen(Image1, confidence=.95)
        if buttonLocation:
            pyautogui.click(buttonLocation)
            return print(f'Clicked on location matching {image}')
 

def Find1Of2Images(image1, image2):
    while True:
        sleep(2)
        getButtonLocation = pyautogui.locateCenterOnScreen(image1, confidence=.95)
        alreadyInLibrary = pyautogui.locateCenterOnScreen(image2, confidence=.95)
        if getButtonLocation:
            #x_val = getLoc.left + (getLoc.width/2)
            #y_val = getLoc.top + (getLoc.height/2)
            pyautogui.click(getButtonLocation)
            return print(f'Clicked on location matching {image1}')
        elif alreadyInLibrary:
            return print('Game already redeemed')
                

def DrawRectangle(LocAllImg):
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    for location in range(len(LocAllImg)):
        top_left = (LocAllImg[location].left, LocAllImg[location].top)
        bottom_right = (LocAllImg[location].left + LocAllImg[location].width, LocAllImg[location].top + LocAllImg[0].height)
        cv.rectangle(screenshot,top_left, bottom_right, color=(0,255,0), thickness=2, lineType=cv.LINE_4)
    cv.imshow("Screenshot", screenshot)
    cv.waitKey(0)

def openUrlInBrowserAndMax(url):
    web.open(url, new=0, autoraise=True)
    sleep(.5)
    window = pygetwindow.getActiveWindow()
    window.maximize()

def openApplicationAndMax(filepath, windowname):
    subprocess.call(filepath)
    sleep(.5)
    window = pygetwindow.getActiveWindow()
    window.maximize()

def moveCursorToCenterScreen():
    screenSizeX = pyautogui.size()[0]
    screenSizeY = pyautogui.size()[1]
    pyautogui.moveTo(screenSizeX/2, screenSizeY/2)

if __name__ == "__main__":
    while True:
        openUrlInBrowserAndMax(url)
        while True:
            freeNowButtonLocationS = pyautogui.locateAllOnScreen(FREENOWIMAGE, grayscale=True, confidence=.92)
            freeNowButtonLocationS = list(freeNowButtonLocationS) #saves result as a list instead of a generator
            
            if not freeNowButtonLocationS:
                print("NOT FOUND")
                pyautogui.scroll(-400)
                    
            elif freeNowButtonLocationS:
                print(f'Found image matching {FREENOWIMAGE}')
                if currentGame == 0:
                    numFreeGames = maxNumOfGames
                print(f'Number of Free Games: {numFreeGames}')
                print(f'Free Now button found at" {freeNowButtonLocationS}')
                x_val = freeNowButtonLocationS[currentGame].left + (freeNowButtonLocationS[currentGame].width/2)
                y_val = freeNowButtonLocationS[currentGame].top + (freeNowButtonLocationS[currentGame].height/2)
                pyautogui.click(x=x_val, y=y_val)
                currentGame += 1
                break
        
        FindClick(GETIMAGE)    
        Find1Of2Images(PLACEORDERIMAGE, INLIBRARYIMAGE)

        if currentGame >= numFreeGames:
            break