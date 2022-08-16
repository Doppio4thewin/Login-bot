from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_puto():
  #Para hacer el browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  #Para desactivar el sandbox de seguridad
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  #Para quitar la seguridad igual
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options = options) #Esta variable contiene todas las options mencionadas arriba
  driver.get('https://titan22.com/')
  return driver

def perra():
  driver = get_puto()
  driver.find_element(by='xpath', value="/html/body/header/div[1]/div[1]/div/div[3]/a[2]/span/svg").send_keys(Keys.RETURN)
  time.sleep(2)
  print(driver.current_url)
  
print(perra())
