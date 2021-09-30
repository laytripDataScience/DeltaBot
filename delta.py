from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities

#from selenium import webdriver
#from selenium.webdriver.firefox.options import Options

from selenium.common.exceptions import NoSuchElementException
import lxml.html
import pandas as pd
from tqdm import tqdm

import time
import pandas as pd
from bs4 import BeautifulSoup
import pandas as pd
from pyvirtualdisplay import Display

#display = Display(visible=0, size=(1920, 1080))
#display.start()

'''
profile = Options()
profile.set_preference("browser.download.folderList", 2);
profile.set_preference("browser.download.manager.showWhenStarting", False);
profile.set_preference("browser.helperApps.neverAsk.openFile",
  "text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml");
profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
"text/csv,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel,image/png,image/jpeg,text/html,text/plain,application/msword,application/xml");
profile.set_preference("browser.helperApps.alwaysAsk.force", False);
profile.set_preference("browser.download.manager.alertOnEXEOpen", False);
profile.set_preference("browser.download.manager.focusWhenStarting", False);
profile.set_preference("browser.download.manager.useWindow", False);
profile.set_preference("browser.download.manager.showAlertOnComplete", False);
profile.set_preference("browser.download.manager.closeWhenDone", False);
profile.set_preference("dom.disable_beforeunload", True);
'''
from selenium.webdriver.chrome.options import Options
'''
chrome_options = Options()
capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptSslCerts'] = True 
capabilities['acceptInsecureCerts'] = True

chrome_options.add_argument("--headless")
'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
'''
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
#browser = webdriver.Chrome(options=chrome_options)
#chrome_options.add_argument("--start-maximized")
'''
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--no-sandbox") # linux only
#chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path="../Downloads/drivers/chromedriver",options=chrome_options) #,desired_capabilities=capabilities)
#options.set_profile(profile);
	#profile.add_argument("--headless")
#driver=webdriver.Firefox(options=profile)
action = ActionChains(driver)

driver.get("https://www.delta.com/apac/en")
time.sleep(10)
a=driver.find_element_by_xpath("//span[@class='airport-code d-block'][1]").click()
print(a)
time.sleep(5)
driver.find_element_by_xpath("//input[@aria-invalid='false'][contains(@id,'input')]").send_keys("SEA")
time.sleep(1)
driver.find_element_by_xpath("//input[@aria-invalid='false'][contains(@id,'input')]").send_keys(Keys.ENTER)


driver.find_element_by_xpath("(//span[contains(@class,'airport-code d-block')])[2]").click()
time.sleep(1)

driver.find_element_by_xpath("//input[@aria-invalid='false'][contains(@id,'input')]").send_keys("LAX")
time.sleep(1)
driver.find_element_by_xpath("//input[@aria-invalid='false'][contains(@id,'input')]").send_keys(Keys.ENTER)

driver.find_element_by_xpath("//span[contains(@id,'selectTripType-val')]").click()
driver.find_element_by_xpath("//li[contains(@id,'ui-list-selectTripType1')]").click()

time.sleep(5)



driver.find_element_by_xpath("//span[contains(@class,'calenderDepartSpan')]").send_keys("10-01-2021")
driver.find_element_by_xpath("//span[contains(@class,'calenderDepartSpan')]").send_keys(Keys.ENTER)

'''
driver.find_element_by_xpath("//input[contains(@type,'email')]").send_keys(Keys.ENTER)

driver.find_element_by_xpath("//input[contains(@type,'password')]").send_keys("F@r3Pl@y")
driver.find_element_by_xpath("//input[contains(@type,'password')]").send_keys(Keys.ENTER)

driver.find_element_by_xpath("//button[@class='el-button el-button--primary btn btn-block btn-primary'][contains(.,'Sign in')]").click()
time.sleep(10)
driver.find_element_by_xpath("//a[@href='/files']").click()
time.sleep(15)
driver.find_element_by_xpath("(//a[@href='#'])[3]").click()
time.sleep(100)
driver.close()
display.stop()
'''
