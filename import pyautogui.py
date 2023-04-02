import pyautogui
import cv2 as cv
import numpy as np
import webbrowser as web

#sets url to open
url = "https://store.epicgames.com/en-US/"

#images to match
freeNowImage = ".\FreeNowImage.png"
getImage = ".\GetImage.png"
placeOrderImage= ".\PlaceOrderImage.png"
currentGame = 0


#open {url} in default browser in new tab and raises the window
#web.open(url, new=0, autoraise=True) ######UNCOMMENT THIS WHEN COMPLETE#####


def FindClick(image):
    #This function will constantly search the page to match the passed image, then click on it.
    #After click, it will also print out which image it matched for confirmation.
    while True:
        getLoc = pyautogui.locateOnScreen(image, confidence=.95)
        if getLoc:
            x_val = getLoc.left + (getLoc.width/2)
            y_val = getLoc.top + (getLoc.height/2)
            pyautogui.click(x=x_val, y=y_val)
            return print(f'Clicked on location matching {image}')

def DrawRectangle(LocAllImg):
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    top_left = (LocAllImg[0].left, LocAllImg[0].top)
    bottom_right = (LocAllImg[0].left + LocAllImg[0].width, LocAllImg[0].top + LocAllImg[0].height)
    cv.rectangle(screenshot,top_left, bottom_right, color=(0,255,0), thickness=2, lineType=cv.LINE_4)
    cv.imshow("Screenshot", screenshot)
    cv.waitKey(0)
while True:
    while True:
        #looks to match the saved image with one on the screen
        freeNowLoc = pyautogui.locateAllOnScreen(freeNowImage, confidence=.90)
        #saves result as a list instead of a generator
        freeNowLoc = list(freeNowLoc)
        #if not found it prints NOT FOUND and scrolls down
        if not freeNowLoc:
            print("NOT FOUND")
            #pyautogui.scroll(-500)
        elif freeNowLoc:
            print(f'Found image matching {freeNowImage}')
            print(freeNowLoc)
            if currentGame == 0:
                numFreeGames = (len(freeNowLoc))
            print(f'Number of Free Games: {numFreeGames}')
            break

    #if found clicks on position found
    if currentGame >= numFreeGames:
        break        
    x_val = freeNowLoc[currentGame].left + (freeNowLoc[currentGame].width/2)
    y_val = freeNowLoc[currentGame].top + (freeNowLoc[currentGame].height/2)
    pyautogui.click(x=x_val, y=y_val)
    currentGame += 1

    '''
    FindClick(getImage)
    FindClick(placeOrderImage)
    '''
    web.open(url, new=0, autoraise=True)


    
    



