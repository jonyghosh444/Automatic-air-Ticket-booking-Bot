# Hare Krishna
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument("start-maximized")
# Chrome is controlled by automated test software
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
s = Service('E:\\Equipment\\software\\driver\\web driver\\chrome driver\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
# Selenium Stealth settings
stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win32",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
  )

actions = ActionChains(driver)


target = "https://www.singaporeair.com"
xPath = '//span[@class="icon icon--close-circle"]'
fromLoc = '//input[@id="flightOrigin1"]'
toLoc = '//input[@id="bookFlightDestination"]'
date = '//input[@id="departDate1"]'
bookingDate = '//li[@date-data="2022-03-24"]'
returnDate = '//li[@date-data="2022-04-13"]'
button = '//button[@class="btn-primary"]'
ticketClass = '//input[@name="cabinClass"]'
passengers = '//input[@name="flightPassengers"]'
adult = '//button[@tabindex="-1" and @class="btn--image_icon input__number--ticker-plus"]'
submit = '//button[@type="submit" and @class="btn btn-primary js-open-loading"]'


if __name__ == '__main__':
    driver.get(target)
    driver.implicitly_wait(5)
    cross = driver.find_element(By.XPATH, xPath)
    cross.click()
    fValue = driver.find_element(By.XPATH, fromLoc)
    fValue.send_keys("Singapore")
    actions.key_down(Keys.DOWN).key_up(Keys.UP).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    driver.implicitly_wait(1)
    tValue = driver.find_element(By.XPATH, toLoc)
    tValue.send_keys('Bangkok')
    actions.key_down(Keys.DOWN).key_up(Keys.DOWN).perform()
    dValue = driver.find_element(By.XPATH, date)
    dValue.click()
    driver.implicitly_wait(3)
    bookingPath = driver.find_element(By.XPATH, bookingDate)
    bookingPath.click()
    returnPath = driver.find_element(By.XPATH, returnDate)
    returnPath.click()
    buttonPath = driver.find_element(By.XPATH, button)
    buttonPath.click()
    tClass = driver.find_element(By.XPATH, ticketClass)
    tClass.click()
    for i in range(3):
        actions.key_down(Keys.DOWN).key_up(Keys.DOWN).perform()
    actions.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    passengersPath = driver.find_element(By.XPATH, passengers)
    passengersPath.click()
    adultPath = driver.find_element(By.XPATH, adult)
    adultPath.click()
    searchPath = driver.find_element(By.XPATH, submit)
    searchPath.click()
    driver.implicitly_wait(5)





