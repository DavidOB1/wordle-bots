import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

## pip install selenium

with open("word-frequencies.txt") as f:
  wDict = f.read().splitlines() 


wDict = [word.split(",")[0] for word in wDict]
wDict = [word for word in wDict if len(word) == 5]


driver = webdriver.Chrome()
driver.get("https://www.powerlanguage.co.uk/wordle")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.title_contains("Wordle"))
time.sleep(0.5)
page = driver.find_element(By.TAG_NAME, "html")
page.click()


def enter_word(word):
  page.send_keys(word)
  page.send_keys(Keys.RETURN)
  time.sleep(2)


def get_data():
  local_data = driver.execute_script("return window.localStorage;")
  game_info = local_data["nyt-wordle-state"]
  evals = json.loads(game_info)["evaluations"]
  return evals


possible_words = wDict
known_letters = []
word = "adieu"
## "adieu" can be changed to any word, this one is just a good strategy in my opinion
enter_word(word)
evals = get_data()


for q in range(5):
  stats = evals[q]
  correct_tally = 0
  for i in range(5):
    if (stats[i] != "absent") and (not word[i] in known_letters):
      known_letters.append(word[i])
    if stats[i] == "correct":
      correct_tally += 1
  if correct_tally == 5:
    time.sleep(2.5)
    page.click()
    quit()
  for i in range(5):
    letter = word[i]
    if stats[i] == "absent":
      if letter in known_letters:
        possible_words = [x for x in possible_words if (x.count(letter) == 1) and (x[i] != letter)]
      else:
        possible_words = [x for x in possible_words if not letter in x]
    elif stats[i] == "present":
      possible_words = [x for x in possible_words if (letter in x) and (x[i] != letter)]
    elif stats[i] == "correct":
      possible_words = [x for x in possible_words if letter == x[i]]
  word = possible_words[0]
  enter_word(word)
  evals = get_data()
  while type(evals[q+1]) is not list:
    for i in range(5):
      page.send_keys(Keys.BACKSPACE)
    possible_words.remove(word)
    word = possible_words[0]
    enter_word(word)
    evals = get_data()


time.sleep(2.5)
page.click()
