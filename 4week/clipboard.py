from seleniumwire import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time, pyperclip

WEB_DRIVE_PATH = "geckodriver"
ID = ""
PASSWORD = ""

def copy_input(driver, xpath, input):
  pyperclip.copy(input)
  driver.find_element_by_xpath(xpath).click()
  time.sleep(2)
  ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform() # 윈도우 경우 Keys.COMMAND 대신 Keys.CONTROL 사용

driver = webdriver.Firefox(capabilities=None, executable_path=WEB_DRIVE_PATH)
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login?')

copy_input(driver, '//*[@id="id"]', ID)
time.sleep(1.5)
copy_input(driver, '//*[@id="pw"]', PASSWORD)
time.sleep(1.5)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()