from selenium import webdriver
driver = webdriver.Edge()
driver.implicitly_wait(50)
with open('musics.txt', 'r') as musics:
  for i in musics:
    driver.get("https://www.bestmp3converter.com/")

    driver.find_element_by_id('search_txt').send_keys(i)
    driver.find_element_by_id('btn-submit').click()

    driver.find_element_by_id('btn-download').click()