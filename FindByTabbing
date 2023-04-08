while True:
    global currentGame
    print(f"Searching for {EPICLOGOIMAGE}")
    if pyautogui.locateOnScreen(EPICLOGOIMAGE, confidence=confidence):
        print(f'Found image matching {EPICLOGOIMAGE}')
        for tabs in range(tabsToGame + currentGame):
            sleep(.005)
            pyautogui.press('tab')
        pyautogui.press("enter")
        currentGame += 1
        return