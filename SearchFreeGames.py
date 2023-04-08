def SearchFreeGames(FREEGAMESIMAGE):
    global currentGame
    while True:
        freeGamesLocation = pyautogui.locateCenterOnScreen(FREEGAMESIMAGE, confidence=confidence)
        if not freeGamesLocation:
            print("NOT FOUND")
            print("NOPE")
            pyautogui.scroll(-400)
        elif freeGamesLocation:
            print(f'Found image matching {FREEGAMESIMAGE} at {freeGamesLocation}')
            if currentGame == 0:
                pyautogui.click(freeGamesLocation[0]+120, freeGamesLocation[1]+325)
            if currentGame == 1:
                pyautogui.click(freeGamesLocation[0]+590, freeGamesLocation[1]+350)
            currentGame += 1
            break