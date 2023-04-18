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

FREE_NOW_LINK_CLASS = "css-aere9z" # this is the css for the div containing the actual link
FREE_NOW_TEXT_CLASS = "css-11xvn05" # this is the css for the "Free Now" text

MATURE_CONTINUE_CLASS = "css-1a6we1t" # use By.CLASS_NAME
GET_BUTTON_CLASS = "css-195czy3"
ADD_TO_CART_CLASS = "css-5cj35r" # unused until add to cart is implemented
PLACE_ORDER_CLASS = "payment-order-confirm"
FREE_GAME_1_XML_PATH = "/html/body/div[1]/div/div[4]/main/div[2]/div/div/div/span[4]/div/div/section/div/div[1]/div/div/a/div/div/div[1]/div[2]/div/div"
FREE_GAME_2_XML_PATH = "/html/body/div[1]/div/div[4]/main/div[2]/div/div/div/span[4]/div/div/section/div/div[2]/div/div/a"
URL = "https://store.epicgames.com/en-US/"
USERNAME = "Mike"
PATH = "C:\Program Files(86x)\chromedriver.exe"

useProfile = False
replit = True

def press_place_order():
    iframe = driver.find_element(By.CSS_SELECTOR, "#webPurchaseContainer > iframe")
    print("switching to iframe: {iframe}")
    driver.switch_to.frame(iframe)
    press_button_with_custom_By(By.CLASS_NAME, PLACE_ORDER_CLASS)
    sleep(5)

def press_button_with_custom_By(ByMethod, html_class, wait=5):
    try:
        button = WebDriverWait(driver, wait).until(
        EC.presence_of_element_located((ByMethod, html_class))
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
    subprocess.call("taskkill /im chrome.exe", shell=True)
    options.add_argument(f"user-data-dir=C:\\Users\\{USERNAME}\\AppData\\Local\\Google\\Chrome\\User Data\\")#Path to your chrome profile  
    options.add_argument('profile-directory=Default')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
# options.add_argument("start-maximized")
# options.page_load_strategy = 'eager'
# options.add_argument("--headless=new")
service = ChromeService(executable_path=ChromeDriverManager().install())
if not replit:
  driver = webdriver.Chrome(options=options, service=service)
else: 
  driver = webdriver.Chrome(options=options)
print("Opening Chrome...")
driver.get(URL)
print(f'URL is: {driver.current_url}')

sleep(3)

free_game_url_dict = dict()

game_links = driver.find_elements(By.CSS_SELECTOR, ".css-aere9z a")

for element in game_links:
  try:
    if element.find_element(By.CLASS_NAME, FREE_NOW_TEXT_CLASS).text == "FREE NOW":
      url = element.get_attribute('href')
      game_name = url.rpartition("/")[-1]
      game_name = game_name.replace("-", " ").title()
      free_game_url_dict[game_name] = url
      print(f'Game: {game_name}')
      print(f'dict: {free_game_url_dict}')
  except NoSuchElementException:
    print(f'Next week game: {element.get_attribute("href")}')


quit()
###############################
#######   END PROGRAM   #######
###############################

links[1].click()
sleep(5)

print(f'\n" + "url is: {driver.current_url}')
print("\n" + "right before press button(MATURE CONTINUE)")
press_button_with_custom_By(By.CLASS_NAME, MATURE_CONTINUE_CLASS)
print("\nright before press button(GET BUTTON)")
press_button_with_custom_By(By.CLASS_NAME, GET_BUTTON_CLASS)
sleep(3)
press_place_order()

# driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0])
# ele = driver.find_elements(By.XPATH, '//*[@id]')
# for x in ele:
#     print(x.tag_name, x.get_attribute('id'))


# Store iframe web element





# print("NEXT IFRAME")
# ele = driver.find_elements(By.TAG_NAME, "fpt_frame")
# for x in ele:
#     print(x.tag_name, x.get_attribute('id'))
#     driver.switch_to.frame(x)



# driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

# element = driver.find_element(By.CLASS_NAME, "payment-order-confirm")
# if element:
#     element.click()
#     print(f"we clicked: {element}")

# press_button_with_class(PLACE_ORDER_CLASS)