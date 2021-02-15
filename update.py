import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "https://www.mercari.com/jp/"

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\take1\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_argument('--profile-directory=Profile 2')  # この行を省略するとDefaultフォルダが指定されます

driver = webdriver.Chrome(executable_path='/mnt/c/Program Files (x86)/chromedriver/chromedriver.exe', options=options)
driver.get(URL)

time.sleep(1)
driver.find_element_by_link_text("マイページ").click()

time.sleep(1)
driver.find_element_by_link_text("出品した商品 - 出品中").click()

item_list = list()

time.sleep(1)
for item in driver.find_elements_by_css_selector(".mypage-item-link"):
  item_list.append(item.get_attribute("href"))
  

for i in item_list:
  print (i)

  time.sleep(random.uniform(10,50))
  driver.get(i)

  time.sleep(random.uniform(1,5))
  driver.find_element_by_link_text("商品の編集").click()

  time.sleep(random.uniform(1,5))
  driver.find_element_by_css_selector('#sell-container > div > div > form:nth-child(3) > div > button').click()


driver.quit()
