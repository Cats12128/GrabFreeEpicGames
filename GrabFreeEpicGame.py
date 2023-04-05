import pyautogui
import cv2 as cv
import numpy as np
import webbrowser as web
import win32gui, win32con
from time import sleep
import subprocess


debug = True

#sets url to open
url = "https://store.epicgames.com/en-US/"

#images to match
freeNowImage = ".\FreeNowImage.png"
getImage = ".\GetImage.png"
placeOrderImage = ".\PlaceOrderImage.png"
InLibraryImage = ".\InLibraryImage.png"
currentGame = 0
maxNumOfGames = 2

def FindClick(image): #This function takes an image, constantly search the screen for a match, then clicks it. Then prints which image it matched.
    
    while True:
        sleep(2)
        getLoc = pyautogui.locateOnScreen(image, confidence=.95)
        alreadyInLibrary = pyautogui.locateOnScreen(InLibraryImage, confidence=.95)
        if getLoc:
            x_val = getLoc.left + (getLoc.width/2)
            y_val = getLoc.top + (getLoc.height/2)
            pyautogui.click(x=x_val, y=y_val)
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

def openEpicInBrowser():#opens url in browser, then maximize
    #open {url} in default browser in new tab and raises the window
    web.open(url, new=0, autoraise=True)
    
    #assigns the window to hwnd
    hwnd = win32gui.GetForegroundWindow()
    #maximizes hwnd (the window)
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    sleep(2)
    screenSizeX = pyautogui.size()[0]
    screenSizeY = pyautogui.size()[1]
    pyautogui.moveTo(screenSizeX/2, screenSizeY/2)

while True:
    openEpicInBrowser()
    while True:
        
        #look for freeNowImage on screen
        freeNowLoc = pyautogui.locateAllOnScreen(freeNowImage, grayscale=True, confidence=.92)
        #saves result as a list instead of a generator
        freeNowLoc = list(freeNowLoc)
        #if not found it prints NOT FOUND and scrolls down
        if not freeNowLoc:
            print("NOT FOUND")
            pyautogui.scroll(-400)
                
        elif freeNowLoc:
            print(f'Found image matching {freeNowImage}')
            if currentGame == 0:
                numFreeGames = maxNumOfGames
            print(f'Number of Free Games: {numFreeGames}')
            print(f'Free Now button found at" {freeNowLoc}')
            x_val = freeNowLoc[currentGame].left + (freeNowLoc[currentGame].width/2)
            y_val = freeNowLoc[currentGame].top + (freeNowLoc[currentGame].height/2)
            pyautogui.click(x=x_val, y=y_val)
            currentGame += 1
            break
    
    FindClick(getImage)    
    FindClick(placeOrderImage)

    if currentGame >= numFreeGames:
        break