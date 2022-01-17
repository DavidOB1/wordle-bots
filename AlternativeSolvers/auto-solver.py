import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

## pip install selenium


driver = webdriver.Chrome()
driver.get("https://www.powerlanguage.co.uk/wordle")
driver.implicitly_wait(30)
time.sleep(0.5)
page = driver.find_element(By.TAG_NAME, "html")
page.click()


local_data = driver.execute_script("return window.localStorage;")
game_info = local_data["gameState"]
answer = json.loads(game_info)["solution"]


page.send_keys(answer)
page.send_keys(Keys.RETURN)
time.sleep(4.5)
page.click()
