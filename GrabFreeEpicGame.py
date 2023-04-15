import pyautogui
import cv2 as cv
import numpy as np
import webbrowser as web
from time import sleep
import subprocess
import pygetwindow
from selenium import webdriver

#variables
url = "https://store.epicgames.com/en-US/"
filepath = "Z:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"
windowname = "epic"
currentGame = 0
maxNumOfGames = 2
pyautogui.FAILSAFE = True
confidence = .70
tabsToGame = 46
css = "css-11xvn05"#"css-aere9z"

#images to match
FREENOWIMAGE = "images\FreeNowImage.png"
GETIMAGE = "images\GetImage.png"
PLACEORDERIMAGE = "images\PlaceOrderImage.png"
INLIBRARYIMAGE = "images\InLibraryImage.png"
FREEGAMESIMAGE = "images\FreeGamesImage.png"
CONTINUEIMAGE = "images\ContinueImage.png"
EPICLOGOIMAGE = "images\EpicLogoImage.png"

def FindClick(image):
    while True:
        buttonLocation = pyautogui.locateCenterOnScreen(image, confidence=confidence)
        if buttonLocation:
            pyautogui.click(buttonLocation)
            return print(f'Clicked on location matching {image}')
 
def Find1OfManyImages(GETIMAGE, INLIBRARYIMAGE, CONTINUEIMAGE):
    print("Searching for GET or IN LIBRARY or CONTINUE")
    while True:
        getButtonLocation = pyautogui.locateCenterOnScreen(GETIMAGE, grayscale=True, confidence=confidence)
        alreadyInLibrary = pyautogui.locateCenterOnScreen(INLIBRARYIMAGE, confidence=confidence)
        matureContinue = pyautogui.locateCenterOnScreen(CONTINUEIMAGE, confidence=confidence)
        if getButtonLocation:
            pyautogui.click(getButtonLocation)
            print(f'Clicked Get Button: {GETIMAGE}')
            return FindClick(PLACEORDERIMAGE)
        elif matureContinue:
            FindClick(CONTINUEIMAGE)
            continue
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

def moveCursorToCenterScreen(time=0):
    screenSizeX = pyautogui.size()[0]
    screenSizeY = pyautogui.size()[1]
    pyautogui.dragTo(screenSizeX/2, screenSizeY/2 ,duration=time)

def ClickFreeGames(css):
    driver = webdriver.Chrome()
    driver.get(url)
    # geeting the button by class name
    button = driver.find_elements_by_class_name(css)
    button.click()
            
def InitializeSelenium(url, user):
    PATH = "C:\Program Files(86x)\chromedriver.exe"
    options = Options()
    options.add_argument(f"user-data-dir=C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data\\")#Path to your chrome profile
    options.add_argument('profile-directory=Default')
    options.add_argument("start-maximized")
    # options.add_argument('--no-sandbox')
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path=PATH, options=options, service=service)
    driver.get(url)

if __name__ == "__main__":
    while True:
        InitializeSelenium(url, "Mike")
        sleep(2)
        #moveCursorToCenterScreen(time=2)
        ClickFreeGames(FREEGAMESIMAGE)        
        Find1OfManyImages(GETIMAGE, INLIBRARYIMAGE, CONTINUEIMAGE)
                 

        if currentGame >= maxNumOfGames:
            break