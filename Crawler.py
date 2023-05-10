from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

closed_set = []

def getAll(link):
  if link in closed_set:
    return None

  closed_set.append(link)

  print(link)
  response = requests.get(link)

  soup = BeautifulSoup(response.content, 'html.parser')
  name = link.replace("/", "").replace("https:", "") + ".txt"
  with open(name, 'w') as f:
    f.write(str(soup))
    
    
  
  driver.get(link)
  
  links = driver.find_elements(By.CSS_SELECTOR, 'a')
  
  for i in links:
    try:
      if i.get_attribute('href').startswith("https://twitter.com"):
        continue
    except:
      None
    try:
      getAll(i.get_attribute('href'))
    except:
      None
getAll("https://www.chess.com/")