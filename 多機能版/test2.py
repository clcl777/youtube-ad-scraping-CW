from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#options = Options()
#options.add_argument('--user-data-dir=C:\\Users\\tisk0\\AppData\\Local\\Google\\Chrome\\User Data')
#options.add_argument('--profile-directory=Profile5')
driver = webdriver.Chrome(executable_path="C:\\Users\\tisk0\\PycharmProjects\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=bbnN65TV64w")

time.sleep(5)
webdriver.ActionChains(driver).key_down(Keys.SHIFT).send_keys('n').perform()
#webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys('n').perform()

#webdriver.ActionChains(driver).key_down(Keys.SPACE).perform()
#webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys(Keys.SPACE).perform()

