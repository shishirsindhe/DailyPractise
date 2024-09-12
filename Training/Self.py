from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
chrome_options=Options()
chrome_options.add_experimental_option(name="detach",value=True)
driver=Chrome(chrome_options)
driver.get("file:///C:/Users/SHISHIR/Desktop/demo.html")
# boxes=driver.find_elements("xpath","//input[@name='download']")
# for box in boxes:
#     box.click()
#     sleep(2)
# names=driver.find_elements("xpath","//table[@name='selenium']//td")
# for name in names:
#     print(name.text)
boxes1=driver.find_elements("xpath","//input[@class='first_row']/..//input[@name='fname']")
car_names=["Mercedes","BMW","kia"]
for box,car in zip(boxes1,car_names):
    box.send_keys(car)
boxes2=driver.find_elements("xpath","//input[@class='second_row']/..//input[@name='fname']")
bike_names=["Kawasaki","Triumph","Ducati"]
for box,bike in zip(boxes2,bike_names):
    box.send_keys(bike)

    