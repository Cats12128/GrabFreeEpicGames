import os
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import undetected_chromedriver as uc
import logging
import win32api

logging.basicConfig(filename='log.txt', filemode='w', level=logging.WARNING)

## TODO truncate numbers at end of games' url
## TODO add login support
## TODO add multiple account support
## TODO test headless mode


## FIND BY VARIABLES
FREE_NOW_LINK_CLASS = 'css-aere9z'  # this is the css for the div containing the actual link
FREE_NOW_TEXT_CLASS = 'css-11xvn05'  # this is the css for the 'Free Now' text
MATURE_CONTINUE_CLASS = 'css-1a6we1t'  # use By.CLASS_NAME
ADD_TO_CART_CLASS = 'css-5cj35r'  # unused until add to cart is implemented
PLACE_ORDER_CLASS = 'payment-order-confirm'
CHECK_OUT_CLASS = "css-187rod9"
CART_PRICE_SELECTOR = "#dieselReactWrapper > div > div.css-1vplx76 > main > div:nth-child(2) > div > div > div > div > section > div > div.css-map4tx > div.css-1791idi > div > div.css-u9q8d2 > div > span"

## OTHER VARIABLES
URL = 'https://store.epicgames.com/en-US/'
CART_URL = "https://store.epicgames.com/en-US/cart"
PATH = os.getenv("LOCALAPPDATA")
print(f'{PATH = }')

debug = False

def press_place_order(wait=5):
    iframe = False
    print('\n' + 'Looking for iframe')
    try:
        iframe = WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#webPurchaseContainer > iframe')))
    except:
        print('NOT FOUND: iframe')    
    finally:
        if iframe:
            iframe = driver.find_element(By.CSS_SELECTOR, '#webPurchaseContainer > iframe')
            print('Moving to iframe')
            driver.switch_to.frame(iframe)
            print('\n' + 'Looking for Place Order Button')
            sleep(5)
            press_button_with_custom_By(By.CLASS_NAME, PLACE_ORDER_CLASS)
        pass
    

def press_button_with_custom_By(ByMethod, html_class, wait=5):
    button = False
    try:
        button = WebDriverWait(driver, wait).until(EC.presence_of_element_located((ByMethod, html_class)))
    except:
        print(f'NOT FOUND: {html_class}')
    finally:
        if button:
            print(f'Clicking {html_class}')
            button.click()
        pass

def get_dict_of_free_games():
    free_game_url_dict = dict()
    game_links = driver.find_elements(By.CSS_SELECTOR, f'.{FREE_NOW_LINK_CLASS} a')
    for element in game_links:
        if debug:
            print(element.get_attribute('href'))
        url = element.get_attribute('href')
        try:
            if element.find_element(By.CLASS_NAME, FREE_NOW_TEXT_CLASS).text == 'FREE NOW':
                game_name = url.rpartition('/')[-1].replace('-', ' ').title()
                free_game_url_dict[game_name] = url
                print(f'FREE GAME: {game_name}')
        except NoSuchElementException:
            ## splits url at /'s, takes right most section and replaces - with spaces
            game_name = url.rpartition('/')[-1].replace('-', ' ').title()
            print(f'NEXT WEEK: {game_name}')
    return free_game_url_dict

#################################
#######   START PROGRAM   #######
#################################

options = Options()

subprocess.call('taskkill /im chrome.exe', shell=True)
options.add_argument(f'--user-data-dir={PATH}\\Google\\Chrome\\User Data\\')  #Path to your chrome profile
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--headless=new')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = uc.Chrome(options=options, service=service)

print('Opening Chrome...')
driver.get(URL)
driver.maximize_window()
print(f'Current URL: {driver.current_url}')

sleep(3)

free_game_url_dict = get_dict_of_free_games()
if debug:
    print(free_game_url_dict)


for game in free_game_url_dict:
    # game is KEY
    driver.get(free_game_url_dict[game])
    print(f'Current URL: {driver.current_url}')
    print('\n' + 'Checking for Mature Content Button')
    press_button_with_custom_By(By.CLASS_NAME, MATURE_CONTINUE_CLASS)
    print('\n' + 'Looking for Add to Cart Button')
    press_button_with_custom_By(By.CLASS_NAME, ADD_TO_CART_CLASS)

sleep(3)

driver.get(CART_URL)
sleep(3)
print("Confirming Price is FREE")
price = driver.find_element(By.CSS_SELECTOR, CART_PRICE_SELECTOR).text
logging.warning(f'{price = }')
if price != "$0.00":
    win32api.MessageBox(0, 'Some games in the cart are not free. Exiting Program.', 'GAMES NOT FREE', 0x00001000) 
    driver.close()
    quit()
else:
    print('😊 Confirmed Price is FREE 😊')   

print("Looking for Check Out Button")
press_button_with_custom_By(By.CLASS_NAME, CHECK_OUT_CLASS)
sleep(3)
press_place_order()
sleep(3)
driver.close()

print("DONE")

###############################
#######   END PROGRAM   #######
###############################