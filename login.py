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
  driver.get('https://amfs.tec.mx/nidp/saml2/sso?id=itesmauth-identidadsl2&sid=0&option=credential&sid=0')
  return driver

def perra():
  driver = get_puto()
  driver.find_element(by='id', value="Ecom_User_ID").send_keys("A01275621")
  time.sleep(2)
  driver.find_element(by='id', value="Ecom_Password").send_keys("TIblanco26*" + Keys.RETURN)
  print(driver.current_url)
  
print(perra())