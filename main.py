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

## CLASS VARS
ADD_CLASS = 'add'
PLACE_ORDER_CLASS = 'payment-order-confirm'
SHOPPING_CART_CLASS = "cart-icon-wrapper"
CHECK_OUT_SELECTOR = "header#sub-nav-container div.footer-btn-group > button"

## OTHER VARS
URL = 'https://www.unrealengine.com/marketplace/en-US/assets?tag=4910'
PATH = os.getenv("LOCALAPPDATA")

logging.basicConfig(format='%(asctime)s %(message)s', filename='log.txt', filemode="w", encoding='utf-8', level=logging.ERROR)

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
            logging.error(f'button={button}')
            print(f'Clicking {html_class}')
            button.click()
        pass

#################################
#######   START PROGRAM   #######
#################################

options = Options()
subprocess.call('taskkill /im chrome.exe', shell=True)
options.add_argument(f'--user-data-dir={PATH}\\Google\\Chrome\\User Data')  #Path to your chrome profile
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--start-maximized')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = uc.Chrome(options=options, service=service)
print('Opening Chrome...')
driver.get(URL)
print(f'Current URL: {driver.current_url}')

free_items = driver.find_elements(By.CLASS_NAME, ADD_CLASS)

logging.info(f'free_items= {free_items}')

if free_items:
    for item in free_items:
        sleep(.5)
        item.click()

sleep(3)

print("Looking for SHOPPING CART")
logging.error("BELOW IS THE SEARCH FOR THE SHOPPING CART")
press_button_with_custom_By(By.CLASS_NAME, SHOPPING_CART_CLASS)
print("Looking for Check Out Button")
sleep(4)
logging.error("BELOW IS THE SEARCH FOR THE CHECKOUT BUTTON")
press_button_with_custom_By(By.CSS_SELECTOR, CHECK_OUT_SELECTOR)
# driver.find_element(By.XPATH, '//*[@id="sub-nav-container"]/div/div[2]/div[3]/div[2]/div/div[1]/section[3]/div[2]/button')



confirm = input('Enter capital "Y" to purchase: ')
if confirm == 'Y':
    press_place_order()
    sleep(5)
else:
    print('"Y" NOT ENTERED - NOT PURCHASED')
print("END OF PROGRAM")

###############################
#######   END PROGRAM   #######
###############################