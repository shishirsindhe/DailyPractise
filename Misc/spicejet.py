from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
chrome_options=Options()
chrome_options.add_experimental_option(name="detach",value=True)
driver=Chrome(chrome_options)
driver.maximize_window()
driver.get("https://www.redbus.in/")
# driver.find_element("xpath","(//div[.='Login'])[2]").click()
# sleep(2)
# driver.find_element("xpath","(//div[text()='Email'])[1]").click()
# sleep(2)
# driver.find_element("css selector","input[type='email']").send_keys("ckarthikc1912@gmail.com")
# loc=driver.find_element("xpath","//div[@data-testid='login-cta']")
# wait_=WebDriverWait(driver,20)
# wait_.until(ec.element_to_be_clickable(loc))
# loc.click()
driver.find_element("xpath","//i[@class='sc-cSHVUG NyvQv icon icon-datev2']").click()
date=driver.find_element("xpath","//text[@class='dateText'][text()='26 Jun']")
date.click()