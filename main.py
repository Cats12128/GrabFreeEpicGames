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

## UNUSED VARS
# FREE_NOW_TEXT_CLASS = 'css-11xvn05'  # this is the css for the 'Free Now' text
# GET_BUTTON_CLASS = 'css-195czy3'
# FREE_GAME_1_XML_PATH = '/html/body/div[1]/div/div[4]/main/div[2]/div/div/div/span[4]/div/div/section/div/div[1]/div/div/a/div/div/div[1]/div[2]/div/div'
# FREE_GAME_2_XML_PATH = '/html/body/div[1]/div/div[4]/main/div[2]/div/div/div/span[4]/div/div/section/div/div[2]/div/div/a'
# MATURE_CONTINUE_CLASS = 'css-1a6we1t'  # use By.CLASS_NAME
# ADD_TO_CART_CLASS = 'css-5cj35r'  # unused until add to cart is implemented
# IN_LIBRARY_CLASS = "css-18uwfgn"

## CLASS VARS
ADD_CLASS = 'add'  # this is the css for the div containing the actual link
PLACE_ORDER_CLASS = 'payment-order-confirm'
CHECK_OUT_CLASS = "btn checkout"
SHOPPING_CART_CLASS = "footer-btn-group"

## OTHER VARS
URL = 'https://www.unrealengine.com/marketplace/en-US/assets?tag=4910'
CART_URL = "https://store.epicgames.com/en-US/cart"
USERNAME = 'Mike'
PATH = os.getenv("LOCALAPPDATA")

print(f'PATH = {PATH}')
PROFILE_PATH = os.path.join(PATH, "\\Google\\Chrome\\User Data")

print(f'\nPROFILE_PATH= {PROFILE_PATH}\n')


Home = True
debug = True


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

def get_dict_of_free_items():
    free_game_url_dict = dict()
    game_links = driver.find_elements(By.CLASS_NAME, ADD_CLASS)
    for element in game_links:
        # if debug:
        #     print(element.get_attribute('href'))
        # url = element.get_attribute('href')
        try:
            if element.find_element(By.CLASS_NAME, FREE_NOW_TEXT_CLASS).text == 'FREE NOW':
                game_name = url.rpartition('/')[-1].replace('-', ' ').title()
                free_game_url_dict[game_name] = url
                print(f'FREE GAME: {game_name}')
        except NoSuchElementException:
            game_name = url.rpartition('/')[-1].replace('-', ' ').title()
            print(f'NEXT WEEK: {game_name}')
    return free_game_url_dict

def check_for_IN_LIBRARY(ByMethod, html_class, wait=5):
    element = False
    try:
        element = WebDriverWait(driver, wait).until(EC.presence_of_element_located((ByMethod, html_class)))
    except:
        print(f'NOT FOUND: {html_class}')
    finally:
        if element:
            print(f'FOUND: {html_class}')
            return True

#################################
#######   START PROGRAM   #######
#################################

options = Options()
if Home:
    subprocess.call('taskkill /im chrome.exe', shell=True)
    options.add_argument(f'user-data-dir={PATH}\\Google\\Chrome\\User Data\\')  #Path to your chrome profile
    # options.add_argument('profile-directory=Default')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# options.add_argument('start-maximized')
# options.page_load_strategy = 'eager'
# options.add_argument('--headless=new')
if Home:
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = uc.Chrome(options=options, service=service)
else:
    driver = webdriver.Chrome(options=options)
print('Opening Chrome...')
driver.get(URL)
print(f'Current URL: {driver.current_url}')

sleep(3)

free_items = driver.find_elements(By.CLASS_NAME, ADD_CLASS)
if debug:
    print(f'free_items= {free_items}')


for item in free_items:
    sleep(1)
    item.click()

sleep(3)

print("Looking for SHOPPING CART")
press_button_with_custom_By(By.CLASS_NAME, SHOPPING_CART_CLASS)
print("Looking for Check Out Button")
press_button_with_custom_By(By.CLASS_NAME, CHECK_OUT_CLASS)


confirm = input('Enter "Y" to purchase')
if confirm == 'Y':
    press_place_order()
    sleep(5)
else:
    print('"Y" NOT ENTERED - NOT PURCHASED')
print("END OF PROGRAM")
quit()
###############################
#######   END PROGRAM   #######
###############################