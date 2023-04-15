import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# Either one of the below FREE_NOW_LINK_CLASS can be used. Both are provided for future proofing.
# If epic changes the web page, it may be necessary to use the other variable.
# Then, if neither work, it will be necessary to go back into the html to find the class(es) and re-set the variables


# FREE_NOW_LINK_CLASS = "css-aere9z" # this is the css for the div containing the actual link
FREE_NOW_LINK_CLASS = "css-11xvn05" # this is the css for the "Free Now" text

MATURE_CONTINUE_CLASS = "css-1a6we1t" # use By.CLASS_NAME
GET_BUTTON_CLASS = "css-195czy3"
PLACE_ORDER_CLASS = "payment__action-container"
URL = "https://store.epicgames.com/en-US/"
user = "Mike"
PATH = "C:\Program Files(86x)\chromedriver.exe"

useProfile = True

def press_button_with_class(html_class, wait_time=5):
    try:
        button = WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.CLASS_NAME, html_class))
    )
    except:
        print(f'NOT FOUND: {html_class}')
        button = False
        
    finally:
        if button:
            print(f'Clicking {html_class}')
            button.click()
        pass



options = Options()
if useProfile:
    subprocess.call("taskkill /f /im chrome.exe", shell=True)
    options.add_argument(f"user-data-dir=C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data\\")#Path to your chrome profile
    options.add_argument('profile-directory=Default')
options.add_argument("start-maximized")
options.add_argument('--no-sandbox')
# options.page_load_strategy = 'eager'
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path=PATH, options=options, service=service)

print("Opening Chrome")
driver.get(URL)
print(f'Opening Chrome, url is: {driver.current_url}')

# Now set the cookie. This one's valid for the entire domain
# cookie = {'name' : 'foo', 'value' : 'bar'}
# driver.add_cookie(cookie)
# # And now output all the available cookies for the current URL
# driver.get_cookies()
# print(f'cookie is: {cookie}')

press_button_with_class(FREE_NOW_LINK_CLASS)

#FREE_NOW_ELEMENT = driver.find_elements(By.CLASS_NAME, FREE_NOW_LINK_CLASS)

# if FREE_NOW_ELEMENT:
#     print("ELEMENT FOUND: ")
#     for e in FREE_NOW_ELEMENT:
#         print(e)
# else:
#     print("ELEMENT NOT FOUND")

# FREE_NOW_ELEMENT[0].click()

print(f'url is: {driver.current_url}')
print("right before press button(MATURE CONTINUE)")
press_button_with_class(MATURE_CONTINUE_CLASS)
print("right before press button(GET BUTTON)")
press_button_with_class(GET_BUTTON_CLASS)

# element = driver.find_element(By.XPATH, "/html/body/div[7]/iframe")
# if element:
#     element.click()
#     print("we done it")
    


# try:
#     input("WAITING")
#     button = WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, "button.payment-btn payment-order-confirm__btn payment-btn--primary"))
# )
    
# except:
#     print(f'NOT FOUND: Place Order')
#     button = False
    
# finally:
#     if button:
#         print(f'Clicking Place Order')
#         button.click()
#     pass


# MATURE_CONTINUE_BUTTON = driver.find_element(By.CLASS_NAME, MATURE_CONTINUE_CLASS)



# GET_BUTTON = driver.find_element(By.CLASS_NAME, GET_BUTTON_CLASS)

 








