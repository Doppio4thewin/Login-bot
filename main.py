from selenium import webdriver

def get_drvier():
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
  driver.get('https://coinmarketcap.com/')
  return driver

def main():
  driver = get_drvier()
  element = driver.find_element(by = 'xpath', value = "/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/section/div[1]/h1")
  return element.text

print(main())