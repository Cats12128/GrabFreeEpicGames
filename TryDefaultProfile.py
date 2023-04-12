#I can open existing chrome profile with selenium but it just stop there. Not visit the link. 
#Please help, 
#Here's code 
#https://groups.google.com/g/selenium-users/c/JmEAnj-k3hE/m/FRdJyFt0AQAJ

options = webdriver.ChromeOptions()

options.add_argument("user-data-dir=C:\\Users\\Shakil\\AppData\\Local\\Google\\Chrome\\User Data")

options.add_argument("profile-directory=Profile 1")#Path to your chrome profile


# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)

driver.get("http://selenium.dev")
