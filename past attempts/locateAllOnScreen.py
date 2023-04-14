'''
This is currently unused as the FreeNowImage seems to be inconsistent to match
Decided instead to match the FreeGamesImage and move the mouse from there to click on the games
'''

while True:
            freeNowButtonLocationS = pyautogui.locateAllOnScreen(FREENOWIMAGE, grayscale=True, confidence=.92)
            freeNowButtonLocationS = list(freeNowButtonLocationS) #saves result as a list instead of a generator
            
            if not freeNowButtonLocationS:
                print("NOT FOUND")
                pyautogui.scroll(-400)
                    
            elif freeNowButtonLocationS:
                print(f'Found image matching {FREENOWIMAGE}')
                if currentGame == 0: # if reimplemented, this will be useful to always grab all free games, regardless of number
                    numFreeGames = maxNumOfGames
                print(f'Number of Free Games: {numFreeGames}')
                print(f'Free Now button found at" {freeNowButtonLocationS}')
                x_val = freeNowButtonLocationS[currentGame].left + (freeNowButtonLocationS[currentGame].width/2)
                y_val = freeNowButtonLocationS[currentGame].top + (freeNowButtonLocationS[currentGame].height/2)
                pyautogui.click(x=x_val, y=y_val)
                currentGame += 1
                break