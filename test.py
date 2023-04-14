#from GrabFreeEpicGame import *
css = "css-11xvn05"#"css-aere9z"
url = "https://store.epicgames.com/en-US/"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def InitializeSelenium(website, user):
    PATH = "C:\Program Files(86x)\chromedriver.exe"
    options = Options()
    options.add_argument(f"user-data-dir=C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data\\")#Path to your chrome profile
    options.add_argument('profile-directory=Default')
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(executable_path=PATH, options=options, service=service)
    driver.maximize_window
    driver.get("website")



'''
options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("user-data-dir=C:\\Users\\Mike\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("start-maximized")
options.page_load_strategy = 'eager'


#


print("1")



print("Opening Chrome")
driver.get("http://selenium.dev")
print(f'current url is {driver.current_url}')
print("End of Program")
input()
driver.close()

###enter 3 apostrophe here
options = ArgOptions()

options.add_argument("profile-path=C:\\Users\\Mike\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
driver = WebDriver(options=options)
driver.get(url)


elem = driver.find_elements(By.CLASS_NAME, css)

if elem:
    print("FOUND")
    for e in elem:
        print(e)
else:
    print("NOT FOUND")
elem[1].click()
driver.getCurrentUrl()

'''


#assert "No results found." not in driver.page_source
