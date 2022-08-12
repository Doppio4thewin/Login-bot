from selenium import webdriver
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
  driver.get('https://www.tradingview.com/symbols/XBT/')
  return driver

def perra():
  driver = get_puto()
  time.sleep(4)
  element = driver.find_element(by = 'xpath', value = "/html/body/div[2]/div[4]/div[2]/header/div/div[3]/div[1]/div/div/div/div[1]/div[1]")
  return element.text

print(perra())